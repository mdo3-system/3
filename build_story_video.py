import asyncio
import os
import re
import sys
import glob
import subprocess
import edge_tts

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
OUTPUT_BASE = os.path.join(BASE_DIR, "video_output")
INBOX_DIR = os.path.join(BASE_DIR, "veo3_inbox")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

os.makedirs(OUTPUT_BASE, exist_ok=True)
os.makedirs(INBOX_DIR, exist_ok=True)

def format_ass_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int(round((seconds - int(seconds)) * 100))
    if centis >= 100:
        centis = 99
    return f"{hours:01d}:{minutes:02d}:{secs:02d}.{centis:02d}"

async def build_veo3_story_video(chapter_num=1, key="tortoise_and_hare", title_en="The Tortoise and the Hare", title_ja="ウサギとカメ", level_label="Eiken Grade 4", voice="en-US-GuyNeural", rate="-6%"):
    print(f"\n=======================================================")
    print(f"🎬 [Veo 3 本番結合レンダリング] Chapter {chapter_num:02d}: {title_en} ({title_ja})")
    print(f"=======================================================")
    
    chapter_dir = os.path.join(OUTPUT_BASE, f"chapter{chapter_num:02d}_{key}")
    os.makedirs(chapter_dir, exist_ok=True)
    
    audio_path = os.path.join(chapter_dir, "narration.mp3")
    ass_path = os.path.join(chapter_dir, "karaoke_subtitles.ass")
    final_video_path = os.path.join(chapter_dir, f"chapter{chapter_num:02d}_{level_label.replace(' ', '_')}.mp4")
    portal_video_path = os.path.join(OUTPUT_BASE, "current_preview.mp4")

    story_text = (
        "A proud hare always laughed at a slow tortoise. "
        '"You walk so slowly! Look at me. I am the fastest animal in the forest," the hare said. '
        'The tortoise smiled and answered, "Let\'s have a race today. I can run faster than you think." '
        'The hare laughed loudly. "That is impossible! But okay, let\'s run." '
        'The race started. The hare ran very fast. Soon, he was far ahead of the tortoise. '
        'He looked back and saw no one. "The tortoise is too slow. I have a lot of time. '
        'I will take a short nap under this big tree," said the hare. He sat down and fell asleep. '
        'Meanwhile, the tortoise kept walking. He did not stop. He walked step by step. '
        'When the hare woke up, the sun was going down. He ran quickly to the finish line. '
        'However, the tortoise was already there! '
        'Slow and steady wins the race.'
    )

    # 1. 音声生成とセンテンス境界取得
    print("[1/4] 高品質ネイティブ音声を生成中...")
    communicate = edge_tts.Communicate(story_text, voice, rate=rate)
    
    sentence_timings = []
    with open(audio_path, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                offset_sec = chunk["offset"] / 10_000_000
                duration_sec = chunk["duration"] / 10_000_000
                sentence_timings.append({
                    "text": chunk["text"],
                    "start": offset_sec,
                    "end": offset_sec + duration_sec,
                    "duration": duration_sec
                })
                
    total_audio_duration = sentence_timings[-1]["end"] + 1.2 if sentence_timings else 70.0
    print(f"   -> 音声尺: {total_audio_duration:.1f} 秒 ({len(sentence_timings)} センテンス)")

    # 2. 英語カラオケ字幕 (.ass) 生成
    print("[2/4] 英語カラオケ字幕 (.ass) を構築中...")
    ass_content = f"""[Script Info]
Title: Chapter {chapter_num} {title_en}
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HeaderTitle,Arial,34,&H00FFFFFF,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,2,0,8,60,60,35,1
Style: KaraokeEnglish,Arial,52,&H00FFFFFF,&H0000E5FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,4,2,2,100,100,75,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ass_content += f"Dialogue: 0,0:00:00.00,{format_ass_time(total_audio_duration)},HeaderTitle,,0,0,0,,{{\\fad(400,400)}}📖 Chapter {chapter_num:02d}: {title_en} ({title_ja})  |  {level_label}\n"
    
    for timing in sentence_timings:
        start_sec = max(0.0, timing["start"])
        end_sec = timing["end"] + 0.3
        
        words = timing["text"].split()
        if not words:
            continue
            
        total_chars = sum(max(1, len(re.sub(r'[^a-zA-Z0-9]', '', w))) for w in words)
        total_duration_csec = max(len(words), int(round(timing["duration"] * 100)))
        
        k_text = ""
        for w in words:
            clean_len = max(1, len(re.sub(r'[^a-zA-Z0-9]', '', w)))
            w_csec = max(1, int(round((clean_len / total_chars) * total_duration_csec)))
            k_text += f"{{\\k{w_csec}}}{w} "
            
        start_str = format_ass_time(start_sec)
        end_str = format_ass_time(end_sec)
        ass_content += f"Dialogue: 1,{start_str},{end_str},KaraokeEnglish,,0,0,0,,{{\\fad(150,150)}}{k_text.strip()}\n"
        
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)

    # 3. veo3_inbox 内の動画クリップを取得
    inbox_files = sorted(glob.glob(os.path.join(INBOX_DIR, "*.mp4")))
    print(f"[3/4] 受信フォルダ内の Veo 3 動画を確認中... ({len(inbox_files)} 本検出)")

    ass_escaped = ass_path.replace("\\", "/").replace(":", "\\:")

    if len(inbox_files) >= 3:
        clip1, clip2, clip3 = inbox_files[0], inbox_files[1], inbox_files[2]
        print(f"   ✓ Clip 1 (起): {os.path.basename(clip1)}")
        print(f"   ✓ Clip 2 (承): {os.path.basename(clip2)}")
        print(f"   ✓ Clip 3 (結): {os.path.basename(clip3)}")
        
        # 3本のVeo動画（各10秒）をスロー＆ループ展開してナレーションの起承転結（約24s, 24s, 22s）に同期
        # 1920x1080 へアップスケール＋カラオケ字幕オーバーレイ
        dur1 = 23.5
        dur2 = 23.5
        dur3 = total_audio_duration - (dur1 + dur2) + 0.5
        
        # FFmpeg Filter Complex
        filter_complex = (
            f"[0:v]setpts=2.35*PTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,trim=duration={dur1}[v0];"
            f"[1:v]setpts=2.35*PTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,trim=duration={dur2}[v1];"
            f"[2:v]setpts=2.3*PTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,trim=duration={dur3}[v2];"
            f"[v0][v1][v2]concat=n=3:v=1:a=0[vcat];"
            f"[vcat]drawbox=y=0:color=black@0.7:width=iw:height=90:t=fill,"
            f"drawbox=y=ih-180:color=black@0.78:width=iw:height=180:t=fill,"
            f"ass='{ass_escaped}'[v]"
        )

        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-i", clip1,
            "-i", clip2,
            "-i", clip3,
            "-i", audio_path,
            "-filter_complex", filter_complex,
            "-map", "[v]",
            "-map", "3:a",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            final_video_path
        ]
    else:
        # 参照イラストによるフォールバック
        ref_image = os.path.join(IMAGES_DIR, f"vol1_{key}.png")
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", ref_image,
            "-i", audio_path,
            "-filter_complex",
            (
                f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
                f"zoompan=z='min(zoom+0.00035,1.18)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30,"
                f"drawbox=y=0:color=black@0.7:width=iw:height=90:t=fill,"
                f"drawbox=y=ih-180:color=black@0.78:width=iw:height=180:t=fill,"
                f"ass='{ass_escaped}'[v]"
            ),
            "-map", "[v]",
            "-map", "1:a",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            final_video_path
        ]

    print("[4/4] FFmpeg で最終動画を合成中...")
    res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        # ポータル用プレビューファイルにもコピー
        import shutil
        shutil.copy2(final_video_path, portal_video_path)
        print(f"\n🎉 [COMPLETE] Veo 3 動画結合が完了しました！")
        print(f"出力ファイル: {final_video_path}")
        print(f"ポータルプレビュー: {portal_video_path}")
    else:
        print(f"❌ [ERROR] レンダリング失敗: {res.stderr}")

if __name__ == "__main__":
    asyncio.run(build_veo3_story_video())

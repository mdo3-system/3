import asyncio
import os
import re
import sys
import glob
import shutil
import subprocess
import edge_tts

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
OUTPUT_BASE = os.path.join(BASE_DIR, "video_output")
INBOX_DIR = os.path.join(BASE_DIR, "veo3_inbox")
SHORTS_DIR = os.path.join(OUTPUT_BASE, "shorts_reels")

os.makedirs(OUTPUT_BASE, exist_ok=True)
os.makedirs(INBOX_DIR, exist_ok=True)
os.makedirs(SHORTS_DIR, exist_ok=True)

def format_ass_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int(round((seconds - int(seconds)) * 100))
    if centis >= 100:
        centis = 99
    return f"{hours:01d}:{minutes:02d}:{secs:02d}.{centis:02d}"

def get_chapter_meta(ch_num):
    import json
    master_json = os.path.join(BASE_DIR, "veo3_production", "veo3_prompts_master.json")
    if os.path.exists(master_json):
        with open(master_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data.get("stories", []):
            if item["chapter"] == ch_num:
                return item["key"], item["titleEn"], item["titleJa"]
    return f"chapter{ch_num:02d}", f"Chapter {ch_num}", f"第{ch_num}話"

def get_chapter_texts(chapter_num=3):
    ch_str = f"{chapter_num:02d}"
    group_idx = (chapter_num - 1) // 10

    def find_file(tier_num):
        # 1. Direct tier prefix: vol2_, vol3_, vol4_
        if tier_num == 1:
            candidates = [f"chapter{ch_str}_*.md", f"vol1_chapter{ch_str}_*.md", f"vol{group_idx * 4 + 1}_chapter{ch_str}_*.md"]
        else:
            candidates = [f"vol{tier_num}_chapter{ch_str}_*.md", f"vol{group_idx * 4 + tier_num}_chapter{ch_str}_*.md"]

        for pat in candidates:
            m = glob.glob(os.path.join(BASE_DIR, pat))
            if m:
                return m[0]
        return ""

    v1_file = find_file(1)
    v2_file = find_file(2)
    v3_file = find_file(3)
    v4_file = find_file(4)

    def read_f(fp):
        if fp and os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    v1_c = read_f(v1_file)
    v2_c = read_f(v2_file)
    v3_c = read_f(v3_file)
    v4_c = read_f(v4_file)

    def ext(pattern, content):
        m = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return m.group(1).strip() if m else ""

    g4_text = ext(r"## 1\. Benchmark Level: Eiken (?:Grade )?4[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v1_c)
    g3_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?3[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v1_c)
    gpre2_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?Pre-?2[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v2_c)
    g2_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?2[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v3_c)
    gpre1_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?Pre-?1[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v4_c)
    classic_text = ext(r"## 3\. Classic Original English Text[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v1_c)

    return [
        {"grade_key": "Grade_4", "label": "Eiken Grade 4 (英検4級)", "voice": "en-US-GuyNeural", "rate": "-6%", "text": g4_text},
        {"grade_key": "Grade_3", "label": "Eiken Grade 3 (英検3級)", "voice": "en-US-ChristopherNeural", "rate": "-3%", "text": g3_text},
        {"grade_key": "Grade_Pre2", "label": "Eiken Grade Pre-2 (英検準2級)", "voice": "en-US-GuyNeural", "rate": "+0%", "text": gpre2_text},
        {"grade_key": "Grade_2", "label": "Eiken Grade 2 (英検2級)", "voice": "en-US-ChristopherNeural", "rate": "+2%", "text": g2_text},
        {"grade_key": "Grade_Pre1", "label": "Eiken Grade Pre-1 (英検準1級)", "voice": "en-US-GuyNeural", "rate": "+4%", "text": gpre1_text},
        {"grade_key": "Classic_Original", "label": "Classic Original (Townsend版)", "voice": "en-GB-RyanNeural", "rate": "-4%", "text": classic_text}
    ]

async def build_grade_video(chapter_num, key, title_en, title_ja, grade_info, clips_video_path):
    grade_key = grade_info["grade_key"]
    label = grade_info["label"]
    voice = grade_info["voice"]
    rate = grade_info["rate"]
    text = grade_info["text"]

    chapter_dir = os.path.join(OUTPUT_BASE, f"chapter{chapter_num:02d}_{key}")
    os.makedirs(chapter_dir, exist_ok=True)

    audio_path = os.path.join(chapter_dir, f"narration_{grade_key}.mp3")
    ass_path = os.path.join(chapter_dir, f"karaoke_{grade_key}.ass")
    final_video = os.path.join(chapter_dir, f"chapter{chapter_num:02d}_{grade_key}.mp4")

    print(f"\n--- 🎙️ [{label}] 音声・字幕・動画生成中 ---")
    
    # 1. 音声生成
    communicate = edge_tts.Communicate(text, voice, rate=rate)
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

    total_audio_duration = sentence_timings[-1]["end"] + 1.2 if sentence_timings else 60.0
    print(f"   -> 音声尺: {total_audio_duration:.1f} 秒")

    # 2. ASS字幕生成
    ass_content = f"""[Script Info]
Title: Chapter {chapter_num} {title_en} - {grade_key}
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HeaderTitle,Arial,34,&H00FFFFFF,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,2,0,8,60,60,35,1
Style: KaraokeEnglish,Arial,52,&H00FFFFFF,&H0000E5FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,4,2,2,100,100,75,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,{format_ass_time(total_audio_duration)},HeaderTitle,,0,0,0,,{{\\fad(400,400)}}📖 Chapter {chapter_num:02d}: {title_en} ({title_ja})  |  {label}
"""
    for timing in sentence_timings:
        start_sec = max(0.0, timing["start"])
        end_sec = timing["end"] + 0.3
        words = timing["text"].strip().split()
        if not words:
            continue
        word_dur_cs = int(((end_sec - start_sec) * 100) / len(words))
        karaoke_text = "".join([f"{{\\k{word_dur_cs}}}{w} " for w in words]).strip()
        ass_content += f"Dialogue: 0,{format_ass_time(start_sec)},{format_ass_time(end_sec)},KaraokeEnglish,,0,0,0,,{{\\fad(200,200)}}{karaoke_text}\n"

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)

    # 3. FFmpeg レンダリング
    ass_escaped = ass_path.replace("\\", "/").replace(":", "\\:")
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-stream_loop", "-1",
        "-i", clips_video_path,
        "-i", audio_path,
        "-t", f"{total_audio_duration:.2f}",
        "-vf", f"ass='{ass_escaped}'",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        final_video
    ]
    subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8")
    print(f"   ✅ 完成: {final_video}")
    return final_video

def generate_shorts_for_chapter(chapter_num, key, title_ja):
    chapter_dir = os.path.join(OUTPUT_BASE, f"chapter{chapter_num:02d}_{key}")
    ch_str = f"{chapter_num:02d}"

    cfgs = [
        ("Grade4", "chapter01_Grade_4.mp4".replace("01", ch_str), f"chapter{ch_str}_shorts_Grade4_9x16.mp4", "📖 【英検4級】", "MDO3出版｜1分シャドーイング (@mdo3_english)"),
        ("Grade3", "chapter01_Grade_3.mp4".replace("01", ch_str), f"chapter{ch_str}_shorts_Grade3_9x16.mp4", "🎯 【英検3級】", "MDO3出版｜入試・英検必須フレーズ (@mdo3_english)"),
        ("Classic", "chapter01_Classic_Original.mp4".replace("01", ch_str), f"chapter{ch_str}_shorts_Classic_9x16.mp4", "🏛️ 【クラシック原文】", "MDO3出版｜大人の教養・古典朗読 (@mdo3_english)")
    ]

    for gid, in_name, out_name, h_title, s_brand in cfgs:
        in_vid = os.path.join(chapter_dir, in_name)
        out_vid = os.path.join(SHORTS_DIR, out_name)
        ass_path = os.path.join(SHORTS_DIR, f"shorts_h_{ch_str}_{gid}.ass")

        ass_content = f"""[Script Info]
Title: Shorts Header
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: ShortsTitle,Arial,52,&H00FFFFFF,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,2,0,1,3,0,8,40,40,80,1
Style: ShortsBrand,Arial,34,&H00F8BD38,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,2,0,8,40,40,150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:01:30.00,ShortsTitle,,0,0,0,,{h_title}{title_ja}
Dialogue: 0,0:00:00.00,0:01:30.00,ShortsBrand,,0,0,0,,{s_brand}
"""
        with open(ass_path, "w", encoding="utf-8") as f:
            f.write(ass_content)

        ass_escaped = ass_path.replace("\\", "/").replace(":", "\\:")
        filter_complex = (
            f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=luma_radius=20:luma_power=2[bg];"
            f"[0:v]scale=1080:1080:force_original_aspect_ratio=decrease[fg];"
            f"[bg][fg]overlay=(W-w)/2:(H-h)/2[base];"
            f"[base]drawbox=y=0:color=black@0.75:width=iw:height=220:t=fill,drawbox=y=ih-240:color=black@0.8:width=iw:height=240:t=fill,ass='{ass_escaped}'[v]"
        )

        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-i", in_vid,
            "-filter_complex", filter_complex,
            "-map", "[v]",
            "-map", "0:a",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-c:a", "copy",
            "-pix_fmt", "yuv420p",
            "-t", "59",
            out_vid
        ]
        subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8")
        print(f"   ✅ 縦型ショート完成: {out_vid}")

    # デフォルトショート更新
    def_s = os.path.join(SHORTS_DIR, f"chapter{ch_str}_shorts_9x16.mp4")
    g4_s = os.path.join(SHORTS_DIR, f"chapter{ch_str}_shorts_Grade4_9x16.mp4")
    if os.path.exists(g4_s):
        shutil.copyfile(g4_s, def_s)

async def build_chapter(chapter_num=2, key="boy_who_cried_wolf", title_en="The Boy Who Cried Wolf", title_ja="オオカミ少年"):
    print(f"\n=======================================================")
    print(f"🚀 [全自動ビルド開始] Chapter {chapter_num:02d}: {title_ja} ({title_en})")
    print(f"=======================================================")

    chapter_dir = os.path.join(OUTPUT_BASE, f"chapter{chapter_num:02d}_{key}")
    os.makedirs(chapter_dir, exist_ok=True)

    clips_combined = os.path.join(chapter_dir, "clips_combined.mp4")

    # 1. Veo 3 インボックスから最新3クリップを取得して結合
    inbox_files = sorted(glob.glob(os.path.join(INBOX_DIR, "*.mp4")), key=os.path.getmtime, reverse=True)
    latest_3 = []
    if len(inbox_files) >= 3:
        latest_3 = sorted(inbox_files[:3], key=os.path.getmtime)
        print("🎬 検出したVeo 3クリップ:")
        for idx, fpath in enumerate(latest_3):
            print(f"   Clip {idx+1}: {os.path.basename(fpath)}")

        # 結合用 concat リスト作成
        concat_txt = os.path.join(chapter_dir, "concat_list.txt")
        with open(concat_txt, "w", encoding="utf-8") as f:
            for fpath in latest_3:
                escaped = fpath.replace("\\", "/")
                f.write(f"file '{escaped}'\n")

        concat_cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_txt,
            "-c", "copy",
            clips_combined
        ]
        subprocess.run(concat_cmd, capture_output=True, text=True, encoding="utf-8")
        print(f"✅ クリップ結合完了: {clips_combined}")
    elif os.path.exists(clips_combined):
        print(f"ℹ️ veo3_inbox に新規動画はありませんが、既存の結合動画を使用します: {clips_combined}")
    else:
        print(f"❌ エラー: veo3_inbox に動画が3本以上なく、既存の clips_combined.mp4 も見つかりません。(現在inbox: {len(inbox_files)}本)")
        return

    # 2. 全6バリエーション（4級、3級、準2級、2級、準1級、クラシック原文）をレンダリング
    grade_list = get_chapter_texts(chapter_num)
    for g_info in grade_list:
        await build_grade_video(chapter_num, key, title_en, title_ja, g_info, clips_combined)

    # 3. 縦型ショート3本生成
    print("\n📱 縦型ショート動画 (9:16) 3本を自動生成中...")
    generate_shorts_for_chapter(chapter_num, key, title_ja)

    # 4. Veo 3 素材クリップを各話の veo3_sources にアーカイブ（inbox の混同を完全防止）
    if latest_3:
        sources_dir = os.path.join(chapter_dir, "veo3_sources")
        os.makedirs(sources_dir, exist_ok=True)
        for idx, fpath in enumerate(latest_3):
            dest_f = os.path.join(sources_dir, f"clip{idx+1}_{os.path.basename(fpath)}")
            if os.path.exists(fpath):
                try:
                    shutil.move(fpath, dest_f)
                    print(f"📦 素材をアーカイブ移動: {dest_f}")
                except Exception as e:
                    shutil.copyfile(fpath, dest_f)

    print(f"\n🎉🎉🎉 Chapter {chapter_num:02d} ({title_ja}) の全動画ビルドが完了しました！ 🎉🎉🎉")

if __name__ == "__main__":
    ch = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    ch_key, t_en, t_ja = get_chapter_meta(ch)
    asyncio.run(build_chapter(ch, ch_key, t_en, t_ja))


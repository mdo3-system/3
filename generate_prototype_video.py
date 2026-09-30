import asyncio
import os
import re
import sys
import subprocess
import edge_tts

# UTF-8 出力設定
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# --- 設定 ---
STORY_TITLE = "The Tortoise and the Hare (ウサギとカメ)"
LEVEL_LABEL = "Eiken Grade 4 (英検4級)"
IMAGE_PATH = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle\images\vol1_tortoise_and_hare.png"
OUTPUT_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle\video_output"
VOICE = "en-US-GuyNeural" # 落ち着いた明瞭なネイティブナレーション
RATE = "-6%" # 4級学習者向けに明瞭で心地よい朗読速度

# 英検4級テキスト（文ごとの英語と日本語対訳）
STORY_SECTIONS = [
    {
        "en": "A proud hare always laughed at a slow tortoise.",
        "ja": "ある誇り高いウサギが、足の遅いカメをいつも笑っていました。"
    },
    {
        "en": '"You walk so slowly! Look at me. I am the fastest animal in the forest," the hare said.',
        "ja": "「君はなんて歩くのが遅いんだ！僕を見てごらん。森で一番足が速いんだ」とウサギは言いました。"
    },
    {
        "en": 'The tortoise smiled and answered, "Let\'s have a race today. I can run faster than you think."',
        "ja": "カメは微笑んで答えました。「今日、かけっこをしよう。君が思うより速く走れるよ」"
    },
    {
        "en": 'The hare laughed loudly. "That is impossible! But okay, let\'s run."',
        "ja": "ウサギは大声で笑いました。「そんなの無理だよ！でもいいよ、走ろう」"
    },
    {
        "en": "The race started. The hare ran very fast. Soon, he was far ahead of the tortoise.",
        "ja": "レースが始まりました。ウサギはとても速く走りました。すぐにカメを大きく引き離しました。"
    },
    {
        "en": 'He looked back and saw no one. "The tortoise is too slow. I have a lot of time. I will take a short nap under this big tree," said the hare.',
        "ja": "ウサギが振り返ると誰も見えません。「カメは遅すぎるな。時間はたっぷりある。この大きな木の下で少し昼寝をしよう」"
    },
    {
        "en": "He sat down and fell asleep. Meanwhile, the tortoise kept walking. He did not stop.",
        "ja": "ウサギは座り込み、眠りに落ちました。その間も、カメは歩き続けました。止まりませんでした。"
    },
    {
        "en": "He walked step by step. When the hare woke up, the sun was going down.",
        "ja": "カメは一歩一歩進みました。ウサギが目を覚ました時、日は沈みかけていました。"
    },
    {
        "en": "He ran quickly to the finish line. However, the tortoise was already there!",
        "ja": "ウサギはゴールへ急いで走りました。しかし、カメはすでにそこにいました！"
    },
    {
        "en": "Slow and steady wins the race.",
        "ja": "【教訓】ゆっくりでも着実に進む者が、レースに勝つ。"
    }
]

os.makedirs(OUTPUT_DIR, exist_ok=True)
AUDIO_PATH = os.path.join(OUTPUT_DIR, "chapter01_g4_audio.mp3")
ASS_PATH = os.path.join(OUTPUT_DIR, "chapter01_g4_karaoke.ass")
VIDEO_PATH = os.path.join(OUTPUT_DIR, "chapter01_g4_prototype.mp4")

async def generate_audio():
    print("[1/3] 高品質ネイティブ音声を生成中...")
    full_text = " ".join([s["en"] for s in STORY_SECTIONS])
    communicate = edge_tts.Communicate(full_text, VOICE, rate=RATE)
    
    sentence_timings = []
    with open(AUDIO_PATH, "wb") as f:
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
    print(f"   -> 音声ファイル生成完了: {AUDIO_PATH}")
    print(f"   -> 検出センテンス数: {len(sentence_timings)}")
    return sentence_timings

def format_ass_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int(round((seconds - int(seconds)) * 100))
    if centis >= 100:
        centis = 99
    return f"{hours:01d}:{minutes:02d}:{secs:02d}.{centis:02d}"

def generate_karaoke_ass(sentence_timings):
    print("[2/3] カラオケ風ハイライト字幕 (.ass) を構築中...")
    
    # 1920x1080 向け ASS スタイル定義
    # PrimaryColour: &H00FFFFFF (未読テキスト: 純白)
    # SecondaryColour: &H0000E5FF (発声中の単語: 鮮やかなネオンゴールド/イエロー &H0000E5FF)
    ass_content = """[Script Info]
Title: Eiken Fables Karaoke Video
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HeaderTitle,Arial,36,&H00FFFFFF,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,2,0,8,60,60,35,1
Style: KaraokeEnglish,Arial,48,&H00FFFFFF,&H0000E5FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,3.5,2,2,100,100,110,1
Style: JapaneseSub,Yu Gothic,32,&H0080E5FF,&H00000000,&H00000000,&H90000000,0,0,0,0,100,100,1,0,1,2,1,2,100,100,45,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    
    total_audio_duration = sentence_timings[-1]["end"] + 3.0 if sentence_timings else 70.0
    # 上部タイトルバー
    ass_content += f"Dialogue: 0,0:00:00.00,{format_ass_time(total_audio_duration)},HeaderTitle,,0,0,0,,{{\\fad(400,400)}}📖 Chapter 01: {STORY_TITLE}  |  {LEVEL_LABEL}\n"
    
    # センテンスと対訳のマッピング
    for i, timing in enumerate(sentence_timings):
        start_sec = max(0.0, timing["start"])
        end_sec = timing["end"] + 0.3
        
        # 対応する日本語訳を取得（インデックス範囲内）
        ja_text = STORY_SECTIONS[min(i, len(STORY_SECTIONS)-1)]["ja"]
        
        # 英文の各単語にカラオケタグ {\k<centiseconds>} を適用
        words = timing["text"].split()
        if not words:
            continue
            
        # 文字数比率に応じたミリ秒割り振り
        total_chars = sum(max(1, len(re.sub(r'[^a-zA-Z0-9]', '', w))) for w in words)
        total_duration_csec = max(len(words), int(round(timing["duration"] * 100)))
        
        k_text = ""
        for w in words:
            clean_len = max(1, len(re.sub(r'[^a-zA-Z0-9]', '', w)))
            w_csec = max(1, int(round((clean_len / total_chars) * total_duration_csec)))
            k_text += f"{{\\k{w_csec}}}{w} "
            
        start_str = format_ass_time(start_sec)
        end_str = format_ass_time(end_sec)
        
        # 英語カラオケ字幕（発声に合わせて左から黄色にハイライト）
        ass_content += f"Dialogue: 1,{start_str},{end_str},KaraokeEnglish,,0,0,0,,{{\\fad(150,150)}}{k_text.strip()}\n"
        # 日本語対訳（下に上品なアクセントカラーで表示）
        ass_content += f"Dialogue: 1,{start_str},{end_str},JapaneseSub,,0,0,0,,{{\\fad(150,150)}}{ja_text}\n"

    with open(ASS_PATH, "w", encoding="utf-8") as f:
        f.write(ass_content)
    print(f"   -> ASS字幕生成完了: {ASS_PATH}")

def render_video():
    print("[3/3] FFmpeg で動画合成を開始（挿絵シネマズーム + 音声 + カラオケ字幕）...")
    ass_escaped = ASS_PATH.replace("\\", "/").replace(":", "\\:")
    img_escaped = IMAGE_PATH.replace("\\", "/")
    
    # FFmpeg コマンド
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", IMAGE_PATH,
        "-i", AUDIO_PATH,
        "-filter_complex",
        (
            f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
            f"zoompan=z='min(zoom+0.00035,1.18)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30,"
            f"drawbox=y=0:color=black@0.7:width=iw:height=90:t=fill,"
            f"drawbox=y=ih-230:color=black@0.78:width=iw:height=230:t=fill,"
            f"ass='{ass_escaped}'[v]"
        ),
        "-map", "[v]",
        "-map", "1:a",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        VIDEO_PATH
    ]
    
    res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        print(f"\n==========================================")
        print(f"[SUCCESS] プロトタイプ動画の生成に成功しました！")
        print(f"出力ファイル: {VIDEO_PATH}")
        print(f"==========================================")
    else:
        print(f"[ERROR] レンダリング失敗:\n{res.stderr}")

async def main():
    timings = await generate_audio()
    generate_karaoke_ass(timings)
    render_video()

if __name__ == "__main__":
    asyncio.run(main())

import os
import sys
import glob
import subprocess

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
OUTPUT_BASE = os.path.join(BASE_DIR, "video_output")
CHAPTER_DIR = os.path.join(OUTPUT_BASE, "chapter01_tortoise_and_hare")
SHORTS_DIR = os.path.join(OUTPUT_BASE, "shorts_reels")

os.makedirs(SHORTS_DIR, exist_ok=True)

SHORTS_CONFIGS = [
    {
        "id": "Grade4",
        "label": "英検4級 基礎版",
        "header_title": "📖 【英検4級】",
        "sub_brand": "MDO3出版｜1分シャドーイング (@mdo3_english)",
        "input_filename": "chapter01_Grade_4.mp4",
        "output_filename": "chapter01_shorts_Grade4_9x16.mp4"
    },
    {
        "id": "Grade3",
        "label": "英検3級 ステップアップ版",
        "header_title": "🎯 【英検3級】",
        "sub_brand": "MDO3出版｜入試・英検必須フレーズ (@mdo3_english)",
        "input_filename": "chapter01_Grade_3.mp4",
        "output_filename": "chapter01_shorts_Grade3_9x16.mp4"
    },
    {
        "id": "Classic",
        "label": "クラシック原文 教訓版",
        "header_title": "🏛️ 【クラシック原文】",
        "sub_brand": "MDO3出版｜大人の教養・古典朗読 (@mdo3_english)",
        "input_filename": "chapter01_Classic_Original.mp4",
        "output_filename": "chapter01_shorts_Classic_9x16.mp4"
    }
]

def generate_vertical_short_item(cfg, chapter_num=1, title_ja="ウサギとカメ"):
    input_video = os.path.join(CHAPTER_DIR, cfg["input_filename"])
    if not os.path.exists(input_video):
        print(f"⚠️ 元動画が見つかりません: {input_video}")
        return None

    output_short = os.path.join(SHORTS_DIR, cfg["output_filename"])
    ass_short_path = os.path.join(SHORTS_DIR, f"shorts_header_{cfg['id']}.ass")
    
    # 9:16 (1080x1920) 向け ASS スタイル
    ass_content = f"""[Script Info]
Title: Shorts Header {cfg['id']}
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
Dialogue: 0,0:00:00.00,0:01:30.00,ShortsTitle,,0,0,0,,{cfg['header_title']}{title_ja}
Dialogue: 0,0:00:00.00,0:01:30.00,ShortsBrand,,0,0,0,,{cfg['sub_brand']}
"""
    with open(ass_short_path, "w", encoding="utf-8") as f:
        f.write(ass_content)

    ass_escaped = ass_short_path.replace("\\", "/").replace(":", "\\:")

    filter_complex = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
        f"boxblur=luma_radius=20:luma_power=2[bg];"
        f"[0:v]scale=1080:1080:force_original_aspect_ratio=decrease[fg];"
        f"[bg][fg]overlay=(W-w)/2:(H-h)/2[base];"
        f"[base]drawbox=y=0:color=black@0.75:width=iw:height=220:t=fill,"
        f"drawbox=y=ih-240:color=black@0.8:width=iw:height=240:t=fill,"
        f"ass='{ass_escaped}'[v]"
    )

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-i", input_video,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "0:a",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "copy",
        "-pix_fmt", "yuv420p",
        "-t", "59",
        output_short
    ]
    
    res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        print(f"✅ 縦型ショート完成 【{cfg['label']}】: {output_short}")
        return output_short
    else:
        print(f"❌ エラー 【{cfg['label']}】: {res.stderr}")
        return None

def generate_all_3_shorts():
    print("🎬 === 3パターンの縦型ショート動画 (9:16) 一括生成開始 ===")
    results = []
    for cfg in SHORTS_CONFIGS:
        out = generate_vertical_short_item(cfg)
        if out:
            results.append(out)
            
    # 既存互換用のデフォルトショート chapter01_shorts_9x16.mp4 も Grade4 版としてコピーまたはリンク
    default_short = os.path.join(SHORTS_DIR, "chapter01_shorts_9x16.mp4")
    g4_short = os.path.join(SHORTS_DIR, "chapter01_shorts_Grade4_9x16.mp4")
    if os.path.exists(g4_short):
        import shutil
        shutil.copyfile(g4_short, default_short)
        print(f"✅ デフォルト互換ショート更新: {default_short}")

    print(f"\n🎉 合計 {len(results)} 本のショート動画を生成しました！")

if __name__ == "__main__":
    generate_all_3_shorts()

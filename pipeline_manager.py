import os
import sys
import time
import glob
import json
import asyncio
import subprocess

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
INBOX_DIR = os.path.join(BASE_DIR, "veo3_inbox")
OUTPUT_DIR = os.path.join(BASE_DIR, "video_output")

os.makedirs(INBOX_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_single_chapter(chapter_num, key, title_en, title_ja, level_label, live_upload=False):
    print(f"\n=======================================================")
    print(f"🚀 パイプライン実行: Chapter {chapter_num:02d} - {title_ja}")
    print(f"=======================================================")

    # Step 1: 動画の合成（build_story_video.py）
    print("▶ [Step 1/3] 動画合成エンジンを実行中...")
    cmd_build = [
        "py", "build_story_video.py"
    ]
    subprocess.run(cmd_build, check=True)

    video_file = os.path.join(OUTPUT_DIR, f"chapter{chapter_num:02d}_{key}", f"chapter{chapter_num:02d}_{level_label.replace(' ', '_')}.mp4")

    # Step 2: YouTube アップロード＆メタデータ生成（youtube_manager.py）
    print("▶ [Step 2/3] YouTube メタデータ生成 / アップロード中...")
    cmd_yt = [
        "py", "youtube_manager.py",
        "--chapter", str(chapter_num),
        "--key", key,
        "--title_en", title_en,
        "--title_ja", title_ja,
        "--level", level_label,
        "--video", video_file
    ]
    if live_upload:
        cmd_yt.append("--live")
    subprocess.run(cmd_yt, check=True)

    # Step 3: Kindle 原稿への自動リンク挿入（sync_kindle_with_youtube.py）
    print("▶ [Step 3/3] Kindle 原稿へ動画リンクを自動反映中...")
    cmd_sync = [
        "py", "sync_kindle_with_youtube.py"
    ]
    subprocess.run(cmd_sync, check=True)

    print(f"\n✅ Chapter {chapter_num:02d} の全工程（動画生成 ➔ YouTube連携 ➔ Kindle原稿リンク反映）が完了しました！")

if __name__ == "__main__":
    # 第1話のテスト実行
    process_single_chapter(
        chapter_num=1,
        key="tortoise_and_hare",
        title_en="The Tortoise and the Hare",
        title_ja="ウサギとカメ",
        level_label="Eiken Grade 4",
        live_upload=False
    )

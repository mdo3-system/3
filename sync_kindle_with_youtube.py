import os
import json
import re
import sys
import glob

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
LINKS_FILE = os.path.join(BASE_DIR, "youtube_links.json")

def format_video_link_block(youtube_url, title_ja, title_en):
    """
    Kindle / EPUB に美しくレンダリングされる 動画リンクボタン HTML ブロック
    """
    block = f"""
<!-- Video Learning Link Start -->
<div style="text-align: center; margin: 18px 0; padding: 12px 16px; background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 8px;">
  <a href="{youtube_url}" style="color: #0969da; font-weight: bold; text-decoration: none; font-size: 1.05em; display: inline-block;">
    🎬 【動画で聴く・シャドーイング】ネイティブ朗読＆カラオケ字幕付き動画（YouTube）▶
  </a>
  <div style="font-size: 0.82em; color: #57606a; margin-top: 4px;">
    ※ タップするとYouTubeが開き、発音に合わせて光るカラオケ字幕で学習できます。
  </div>
</div>
<!-- Video Learning Link End -->
"""
    return block

def update_markdown_files():
    print("=======================================================")
    print("📖 Kindle 原稿へ YouTube 動画リンクを自動挿入中...")
    print("=======================================================")

    if not os.path.exists(LINKS_FILE):
        print(f"❌ リンク管理ファイルが存在しません: {LINKS_FILE}")
        return

    with open(LINKS_FILE, "r", encoding="utf-8") as f:
        links_data = json.load(f)

    # 1. 個別チャプターファイル (chapter*.md, vol2_chapter*.md, vol3_chapter*.md, etc.)
    all_chapter_files = glob.glob(os.path.join(BASE_DIR, "*chapter*.md"))
    updated_count = 0

    for file_path in all_chapter_files:
        filename = os.path.basename(file_path)
        # 章番号の特定
        match = re.search(r'chapter(\d+)', filename, re.IGNORECASE)
        if not match:
            continue
        
        ch_num = int(match.group(1))
        ch_key = f"chapter{ch_num:02d}"

        if ch_key not in links_data:
            continue

        video_info = links_data[ch_key]
        youtube_url = video_info["url"]

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 既存のリンクブロックがあれば更新、なければ挿絵タグの直後に挿入
        link_block = format_video_link_block(youtube_url, "ウサギとカメ", "The Tortoise and the Hare")

        if "<!-- Video Learning Link Start -->" in content:
            # 置換
            new_content = re.sub(
                r'<!-- Video Learning Link Start -->.*?<!-- Video Learning Link End -->',
                link_block.strip(),
                content,
                flags=re.DOTALL
            )
        else:
            # 挿絵の </div> の直後、または 第1見出し直後に挿入
            if 'alt="' in content and '</div>' in content:
                # 最初の </div> の後ろに挿入
                parts = content.split('</div>', 1)
                new_content = parts[0] + '</div>\n' + link_block + parts[1]
            else:
                new_content = link_block + "\n" + content

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"   ✓ 更新完了: {filename} (Chapter {ch_num:02d})")
            updated_count += 1

    print(f"\n🎉 合計 {updated_count} 個の Markdown ファイルに動画リンクを反映しました！")

if __name__ == "__main__":
    update_markdown_files()

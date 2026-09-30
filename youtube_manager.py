import os
import json
import sys
import argparse

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# --- 設定 ---
BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
METADATA_DIR = os.path.join(BASE_DIR, "youtube_metadata")
LINKS_FILE = os.path.join(BASE_DIR, "youtube_links.json")
CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, "client_secrets.json")

os.makedirs(METADATA_DIR, exist_ok=True)

def generate_youtube_metadata(chapter_num, key, title_en, title_ja, level_label, grade_key):
    """
    YouTube SEOに完全最適化された タイトル・説明欄・タグ を自動生成する
    """
    title = f"【{level_label}】{title_ja} ({title_en}) ネイティブ朗読＆カラオケ字幕 | イソップ英語多読"
    # YouTube タイトル長上限100文字
    if len(title) > 100:
        title = title[:97] + "..."

    description = f"""📖 イソップ寓話で鍛える英語力：Chapter {chapter_num:02d}「{title_ja} ({title_en})」
【対象レベル: {level_label}】

ネイティブスピーカーによる自然でクリアな朗読音声と、発音に合わせてリアルタイムに光るカラオケ風字幕付き動画です。
リスニング力アップ、シャドーイング、オーバーラッピングの学習に最適です！

--------------------------------------------------
📚 Amazon Kindle電子書籍 本編のご案内
--------------------------------------------------
本書はAmazon Kindleストアにて好評配信中！
各レベルの読み比べ対比学習、頻出英単語・イディオム解説、暗唱用フレーズカードを完全収録しています。

▼ Kindle本はこちら（Kindle Unlimited対応）
https://www.amazon.co.jp/dp/B0XXXXXXXX (※Amazonリンク)

--------------------------------------------------
⏱ チャプター (タイムスタンプ)
--------------------------------------------------
0:00 オープニング (Opening)
0:05 本文朗読＆カラオケ字幕 (Story Reading with Highlight)
1:05 最後のまとめ・教訓 (Moral & Wrap-up)

--------------------------------------------------
💡 おすすめの学習ステップ
--------------------------------------------------
1. 【リスニング】まずは字幕を見ずに耳だけでストーリーを聴く
2. 【オーバーラッピング】カラオケ字幕を目で追いながら、音声と同時に声に出して読む
3. 【シャドーイング】音声から少し遅れて影のように復唱する

#英語学習 #英検 #{level_label.replace(' ', '')} #イソップ寓話 #リスニング #シャドーイング #英語多読 #Kindle
"""

    tags = [
        "英語学習",
        "英検",
        level_label,
        "イソップ寓話",
        title_ja,
        title_en,
        "リスニング",
        "シャドーイング",
        "オーバーラッピング",
        "英語 多読",
        "Aesop Fables",
        "Learn English",
        "Kindle"
    ]

    return {
        "chapter": chapter_num,
        "key": key,
        "title": title,
        "description": description,
        "tags": tags,
        "privacyStatus": "public" # public, unlisted, private
    }

def get_youtube_service():
    """
    Google API クライアント初期化 (OAuth 2.0)
    """
    if not os.path.exists(CLIENT_SECRETS_FILE):
        return None
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        
        SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        credentials = flow.run_local_server(port=0)
        return build("youtube", "v3", credentials=credentials)
    except Exception as e:
        print(f"[WARN] YouTube API 認証スキップ: {e}")
        return None

def upload_or_mock_youtube(video_path, meta, dry_run=True):
    """
    動画をYouTubeにアップロード（またはシミュレーション）し、URLを発行・保存する
    """
    ch_key = f"chapter{meta['chapter']:02d}"
    
    # 既存のリンク管理ファイルを読み込み
    links_data = {}
    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE, "r", encoding="utf-8") as f:
            links_data = json.load(f)

    # メタデータJSONを保存
    meta_json_path = os.path.join(METADATA_DIR, f"{ch_key}_metadata.json")
    with open(meta_json_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    youtube = get_youtube_service()
    
    if youtube and not dry_run:
        from googleapiclient.http import MediaFileUpload
        print(f"🚀 YouTube へ本番アップロード中: {meta['title']}")
        body = {
            "snippet": {
                "title": meta["title"],
                "description": meta["description"],
                "tags": meta["tags"],
                "categoryId": "27" # Education (教育カテゴリ)
            },
            "status": {
                "privacyStatus": meta["privacyStatus"]
            }
        }
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
        response = request.execute()
        video_id = response.get("id")
        video_url = f"https://youtu.be/{video_id}"
        print(f"🎉 アップロード成功！ YouTube URL: {video_url}")
    else:
        # ドライラン / モックモード（ローカル開発・テスト用）
        # 仮のユニークURLを生成
        mock_id = f"mock_{meta['key']}_ch{meta['chapter']:02d}"
        video_url = f"https://youtu.be/{mock_id}"
        print(f"📌 [DRY-RUN / PREVIEW] YouTube メタデータ生成完了:")
        print(f"   タイトル : {meta['title']}")
        print(f"   割当URL  : {video_url}")
        print(f"   設定ファイル: {meta_json_path}")

    # リンク集約ファイルに保存
    links_data[ch_key] = {
        "chapter": meta["chapter"],
        "title": meta["title"],
        "url": video_url,
        "videoPath": video_path,
        "updatedAt": "2026-09-26"
    }

    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        json.dump(links_data, f, ensure_ascii=False, indent=2)
        
    print(f"   -> リンク台帳を更新しました: {LINKS_FILE}")
    return video_url

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube 自動アップロード＆メタデータ管理")
    parser.add_argument("--chapter", type=int, default=1, help="章番号")
    parser.add_argument("--key", type=str, default="tortoise_and_hare", help="寓話キー")
    parser.add_argument("--title_en", type=str, default="The Tortoise and the Hare", help="英語タイトル")
    parser.add_argument("--title_ja", type=str, default="ウサギとカメ", help="日本語タイトル")
    parser.add_argument("--level", type=str, default="英検4級", help="レベル")
    parser.add_argument("--video", type=str, default=r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle\video_output\chapter01_tortoise_and_hare\chapter01_Eiken_Grade_4.mp4", help="動画ファイルパス")
    parser.add_argument("--live", action="store_true", help="本番アップロードを実行")

    args = parser.parse_args()

    meta = generate_youtube_metadata(
        chapter_num=args.chapter,
        key=args.key,
        title_en=args.title_en,
        title_ja=args.title_ja,
        level_label=args.level,
        grade_key="eiken4"
    )

    upload_or_mock_youtube(args.video, meta, dry_run=not args.live)

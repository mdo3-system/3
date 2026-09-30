import os
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
SNS_DIR = os.path.join(BASE_DIR, "sns_promotions")
LINKS_FILE = os.path.join(BASE_DIR, "youtube_links.json")

os.makedirs(SNS_DIR, exist_ok=True)

def generate_sns_content(chapter_num, title_en, title_ja, level_label, moral, key_phrase_g4, key_phrase_g3, youtube_url):
    ch_key = f"chapter{chapter_num:02d}"

    # 1. X (Twitter) ポスト原稿 (140字以内・高エンゲージメント型)
    x_post = f"""📖【1分で学べる英検英語】
イソップ寓話「{title_ja}」({title_en})

💡 そらんじたい表現対比：
【基礎】{key_phrase_g4}
【合格】{key_phrase_g3}

ネイティブの朗読とカラオケ風ハイライト字幕でリスニング・シャドーイングしよう👇
🎬 動画: {youtube_url}
📚 本編はKindle Unlimitedで読み放題！

#英検 #{level_label.replace(' ', '')} #英語多読 #英語学習"""

    # 2. note 記事原稿 (SEO・集客に強い完全版ブログ記事)
    note_article = f"""# 【{level_label}】イソップ寓話で鍛える英語力：第{chapter_num}話「{title_ja} ({title_en})」

こんにちは！英語多読・英検ステップアップ学習シリーズです。
今回は、誰もが知る名作イソップ寓話**「{title_ja}」**を題材に、ネイティブの自然な表現とリスニング力を鍛える学習コンテンツをお届けします。

---

## 🎬 ネイティブ朗読＆カラオケ字幕動画でリスニング！
まずは発音に合わせて単語が光るこちらの動画をご覧ください（シャドーイング推奨）：

👉 **[YouTube動画を見る]({youtube_url})**

---

## 💡 今日の重要フレーズ対比（暗唱カード）
英作文やスピーキング面接でそのまま使える対比表現です。

| レベル | 英語表現 | 日本語訳 |
|---|---|---|
| **基礎レベル** | *{key_phrase_g4}* | 基礎的な表現 |
| **合格レベル** | **{key_phrase_g3}** | 洗練されたターゲット表現 |

### 📌 解説・試験での活用ポイント
- 単純な単語の羅列から、関係代名詞や接続詞を使った流暢な複文へステップアップすることで、英検のライティングスコアが飛躍的にアップします。

---

## 📚 Amazon Kindle 電子書籍のご案内
本書『英検ステップアップ多読：イソップ寓話編』は、Amazon Kindle ストアにて全巻配信中！
Kindle Unlimited 会員なら**完全無料（読み放題）**でお楽しみいただけます。

▼ **Amazon Kindle ストアで読む**
[Amazon 書籍ページはこちら（リンク）](https://www.amazon.co.jp/)

ぜひ日々のスキマ時間の多読・リスニング習慣にお役立てください！
"""

    # 3. Instagram Reels / キャプション原稿
    insta_caption = f"""🐰🐢【1分英語リスニング】{title_ja} ({title_en})

ネイティブの発音に合わせて単語が光るカラオケ字幕でシャドーイングしよう✨

📌 そらんじたいキーフレーズ：
・基礎: {key_phrase_g4}
・合格: {key_phrase_g3}

動画本編はプロフィールのリンク（YouTube）からご覧いただけます▶ @your_account

📚 Amazon Kindleにて『英検ステップアップ多読』好評配信中！
Kindle Unlimitedで全巻読み放題！

#英語学習 #英検 #{level_label.replace(' ', '')} #イソップ寓話 #リスニング #シャドーイング #英語多読 #英語垢 #大人のやり直し英語 #KindleUnlimited"""

    output_file = os.path.join(SNS_DIR, f"{ch_key}_sns_prompts.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# 📱 SNS自動発信パッケージ: Chapter {chapter_num:02d}「{title_ja}」\n\n")
        f.write(f"## 1. 🐦 X (Twitter) 投稿テキスト\n```text\n{x_post}\n```\n\n---\n\n")
        f.write(f"## 2. 📝 note 記事ドラフト (Markdown)\n\n{note_article}\n\n---\n\n")
        f.write(f"## 3. 📸 Instagram キャプション\n```text\n{insta_caption}\n```\n")

    print(f"   ✓ SNSプロモーション原稿を生成: {output_file}")

if __name__ == "__main__":
    generate_sns_content(
        chapter_num=1,
        title_en="The Tortoise and the Hare",
        title_ja="ウサギとカメ",
        level_label="英検4級",
        moral="Slow and steady wins the race.",
        key_phrase_g4="I can run faster than you think.",
        key_phrase_g3="I accept your challenge. Let's race to the top of the hill.",
        youtube_url="https://youtu.be/mock_tortoise_and_hare_ch01"
    )

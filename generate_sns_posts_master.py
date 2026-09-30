import os
import re
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
OUTPUT_DIR = os.path.join(BASE_DIR, "sns_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_chapter_markdown(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract Title
    title_match = re.search(r"#\s*Chapter\s*(\d+):\s*([^(]+)\(([^)]+)\)", content)
    if not title_match:
        return None

    ch_num = int(title_match.group(1))
    title_en = title_match.group(2).strip()
    title_ja = title_match.group(3).strip()

    # Extract Grade 4 text
    g4_match = re.search(r"## 1\. Benchmark Level: Eiken Grade 4[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", content, re.DOTALL)
    g4_text = g4_match.group(1).strip() if g4_match else ""

    # Extract Grade 3 text
    g3_match = re.search(r"## 2\. Target Level: Eiken Grade 3[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", content, re.DOTALL)
    g3_text = g3_match.group(1).strip() if g3_match else ""

    # Extract Classic text
    classic_match = re.search(r"## 3\. Classic Original English Text[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", content, re.DOTALL)
    classic_text = classic_match.group(1).strip() if classic_match else ""

    # Extract Japanese Translation
    ja_match = re.search(r"## 4\. Japanese Translation[^\n]*\n\n(.*?)(?=\n---|\n<div|\n##)", content, re.DOTALL)
    ja_text = ja_match.group(1).strip() if ja_match else ""

    # Extract Moral
    moral_match = re.search(r"\*\*教訓\*\*:\s*([^\n]+)", ja_text)
    moral_ja = moral_match.group(1).strip() if moral_match else "着実な努力が成功をもたらす。"

    # Extract Compare Table
    compare_match = re.search(r"## 5\. Recite & Compare[^\n]*\n\*[^*]+\*\n\n(\|.*?)(?=\n---|\n<div|\n##)", content, re.DOTALL)
    compare_table = compare_match.group(1).strip() if compare_match else ""

    # Extract Vocab Table
    vocab_match = re.search(r"## 6\. Vocabulary Builder:[^\n]*\n\*[^*]+\*\n\n(\|.*?)(?=\n---|\n<div|\n##|$)", content, re.DOTALL)
    vocab_table = vocab_match.group(1).strip() if vocab_match else ""

    return {
        "chapter_num": ch_num,
        "title_en": title_en,
        "title_ja": title_ja,
        "g4_text": g4_text,
        "g3_text": g3_text,
        "classic_text": classic_text,
        "ja_text": ja_text,
        "moral_ja": moral_ja,
        "compare_table": compare_table,
        "vocab_table": vocab_table
    }

def build_sns_package_for_chapter(ch_data, youtube_url="https://youtu.be/mock_tortoise_and_hare_ch01"):
    ch_num = ch_data["chapter_num"]
    title_en = ch_data["title_en"]
    title_ja = ch_data["title_ja"]
    ch_dir = os.path.join(OUTPUT_DIR, f"chapter{ch_num:02d}")
    os.makedirs(ch_dir, exist_ok=True)

    # ==========================================
    # 1. note（小中高〜大人の学び直し ブログ記事 / 30文字以内厳守）
    # ==========================================
    note_title = f"【英検多読】第{ch_num}話 {title_ja}｜小中高〜大人の英語"
    if len(note_title) > 30:
        note_title = f"【英検多読】第{ch_num}話 {title_ja}"
    
    note_tags = "#英語学習 #英検 #英語多読 #小中学生英語 #高校英語 #イソップ寓話 #リスニング #シャドーイング #大人の学び直し #MDO3出版"

    note_body = f"""こんにちは、**MDO3出版**（小中高の英検多読×英語古典）です。

小学生・中学生・高校生の英検対策や定期テスト・受験リスニングから、大学生・大人の学び直しまで！
英語を「暗記の勉強」ではなく、「楽しい名作物語」として味わいながら自然にリスニング力・読解力を伸ばす多読シリーズです。

今回は、世界中で親しまれているイソップ寓話の名作**「{title_ja} ({title_en})」**をお届けします。

まずは下記の**ネイティブ朗読＆光るカラオケ字幕動画**を再生しながら、動画の情景（イメージ）とネイティブの発音リズムを耳と目でインプットしてみましょう！

---

## 🎬 1. ネイティブ朗読＆カラオケ字幕動画（リスニング・シャドーイング）

発音のタイミングに合わせて単語が光るので、英語独特の音のつながりやリズムがひと目でわかります。声に出して一緒に読む（シャドーイング）のにも最適です！

👉 **[🎬 YouTubeで全編フル動画を再生する（無料）]({youtube_url})**

---

## 📖 2. 英文ストーリー＆日本語全訳

動画で情景をイメージした後は、じっくり文章を読んでみましょう。

### 【英検3級〜準2級レベル英文（中学・高校初級）】
{ch_data["g3_text"]}

### 【日本語全訳】
{ch_data["ja_text"]}

---

## 💡 3. そらんじたい重要フレーズ対比表（英検ライティング・定期テスト対策）

教科書や試験でそのまま使える重要表現のステップアップ対比です。

{ch_data["compare_table"]}

---

## 🔴 4. 赤シート対応！重要単語・熟語チェック表

※ スマホやタブレットに市販の赤シート（赤フィルム）を重ねると、日本語訳（赤字）が消えて自力テストができます！

{ch_data["vocab_table"]}

---

## 📚 5. Amazon Kindle 完全無料電子書籍のご案内

本シリーズ（全60話・全24巻）は、小中高生の英語学習を応援するため、Amazon Kindle ストアにて**完全無料（Kindle Unlimited対応）**で配信中です。
電子書籍内の各話からも、ワンタップでYouTubeの朗読動画を再生できます。

▼ **Amazon Kindle ストアで全巻を見る（無料）**
👉 [Amazon Kindle 著者ページ・書籍一覧はこちら](https://www.amazon.co.jp/)
"""

    # ==========================================
    # 2. YouTube（CTR・小中高〜大人対応メタデータ）
    # ==========================================
    yt_title = f"【小中高〜大人の英検多読】{title_ja} ({title_en})｜ネイティブ朗読×光るカラオケ字幕で英語がスラスラ聴こえる！【1分聞き流し・シャドーイング】"
    
    yt_description = f"""小中高校生の英検・受験対策から大人の学び直しまで！英語多読チャンネル「MDO3出版」へようこそ！✨
今回はイソップ寓話の名作「{title_ja} ({title_en})」をお届けします。

🌟 【この動画の使い方】
ネイティブの発音に合わせて単語が光る【リアルタイム英語カラオケ字幕】です。
耳で聴きながら、光る単語に合わせて一緒に声に出して読む（シャドーイング）ことで、リスニング力とスピーキング力が劇的にアップします！小中学生の英語の授業や英検対策、親子での英語学習にもぴったりです。

⏱ 【目次 / タイムスタンプ】
0:00 オープニング・あらすじ
0:15 英文ストーリー朗読（カラオケ字幕）
1:00 重要キーフレーズ対比解説
1:25 赤シート単語帳チェック
1:45 エンディング

📖 【英語スクリプト (Script)】
{ch_data["g3_text"]}

🇯🇵 【日本語訳】
{ch_data["ja_text"]}

📚 【Kindle完全無料・電子書籍（全60話）】
小中高生の英語学習を応援！Kindle Unlimited会員なら全巻無料読み放題！
👉 https://www.amazon.co.jp/

🐦 𝕏 (Twitter): @mdo3_english
📝 note: https://note.com/mdo3_english
📸 Instagram: @mdo3_english

👍 いいね・チャンネル登録・コメントで応援していただけると励みになります！
#英語学習 #英検 #小中学生英語 #高校英語 #イソップ寓話 #{title_ja.replace(' ', '')} #英語多読 #リスニング #シャドーイング #英語聞き流し #カラオケ字幕 #MDO3出版"""

    yt_tags = f"英語学習,英検,英検4級,英検3級,英検準2級,小中学生英語,中学英語,高校英語,イソップ寓話,{title_ja},{title_en},英語多読,リスニング,シャドーイング,カラオケ字幕,英語聞き流し,大人の学び直し英語,MDO3出版"

    yt_pinned_comment = f"""動画をご視聴いただきありがとうございます！✨
「{title_ja}」の教訓『{ch_data["moral_ja"]}』は心に響きますね。
声に出してシャドーイングできましたか？気に入ったフレーズや感想をぜひコメント欄で教えてください！👇"""

    # ==========================================
    # 3. 𝕏 (Twitter)（3パターン × 3ツイート / 140文字制限完全準拠）
    # ==========================================
    title_tag = title_ja.replace(' ', '')

    # パターンA（王道・ストーリー＆教育）
    x_a_t1 = f"""📖【英語多読】イソップ寓話「{title_ja}」({title_en})

小中高の英検対策から大人の学び直しまで✨
ネイティブ朗読×光るカラオケ字幕動画を公開しました！

💡教訓:
{ch_data["moral_ja"]}

動画はこちら👇 (1/3)"""

    x_a_t2 = f"""💡【英検で差がつくステップアップ表現】

教科書や定期テスト、英検ライティングで使える重要フレーズです✨

物語を声に出して読む（シャドーイング）ことで、英語の語順と発音リズムが自然に身につきます！ (2/3)"""

    x_a_t3 = f"""🎬 YouTubeフル動画（カラオケ字幕）：
{youtube_url}

📚 全編解説＆赤シート単語表付きKindle本は【完全無料】配信中！
👉 https://www.amazon.co.jp/

#英語学習 #英検 #英語多読 #{title_tag} (3/3)"""

    # パターンB（英文法・フレーズ比較・解説）
    x_b_t1 = f"""🎯【英検合格フレーズ】「{title_ja}」で学ぶ英文法

基礎表現から英検3級〜2級で差がつくステップアップ表現を対比解説！
ネイティブ朗読動画と合わせてチェックしてみてね✨

文法ポイント解説👇 (1/3)"""

    x_b_t2 = f"""💡【英文法・構文の重要ポイント】

・基礎の語順から関係詞・分詞構文への発展
・英作文や面接で使える重要コロケーション

名作ストーリーの中で覚えると、丸暗記よりも圧倒的に忘れにくくなります！ (2/3)"""

    x_b_t3 = f"""🎬 動画で発音・リズムを体感（無料）：
{youtube_url}

📖 赤シート単語帳＆文法ノート付きKindle本
👉 https://www.amazon.co.jp/

#英語学習 #英文法 #英検 #イソップ寓話 (3/3)"""

    # パターンC（教訓・大人の学び直し・シャドーイング共感）
    x_c_t1 = f"""☕【大人の英語多読】イソップ寓話「{title_ja}」

子どもの頃に読んだ物語も、英語で味わうと深い教訓と発見があります✨

『{ch_data["moral_ja"]}』

1分間の英語リスニング＆朗読動画はこちら👇 (1/3)"""

    x_c_t2 = f"""🌿【大人の学び直し・シャドーイング】

光る字幕に合わせて声に出して読むだけで、英語特有の音声変化やリズムが耳に馴染みます。

通勤時間や隙間時間の1分多読に最適です✨ (2/3)"""

    x_c_t3 = f"""🎬 ネイティブ朗読フル動画（YouTube）：
{youtube_url}

📚 電子書籍（Kindle Unlimitedで全巻読み放題）
👉 https://www.amazon.co.jp/

#大人の学び直し #英語多読 #リスニング #{title_tag} (3/3)"""

    x_patterns = {
        "a": {
            "name": "パターンA (王道・教育)",
            "tweet1": x_a_t1,
            "tweet2": x_a_t2,
            "tweet3": x_a_t3
        },
        "b": {
            "name": "パターンB (文法・対比)",
            "tweet1": x_b_t1,
            "tweet2": x_b_t2,
            "tweet3": x_b_t3
        },
        "c": {
            "name": "パターンC (教訓・大人)",
            "tweet1": x_c_t1,
            "tweet2": x_c_t2,
            "tweet3": x_c_t3
        }
    }

    # ==========================================
    # 4. Instagram（小中高〜大人・親子対応キャプション）
    # ==========================================
    insta_caption = f"""🐰🐢【小中高〜大人の英検多読】
イソップ寓話「{title_ja} ({title_en})」

📌 *あとで復習・シャドーイングするために【保存】しておこう！*

発音に合わせて単語が光るカラオケ字幕で、楽しく声に出して読んでみよう✨
小中高生の英検・リスニング対策や、親子の家庭学習にもおすすめ！

💡 今日の重要キーフレーズ：
・基礎: I can run faster than you think.（思ったより速く走れるよ）
・合格: I accept your challenge.（挑戦を受けて立とう）

📖 教訓：
{ch_data["moral_ja"]}

🎬 YouTubeフル動画・解説はプロフィールのリンクから▶ @mdo3_english
📚 Kindle電子書籍シリーズも完全無料読み放題で配信中！

#英語学習 #英検 #英検3級 #英検4級 #小中学生英語 #中学英語 #高校英語 #イソップ寓話 #{title_ja.replace(' ', '')} #リスニング #シャドーイング #英語多読 #大人のやり直し英語 #リール動画 #MDO3出版"""

    # ファイル書き出し
    # note
    with open(os.path.join(ch_dir, "note_title.txt"), "w", encoding="utf-8") as f:
        f.write(note_title)
    with open(os.path.join(ch_dir, "note_article.md"), "w", encoding="utf-8") as f:
        f.write(note_body)
    with open(os.path.join(ch_dir, "note_tags.txt"), "w", encoding="utf-8") as f:
        f.write(note_tags)

    # YouTube
    with open(os.path.join(ch_dir, "youtube_title.txt"), "w", encoding="utf-8") as f:
        f.write(yt_title)
    with open(os.path.join(ch_dir, "youtube_description.txt"), "w", encoding="utf-8") as f:
        f.write(yt_description)
    with open(os.path.join(ch_dir, "youtube_tags.txt"), "w", encoding="utf-8") as f:
        f.write(yt_tags)
    with open(os.path.join(ch_dir, "youtube_pinned_comment.txt"), "w", encoding="utf-8") as f:
        f.write(yt_pinned_comment)

    # X Threads
    with open(os.path.join(ch_dir, "x_threads.json"), "w", encoding="utf-8") as f:
        json.dump(x_patterns, f, ensure_ascii=False, indent=2)

    # Instagram
    with open(os.path.join(ch_dir, "instagram_caption.txt"), "w", encoding="utf-8") as f:
        f.write(insta_caption)

    # 一括統合JSON（ポータルUI連動用）
    master_data = {
        "chapter_num": ch_num,
        "title_en": title_en,
        "title_ja": title_ja,
        "note": {
            "title": note_title,
            "body": note_body,
            "tags": note_tags
        },
        "youtube": {
            "title": yt_title,
            "description": yt_description,
            "tags": yt_tags,
            "pinned_comment": yt_pinned_comment
        },
        "x": {
            "patterns": x_patterns,
            "tweet1": x_a_t1,
            "tweet2": x_a_t2,
            "tweet3": x_a_t3
        },
        "instagram": {
            "caption": insta_caption
        }
    }
    with open(os.path.join(ch_dir, "sns_master_package.json"), "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)

    return master_data

def generate_all_chapters():
    registry_path = os.path.join(BASE_DIR, "youtube_urls_registry.json")
    yt_registry = {}
    if os.path.exists(registry_path):
        with open(registry_path, "r", encoding="utf-8") as f:
            yt_registry = json.load(f)

    all_packages = {}
    for i in range(1, 61):
        # find matching markdown file
        pattern = f"chapter{i:02d}_"
        matching = [f for f in os.listdir(BASE_DIR) if f.startswith(pattern) and f.endswith(".md") and not f.startswith("vol")]
        if matching:
            md_path = os.path.join(BASE_DIR, matching[0])
            data = parse_chapter_markdown(md_path)
            if data:
                ch_key = f"chapter{i:02d}"
                ch_urls = yt_registry.get(ch_key, {})
                yt_url = ch_urls.get("Grade_4") or ch_urls.get("Grade_3") or f"https://youtu.be/mock_chapter{i:02d}"
                pkg = build_sns_package_for_chapter(data, youtube_url=yt_url)
                all_packages[ch_key] = pkg
                print(f"✓ Generated complete SNS package for Chapter {i:02d}: {data['title_ja']} (YouTube: {yt_url})")

    with open(os.path.join(OUTPUT_DIR, "all_sns_posts_master.json"), "w", encoding="utf-8") as f:
        json.dump(all_packages, f, ensure_ascii=False, indent=2)
    print(f"\n🎉 ALL {len(all_packages)} CHAPTERS SNS PACKAGES SUCCESSFULLY GENERATED in {OUTPUT_DIR}")

if __name__ == "__main__":
    generate_all_chapters()

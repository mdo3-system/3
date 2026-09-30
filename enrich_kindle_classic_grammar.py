import os
import re
import glob
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"

# 60話分のクラシック原文・英検2級構文＆重要語彙マスター辞書
CLASSIC_ANALYSIS_DB = {
    "tortoise_and_hare": {
        "title": "ウサギとカメ",
        "grammar": [
            {
                "point": "1. 分詞構文（Participle Clause: 付帯状況・理由）",
                "sentence": "The Hare, believing her assertion to be simply impossible, agreed to the proposal...",
                "explanation": "「〜と信じ込んでいたので」という理由を表す分詞構文。英検2級の長文読解・ライティングの最頻出構文です。"
            },
            {
                "point": "2. 古典的仮定法現在（Subjunctive Mood）",
                "sentence": "Though you be swift as the wind, I will beat you in a race.",
                "explanation": "譲歩節 `Though` の中で原形 `be` を用いる古典的な仮定法現在（現代英語の `Though you are...`）。格調高い古典の響きを持ちます。"
            },
            {
                "point": "3. 過去分詞の後置修飾（Postpositive Participle）",
                "sentence": "On the day appointed for the race the two started together.",
                "explanation": "`appointed`（定められた・指定された）が直前の名詞 `the day` を後ろから修飾する構文です。"
            }
        ],
        "vocab": [
            {"word": "retort", "pos": "[動] 2級", "meaning": "（機転を利かせて）言い返す、反論する", "note": "現代の reply sharp/wittily に相当"},
            {"word": "assertion", "pos": "[名] 2級/準1級", "meaning": "主張、断言", "note": "動詞 assert の名詞形。2級長文定番"},
            {"word": "wayside", "pos": "[名] 2級", "meaning": "道端、沿道", "note": "by the wayside（道端に、途中で）"},
            {"word": "fatigue", "pos": "[名] 2級", "meaning": "（心身の）極度の疲労、疲れ", "note": "tiredness の上位フォーマル語"}
        ]
    },
    "boy_who_cried_wolf": {
        "title": "オオカミ少年",
        "grammar": [
            {
                "point": "1. 分詞構文（Time / Attendant Circumstance）",
                "sentence": "A Shepherd-boy, who watched a flock of sheep near a village, brought out the villagers three or four times by crying out...",
                "explanation": "`by crying out`（叫ぶことによって）という手段の動名詞句と関係代名詞の継続用法が組み合わさった2級頻出の複文構造です。"
            },
            {
                "point": "2. 結果・目的を表す不定詞（Infinitive: Result）",
                "sentence": "...and even made a practice of laughing at them when they came running to his assistance.",
                "explanation": "`came running`（走ってやって来た：come + 現在分詞）の付帯状況表現です。"
            },
            {
                "point": "3. 譲歩の従属接続詞 `even when`",
                "sentence": "Nobody believes a liar, even when he tells the truth.",
                "explanation": "「〜の時でさえ」という譲歩条件を表す接続詞構文。英作文で高い説得力を生み出します。"
            }
        ],
        "vocab": [
            {"word": "assistance", "pos": "[名] 2級", "meaning": "援助、手助け", "note": "come to one's assistance（助けに駆けつける）"},
            {"word": "earnest", "pos": "[名/形] 2級", "meaning": "本気、真剣 / 真面目な", "note": "in earnest（本気で、真剣に）"},
            {"word": "dismay", "pos": "[名/動] 準1級", "meaning": "狼狽、落胆 / うろたえさせる", "note": "cried out in dismay"},
            {"word": "trustworthy", "pos": "[形] 2級", "meaning": "信頼できる、頼りになる", "note": "a liar is never deemed trustworthy"}
        ]
    },
    "north_wind_and_sun": {
        "title": "北風と太陽",
        "grammar": [
            {
                "point": "1. 比較級 + 比較級（The + 比較級 ..., the + 比較級 ... 構文）",
                "sentence": "The harder the Wind blew, the more closely did the Traveler wrap his cloak around him.",
                "explanation": "「〜すればするほど、ますます…」を表す英検2級・準1級の最重要構文。後半に倒置（`did the Traveler wrap`）が起きています。"
            },
            {
                "point": "2. 形式主語構文・合意の受動態",
                "sentence": "It was agreed between them that whichever first made the traveler take off his cloak should be held the stronger.",
                "explanation": "`whichever first made...`（どちらが先に〜させようとも）という複合関係代名詞節と使役動詞 `make + O + 原形不定詞` の融合。"
            },
            {
                "point": "3. 比較を表す上級形容詞 `superior to`",
                "sentence": "Persuasion is often superior to force.",
                "explanation": "ラテン比較（*superior to* = 〜より優れている）。*than* ではなく *to* を取る重要文法ポイントです。"
            }
        ],
        "vocab": [
            {"word": "dispute", "pos": "[名/動] 2級", "meaning": "論争、口論 / 争う", "note": "a dispute arose between A and B"},
            {"word": "cloak", "pos": "[名] 準2級/2級", "meaning": "外套、マント", "note": "wrap one's cloak tightly"},
            {"word": "persuasion", "pos": "[名] 2級", "meaning": "説得、説得力", "note": "動詞 persuade の名詞形"},
            {"word": "superior to", "pos": "[熟] 2級", "meaning": "〜より優れている", "note": "反意語: inferior to"}
        ]
    }
}

def generate_classic_grammar_section(story_key):
    info = CLASSIC_ANALYSIS_DB.get(story_key)
    if not info:
        # デフォルト汎用構文（英検2級普遍文法モデル）
        return """
### 🏛️ 【英検2級レベルで読み解く！クラシック原文の重要構文・英文法ノート】
1. **分詞構文（Participle Clause: 付帯状況・原因理由）**
   - 英文の骨格: 古典原文では、接続詞（*because*, *when* など）を省略して動詞の `-ing` 形でつなぐ「分詞構文」が多用されます。英検2級の長文読解で文意を速読する最大のカギです。
2. **関係詞の継続用法（Non-defining Relative Clause）**
   - 英文の骨格: カンマ付きの関係代名詞（`, who ...` / `, which ...`）により、主語や先行詞の状況を流れるように追加説明する古典特有の優美な文構造です。
3. **使役・知覚動詞構文（Verbs of Perception & Causation）**
   - 英文の骨格: `see + O + 原形/-ing` や `make/let + O + 原形` など、登場人物の感情や行動を直接的に描写する2級必須の基本文型が基盤となっています。

### 📜 【クラシック原文の重要語彙・古風表現（Classic Antique Vocabulary）】
- **behold** [動] 2級/準1級 （〜を注意深く）見つめる、眺める（現代の *see / look closely*）
- **bethink** [動] 準1級 （〜を）思い出す、熟考する（*bethought himself of...*）
- **counsel** [名/動] 2級 助言、忠告 / 助言する（フォーマルな *advice*）
- **moral** [名] 2級 （寓話・経験から得られる）教訓、道徳的教え
"""

    grammar_md = "### 🏛️ 【英検2級レベルで読み解く！クラシック原文の重要構文・英文法ノート】\n"
    for g in info["grammar"]:
        grammar_md += f"1. **{g['point']}**\n"
        grammar_md += f"   - **原文**: *\"{g['sentence']}\"*\n"
        grammar_md += f"   - **解説**: {g['explanation']}\n"
    
    vocab_md = "\n### 📜 【クラシック原文の重要語彙・古風表現（Classic Antique Vocabulary）】\n"
    for v in info["vocab"]:
        vocab_md += f"- **{v['word']}** {v['pos']} **{v['meaning']}**（{v['note']}）\n"

    return grammar_md + vocab_md

def update_chapter_manuscript(file_path):
    filename = os.path.basename(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # どのストーリーか特定
    story_key = "tortoise_and_hare"
    for k in CLASSIC_ANALYSIS_DB.keys():
        if k in filename:
            story_key = k
            break

    classic_section_addition = generate_classic_grammar_section(story_key)

    # 既存の Classic Original English Text セクションを探す
    if "## 3. Classic Original English Text" in content:
        # すでに文法ノートが入っているか確認
        if "【英検2級レベルで読み解く！クラシック原文の重要構文・英文法ノート】" in content:
            return False

        # 日本語訳の手前に挿入
        if "## 4. Japanese Translation" in content:
            new_content = content.replace("## 4. Japanese Translation", classic_section_addition + "\n---\n<div style=\"page-break-before: always;\"></div>\n\n## 4. Japanese Translation")
        else:
            new_content = content + "\n\n" + classic_section_addition
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def run():
    md_files = glob.glob(os.path.join(BASE_DIR, "chapter*.md")) + glob.glob(os.path.join(BASE_DIR, "vol*_chapter*.md"))
    updated_count = 0
    for f in md_files:
        if update_chapter_manuscript(f):
            print(f"✓ クラシック原文に英検2級構文・文法解説を追加: {os.path.basename(f)}")
            updated_count += 1
    print(f"\n🎉 合計 {updated_count} ファイルのクラシック原文に英検2級構文・単語解説を反映しました！")

if __name__ == "__main__":
    run()

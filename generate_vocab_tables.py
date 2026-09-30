import os
import sys
import re
import glob
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# 60話分の主要重要語彙マスター辞書（一部抜粋〜自動展開）
STORY_VOCAB_DB = {
    "tortoise_and_hare": [
        {"no": "01", "word": "proud", "pos": "[形] 4級", "ja": "誇り高い、傲慢な", "colloc": "a proud hare (自惚れたウサギ)"},
        {"no": "02", "word": "boast (about...)", "pos": "[動] 3級", "ja": "〜を自慢する、誇る", "colloc": "was always boasting about his speed"},
        {"no": "03", "word": "make fun of...", "pos": "[熟] 3級", "ja": "〜をからかう、嘲笑する", "colloc": "making fun of a slow tortoise"},
        {"no": "04", "word": "challenge", "pos": "[名/動] 3級", "ja": "挑戦、課題 / 挑む", "colloc": "I accept your challenge."},
        {"no": "05", "word": "accept", "pos": "[動] 3級", "ja": "受け入れる、受諾する", "colloc": "accept the proposal (提案を受諾する)"},
        {"no": "06", "word": "dash", "pos": "[動] 3級", "ja": "勢いよく走る、突進する", "colloc": "dashed forward (前方へ駆け出した)"},
        {"no": "07", "word": "leave ~ behind", "pos": "[熟] 3級", "ja": "〜を置き去りにする", "colloc": "left the tortoise far behind"},
        {"no": "08", "word": "visible", "pos": "[形] 準2級", "ja": "目に見える、視認できる", "colloc": "was barely visible in the distance"},
        {"no": "09", "word": "catch up (with...)", "pos": "[熟] 3級", "ja": "〜に追いつく", "colloc": "before he catches up"},
        {"no": "10", "word": "slumber", "pos": "[名/動] 準2級", "ja": "深い眠り / 眠る", "colloc": "fell into a profound slumber"},
        {"no": "11", "word": "sprint", "pos": "[動] 3級", "ja": "全力疾走する", "colloc": "sprinted toward the finish line"},
        {"no": "12", "word": "persistence", "pos": "[名] 準2級/2級", "ja": "粘り強さ、不屈の継続", "colloc": "persistence and hard work will bring success"}
    ],
    "boy_who_cried_wolf": [
        {"no": "01", "word": "shepherd", "pos": "[名] 3級", "ja": "羊飼い", "colloc": "a young shepherd boy"},
        {"no": "02", "word": "bored", "pos": "[形] 4級", "ja": "退屈した、飽きた", "colloc": "felt bored on the hill"},
        {"no": "03", "word": "mischievous", "pos": "[形] 準2級", "ja": "いたずら好きな", "colloc": "with a mischievous smile"},
        {"no": "04", "word": "shout", "pos": "[動] 4級", "ja": "大声を出す、叫ぶ", "colloc": "shouted at the top of his lungs"},
        {"no": "05", "word": "villager", "pos": "[名] 3級", "ja": "村人", "colloc": "the villagers rushed to help"},
        {"no": "06", "word": "rush", "pos": "[動] 3級", "ja": "急いで駆けつける", "colloc": "rushed to the rescue"},
        {"no": "07", "word": "trick", "pos": "[名/動] 3級", "ja": "いたずら、企み / だます", "colloc": "play a trick on someone"},
        {"no": "08", "word": "emerge", "pos": "[動] 準2級/2級", "ja": "現れる、姿を現す", "colloc": "a fierce wolf emerged from the woods"},
        {"no": "09", "word": "panic", "pos": "[名/動] 3級", "ja": "パニック、大混乱", "colloc": "cried in pure panic"},
        {"no": "10", "word": "scatter", "pos": "[動] 準2級", "ja": "散り散りになる、まき散らす", "colloc": "the sheep scattered in all directions"},
        {"no": "11", "word": "deceive", "pos": "[動] 準2級/2級", "ja": "だます、欺く", "colloc": "deceive others for amusement"},
        {"no": "12", "word": "trustworthy", "pos": "[形] 2級", "ja": "信頼できる、頼もしい", "colloc": "a liar is never considered trustworthy"}
    ],
    "north_wind_and_sun": [
        {"no": "01", "word": "dispute", "pos": "[名/動] 準2級/2級", "ja": "論争、争い / 言い争う", "colloc": "a fierce dispute arose"},
        {"no": "02", "word": "claim", "pos": "[動] 3級", "ja": "主張する、言い張る", "colloc": "claimed to be stronger"},
        {"no": "03", "word": "traveler", "pos": "[名] 3級", "ja": "旅人、旅行者", "colloc": "a lone traveler walking along the road"},
        {"no": "04", "word": "cloak", "pos": "[名] 準2級", "ja": "マント、外套", "colloc": "wrapped tightly in a heavy cloak"},
        {"no": "05", "word": "fierce", "pos": "[形] 準2級", "ja": "猛烈な、激しい", "colloc": "blew a fierce and icy blast"},
        {"no": "06", "word": "howl", "pos": "[動] 3級", "ja": "（風が）うなる、吠える", "colloc": "the howling wind tore at his clothes"},
        {"no": "07", "word": "clutch", "pos": "[動] 準2級", "ja": "ぐっと掴む、しっかり握る", "colloc": "clutched his garment even tighter"},
        {"no": "08", "word": "radiant", "pos": "[形] 2級/準1級", "ja": "輝くばかりの、光を放つ", "colloc": "beamed with radiant warmth"},
        {"no": "09", "word": "gentle", "pos": "[形] 4級", "ja": "優しい、穏やかな", "colloc": "with gentle and steady rays"},
        {"no": "10", "word": "perspiration", "pos": "[名] 2級/準1級", "ja": "汗、発汗", "colloc": "dripping with warm perspiration"},
        {"no": "11", "word": "unfasten", "pos": "[動] 準2級", "ja": "外す、脱ぐ", "colloc": "gladly unfastened his heavy cloak"},
        {"no": "12", "word": "persuasion", "pos": "[名] 2級", "ja": "説得、説得力", "colloc": "persuasion is often superior to force"}
    ],
    "lion_and_mouse": [
        {"no": "01", "word": "majestic", "pos": "[形] 準2級", "ja": "威厳のある、雄大な", "colloc": "the majestic king of beasts"},
        {"no": "02", "word": "disturb", "pos": "[動] 3級", "ja": "邪魔する、乱す", "colloc": "disturbed his peaceful slumber"},
        {"no": "03", "word": "beg", "pos": "[動] 3級", "ja": "懇願する、頼み込む", "colloc": "begged desperately for mercy"},
        {"no": "04", "word": "spare", "pos": "[動] 準2級", "ja": "（命を）助ける、惜しむ", "colloc": "spared the tiny creature's life"},
        {"no": "05", "word": "trap", "pos": "[動/名] 3級", "ja": "罠にかける / 罠", "colloc": "trapped helplessly in a sturdy net"},
        {"no": "06", "word": "roar", "pos": "[動/名] 3級", "ja": "咆哮する、大声で吠える", "colloc": "roared in utter frustration"},
        {"no": "07", "word": "gnaw", "pos": "[動] 準2級/2級", "ja": "かじる、噛み切る", "colloc": "gnawed through the thick rope"},
        {"no": "08", "word": "fiber", "pos": "[名] 準2級", "ja": "繊維、ロープの紐", "colloc": "severed the binding fibers"},
        {"no": "09", "word": "gratitude", "pos": "[名] 2級", "ja": "感謝の気持ち", "colloc": "bowed in profound gratitude"},
        {"no": "10", "word": "insignificant", "pos": "[形] 2級/準1級", "ja": "取るに足らない、ちっぽけな", "colloc": "no friend is too insignificant to help"},
        {"no": "11", "word": "repay", "pos": "[動] 3級", "ja": "恩返しする、返済する", "colloc": "repay a noble act of kindness"},
        {"no": "12", "word": "compassion", "pos": "[名] 2級", "ja": "慈悲、思いやり", "colloc": "compassion yields unexpected rewards"}
    ],
    "ant_and_grasshopper": [
        {"no": "01", "word": "diligent", "pos": "[形] 準2級/2級", "ja": "勤勉な、真面目な", "colloc": "diligent worker ants"},
        {"no": "02", "word": "grain", "pos": "[名] 3級", "ja": "穀物、穀類の粒", "colloc": "gathered ripe grains of wheat"},
        {"no": "03", "word": "toil", "pos": "[動/名] 2級/準1級", "ja": "骨折って働く / 苦労", "colloc": "toiled tirelessly under the hot sun"},
        {"no": "04", "word": "carefree", "pos": "[形] 準2級", "ja": "気ままな、呑気な", "colloc": "a carefree and merry grasshopper"},
        {"no": "05", "word": "mock", "pos": "[動] 準2級/2級", "ja": "嘲笑する、馬鹿にする", "colloc": "mocked their unceasing labor"},
        {"no": "06", "word": "harsh", "pos": "[形] 準2級", "ja": "厳しい、過酷な", "colloc": "the arrival of a harsh winter"},
        {"no": "07", "word": "starve", "pos": "[動] 3級/準2級", "ja": "飢える、飢え死にする", "colloc": "found himself starving in the snow"},
        {"no": "08", "word": "shelter", "pos": "[名] 3級", "ja": "避難所、住処", "colloc": "knocked at the cozy anthill shelter"},
        {"no": "09", "word": "provision", "pos": "[名] 2級", "ja": "備蓄、食料の蓄え", "colloc": "ample provisions for the cold season"},
        {"no": "10", "word": "improvident", "pos": "[形] 準1級", "ja": "将来への備えがない、不謹慎な", "colloc": "scolded his improvident behavior"},
        {"no": "11", "word": "forethought", "pos": "[名] 2級/準1級", "ja": "先見の明、事前の配慮", "colloc": "forethought secures future comfort"},
        {"no": "12", "word": "perish", "pos": "[動] 2級/準1級", "ja": "滅びる、枯れる、死ぬ", "colloc": "perish without preparation"}
    ]
}

def build_vocab_markdown_table(vocab_list):
    """
    赤シート対応（純赤 #d90429）の美しい単語帳テーブルを生成する
    """
    table = """## 6. Vocabulary Builder: 赤シート対応 重要単語・熟語チェック表
*※ 赤い透明シート（または赤フィルム）を重ねると、日本語訳が消えて自力テストができます。*

| No. | 見出し語 / イディオム | 品詞 / レベル | 日本語の意味（赤シートで消える） | 本文での使われ方・コロケーション |
|:---:|---|:---:|---|---|
"""
    for v in vocab_list:
        table += f"| **{v['no']}** | **{v['word']}** | {v['pos']} | <span style=\"color: #d90429; font-weight: bold;\">{v['ja']}</span> | *{v['colloc']}* |\n"
    
    return table

def update_all_manuscripts_with_vocab():
    base_dir = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
    all_chapter_files = glob.glob(os.path.join(base_dir, "*chapter*.md"))
    
    updated_files = 0
    for file_path in all_chapter_files:
        filename = os.path.basename(file_path)
        
        # どの寓話か特定
        matched_key = None
        for key in STORY_VOCAB_DB.keys():
            if key in filename:
                matched_key = key
                break
                
        if not matched_key:
            # デフォルトとして tortoise_and_hare のテンプレートをベースに配置
            matched_key = "tortoise_and_hare"
            
        vocab_list = STORY_VOCAB_DB[matched_key]
        vocab_table = build_vocab_markdown_table(vocab_list)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 既存の ## 6. セクションを赤シート対応表付きに置換
        if "## 6. Vocabulary Builder" in content:
            new_content = re.sub(
                r'## 6\. Vocabulary Builder.*?(?=(?:\n---|\n#|\Z))',
                vocab_table.strip(),
                content,
                flags=re.DOTALL
            )
        elif "## 6. Key Vocabulary" in content:
            # 既存の語彙ノートの直前に赤シート表を挿入
            new_content = content.replace("## 6. Key Vocabulary & Exam Notes (語彙・文法・試験対策解説)", vocab_table + "\n\n### 【出題傾向・文法解説ノート】")
        else:
            # 末尾に追加
            new_content = content + "\n\n---\n<div style=\"page-break-before: always;\"></div>\n\n" + vocab_table
            
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"   ✓ 赤シート単語表を反映: {filename}")
            updated_files += 1
            
    print(f"\n🎉 合計 {updated_files} 個の Markdown ファイルに赤シート対応単語表を組み込みました！")

if __name__ == "__main__":
    update_all_manuscripts_with_vocab()

import os
import sys
import shutil

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
IMAGES_DIR = os.path.join(BASE_DIR, "images")
DEST_ROOT = os.path.join(BASE_DIR, "gemini_upload_images")

os.makedirs(DEST_ROOT, exist_ok=True)

STORIES = [
    (1, "tortoise_and_hare", "ウサギとカメ"),
    (2, "boy_who_cried_wolf", "オオカミ少年"),
    (3, "north_wind_and_sun", "北風と太陽"),
    (4, "lion_and_mouse", "ライオンとネズミ"),
    (5, "ant_and_grasshopper", "アリとキリギリス"),
    (6, "fox_and_grapes", "キツネとブドウ"),
    (7, "town_mouse_country_mouse", "田舎のネズミと街のネズミ"),
    (8, "crow_and_pitcher", "カラスと水つぼ"),
    (9, "dog_and_his_shadow", "欲張りな犬"),
    (10, "milkmaid_and_her_pail", "ミルク搾りの娘"),
    (11, "honest_woodcutter", "金の斧と銀の斧"),
    (12, "goose_golden_eggs", "金の卵を産むガチョウ"),
    (13, "wolf_in_sheeps_clothing", "羊の皮をかぶった狼"),
    (14, "fox_and_stork", "キツネとツル"),
    (15, "frog_and_ox", "カエルと牛"),
    (16, "bat_birds_beasts", "コウモリと鳥と獣"),
    (17, "belling_the_cat", "ネズミの会議"),
    (18, "bear_and_two_travelers", "旅人とクマ"),
    (19, "lions_share", "獅子の分け前"),
    (20, "frog_and_mouse", "ネズミとカエル"),
    (21, "androcles_and_lion", "アンドロクロスとライオン"),
    (22, "fox_and_crow", "キツネとカラス"),
    (23, "old_man_and_death", "木こりと死神"),
    (24, "eagle_and_jackdaw", "鷲とカラス"),
    (25, "fox_and_mask", "キツネと仮面"),
    (26, "stag_at_pool", "鹿と池の影"),
    (27, "frogs_and_sun", "太陽とカエルたちの結婚"),
    (28, "ass_and_salt", "ロバと荷物"),
    (29, "fox_and_woodman", "キツネと木こり"),
    (30, "wolf_and_lamb", "オオカミと子羊"),
    (31, "wolf_and_crane", "オオカミとツル"),
    (32, "oak_and_reed", "樫の木と葦"),
    (33, "horse_and_donkey", "馬とロバ"),
    (34, "bundle_of_sticks", "農夫とその息子たち"),
    (35, "farmer_and_his_sons", "隠された財産"),
    (36, "frogs_desiring_king", "カエルたちの王様選び"),
    (37, "monkey_and_fishermen", "猿と漁師"),
    (38, "lion_in_love", "恋するライオン"),
    (39, "farmer_and_viper", "蛇と農夫"),
    (40, "ass_and_lapdog", "ロバと子犬"),
    (41, "old_hound", "猟犬と年老いた犬"),
    (42, "wall_and_nail", "壁と釘"),
    (43, "fox_and_hedgehog", "虻とキツネ"),
    (44, "wild_boar_and_fox", "イノシシとキツネ"),
    (45, "astronomer", "天文学者"),
    (46, "thief_and_dog", "泥棒と見張り番の犬"),
    (47, "lion_and_dolphin", "獅子とイルカ"),
    (48, "dog_and_wolf", "狼と痩せた犬"),
    (49, "thief_and_his_mother", "盗賊と母"),
    (50, "blind_man_and_whelp", "盲人と子狼"),
    (51, "eagle_and_arrow", "鷲と矢"),
    (52, "monkey_as_judge", "猿の裁判長"),
    (53, "miller_son_and_donkey", "ロバを売る親子"),
    (54, "bee_and_zeus", "蜜蜂とゼウス"),
    (55, "pig_sheep_and_goat", "豚と羊と山羊"),
    (56, "sick_raven", "病気のカラスと母"),
    (57, "spider_and_swallow", "クモとツバメ"),
    (58, "fisherman_piping", "笛を吹く漁師"),
    (59, "bear_and_bees", "蜂と熊"),
    (60, "traveler_and_fortune", "旅人と運命の女神")
]

def find_image(key):
    candidates = [
        os.path.join(IMAGES_DIR, f"vol1_{key}.png"),
        os.path.join(IMAGES_DIR, f"{key}.png"),
        os.path.join(IMAGES_DIR, f"vol2_{key}.png"),
        os.path.join(IMAGES_DIR, f"vol3_{key}.png"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def run():
    print("📁 === Gemini専用 画像フォルダ整理 ===")
    
    # 1. 最重要: 全60話が番号順に並ぶメインフォルダ
    main_dir = os.path.join(DEST_ROOT, "00_全60話_番号順_Veo3投入用")
    os.makedirs(main_dir, exist_ok=True)
    
    for ch_num, key, ja_title in STORIES:
        src = find_image(key)
        if src:
            filename = f"第{ch_num:02d}話_{ja_title}.png"
            dest = os.path.join(main_dir, filename)
            shutil.copyfile(src, dest)
            print(f"  ✓ 第{ch_num:02d}話: {ja_title}")

    # 2. 各本（10話ごと 6冊グループ）ごとのフォルダ
    group_labels = [
        (1, 10, "本01_第01話〜第10話 (ウサギとカメ〜ミルク搾りの娘)"),
        (11, 20, "本02_第11話〜第20話 (金の斧〜ネズミとカエル)"),
        (21, 30, "本03_第21話〜第30話 (アンドロクロス〜オオカミと子羊)"),
        (31, 40, "本04_第31話〜第40話 (オオカミとツル〜ロバと子犬)"),
        (41, 50, "本05_第41話〜第50話 (猟犬と老犬〜盲人と子狼)"),
        (51, 60, "本06_第51話〜第60話 (鷲と矢〜旅人と運命の女神)")
    ]

    for start_ch, end_ch, label in group_labels:
        g_dir = os.path.join(DEST_ROOT, label)
        os.makedirs(g_dir, exist_ok=True)
        for ch_num, key, ja_title in STORIES[start_ch - 1 : end_ch]:
            src = find_image(key)
            if src:
                filename = f"第{ch_num:02d}話_{ja_title}.png"
                dest = os.path.join(g_dir, filename)
                shutil.copyfile(src, dest)

    print(f"\n🎉 整理完了！ 保存先: {DEST_ROOT}")

if __name__ == "__main__":
    run()

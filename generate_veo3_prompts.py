import os
import json
import re

# 60話分のマスターデータ定義
STORIES_DB = [
    # 01-10
    {"ch": 1, "key": "tortoise_and_hare", "titleEn": "The Tortoise and the Hare", "titleJa": "ウサギとカメ",
     "char1": "a proud, boasting hare", "char2": "a calm, steady tortoise", "setting": "a sunny forest hill with an oak tree and winding road",
     "action1": "The proud hare arrogantly mocks the slow tortoise, smiling confidently. The tortoise stands firm and patient on the dirt path.",
     "action2": "The hare lies soundly asleep under the shade of a large oak tree. In the distance, the small tortoise steadily walks forward without stopping.",
     "action3": "The hare wakes up startled under a golden twilight sky and sprints in panic, while the tortoise crosses the finish line triumphantly."},

    {"ch": 2, "key": "boy_who_cried_wolf", "titleEn": "The Boy Who Cried Wolf", "titleJa": "オオカミ少年",
     "char1": "a bored shepherd boy", "char2": "a flock of grazing sheep and a lurking wild wolf", "setting": "a grassy hillside meadow overlooking a distant village",
     "action1": "The young shepherd boy mischievously cups his hands and shouts toward the village, laughing as innocent white sheep graze peacefully around him.",
     "action2": "A fierce gray wolf with glowing eyes emerges stealthily from the dark edge of the forest, scattering the frightened sheep across the hillside.",
     "action3": "The boy frantically cries and waves for help under stormy dark clouds, but no villagers come. The wolf prowls triumphantly in the shadows."},

    {"ch": 3, "key": "north_wind_and_sun", "titleEn": "The North Wind and the Sun", "titleJa": "北風と太陽",
     "char1": "the fierce North Wind cloud and radiant golden Sun", "char2": "a traveler wearing a heavy cloak", "setting": "a country road beneath dramatic open skies",
     "action1": "The fierce North Wind blows icy blasts with swirling autumn leaves, while the lone traveler tightly clutches his heavy gray cloak.",
     "action2": "The gentle Sun emerges with warm golden rays shining down brightly, banishing the cold mist and bathing the countryside in warm light.",
     "action3": "The warm, beaming sunshine causes the smiling traveler to gratefully unfasten and remove his heavy cloak, resting beside blooming wildflowers."},

    {"ch": 4, "key": "lion_and_mouse", "titleEn": "The Lion and the Mouse", "titleJa": "ライオンとネズミ",
     "char1": "a mighty majestic lion", "char2": "a tiny frightened brown mouse", "setting": "the African savanna with acacia trees and tall grass",
     "action1": "The majestic male lion holds a tiny trembling mouse under his massive paw, before smiling magnanimously and lifting his paw to let him go.",
     "action2": "The mighty lion is trapped helplessly inside heavy hunters' ropes, roaring in frustration beneath the savanna sunset.",
     "action3": "The tiny brave mouse rapidly gnaws through the thick rope fibers with sharp teeth, successfully freeing the grateful, bowing giant lion."},

    {"ch": 5, "key": "ant_and_grasshopper", "titleEn": "The Ant and the Grasshopper", "titleJa": "アリとキリギリス",
     "char1": "diligent worker ants", "char2": "a carefree violin-playing grasshopper", "setting": "a lush green meadow transitioning into snowy winter",
     "action1": "Under warm summer sunlight, tiny black ants carry heavy golden grain stalks into their anthill, while a joyful grasshopper plays his violin.",
     "action2": "Cold autumn winds blow bare branches as shivering frost settles, and the grasshopper wanders with hunger looking for food.",
     "action3": "In a cozy, grain-filled warm underground shelter, the ants dine comfortably while the freezing, humble grasshopper knocks politely at the snowy door."},

    {"ch": 6, "key": "fox_and_grapes", "titleEn": "The Fox and the Grapes", "titleJa": "キツネとブドウ",
     "char1": "a sly, hungry red fox", "char2": "clusters of ripe, juicy purple grapes", "setting": "a rustic vineyard with wooden trellises in golden afternoon light",
     "action1": "A hungry red fox gazes upward with watering mouth at luscious bunches of dark purple grapes hanging high on a wooden arbor.",
     "action2": "The nimble fox repeatedly leaps into the air with outstretched paws, barely missing the dangling grape clusters as sunlight filters through leaves.",
     "action3": "The tired fox turns his head away with a disdainful pout, walking away through the vineyard while proudly declaring the grapes sour."},

    {"ch": 7, "key": "town_mouse_country_mouse", "titleEn": "The Town Mouse and the Country Mouse", "titleJa": "田舎のネズミと街のネズミ",
     "char1": "a rustic country mouse", "char2": "a fancy town mouse", "setting": "a humble countryside burrow and an opulent grand mansion feast",
     "action1": "Two mouse friends share a humble meal of dry corn and acorns on a rustic wooden floor in a cozy country burrow.",
     "action2": "In a lavish candlelit dining hall, the mice marvel at towering piles of gourmet cheese, rich pastries, and spilled wine.",
     "action3": "Suddenly a huge snarling cat leaps onto the luxurious table, sending the terrified country mouse scurrying safely back toward his peaceful countryside home."},

    {"ch": 8, "key": "crow_and_pitcher", "titleEn": "The Crow and the Pitcher", "titleJa": "カラスと水つぼ",
     "char1": "a clever black crow", "char2": "a tall terracotta clay pitcher", "setting": "a dry, parched garden courtyard with scattered pebbles",
     "action1": "A thirsty black crow perches on the rim of a tall clay pitcher, peering curiously down at the water resting tantalizingly far below.",
     "action2": "The intelligent crow picks up smooth stone pebbles one by one in its sharp beak, carefully dropping them into the narrow neck of the jar.",
     "action3": "As the water level steadily rises to the top of the vessel, the triumphant crow happily dips its beak to take a long, refreshing drink."},

    {"ch": 9, "key": "dog_and_his_shadow", "titleEn": "The Dog and His Shadow", "titleJa": "欲張りな犬",
     "char1": "a greedy hound", "char2": "a large juicy piece of meat and clear stream reflection", "setting": "a narrow wooden footbridge over a crystal-clear brook",
     "action1": "A proud dog trotting across a wooden bridge holds a large, succulent bone in his mouth, looking down into the sparkling stream.",
     "action2": "The dog sees his own reflection in the calm water, greedily believing it is another dog carrying an even bigger piece of meat.",
     "action3": "The foolish dog snaps aggressively at the water; the bone drops from his jaws and splashes into the flowing current, sinking out of reach."},

    {"ch": 10, "key": "milkmaid_and_her_pail", "titleEn": "The Milkmaid and Her Pail", "titleJa": "ミルク搾りの娘",
     "char1": "a day-dreaming milkmaid in a rustic apron", "char2": "a full wooden pail of fresh white milk", "setting": "a blooming spring meadow path leading to market",
     "action1": "A graceful young country maid walks gracefully along a sunny path, balancing a full wooden pail of creamy milk atop her head.",
     "action2": "She gazes into the sky with an excited daydreaming expression, envisioning baskets of chicks, fancy dresses, and dancing at the village fair.",
     "action3": "She tosses her head in proud imagination, causing the heavy pail to tip and splash all the white milk across the green grass."},

    # 11-20
    {"ch": 11, "key": "honest_woodcutter", "titleEn": "The Honest Woodcutter", "titleJa": "金の斧と銀の斧",
     "char1": "an honest woodcutter in peasant attire", "char2": "the divine water spirit Hermes/Mercury", "setting": "a mystical forest river pool shimmering in divine light",
     "action1": "A humble woodcutter weeps beside a deep river after accidentally dropping his old iron axe into the swirling water.",
     "action2": "A glowing water deity emerges gracefully from the sparkling pool, presenting a glittering pure gold axe and a brilliant silver axe.",
     "action3": "The modest woodman honestly claims only his plain iron axe, and the delighted deity rewards him with all three shining axes in glowing harmony."},

    {"ch": 12, "key": "goose_golden_eggs", "titleEn": "The Goose that Laid the Golden Eggs", "titleJa": "金の卵を産むガチョウ",
     "char1": "a greedy farmer and his wife", "char2": "a magical white goose and shining golden eggs", "setting": "a rustic farm cottage barn bathed in morning sun",
     "action1": "A humble farmer discovers a heavy, radiant golden egg inside the nest of his plump white goose, beaming with astonishment.",
     "action2": "Golden coins and luxury fill the cottage as the couple stares with mounting, feverish greed at the precious goose.",
     "action3": "The remorseful farmer stands empty-handed with an empty hands in the barn, realizing his foolish greed has left him with an ordinary empty nest and no more golden eggs."},

    {"ch": 13, "key": "wolf_in_sheeps_clothing", "titleEn": "The Wolf in Sheep's Clothing", "titleJa": "羊の皮をかぶった狼",
     "char1": "a deceitful wolf wrapped in a white fleece", "char2": "a flock of grazing sheep and the shepherd", "setting": "a misty hilltop pasture at sunset",
     "action1": "A cunning wolf carefully drapes a thick white wool fleece over his back, blending invisibly into the unsuspecting flock.",
     "action2": "The disguised predator grazes quietly among the lambs as twilight descends, creeping closer to the center of the fold.",
     "action3": "Under the moonlight, the shepherd enters the pen to prepare the evening meal and unknowingly captures the hidden wolf in his disguise."},

    {"ch": 14, "key": "fox_and_stork", "titleEn": "The Fox and the Stork", "titleJa": "キツネとツル",
     "char1": "a sly red fox", "char2": "a tall, elegant long-beaked stork", "setting": "a cozy animal cottage dining room",
     "action1": "The mischievous fox serves delicious soup in a flat, shallow plate, laughing as the long-beaked stork cannot drink a single drop.",
     "action2": "The polite stork invites the fox to dinner, serving savory stew inside a tall, narrow-necked glass jar.",
     "action3": "The elegant stork easily sips through the tall neck while the hungry fox fruitlessly licks the rim, receiving a taste of his own medicine."},

    {"ch": 15, "key": "frog_and_ox", "titleEn": "The Frog and the Ox", "titleJa": "カエルと牛",
     "char1": "an envious green frog father", "char2": "a massive, calm meadow ox and tiny baby frogs", "setting": "a muddy pond marsh with reeds and water lilies",
     "action1": "A little frog tells his father about a monstrous giant beast grazing in the meadow, pointing toward a colossal horned ox.",
     "action2": "The proud father frog inhales deeply, puffing out his green skin like a balloon to match the enormous size of the ox.",
     "action3": "Ignoring the warnings of his children, the stubborn frog puffs himself up even further until he pops harmlessly with an over-inflated gasp."},

    {"ch": 16, "key": "bat_birds_beasts", "titleEn": "The Bat, Birds, and Beasts", "titleJa": "コウモリと鳥と獣",
     "char1": "an opportunistic black bat", "char2": "armies of birds in the sky and beasts on the land", "setting": "a dramatic battle clearing between sky and forest",
     "action1": "A great contest arises between feathered birds soaring in the sky and four-legged beasts gathered on the battlefield below.",
     "action2": "The shifting bat flies to the winning side, showing his wings to the birds and his furry body and teeth to the beasts.",
     "action3": "When peace is declared, both birds and beasts shun the treacherous bat, banishing him to fly alone in dark nocturnal caves."},

    {"ch": 17, "key": "belling_the_cat", "titleEn": "Belling the Cat", "titleJa": "ネズミの会議",
     "char1": "a gathering of mouse elders and a young mouse", "char2": "a shiny golden bell and a prowling black cat", "setting": "a dimly lit cellar corner beneath wooden floorboards",
     "action1": "A council of concerned mice debate heatedly beneath the floorboards about how to detect the stealthy approaching cat.",
     "action2": "A proud young mouse proposes tying a bright brass bell around the cat's neck, receiving enthusiastic applause from the crowd.",
     "action3": "An old, wise mouse stands up with folded arms and quietly asks who will volunteer to hang the bell, leaving the room in fallen silence."},

    {"ch": 18, "key": "bear_and_two_travelers", "titleEn": "The Bear and the Travelers", "titleJa": "旅人とクマ",
     "char1": "two traveling companions", "char2": "a gigantic wild brown bear", "setting": "a dense ancient pine forest path",
     "action1": "Two friends strolling through a deep mountain forest suddenly freeze in horror as a colossal brown bear crashes through the trees.",
     "action2": "One traveler swiftly climbs high into a sturdy pine tree, leaving his abandoned companion to drop flat on the ground and hold his breath.",
     "action3": "The huge bear sniffs closely at the motionless traveler's ear before ambling away peacefully, teaching a lasting lesson on true friendship."},

    {"ch": 19, "key": "lions_share", "titleEn": "The Lion's Share", "titleJa": "獅子の分け前",
     "char1": "a dominant regal lion", "char2": "his hunting partners: a fox, a wolf, and a jackal", "setting": "a rocky hunting plateau overlooking the wild plains",
     "action1": "A lion, a wolf, a fox, and a jackal successfully bring down a large stag through a cooperative hunt on the rocky ridge.",
     "action2": "The stag is divided into four equal portions, and the fierce lion places his heavy paw firmly over the entire prize of the hunt.",
     "action3": "The regal lion claims all four portions through royal right, strength, and defiance, leaving the intimidated partners with nothing."},

    {"ch": 20, "key": "frog_and_mouse", "titleEn": "The Frog and the Mouse", "titleJa": "ネズミとカエル",
     "char1": "a treacherous green frog and an innocent field mouse", "char2": "a soaring predatory hawk/kite", "setting": "a blooming pond shore beneath an open blue sky",
     "action1": "A playful frog ties his leg with a string to the foot of a curious field mouse to guide him across the marshland.",
     "action2": "The malicious frog dives into the deep pool, pulling the struggling, swimming mouse beneath the shimmering water surface.",
     "action3": "A sharp-eyed hawk swoops down from above, seizing the floating mouse in its talons and carrying both bound creatures into the sky."},

    # 21-30 (Phase 3)
    {"ch": 21, "key": "androcles_and_lion", "titleEn": "Androcles and the Lion", "titleJa": "アンドロクレスとライオン",
     "char1": "a runaway slave named Androcles in ragged Roman tunic", "char2": "a massive wounded lion with a huge thorn in its paw", "setting": "a shadowy desert cave and a grand Roman colosseum arena",
     "action1": "In a dark rocky cave, the frightened Androcles gently inspects the swollen paw of a giant roaring lion, carefully pulling out a large wooden thorn.",
     "action2": "The grateful lion nuzzles and affectionately licks the hands of Androcles under the soft sunlight filtering through the cave entrance.",
     "action3": "In the middle of a sunlit Roman amphitheater arena, the released fierce lion recognizes Androcles, joyfully leaping forward to purr and embrace him before the astonished emperor."},

    {"ch": 22, "key": "fox_and_crow", "titleEn": "The Fox and the Crow", "titleJa": "キツネとカラス",
     "char1": "a cunning red fox looking up with flattering smile", "char2": "a proud black crow perched on an oak branch holding cheese", "setting": "a peaceful woodland glade beneath an ancient oak tree",
     "action1": "A glossy black crow proudly perches high on an oak tree branch, holding a delicious chunk of yellow cheese securely in her sharp beak.",
     "action2": "A flattering red fox stands below on the grass, gesturing with dramatic praise and bowing as he begs the beautiful crow to sing her sweet song.",
     "action3": "The vanity-filled crow opens her beak wide to caw aloud, causing the yellow cheese to plummet directly into the waiting, open jaws of the grinning fox."},

    {"ch": 23, "key": "old_man_and_death", "titleEn": "The Old Man and the mysterious spirit", "titleJa": "木こりと死神",
     "char1": "a frail, exhausted old woodcutter carrying heavy wood bundles", "char2": "a mysterious shadowy robed spirit holding a tall wooden staff", "setting": "a dusty uphill forest road under a somber twilight sky",
     "action1": "An elderly, bent-backed woodcutter groans under a crushing bundle of faggots, collapsing onto the dusty forest path and despairingly calling upon the mysterious spirit.",
     "action2": "A tall, eerie cloaked mysterious robed traveler suddenly materializes from the swirling mist, holding a wooden walking staff and asking why he was summoned.",
     "action3": "Terrified by the grim specter, the trembling old man hastily stammers an apology, pleading only for help lifting the heavy bundle back onto his shoulders."},

    {"ch": 24, "key": "eagle_and_jackdaw", "titleEn": "The Eagle and the Jackdaw", "titleJa": "鷲とカラス",
     "char1": "a majestic golden eagle and an envious foolish jackdaw", "char2": "a flock of sheep with heavy curly wool and the shepherd", "setting": "a rugged alpine mountain crag and a green pasture below",
     "action1": "A majestic golden eagle swoops gracefully from a high mountain cliff, cleanly lifting a small lamb in its powerful curved talons.",
     "action2": "An ambitious little jackdaw tries to imitate the eagle, diving recklessly onto the back of a huge ram and hopelessly entangling its tiny claws in the thick curly fleece.",
     "action3": "The grinning shepherd easily captures the flapping, trapped jackdaw by hand, clipping its wings to take home to his amused children."},

    {"ch": 25, "key": "fox_and_mask", "titleEn": "The Fox and the Mask", "titleJa": "キツネと仮面",
     "char1": "a curious inquisitive red fox", "char2": "a theatrical tragic mask with carved hollow eyes", "setting": "an artist's rustic workshop studio scattered with classical sculptures",
     "action1": "A curious red fox sneaks into a sculptor's studio, inspecting marble busts, carved stones, and antique theater props.",
     "action2": "The fox discovers a beautifully painted classical tragic theater mask, turning it over with his paw to examine the lifelike face.",
     "action3": "The fox peers behind the empty hollow head with a smirk, tapping the hollow wood and remarking what a magnificent head with no brains inside."},

    {"ch": 26, "key": "stag_at_pool", "titleEn": "The Stag at the Pool", "titleJa": "鹿と池の影",
     "char1": "a graceful stag with majestic branched antlers and slender legs", "char2": "a pack of hunting hounds and archers in pursuit", "setting": "a crystal-clear forest pond and a dense thicket of tangled branches",
     "action1": "A magnificent stag gazes proudly at his reflection in a calm mirror-like pool, admiring his branching antlers while despising his thin spindly legs.",
     "action2": "The alarm of barking hounds rings out; the stag's swift legs carry him effortlessly across the open meadow, outrunning the hunters.",
     "action3": "Entering the deep forest, his ornate antlers get firmly tangled in the low branches in low-hanging branches, realizing too late that his despised legs were his salvation."},

    {"ch": 27, "key": "frogs_and_sun", "titleEn": "The Frogs and the Sun", "titleJa": "太陽とカエルたちの結婚",
     "char1": "a chorus of rejoicing frogs and an old wise toad elder", "char2": "the blazing radiant Sun in the celestial heavens", "setting": "a lush summer marshland with lily pads under scorching heat",
     "action1": "All the village animals and joyous frogs prepare feasts and dance in celebration upon hearing that the glorious Sun is to be married.",
     "action2": "A wise old frog croaks solemnly from a mossy log, warning what will happen when the Sun has children to scorch the earth even hotter.",
     "action3": "The cheering marsh falls into worried silence as the frogs gaze up at the blazing sky, realizing that extra suns would dry up all the rivers and ponds forever."},

    {"ch": 28, "key": "ass_and_salt", "titleEn": "The Ass and the Load of Salt", "titleJa": "ロバと荷物",
     "char1": "a cunning donkey carrying heavy woven saddlebags", "char2": "a wise country merchant driver", "setting": "a rocky river crossing stream in a sunny country valley",
     "action1": "A heavy-laden donkey carrying bags of salt slips accidentally in a deep stream, rising with delight as the salt dissolves away and lightens the load.",
     "action2": "On the next journey, the tricky donkey intentionally tumbles into the river again, braying happily as the salt once more washes away.",
     "action3": "The clever merchant packs the bags with dry sponges next time; when the donkey plunges into the water, the sponges absorb massive weight, making him struggle under an immense load."},

    {"ch": 29, "key": "fox_and_woodman", "titleEn": "The Fox and the Woodman", "titleJa": "キツネと木こり",
     "char1": "a panting pursued red fox", "char2": "a double-dealing woodcutter and mounted royal huntsmen with hounds", "setting": "a rustic woodcutter's cottage yard and stacked log sheds",
     "action1": "A panting, exhausted fox begs a passing woodcutter for a hiding place, swiftly crawling inside a hollow stack of firewood.",
     "action2": "When huntsmen ride up asking for the fox, the woodcutter loudly denies seeing him while slyly pointing his finger toward the woodpile.",
     "action3": "The hunters ride past without noticing the signal, and the disgusted fox slips away, reproaching the hypocritical man whose hand betrayed what his tongue spoke."},

    {"ch": 30, "key": "wolf_and_lamb", "titleEn": "The Wolf and the Lamb", "titleJa": "オオカミと子羊",
     "char1": "a fierce, menacing gray wolf", "char2": "a gentle innocent white lamb drinking downstream", "setting": "a winding woodland brook with stones and overhanging willow trees",
     "action1": "A thirsty white lamb drinks peacefully from the lower stream, when a ferocious gray wolf appears higher up the bank, snarling with manufactured rage.",
     "action2": "The cruel wolf falsely accuses the gentle lamb of muddying his drinking water, even though the water flows downward from wolf to lamb.",
     "action3": "Refusing to accept the lamb's humble, logical defenses, the tyrannical wolf bares his sharp fangs, showing that any excuse serves an unjust ruler."},
]

def build_veo3_prompt(story, clip_num, clip_type, action_desc):
    """
    Veo 3 (Google Veo) の新仕様（1回最大10秒出力）に最適化された
    タイムライン連動型・ハイダイナミック動画生成プロンプトを構築する
    """
    if clip_num == 1:
        timeline = (
            f"[10-Second Continuous Animation Timeline]: "
            f"0-5s: The scene opens with {story['char1']} and {story['char2']} in {story['setting']}. Smooth cinematic camera dolly-in as characters begin expressive physical gestures, lively eye contact, and authentic interaction. "
            f"5-10s: {action_desc} The movement accelerates with dynamic character posture shifts, flowing body motion, and shifting atmospheric sunlight."
        )
    elif clip_num == 2:
        timeline = (
            f"[10-Second Continuous Animation Timeline]: "
            f"0-5s: High-energy action commences immediately. {action_desc} Camera tracks laterally with energetic motion blur and changing perspective. "
            f"5-10s: The dramatic turning point unfolds with rapid character movement, swirling environmental elements (leaves, dust, wind), and intense dramatic lighting."
        )
    else:
        timeline = (
            f"[10-Second Continuous Animation Timeline]: "
            f"0-5s: The pivotal climax and resolution occur. {action_desc} Characters show powerful emotional reactions with vivid, expressive bodily animation. "
            f"5-10s: The action resolves smoothly as the camera gently dollies back to reveal a grand, atmospheric storybook tableau with warm golden light."
        )

    prompt = (
        f"Image-to-Video. 10-second continuous cinematic animation (Part {clip_num}/3: {clip_type}). "
        f"Maintain the exact same vintage storybook engraving illustration style, classical woodcut etching texture, and warm antique paper tone as the reference image. "
        f"Setting: {story['setting']}. Characters: {story['char1']}, {story['char2']}. "
        f"{timeline} "
        f"[Cinematic & Motion Direction]: Continuous fluid character motion with zero static pausing across all 10 seconds. Rich physical dynamics, lively micro-expressions, authentic weight in motion, and cinematic depth of field. Preserve fine antique crosshatch lines and classical aesthetic."
    )
    return prompt

def generate_master_schedule():
    """
    全話のプロンプトを生成し、10秒尺×3クリップ（計30秒）の投入スケジュールを作成する。
    """
    master_data = []
    
    for s in STORIES_DB:
        ch_num = s["ch"]
        key = s["key"]
        img_name = f"vol1_{key}.png"
        img_path = f"images/{img_name}"
        
        clips = [
            {
                "clipIndex": 1,
                "sceneName": "Part 1: Opening & Setup (起/導入・対峙 0-10s)",
                "durationSec": 10,
                "action": s["action1"],
                "prompt": build_veo3_prompt(s, 1, "Opening & Setup", s["action1"])
            },
            {
                "clipIndex": 2,
                "sceneName": "Part 2: Dynamic Action & Crisis (承/急展開・動的アクション 0-10s)",
                "durationSec": 10,
                "action": s["action2"],
                "prompt": build_veo3_prompt(s, 2, "Dynamic Action & Crisis", s["action2"])
            },
            {
                "clipIndex": 3,
                "sceneName": "Part 3: Climax & Resolution (結/結末・大逆転 0-10s)",
                "durationSec": 10,
                "action": s["action3"],
                "prompt": build_veo3_prompt(s, 3, "Climax & Resolution", s["action3"])
            }
        ]
        
        master_data.append({
            "chapter": ch_num,
            "key": key,
            "titleEn": s["titleEn"],
            "titleJa": s["titleJa"],
            "referenceImage": img_path,
            "clips": clips
        })
        
    return master_data

def assign_accounts(master_data):
    """
    1日15本（5アカウント × 3本 = 1日5話分）の投入スケジュール表を作成
    """
    tasks = []
    task_id = 1
    
    for story in master_data:
        for clip in story["clips"]:
            day_num = ((task_id - 1) // 15) + 1
            slot_in_day = (task_id - 1) % 15
            account_num = (slot_in_day // 3) + 1
            clip_in_account = (slot_in_day % 3) + 1
            
            tasks.append({
                "taskId": task_id,
                "day": day_num,
                "account": f"Account {account_num}",
                "chapter": story["chapter"],
                "titleEn": story["titleEn"],
                "titleJa": story["titleJa"],
                "clipIndex": clip["clipIndex"],
                "sceneName": clip["sceneName"],
                "imagePath": story["referenceImage"],
                "prompt": clip["prompt"]
            })
            task_id += 1
            
    return tasks

def save_outputs(master_data, tasks):
    output_dir = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle\veo3_production"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. JSON マスター
    json_path = os.path.join(output_dir, "veo3_prompts_master.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"stories": master_data, "tasks": tasks}, f, ensure_ascii=False, indent=2)
        
    # 2. 人間がコピペしやすい Markdown 指示書
    md_path = os.path.join(output_dir, "VEO3_PROMPTS_ACTION_GUIDE.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 🎬 Veo 3 動画制作マスター指示書 (5アカウント分散 投入シート)\n\n")
        f.write("Google Veo 3（Image-to-Video）に各アカウントから投入するためのプロンプト指示シートです。\n")
        f.write("- **1日のノルマ**: 5アカウント × 3クリップ = **1日15クリップ（5話分）**\n")
        f.write("- **重要原則**: 必ず各話の参照元画像（`images/vol1_*.png`）をVeo 3にアップロードした上でプロンプトを入力してください。\n\n")
        f.write("---\n\n")
        
        current_day = None
        current_acc = None
        
        for t in tasks:
            if t["day"] != current_day:
                current_day = t["day"]
                f.write(f"\n## 📅 【Day {current_day}】 投入スケジュール (15クリップ)\n\n")
                
            if t["account"] != current_acc:
                current_acc = t["account"]
                f.write(f"### 👤 {current_acc} 担当分 (3クリップ)\n\n")
                
            f.write(f"#### 🎯 Task #{t['taskId']:02d} | Chapter {t['chapter']:02d}: {t['titleEn']} ({t['titleJa']}) - Clip {t['clipIndex']}\n")
            f.write(f"- **シーン**: {t['sceneName']}\n")
            f.write(f"- **参照画像**: `{t['imagePath']}`\n")
            f.write(f"```text\n{t['prompt']}\n```\n\n")
            
    print(f"[SUCCESS] Veo 3 マスター指示書を生成しました！")
    print(f"  - JSON: {json_path}")
    print(f"  - Markdown: {md_path}")

if __name__ == "__main__":
    master_data = generate_master_schedule()
    tasks = assign_accounts(master_data)
    save_outputs(master_data, tasks)

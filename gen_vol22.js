const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;

// Read Volume 21 chapters to easily extract benchmark texts
const v21Script = fs.readFileSync(path.join(kindleDir, 'gen_vol21.js'), 'utf8');

// We have the 10 stories defined with full Pre-2 target, cards, vocab, grammar, and tips
const pre2Data = [
  {
    num: 51,
    key: "eagle_and_arrow",
    titleEn: "The Eagle and the Arrow",
    titleJa: "鷲と矢",
    imgFile: "images/vol2_eagle_and_arrow.png",
    targetPre2: `Perched majestically upon an alpine promontory, a sovereign eagle surveyed the expansive valleys beneath his domain. Endowed with acute optical perception and formidable predatory instincts, the avian monarch habitually scrutinized the terrain from immense altitudes, readily detecting any vulnerable quarry concealing itself amidst the foliage.

During a tranquil twilight, the predator descended to a prominent granite outcrop, patiently anticipating the emergence of a hare. Wholly absorbed in monitoring the valley floor, the eagle remained entirely oblivious to an experienced archer who was quietly maneuvering through the dense undergrowth below.

Discerning the silhouette of the noble raptor against the horizon, the hunter methodically notched a feathered projectile into his recurve bow. Drawing the cord to its maximum tension with practiced precision, he discharged the missile toward the summit.

The arrow traversed the intervening atmosphere with lethal velocity, penetrating deeply into the eagle's vital organs. Traumatized by the catastrophic impact, the sovereign of the skies experienced instantaneous equilibrium failure, plummeting precipitously to the rocky embankment beneath.

Lying prostrate and hemorrhaging upon the stony earth, the dying predator cast his failing gaze upon the fatal shaft protruding from his chest. With profound shock and existential despair, he identified the stabilizing fletchings fixed to the arrow's tail. They were identical to the magnificent plumage he had naturally shed from his own pinions during the preceding seasonal molt.

Experiencing an acute pang of tragic irony, the mortally wounded raptor gasped his dying lamentation: "While physical extinction is inherently agonizing, it constitutes an infinitely more grievous torment to comprehend that my own shed feathers furnished the aerodynamic instruments that orchestrated my destruction."`,
    transJa: `高山帯の岬の上に威風堂々と止まり、君主たるワシは自らの領土の眼下に広がる広大な谷を見渡していました。鋭敏な視覚的知覚と恐るべき捕食本能を授かっていたこの鳥類の君主は、途方もない高度から地形を日常的に精査し、葉の間に身を隠すいかなる脆弱な獲物をも容易に探知していました。

穏やかな黄昏時、その捕食者は目立つ花崗岩の露出部へと舞い降り、野ウサギの出現を辛抱強く待っていました。谷底の監視に完全に没頭していたため、ワシは下方の密生した下草の間を静かに接近していた熟練の射手（狩人）にまったく気づいていませんでした。

地平線を背景とする高貴な猛禽類のシルエットを認めた狩人は、羽のついた投射体（矢）を規則正しく自らの弓へと番えました。熟練の精密さをもって弦を最大張力まで引き絞ると、彼は山頂に向かって矢を放ちました。

矢は致死的な速度で大気中を横断し、ワシの生命維持器官深くへと貫通しました。壊滅的な衝撃によって外傷を負い、空の主権者は瞬時的な平衡感覚の崩壊を経験し、下方の岩がちの土手へと真っ逆さまに急転落しました。

石だらけの地面の上に平伏し出血しながら、死にゆく捕食者は胸から突き出ている致命的な矢の柄へと衰えゆく視線を投げかけました。深刻な衝撃と実存的な絶望の中で、彼は矢の尾部に固定されている安定用の矢羽を識別しました。それらは、彼が前回の季節の換羽期に自らの翼から自然に脱落させた見事な羽毛と完全に同一のものだったのです。

悲劇的な皮肉の激しい痛痒を経験しながら、致命傷を負った猛禽類は息絶えゆく嘆きの言葉を絞り出しました。「肉体的な死そのものも生来耐え難い苦痛であるが、自らが抜け落とした羽が、自らの破滅を組織した空気力学的道具を提供していたのだと理解することは、無限により痛ましい苦悶である。」`,
    moral: "We often supply the means of our own destruction.（人間はしばしば、自らが過去に生み落とした技術・情報・人材によって、皮肉にも自らを仕留める最も効率的な武器を敵に提供してしまう。）",
    cards: [
      {
        header: "フレーズ 1：高山の岬から谷の獲物を精査する",
        g3: "Because he possessed extraordinary eyesight, he surveyed the vast valley below.",
        pre2: "Endowed with acute optical perception, he scrutinized the terrain from immense altitudes.",
        note: "準2級頻出の分詞構文「Endowed with...（〜を授かって）」とアカデミック動詞「scrutinize（精査する）」の洗練文体です。"
      },
      {
        header: "フレーズ 2：最大張力まで弓を引き絞り矢を放つ",
        g3: "He pulled the bow with great power and released the arrow.",
        pre2: "Drawing the cord to its maximum tension with practiced precision, he discharged the missile.",
        note: "分詞構文「Drawing the cord to its maximum tension...」と軍事・物理動詞「discharge（発射する）」の結合です。"
      },
      {
        header: "フレーズ 3：自らの翼から脱落した羽と同一だと識別する",
        g3: "He noticed the feathers that had fallen from his own wings.",
        pre2: "He identified the fletchings as identical to the plumage naturally shed from his own pinions.",
        note: "「identical to...（〜と同一の）」と文学的語彙「plumage（羽毛）」「pinions（翼）」を用いた格調高い表現です。"
      },
      {
        header: "フレーズ 4：自らの羽が自らの破滅を組織した悲劇の皮肉",
        g3: "My own feathers provided the very wings that brought death to my heart.",
        pre2: "My own shed feathers furnished the aerodynamic instruments that orchestrated my destruction.",
        note: "「furnished aerodynamic instruments（空気力学的道具を提供した）」と「orchestrated my destruction」の圧巻の修辞です。"
      }
    ],
    vocab: [
      { w: "promontory", pos: "名", m: "岬、高台の突き出た岩" },
      { w: "scrutinize", pos: "動", m: "〜を綿密に調べる、精査する" },
      { w: "quarry", pos: "名", m: "獲物、追求されるもの" },
      { w: "outcrop", pos: "名", m: "（岩石の）露出部" },
      { w: "fletching", pos: "名", m: "矢羽（矢の尾部の羽根）" },
      { w: "pinion", pos: "名", m: "鳥の翼、風切羽" },
      { w: "hemorrhage", pos: "動", m: "大出血する [名] 出血" },
      { w: "orchestrate", pos: "動", m: "〜を組織化する、画策する" }
    ],
    grammar: [
      { title: "Endowed with + 名詞, S + V", exp: "過去分詞による分詞構文。「〜を生まれつき授かって、Sは…する」。" },
      { title: "furnish + A + with + B / furnish + B", exp: "「〜に…を供給する、備え付ける」。*provide* の高度な同義表現です。" }
    ],
    tips: [
      "オープンソース技術の軍事転用や技術流出のリスクについて、*Technological pioneers often discover that their open innovations furnished the precise mechanisms that undermined their security.* と論述できます。"
    ]
  },
  {
    num: 52,
    key: "monkey_as_judge",
    titleEn: "The Monkey as Judge",
    titleJa: "猿の裁判長",
    imgFile: "images/vol2_monkey_as_judge.png",
    targetPre2: `While foraging through an agrarian settlement, two feral felines stumbled upon an opulent block of aged dairy cheese. Initially electrified by this fortuitous acquisition, the predators were almost immediately engulfed in contentious litigation regarding proprietary distribution.

Neither party demonstrated the slightest inclination to negotiate an equitable compromise. The dark feline asserted priority of discovery, whereas the white counterpart maintained tangible possession. Recognizing the absolute deadlock of their bilateral negotiations, the naive litigants resolved to submit their conflict to external judicial arbitration.

Materializing opportunistically from the canopy, an unscrupulous simian offered his professional mediation. Projecting an aura of judicial solemnity, the monkey assured them that his objective calibration would guarantee egalitarian equity. Subordinating skepticism to legal desperation, the felines surrendered their prize to the magistrate.

The primate promptly deployed an apparatus of balancing scales. Bisecting the cheese into deliberately unequal proportions, he deposited the fragments upon opposite pans, causing the heavier sector to plunge abruptly.

"An intolerable structural imbalance," observed the magistrate with theatrical gravity. "Equilibrium must be restored through regulatory adjustment." Thereupon, the arbiter consumed a substantial mouthful from the dominant fragment. However, this clumsy subtraction reversed the disparity, necessitating a reciprocal bite from the opposite side.

Iterating this manipulative oscillation, the feline spectators witnessed their asset systematically liquidated before their eyes. Terrified by the rapid vanishing of their property, the litigants implored the court to terminate the proceedings: "Surrender the residual fragments! We dissolve our appeal!"

"Judicial procedure cannot be summarily aborted without the satisfaction of professional stipends," retorted the simian. Devouring the final crumbs with nonchalant satisfaction, the arbiter absconded into the forest, leaving the litigants thoroughly destitute.`,
    transJa: `ある農耕集落を採餌中、二匹の野良猫が熟成した乳製品チーズの贅沢な塊を偶然発見しました。最初はこの偶発的な獲得に興奮した捕食者たちでしたが、所有権の分配を巡る論争の的となる口論にほぼ即座に巻き込まれていきました。

どちらの当事者も、公平な妥協案を交渉する微塵の傾向も示しませんでした。黒い猫は発見の優先権を主張し、白い相棒は具体的な占有権を維持しました。自らの二者間交渉の絶対的な行き詰まりを認識した素朴な訴訟当事者たちは、自らの紛争を外部の司法的仲裁に委ねることを決意しました。

樹冠から日和見主義的に姿を現した不謹慎なサルが、自らの専門的な調停を申し出ました。司法の厳粛さのオーラを醸し出しながら、サルは自らの客観的な測定が平等主義的な衡平性を保証すると彼らに断言しました。懐疑心を法的な絶望に従属させ、猫たちは判事に自らの賞品を引き渡してしまいました。

霊長類の調停者は即座に天秤ばかりの装置を展開しました。意図的に不平等な割合へとチーズを二分すると、彼は反対側の皿の上に破片を載せ、重い方のセクターを急激に沈下させました。

「容認しがたい構造的不均衡である」と判事は演劇的な重々しさをもって述べました。「規制調整を通じて均衡を回復せねばならない。」そうして、仲裁者は支配的な破片からかなりの一口を消費しました。しかしながら、この粗野な引き算は格差を逆転させ、反対側からの相互の（新たな）一口を必要とさせたのです。

この巧妙な往復運動を繰り返すことで、猫の傍聴者たちは自らの資産が目の前で組織的に清算（消滅）されていくのを目撃しました。自らの財産が急速に消え去ることに怯えた訴訟当事者たちは、手続きを終了するよう法廷に懇願しました。「残りの破片を引き渡してください！ 私たちは上訴を取り下げます！」

「専門職の手当が満たされることなしに、司法手続きを即決で中止することはできない」とサルは反論しました。平然とした満足感をもって最後のパンくずを平らげると、仲裁者は森林の中へと逃走し、訴訟当事者たちを完全に無一文のまま置き去りにしたのです。`,
    moral: "In petty disputes, the arbiter consumes the prize.（強欲な私利私欲の争いにおいて第三者の司法仲裁に頼ると、訴訟費用の名目で仲裁者に資産の全てを収奪され、当事者双方が破産する。）",
    cards: [
      {
        header: "フレーズ 1：二者間交渉の行き詰まりと外部仲裁への委託",
        g3: "Unable to resolve disagreement, they decided to find an impartial judge.",
        pre2: "Recognizing the absolute deadlock, the litigants resolved to submit conflict to judicial arbitration.",
        note: "法律・ビジネス交渉用語「deadlock（行き詰まり）」「litigants（訴訟当事者）」「judicial arbitration（司法仲裁）」の融合です。"
      },
      {
        header: "フレーズ 2：意図的に不均等に分割して天秤を傾かせる",
        g3: "He divided the cheese into irregular pieces and placed one on each pan.",
        pre2: "Bisecting the cheese into deliberately unequal proportions, he caused the heavier sector to plunge.",
        note: "「bisect（二等分する・二分する）」と「deliberately unequal proportions（意図的に不平等な比率）」の表現です。"
      },
      {
        header: "フレーズ 3：資産が目の前で組織的に清算されていく",
        g3: "The anxious cats watched their treasure dwindle to almost nothing.",
        pre2: "The feline spectators witnessed their asset systematically liquidated before their eyes.",
        note: "金融・司法用語「asset systematically liquidated（資産が組織的に清算・消滅される）」の卓越した用例です。"
      },
      {
        header: "フレーズ 4：専門職の手当なしに訴訟を中止できない屁理屈",
        g3: "A magistrate must always receive compensation for his professional services.",
        pre2: "Judicial procedure cannot be summarily aborted without satisfaction of professional stipends.",
        note: "法廷用語「summarily aborted（即決で打ち切られる）」「professional stipends（職務手当・報酬）」の格調高い文体です。"
      }
    ],
    vocab: [
      { w: "contentious", pos: "形", m: "論争好きな、議論を呼ぶ（*contentious litigation*）" },
      { w: "litigant", pos: "名", m: "訴訟当事者、原告・被告" },
      { w: "arbitration", pos: "名", m: "仲裁、調停（*binding arbitration*）" },
      { w: "bisect", pos: "動", m: "〜を二分する、二等分する" },
      { w: "disparity", pos: "名", m: "格差、不均衡、相違" },
      { w: "liquidate", pos: "動", m: "〜を清算する、換金する、根絶する" },
      { w: "stipend", pos: "名", m: "給与、手当、報酬" },
      { w: "destitute", pos: "形", m: "極貧の、すべてを失った（*left destitute*）" }
    ],
    grammar: [
      { title: "cannot be + 過去分詞 + without + 名詞", exp: "二重否定による必要条件の強調。「〜なしには…され得ない」。" },
      { title: "subordinate + A + to + B", exp: "「AをBに従属させる、劣後させる」。理性と感情の対立を描く重要動詞句です。" }
    ],
    tips: [
      "国際紛争や企業間の泥沼訴訟のリスクについて、*Protracted legal battles often enrich external legal intermediaries while systematically liquidating the disputed assets.* と論証できます。"
    ]
  },
  {
    num: 53,
    key: "miller_son_and_donkey",
    titleEn: "The Miller, His Son and the Donkey",
    titleJa: "ロバを売る親子",
    imgFile: "images/vol2_miller_son_and_donkey.png",
    targetPre2: `An aged miller accompanied by his adolescent son departed their homestead at daybreak, escorting an equine beast of burden toward a commercial market. Prioritizing the preservation of the animal's marketable vigor, the custodians elected to travel pedestrian-style alongside their quadruped.

While traversing a public thoroughfare, they intersected with an assembly of maidens congregating around a communal fountain. "Observe the incomprehensible ineptitude of those wanderers!" ridiculed one spectator. "For what conceivable objective does one maintain a beast if both custodians subject themselves to arduous pedestrian exertion?"

Excessively susceptible to external social judgment, the patriarch instructed his offspring to mount the donkey's dorsal ridge while he persevered on foot.

Inevitably, this configuration attracted swift condemnation from a council of village elders. "Bear witness to the moral degeneration of modern youth!" proclaimed a dogmatic patriarch. "A vigorous youth reclines in ostentatious comfort, compelling his decrepit progenitor to trudge through the dust."

Mortified by this public chastisement, the adolescent vacated the saddle and demanded that his father occupy the mount. Reluctantly acquiescing, the miller assumed the equestrian posture, confident that filial propriety had been restored.

Nevertheless, subsequent observers formulated an antithetical grievance. Encountering agrarian laborers, the pair was violently excoriated: "What reprehensible paternal egoism! An adult male indulges in luxury while an underdeveloped minor pantingly expends his vitality attempting to sustain velocity!"

Paralyzed by anxiety regarding communal perception, the miller hoisted the adolescent onto the saddle, endeavoring to achieve consensus through simultaneous transport.

Yet, upon entering the metropolitan periphery, civic spectators voiced visceral indignation regarding alleged animal cruelty: "Invert the arrangement, you tyrannical oppressors! The physical dimensions of the riders vastly eclipse the carrying capacity of the quadruped!"

Reduced to cognitive paralysis by endless contradictory dictates, the desperate pair bound the animal's hooves to a horizontal timber, hoisting the inverted beast upon their shoulders.

Confronted with this surreal pantomime upon a municipal aqueduct, the populace exploded in derisive pandemonium. Convulsed by sensory panic, the inverted donkey fractured the hemp restraints, plummeted into the torrent, and perished.

The destitute miller returned home having assimilated an immutable sociological verity: he who calibrates his conduct solely to conciliate universal approval inevitably orchestrates his own total ruin.`,
    transJa: `年老いた粉屋が思春期の息子を伴い、商業市場に向けて役畜のロバを護送しながら、夜明けとともに自らの農家を出発しました。動物の市場価値のある活力を保全することを優先し、管理者（親子）は四足獣の隣を徒歩形式で旅することを選択したのです。

公道を進む途中、彼らは共同の泉の周囲に集まっていた乙女たちの一団と交差しました。「あの放浪者たちの理解不能な不手際を見てごらんなさい！」と一人の観察者が嘲笑しました。「両方の管理者が過酷な徒歩運動に身を晒すくらいなら、いったい何のために獣を飼っているというのかしら？」

外部の社会的判断（世間の目）に対して過敏すぎた家長は、自らは徒歩を続けながら、息子の背骨の突起（ロバの背）に乗るよう指示しました。

必然的に、この配置は村の長老会議からの即座の非難を引き寄せました。「現代の若者の道徳的退廃を目撃せよ！」と独善的な長老が宣言しました。「健康な若者がけばけばしい安楽の中にもたれかかり、老衰した自らの実父に埃の中をとぼとぼ歩くことを強要しているではないか。」

この公の叱責に打ちのめされ、青年は鞍を明け渡し、父親が乗り場を占拠するよう要求しました。不本意ながらも同意し、粉屋は親子の礼儀が回復されたと確信して、騎乗の姿勢を取りました。

それにもかかわらず、その後に遭遇した観察者たちは正反対の不満を表明しました。農耕労働者たちに出くわしたとき、その二人組は激しく罵倒されました。「なんと非難されるべき父親の利己主義だろう！ 発達途上の未成年者が速度を維持しようと息を切らして活力を浪費している間に、成人の男性が贅沢にふけっているではないか！」

共同体の認識に対する不安によって麻痺した粉屋は、同時輸送によって合意を達成しようと試み、少年を鞍の上へと引き上げました。

しかし大都市の周辺部に入ると、市民の傍観者たちは、疑わしい動物虐待に関して本能的な憤りを表明したのです。「その配置を逆にせよ、この専制的な抑圧者どもめ！ 乗り手の物理的寸法は、四足獣の積載能力を遥かに凌駕しているではないか！」

終わりのない矛盾した命令によって認知的麻痺に陥った絶望的な二人組は、動物の蹄を水平の材木に縛り付け、逆さになった獣を自分たちの肩の上へと担ぎ上げました。

市立の高架橋の上でこの超現実的なパントマイムに直面した大衆は、嘲笑の狂乱を爆発させました。感覚的パニックによって痙攣した逆さロバは、麻の拘束具を破壊し、奔流の中へと急落して絶命したのです。

普遍的な承認を調停（迎合）することにのみ自らの行動を校正する者は、必然的に自らの完全な破滅を組織することになるという不変の社会学的真理を骨身に刻み、無一文になった粉屋は帰宅しました。`,
    moral: "Please all, and you will please none.（世間や群衆の矛盾した意見に迎合して全ての人間に好かれようとする者は、自己の指針を完全に見失い、嘲笑と悲惨な自己破滅を迎える。）",
    cards: [
      {
        header: "フレーズ 1：外部の社会的評価に過敏すぎる家長",
        g3: "Sensitive to public criticism, the miller instructed his son to mount the donkey.",
        pre2: "Excessively susceptible to external social judgment, the patriarch instructed his offspring to mount.",
        note: "社会学・心理学用語「susceptible to external social judgment（外部の社会的評価に影響されやすい）」を用いた表現です。"
      },
      {
        header: "フレーズ 2：観察者たちによる正反対の不満の噴出",
        g3: "However, their satisfaction was short-lived. Women soon crossed their path.",
        pre2: "Subsequent observers formulated an antithetical grievance, violently excoriating the pair.",
        note: "「antithetical grievance（正反対の苦情・不満）」「excoriate（痛烈に非難する）」のハイレベル語彙です。"
      },
      {
        header: "フレーズ 3：矛盾する命令による認知的麻痺の末の奇行",
        g3: "Thoroughly bewildered by conflicting opinions, they tied the donkey's legs to a pole.",
        pre2: "Reduced to cognitive paralysis by contradictory dictates, they bound the hooves to a timber.",
        note: "現代認知科学用語「Reduced to cognitive paralysis（認知的麻痺に陥らされて）」の洗練された論述です。"
      },
      {
        header: "フレーズ 4：万人への迎合が自らの完全な破滅を招く",
        g3: "He who attempts to please everybody pleases nobody.",
        pre2: "He who calibrates conduct solely to conciliate universal approval inevitably orchestrates ruin.",
        note: "「calibrates conduct to conciliate universal approval（普遍的承認を宥和するために行動を校正する）」という最高峰の哲学格言です。"
      }
    ],
    vocab: [
      { w: "equine", pos: "形", m: "馬の、ロバの、ウマ科の" },
      { w: "susceptible", pos: "形", m: "影響を受けやすい、感染しやすい（*susceptible to*）" },
      { w: "ostentatious", pos: "形", m: "見せびらかしの、これ見よがしの" },
      { w: "excoriate", pos: "動", m: "〜を激しく非難する、皮を剥ぐ" },
      { w: "visceral", pos: "形", m: "直感的な、本能的な、内臓の" },
      { w: "conciliate", pos: "動", m: "〜を懐柔する、宥和する、なだめる" },
      { w: "pandemonium", pos: "名", m: "大混乱、修羅場、地獄の騒ぎ" },
      { w: "immutable", pos: "形", m: "不変の、変わらない（*immutable truth*）" }
    ],
    grammar: [
      { title: "Reduced to + 名詞, S + V", exp: "分詞構文。「〜にまで落ちぶれて、〜の状態に追い込まれて」。" },
      { title: "calibrate + A + to + 原形動詞", exp: "「〜するようにAを精密に調整する、校正する」。" }
    ],
    tips: [
      "ポピュリズム政策や迎合的な企業ブランディングの破綻について、*Organizations that calibrate policy merely to conciliate fragmented public demands inevitably suffer operational paralysis.* と論証できます。"
    ]
  },
  {
    num: 54,
    key: "bee_and_zeus",
    titleEn: "The Bee and Zeus",
    titleJa: "蜜蜂とゼウス",
    imgFile: "images/vol2_bee_and_zeus.png",
    targetPre2: `The matriarch of an apiary colony inhabited a fortified arboreal hollow. Throughout the pollen season, her synchronized foragers manufactured dense reserves of amber honey. However, because both human gatherers and woodland quadrupeds perpetually raided the comb, the queen cultivated an obsessive, vindictive paranoia.

Determined to procure an invincible defensive deterrent, the insect embarked on an arduous ascent to the celestial court of Mount Olympus. Penetrating the ethereal halls, she deposited an offering of virgin, aromatic honey before Zeus, the sovereign Olympian ruler.

Captivated by the sublime flavor of the tribute, the deity expressed benevolent patronage and articulated an unconditional covenant: "In remuneration for this ambrosial delicacy, name whatever boon your heart covets, and it shall be granted."

Unmasking the poisonous malevolence underlying her pilgrimage, the bee articulated a draconian petition: "Omnipotent sovereign, equip my anatomy with a lethal venomous spine! Whenever any trespasser presumes to compromise my nectar, empower me to inflict a terminal sting, extinguishing their life instantaneously."

Zeus experienced profound revulsion regarding this ruthless animosity, harboring deep paternal affection for mortal humanity. Nevertheless, constrained by the sacrosanct sanctity of an Olympian pledge, the deity could not annul his dispensation.

Consequently, Zeus tempered the decree with poetic jurisprudence: "Your petition is ratified; a sharp barb shall be bestowed upon your frame. However, whenever you discharge your toxic projectile into an assailant, the serrated stinger shall become permanently anchored in the victim's epidermis. As you attempt to disengage, your internal viscera shall rupture, terminating your own existence. The lethal mechanism engineered to slaughter others shall function as the instrument of your own capital execution."`,
    transJa: `養蜂コロニーの母たる女王蜂が、要塞化された樹木のうろの中に住まっていました。花粉の季節を通じて、彼女の同期した採餌者（働き蜂）たちは琥珀色の蜂蜜の高密度な備蓄を製造しました。しかしながら、人間の採取者も森の四足獣たちも巣を絶え間なく襲撃したため、女王蜂は執拗で復讐心に満ちた偏執病（被害妄想）を育んでいきました。

無敵の防衛的抑止力を調達することを決意したその昆虫は、オリュンポス山の天上の宮廷への過酷な上昇（登山）に乗り出しました。霊妙な大広間に侵入すると、彼女はオリュンポスの主権者たる支配者ゼウスの前に、芳醇な処女蜜（初蜜）の供物を捧げました。

その贈り物の神々しい風味に魅了された神は、慈悲深い後援の意を表明し、無条件の契約を宣言しました。「この神酒のような美味への報酬として、お前の心が熱望するいかなる恩恵をも名指すがよい。必ずや叶えてやろう。」

自らの巡礼の根底にある有毒な悪意の仮面を脱ぎ捨て、蜂は過酷な請願を口にしました。「全能の主権者よ、私の解剖学的構造に致死的な有毒のトゲを備え付けてください！ いかなる侵入者であれ私の蜜を脅かそうと図ったときには、即座にその命を消滅させる、終末的な一刺しを加える力を私にお授けください。」

死すべき人間に対して深い父親のような愛情を抱いていたゼウスは、この無慈悲な敵意に関して深甚な嫌悪を経験しました。それにもかかわらず、オリュンポスの誓約の侵すべからざる神聖さに制約されていたため、神は自らの特赦（約束）を取り消すことができませんでした。

その結果、ゼウスは詩的な法理学（因果応報）をもってその布告を調整しました。「お前の請願は批准された。鋭いトゲがお前の肉体に授けられるであろう。しかしながら、お前が襲撃者の中へと有毒な発射体を放出するときにはいつでも、その鋸歯状の針は犠牲者の表皮の中に永続的に錨を下ろす（固定される）ことになる。お前が離脱を試みるとき、お前の体内臓器は破裂し、お前自身の生存を終わらせるだろう。他者を虐殺するために設計されたその致死の機構は、お前自身を死刑執行する道具として機能するのだ。」`,
    moral: "Weapons forged in malice exact the ultimate price from the wielder.（他者を害するための報復兵器を求める者は、その兵器自体の構造的代償によって、自らの生命そのものを差し出さねばならない。）",
    cards: [
      {
        header: "フレーズ 1：無敵の防衛抑止力を手に入れようとする",
        g3: "Desiring a lethal weapon to defend her property, the bee undertook a pilgrimage.",
        pre2: "Determined to procure an invincible defensive deterrent, the insect embarked on an ascent.",
        note: "軍事・安全保障用語「procure an invincible defensive deterrent（無敵の防衛的抑止力を調達する）」の高度な表現です。"
      },
      {
        header: "フレーズ 2：神酒のような美味への無条件の契約",
        g3: "Zeus praised the gift and promised to grant whatever request she formulated.",
        pre2: "In remuneration for this ambrosial delicacy, name whatever boon your heart covets.",
        note: "神話・文学用語「remuneration（報酬）」「ambrosial delicacy（神の美酒・美味）」「covet（熱望する）」の融合です。"
      },
      {
        header: "フレーズ 3：侵入者の命を瞬時に消滅させる毒針の懇願",
        g3: "Whenever an intruder approaches, I wish to inflict a fatal sting so that they perish.",
        pre2: "Whenever any trespasser presumes to compromise my nectar, empower me to inflict a terminal sting.",
        note: "「presumes to compromise...（〜を侵害しようと図る）」「inflict a terminal sting」の格調高い文体です。"
      },
      {
        header: "フレーズ 4：他者を虐殺する機構が己を処刑する道具となる",
        g3: "The very instrument of your malice shall seal your destruction.",
        pre2: "The lethal mechanism engineered to slaughter others shall function as the instrument of your own execution.",
        note: "工学・法学用語「mechanism engineered to slaughter...（虐殺するよう設計された機構）」と「instrument of execution」の対比です。"
      }
    ],
    vocab: [
      { w: "apiary", pos: "名", m: "養蜂場、ミツバチの巣" },
      { w: "arboreal", pos: "形", m: "樹木の、樹木に棲む" },
      { w: "deterrent", pos: "名", m: "抑止力、抑止物（*defensive deterrent*）" },
      { w: "ambrosial", pos: "形", m: "神酒のような、この上なく美味な" },
      { w: "boon", pos: "名", m: "恩恵、恵み、頼み事" },
      { w: "trespasser", pos: "名", m: "不法侵入者、侵害者" },
      { w: "serrated", pos: "形", m: "鋸歯状の、ギザギザのついた" },
      { w: "viscera", pos: "名", m: "内臓、はらわた（複数扱い）" }
    ],
    grammar: [
      { title: "name + whatever + 名詞 + S + V", exp: "「Sが〜するいかなる…でも名指しせよ」。譲歩・包括の表現です。" },
      { title: "engineered to + 原形動詞", exp: "「〜するように巧妙に作られた」。" }
    ],
    tips: [
      "大量破壊兵器の相互確証破壊（MAD）について、*Weapons engineered for unilateral annihilation inherently mandate the catastrophic destruction of the wielder.* と論述できます。"
    ]
  },
  {
    num: 55,
    key: "pig_sheep_and_goat",
    titleEn: "The Pig, the Sheep and the Goat",
    titleJa: "豚と羊と山羊",
    imgFile: "images/vol2_pig_sheep_and_goat.png",
    targetPre2: `Within the pastoral perimeter of a rustic paddock, a swine, an ovine sheep, and a caprine goat coexisted in apparent pastoral tranquility. Sharing the same forage and sheltered beneath the same timber lean-to, the animals appeared to enjoy equivalent social status under their human overseer.

However, during a routine inspection, the herdsman suddenly lunged past the ruminants, violently securing the squealing swine by his calcified hock.

Instantly recognizing the existential gravity of the assault, the pig inaugurated a frantic, convulsive struggle. He thrashed against the terrestrial surface, projecting deafening, high-decibel acoustic detonations that reverberated through the agricultural valley.

The herdsman remorselessly dragged the thrashing mammal toward a motorized transport bound for the municipal abattoir.

Observing this undignified resistance, the sheep and the goat exhibited profound moral condescension. Approaching the barrier, the ruminants interrogated the captive regarding his complete abandonment of philosophical composure.

"Why orchestrate such an unseemly hysterical spectacle?" bleated the sheep with aloof disapproval. "The proprietor subjects our flock to periodic physical detention, shearing our woolen coats without provoking such vulgar vocalizations."

"Precisely," reinforced the goat with self-congratulatory pride. "The dairy master confines me daily to extract lactation, yet I submit with stoic passivity. Why can you not assimilate the rudimentary tenets of dignified resignation?"

The condemned swine fixed his terrified eyes upon his sanctimonious peers, articulating a scathing socio-philosophical rebuke: "How grotesquely disingenuous for creatures facing zero existential jeopardy to sermonize about stoic etiquette! When the overseer apprehends your bodies, he extracts merely surplus secondary commodities—renewable fleece or nutritional secretions. But when his talons enclose my flesh, he solicits neither fiber nor dairy; he demands my total biological liquidation! You surrender a superficial haircut, whereas I am conveyed to the butchering block!"

Confronted with the stark disparity of their existential stakes, the sheep and goat lapsed into stunned, sheepish silence.`,
    transJa: `素朴な放牧場の牧歌的な境界内において、ブタ、ヒツジ、そしてヤギが、外見上は牧歌的な静けさの中で共存していました。同じ飼料を分け合い、同じ木造の差し掛け小屋の下に身を寄せ合い、動物たちは人間の監視者のもとで同等の社会的地位を享受しているかのように見えました。

しかしながら、日常の巡回点検の最中、牧夫は突如として反芻動物（羊と山羊）を通り抜け、金切り声を上げるブタの石灰化した飛節（後ろ足の関節）を力任せに拘束しました。

襲撃の実存的重大性を瞬時に認識したブタは、狂乱の痙攣的抵抗を開始しました。彼は地面に対して激しくもがき、農業の谷間に反響する耳を聾するような高デシベルの音響的爆発（悲鳴）を放ちました。

牧夫は身もだえする哺乳類を、市の屠殺場へと向かう電動輸送車両（トラック）へと容赦なく引きずっていきました。

この威厳のない抵抗を観察した羊と山羊は、深甚な道徳的見下し（上から目線の説教）を示しました。柵に歩み寄り、反芻動物たちは哲学的沈着の完全な放棄について囚人を尋問しました。

「なぜそのような見苦しいヒステリックな見世物を演出するのかね？」と羊は冷淡な不賛成を込めて鳴きました。「所有者は我々の群れを定期的な身体拘束に服従させ、羊毛のコートを刈り取りますが、そのような下品な発声（叫び）を引き起こしたことなどありませんよ。」

「その通りだ」と山羊も自己満足的な誇りをもって補強しました。「酪農の主人は乳を搾取するために毎日私を監禁するが、私はストイックな受動性をもって服従している。なぜ君は尊厳ある諦念の初歩的な教義を同化（理解）できないのかね？」

死刑を宣告されたブタは、自らの独善的な同輩たちに怯えた目を据え、痛烈な社会哲学的叱責を口にしました。「実存的危機（命の危険）にまったく直面していない生き物が、ストイックなエチケットについて説教するなど、なんと奇怪で不誠実なことか！ 監視者があなた方の肉体を拘束するとき、彼が抽出するのは単なる余剰の二次的商品——再生可能な羊毛か、栄養の分泌物（ミルク）に過ぎない。しかし彼の鉤爪が私の肉体を包み込むとき、彼が求めているのは繊維でも乳でもない。彼は私の完全な生物学的清算（屠殺）を要求しているのだ！ あなた方が差し出すのは表面的な散髪に過ぎないが、私が運ばれているのは解体台なのだ！」

自らの実存的利害（失うものの重み）の明白な格差に直面し、羊と山羊は茫然自失の、居心地の悪い沈黙へと沈んでいきました。`,
    moral: "Empathy falters when stakes of peril are unequal.（直面している危機の重みと利害が決定的に異なる他者に対して、何のリスクも負っていない者が安易に冷静さや諦念を説くことは、最も下劣な道徳的欺瞞である。）",
    cards: [
      {
        header: "フレーズ 1：外見上は牧歌的な調和の中で共存する",
        g3: "They shared the pasture in apparent harmony, enjoying peaceful life.",
        pre2: "They coexisted in apparent pastoral tranquility, sharing forage beneath the same shelter.",
        note: "動物学・生態学用語「swine（豚）」「ovine（羊）」「caprine（山羊）」と「pastoral tranquility」の格調高い文体です。"
      },
      {
        header: "フレーズ 2：哲学的沈着の完全な放棄を非難する",
        g3: "The sheep and goat criticized their companion for his lack of composure.",
        pre2: "The ruminants interrogated the captive regarding his complete abandonment of philosophical composure.",
        note: "「interrogated the captive（囚人を尋問した）」「abandonment of philosophical composure（哲学的沈着の放棄）」という洗練表現です。"
      },
      {
        header: "フレーズ 3：実存的危険のない者がエチケットを説く奇怪さ",
        g3: "How easy it is for you to preach composure when your lives are never at risk!",
        pre2: "How grotesquely disingenuous for creatures facing zero existential jeopardy to sermonize about stoic etiquette!",
        note: "「grotesquely disingenuous（奇怪なほど不誠実な・偽善的な）」「existential jeopardy（実存的危機）」の最高峰の知性表現です。"
      },
      {
        header: "フレーズ 4：二次的商品と完全な生物学的清算の格差",
        g3: "You risk only a haircut, but I face the butcher's knife!",
        pre2: "He extracts merely surplus secondary commodities, whereas he demands my total biological liquidation!",
        note: "経済・生物学用語「surplus secondary commodities（余剰二次商品）」と「total biological liquidation（完全な生物学的清算）」の見事な対比です。"
      }
    ],
    vocab: [
      { w: "paddock", pos: "名", m: "放牧場、パドック" },
      { w: "ruminant", pos: "名", m: "反芻動物（羊・山羊・牛など）" },
      { w: "abattoir", pos: "名", m: "屠殺場（フランス語由来の格調高い語）" },
      { w: "condescension", pos: "名", m: "見下すような態度、恩着せがましさ" },
      { w: "stoic", pos: "形", m: "禁欲的な、感情を抑えた、ストイックな" },
      { w: "disingenuous", pos: "形", m: "不誠実な、偽善的な、腹黒い" },
      { w: "jeopardy", pos: "名", m: "危険、危機（*in jeopardy*）" },
      { w: "liquidation", pos: "名", m: "清算、全滅、抹殺" }
    ],
    grammar: [
      { title: "How + 副詞 + 形容詞 + for 人 + to do", exp: "強調感嘆文。「〜が…するとはなんと…なことか！」。" },
      { title: "whereas + S + V", exp: "対比の接続詞。「〜であるのに対して、…である」。" }
    ],
    tips: [
      "利害関係の不均衡と上から目線の安全論について、*Commentators insulated from economic devastation must recognize that sermonizing stoicism to bankrupt citizens is grotesquely disingenuous.* と論評できます。"
    ]
  },
  {
    num: 56,
    key: "sick_raven",
    titleEn: "The Sick Raven",
    titleJa: "病気のカラスと母",
    imgFile: "images/vol2_sick_raven.png",
    targetPre2: `Incarcerated by acute pathological delirium within his arboreal roost, a raven languished under the assault of a terminal pestilence. Throughout his arrogant youth, the predatory corvid had conducted an unabashedly profane career: whenever religious supplicants deposited sacred viands and floral tributes upon stone altars, the corvid audaciously pillaged the sanctified offerings.

Now, incapacitated by violent hyperthermia and systemic respiratory collapse, the juvenile scavenger perceived that his vital pulse was irreversibly decelerating. Gathering his residual breath, he petitioned his maternal attendant, who perched beside the deathbed in ritual mourning.

"Revered mother," articulated the stricken corvid between convulsive gasps, "undertake immediate flight to the monumental acropolis of Apollo! Humiliate yourself before the celestial tribunal, imploring therapeutic salvation. Vow that should the gods preserve my biological integrity, I shall consecrate a monumental holocaust of cattle upon their altars!"

The matriarch scrutinized her doomed progeny with an expression of melancholic severity. Exhaling a heavy sigh, she shattered his superstitious delusions with devastating analytical precision:

"Deluded child, upon which celestial sovereign can your appeal possibly register? Enumerate a single temple whose sacred perimeter you have not desecrated, or an isolated sacrificial brazier from which you have not purloined sacred flesh! Throughout your prosperous vitality, you exhibited sovereign contempt for holy jurisprudence. To imagine that celestial deities will extend miraculous clemency to an inveterate thief at the threshold of biological extinction is the nadir of narcissistic absurdity."

Stunned by the unassailable equity of her judgment, the dying corvid collapsed in silent resignation as cognitive darkness extinguished his consciousness.`,
    transJa: `樹木のねぐらの中で急性の病理学的譫妄（せんもう）に幽閉され、あるカラスが末期の疫病の急襲のもとで衰弱していました。自らの傲慢な若年期を通じて、この捕食性のカラス科の鳥は、恥知らずなまでに不敬な経歴を積んできました。宗教的懇願者たちが石の祭壇の上に神聖な食糧や花の捧げ物を供えるたびに、このカラス科の鳥は大胆不敵にも神聖化された捧げ物を略奪していたのです。

今や、激しい高体温症と全身性の呼吸器崩壊によって行動不能となり、この若い清掃動物は自らの生命の脈拍が不可逆的に減速していることを知覚しました。残された息をかき集め、彼は臨終の床の隣に儀礼的喪に服して止まっていた実母に請願しました。

「敬愛なる母よ」と打ちのめされたカラスは痙攣するあえぎの合間に言葉を絞り出しました。「アポロンの記念碑的なアクロポリス（神殿）へと即座の飛行に乗り出してください！ 天上の法廷の前に自らを辱めてひれ伏し、治療的救済を懇願してください。もし神々が私の生物学的完全性（生命）を保存してくださるならば、祭壇の上に牛の記念碑的な全焼の生贄（ホロコースト）を奉献すると誓ってください！」

母鳥は憂鬱な厳しさの表情をもって、破滅を運命づけられた我が子を精査しました。重いため息を吐き出すと、彼女は壊滅的な分析的精密さをもって、息子の迷信的な妄想を粉々に打ち砕きました。

「迷妄の子よ、いったいどの天の主権者にあなたの訴えが届く可能性があるというのですか？ あなたがその神聖な境界を冒涜しなかった神殿を一つでも列挙できるのですか、あるいはあなたが神聖な肉をかすめ取らなかった孤立した生贄の火鉢が一つでもあるのですか！ 繁栄した活力の全期間を通じて、あなたは神聖な法理学に対する絶対的な軽蔑を示してきました。生物学的絶滅の敷居（死の淵）に至った今になって、天の神々が根っからの盗人に奇跡的な寛大さを差し伸べてくれるなどと妄想することは、自己愛的な不条理の極致（どん底）です。」

母親の判断の反論の余地なき公平さに圧倒され、死にゆくカラスは、認識の暗闇が自らの意識を消滅させる中、無言の諦念のうちに崩れ落ちました。`,
    moral: "Vows made only in mortal crisis win no divine favor.（過去の全生涯において神聖な義務や他者の権利を組織的に蹂躙してきた者が、自らの破滅に直面した土壇場でのみ慌てて捧げる空虚な誓約や祈りは、天にも人にも届かない。）",
    cards: [
      {
        header: "フレーズ 1：神聖な捧げ物を恥知らずに略奪した過去",
        g3: "The raven would swoop down with audacity and steal the consecrated offerings.",
        pre2: "The corvid had conducted an unabashedly profane career, audaciously pillaging sanctified offerings.",
        note: "「unabashedly profane（恥知らずなまでに不敬な）」「pillaging sanctified offerings（神聖な捧げ物を略奪する）」の洗練表現です。"
      },
      {
        header: "フレーズ 2：生命を保全してくれるなら牛の生贄を捧げると誓う",
        g3: "Promise them that if they spare my life, I will dedicate a magnificent sacrifice.",
        pre2: "Vow that should the gods preserve my integrity, I shall consecrate a monumental holocaust of cattle.",
        note: "仮定法倒置「should the gods preserve...」と宗教学用語「consecrate a holocaust（全焼生贄を奉納する）」の高度な文体です。"
      },
      {
        header: "フレーズ 3：一度も冒涜しなかった神殿を列挙できるかという追及",
        g3: "Can you name a single celestial patron whose holy altar you have not purloined?",
        pre2: "Enumerate a single temple whose sacred perimeter you have not desecrated!",
        note: "命令文「Enumerate a single temple...」と関係代名詞「whose」を用いた法廷尋問的表現です。"
      },
      {
        header: "フレーズ 4：絶滅の淵に至って慈悲を妄想する自己愛的不条理",
        g3: "It is preposterous to expect divine compassion now that you face mortality.",
        pre2: "To imagine deities will extend clemency to an inveterate thief at extinction is the nadir of absurdity.",
        note: "「extend clemency to an inveterate thief（常習的盗人に恩赦・慈悲を与える）」と「the nadir of absurdity（不条理のどん底）」の白眉の修辞です。"
      }
    ],
    vocab: [
      { w: "delirium", pos: "名", m: "精神錯乱、譫妄" },
      { w: "profane", pos: "形", m: "冒涜的な、不敬な、世俗の" },
      { w: "hyperthermia", pos: "名", m: "高体温症、異常発熱" },
      { w: "holocaust", pos: "名", m: "全焼の生贄、大虐殺、大惨事（ギリシャ語由来の原義）" },
      { w: "desecrate", pos: "動", m: "〜を冒涜する、神聖を汚す" },
      { w: "clemency", pos: "名", m: "慈悲、寛大な処置、恩赦" },
      { w: "inveterate", pos: "形", m: "根深い、常習的な（*inveterate thief*）" },
      { w: "nadir", pos: "名", m: "どん底、最悪の瞬間（⇔ *zenith* 天頂）" }
    ],
    grammar: [
      { title: "Vow that should + S + 原形動詞, S + shall ...", exp: "条件節の if 省略倒置。「万一〜ならば…すると誓え」。格調高い誓約文です。" },
      { title: "extend + 名詞 + to ...", exp: "「〜に…（慈悲・援助・歓迎）を差し向ける、与える」。*extend clemency*。" }
    ],
    tips: [
      "日頃の倫理的コンプライアンスを怠った組織の危機における孤立について、*Enterprises that systematically desecrate public trust cannot expect regulatory clemency when confronting systemic crises.* と論証できます。"
    ]
  },
  {
    num: 57,
    key: "spider_and_swallow",
    titleEn: "The Spider and the Swallow",
    titleJa: "クモとツバメ",
    imgFile: "images/vol2_spider_and_swallow.png",
    targetPre2: `An enterprising arachnid had established her architectural dominion across the shadowy alcoves of a baronial courtyard. Deploying high-tensile protein filaments, she fabricated elaborate orbicular webs that flawlessly arrested airborne gnats and diptera. Over time, uninterrupted foraging success engendered a fatal delusion regarding the sovereign efficacy of her mechanical contrivance.

During the summer solstice, a swift swallow colonized the courtyard airspace. Endowed with razor-honed aerodynamics and predatory velocity, the avian insectivore executed breathtaking aerial maneuvers, harvesting clouds of prey mid-trajectory.

Watching this kinetic phenomenon from her perimeter, the spider suffered profound narcissistic mortification. "That feathered interloper flagrantly usurps my legitimate territory," the arachnid hissed. "Humanity extols avian grace, but structural engineering is superior. I shall weave a barrier of such unprecedented density that it will immobilize the tyrant mid-flight."

Laboring throughout the diurnal cycle, the megalomaniacal spinner strung an expansive web spanning the central gateway. Stationing herself within the central hub, she anticipated the humiliating capture of her adversary.

Presently, the swallow plummeted through the portal at terminal acceleration.

The anticipated interception never materialized. Far from arresting the speeding avian mass, the microscopic gossamer web ruptured instantaneously, offering zero perceptible aerodynamic resistance. The swallow traversed the perimeter without the slightest deceleration. However, the fractured silk strands, along with their hapless architect, became tenaciously entangled within the bird's dorsal feathers.

Propelled toward the upper troposphere by the bird's relentless kinetics, the crushed arachnid articulated her posthumous epigram: "Alas! In my miniature realm of subjugating helpless gnats, I conflated petty predatory competence with the power to constrain the sovereign kinetic forces of the cosmos!"`,
    transJa: `ある進取的なクモが、男爵の館の中庭の薄暗い壁窪を横切るように、自らの建築的支配権を確立していました。高張力のタンパク質繊維を展開し、彼女は空中のブヨや双翅目昆虫を寸分の狂いもなく拘束する、精巧な円形の網を製造していました。時が経つにつれ、途切れることのない採餌の成功が、自らの機械的仕掛けの主権的有効性（万能さ）に関する致命的な妄想を生み出していきました。

夏至の間、敏捷なツバメが中庭の空域を植民地化（縄張り化）しました。剃刀のように研ぎ澄まされた空気力学と捕食速度を授けられたこの鳥類の食虫動物は、息をのむような空中機動を実行し、軌道の半ばで獲物の雲を収穫していきました。

自らの縄張りの縁からこの運動現象を観察しながら、クモは深甚な自己愛の屈辱に苦しみました。「あの羽の生えた不法侵入者は、私の正当な領土をあからさまに強奪している」とクモは毒づきました。「人類は鳥類の優雅さを称賛するが、構造工学の方が優れているのだ。あの暴君を飛行の最中に行動不能にするほどの、前例のない密度の防壁を織り上げてやるわ。」

昼の周期の全体を通じて骨折って働き、誇大妄想的な紡ぎ手は中央の門を横切る広大な網を張り巡らせました。中央のハブ（中心）に陣取り、彼女は敵対者の屈辱的な捕獲を心待ちにしていました。

やがてツバメが、終末加速度をもって門を通り抜けて急降下してきました。

予期された迎撃はついに具現化しませんでした。疾走する鳥類の質量を拘束するどころか、微細な薄絹の網は瞬時に破断し、知覚可能な空気力学的抵抗を微塵も提供しませんでした。ツバメは微小な減速すらすることなく境界を横断しました。しかしながら、破断した絹の繊維は、その不運な設計者自身とともに、鳥の背の羽の中に頑固に絡みついてしまったのです。

鳥の容赦ない運動エネルギーによって上部対流圏（超上空）へと推進されながら、押し潰されたクモは自らの死後の警句を口にしました。「ああ！ 無力なブヨを征服する自らのミニチュアの領域において、私は些細な捕食能力と、宇宙の主権的な運動エネルギーの力を拘束する能力とを混同してしまったのだ！」`,
    moral: "Frail stratagems are shattered in an instant by superior forces.（小手先の技術や局所的成功に酔いしれ、自らの規模を遥かに超える巨大なマクロの力学を制御できると錯覚する者は、自らの仕掛けた罠に絡め取られて吹き飛ばされる。）",
    cards: [
      {
        header: "フレーズ 1：機械的仕掛けの万能さに対する致命的妄想",
        g3: "Day after day she caught flies, which fostered a dangerous sense of arrogance.",
        pre2: "Foraging success engendered a fatal delusion regarding the sovereign efficacy of her contrivance.",
        note: "心理学・哲学用語「engendered a fatal delusion（致命的妄想を生み出した）」「sovereign efficacy（主権的有効性）」の格調高い文体です。"
      },
      {
        header: "フレーズ 2：飛翔する暴君を行動不能にする防壁を織る",
        g3: "I shall construct a net so formidable that it will ensnare the intruder herself.",
        pre2: "I shall weave a barrier of unprecedented density to immobilize the tyrant mid-flight.",
        note: "「unprecedented density（前例のない密度）」「immobilize the tyrant mid-flight」の力強い表現です。"
      },
      {
        header: "フレーズ 3：空気抵抗すら与えずに瞬時に破断する網",
        g3: "The fragile silk filaments disintegrated instantly upon impact.",
        pre2: "The gossamer web ruptured instantaneously, offering zero perceptible aerodynamic resistance.",
        note: "物理学用語「ruptured instantaneously（瞬時に破断した）」「zero perceptible resistance」の精緻な描写です。"
      },
      {
        header: "フレーズ 4：小手先の能力と宇宙の巨大な力を混同した愚",
        g3: "I foolishly imagined my frail apparatus could withstand the sovereign forces.",
        pre2: "I conflated petty predatory competence with the power to constrain sovereign kinetic forces!",
        note: "認識論動詞「conflated A with B（AとBを混同した）」と「sovereign kinetic forces（主権的運動力学）」の結実です。"
      }
    ],
    vocab: [
      { w: "alcove", pos: "名", m: "壁窪、小部屋、くぼみ" },
      { w: "contrivance", pos: "名", m: "工夫、仕掛け、考案物" },
      { w: "interloper", pos: "名", m: "不法侵入者、出しゃばり" },
      { w: "flagrantly", pos: "副", m: "あからさまに、目にあまるほどに" },
      { w: "gossamer", pos: "形", m: "薄絹のような、繊細な、クモの糸の" },
      { w: "troposphere", pos: "名", m: "対流圏（大気圏の最下層）" },
      { w: "epigram", pos: "名", m: "警句、寸鉄人を刺す短い詩" },
      { w: "conflate", pos: "動", m: "〜を混同する、ごたまぜにする" }
    ],
    grammar: [
      { title: "conflate + A + with + B", exp: "「AとBを混同する」。概念の誤謬を指摘する最頻出アカデミック動詞です。" },
      { title: "offering + 名詞, S + V", exp: "分詞構文（結果・付帯状況）。「その結果〜を提供した」。" }
    ],
    tips: [
      "スタートアップが巨大テック企業のプラットフォーム規制に無謀に挑むリスクについて、*Micro-enterprises often conflate niche software agility with the capacity to constrain macro-monopolistic kinetic forces.* と論述できます。"
    ]
  },
  {
    num: 58,
    key: "fisherman_piping",
    titleEn: "The Fisherman Piping",
    titleJa: "笛を吹く漁師",
    imgFile: "images/vol2_fisherman_piping.png",
    targetPre2: `A littoral mariner celebrated among provincial villagers for his virtuoso flute performances traversed a rocky coastline during morning low tide. Equipped with both his acoustic wind instrument and functional marine trawls, the artisan entertained an unorthodox theoretical hypothesis.

Schooled in classical fables professing that marine organisms were innately susceptible to melodic cadence, the piper postulated that harmonious acoustic stimuli could induce the fish to emerge spontaneously upon dry land. "Why endure the grueling biomechanical attrition of manual netting," he reasoned, "when acoustic persuasion can orchestrate voluntary self-harvesting?"

Stationing himself upon a jagged maritime cliff jutting into the cerulean surf, the artisan applied his lips to the flute aperture. He broadcast an elaborate sequence of pastoral cantatas, followed by rhythmic dance orchestrations that resonated across the waves. For hours under intense ultraviolet exposure, he maintained his acoustic recital, peering intently into the translucent depths.

The marine ecosystem exhibited profound indifference. The fish circulated tranquilly within their subterranean kelp forests, utterly anesthetized to his symphonic overtures.

Infuriated by the comprehensive empirical bankruptcy of his hypothesis, the piper terminated the musical performance. Abandoning his instrument upon the rocks, he deployed his weighted casting net, hurling the mesh into the breakers with practiced athletic leverage. Dragging the cordage ashore, he extracted an immense harvest of thrashing, dyspneic marine vertebrates.

Discharging the catch across the desiccated gravel, the fish convulsed frantically in atmospheric asphyxiation, executing violent, erratic bounds across the stones.

Contemplating their agonizing kinetic paroxysms, the fisherman delivered a sarcastic philosophical indictment: "What incorrigibly paradoxical organisms you are! When I deployed melodious cadences specifically to solicit your merry dance, you maintained obstinate immobility. Yet now that my artistic performance has definitively terminated, you execute the most furious choreography of your lives!"`,
    transJa: `名演奏のフルート演技によって地方の村人たちの間で賞賛されていたある沿岸の船乗りが、朝の引き潮の最中に岩だらけの海岸線を横断していました。音響的な管楽器と機能的な海洋投網の両方を備えていたその職人は、正統派から外れた奇妙な理論的仮説を抱いていました。

海洋生物は生来的に旋律のケイデンス（律動）に影響されやすいと公言する古典的な寓話に学んでいたその笛吹きは、調和のとれた音響刺激が魚たちを自発的に乾燥した陸上へと出現させ得ると仮定したのです。「音響的な説得が自発的なセルフ収穫を組織できるというのに、なぜ手動による網引きの過酷な生体力学的消耗に耐えねばならないのか」と彼は推論しました。

青碧の砕波の中に突き出たギザギザの海洋の崖の上に陣取り、職人はフルートの吹き口に唇を当てました。彼は精巧な一連の牧歌的カンタータを発信し、続いて波間に共鳴するリズミカルな舞踊の管弦楽曲を演奏しました。強烈な紫外線の暴露のもとで何時間も、彼は透明な深淵を熱心に覗き込みながら、自らの音響リサイタルを維持しました。

海洋生態系は深甚な無関心を示しました。魚たちは自らの地下の昆布の森の中で穏やかに回遊し、彼の交響的序曲に対して完全に麻酔された（無感覚な）ままでした。

自らの仮説の包括的な実証的破産（完全な失敗）に激怒した笛吹きは、音楽的演奏を終了しました。岩の上に楽器を遺棄すると、彼は加重された投網を展開し、熟練した運動てこの力をもって砕波の中へと網を投げ込みました。ロープを岸へと引き揚げると、彼は暴れあえぐ海洋脊椎動物の巨大な収穫物を抽出しました。

乾燥した砂利の上に獲物を放出すると、魚たちは大気中での窒息の中で狂乱して痙攣し、石の上で暴力的で不規則な跳躍を実行しました。

彼らの苦悶に満ちた運動発作を観察しながら、漁師は皮肉な哲学的告発を述べました。「なんと救いようのないほど逆説的な生物たちだろう！ 私がお前たちの陽気なダンスを懇願するために特別に旋律的なリズムを展開していたときには、お前たちは頑固な不動を維持した。それなのに私の芸術的演奏が決定的に終了した今になって、お前たちは生涯で最も猛烈な振り付け（ダンス）を実行しているではないか！」`,
    moral: "Action out of season yields no fruit; timely vigor is everything.（時機を完全に逸した行動は喜劇であり悲劇である。要請されている平時に適切な行動を起こさず、すべてが手遅れになった絶体絶命の危機において慌てて跳ね回っても、嘲笑とともに死を迎えるだけである。）",
    cards: [
      {
        header: "フレーズ 1：音響的説得が自発的収穫を促すという奇妙な仮説",
        g3: "He believed he could entice the fish to beach themselves voluntarily.",
        pre2: "He postulated that harmonious acoustic stimuli could induce the fish to emerge spontaneously.",
        note: "科学論文用語「postulate that...（〜と仮定・提唱する）」「acoustic stimuli（音響刺激）」の表現です。"
      },
      {
        header: "フレーズ 2：仮説の実証的破産に怒り網を投げる",
        g3: "Frustrated by his failure, the piper recognized the futility of his approach.",
        pre2: "Infuriated by the empirical bankruptcy of his hypothesis, the piper deployed his casting net.",
        note: "「empirical bankruptcy of hypothesis（仮説の実証的破綻・破産）」という最高峰のアカデミックな批判文体です。"
      },
      {
        header: "フレーズ 3：大気中での窒息による狂乱の痙攣",
        g3: "The fish flopped frantically beneath the sun in desperate bids for survival.",
        pre2: "The fish convulsed frantically in atmospheric asphyxiation, executing erratic bounds.",
        note: "生理学用語「atmospheric asphyxiation（大気中窒息）」「convulsed frantically」の臨床的描写です。"
      },
      {
        header: "フレーズ 4：音楽が終わった今になって猛烈なダンスを演じる",
        g3: "When I piped, you refused to dance. Yet now that music ceased, you dance!",
        pre2: "When I deployed cadences to solicit your dance, you refused. Now that it terminated, you execute furious choreography!",
        note: "芸術・演劇の比喩「execute furious choreography（猛烈な振り付け・ダンスを実行する）」による皮肉の極致です。"
      }
    ],
    vocab: [
      { w: "virtuoso", pos: "名", m: "（芸術・音楽の）名手、大家 [形] 名演奏の" },
      { w: "unorthodox", pos: "形", m: "正統でない、異端の、型破りな" },
      { w: "postulate", pos: "動", m: "〜を（自明のこととして）仮定する、前提とする" },
      { w: "attrition", pos: "名", m: "消耗、摩耗（*war of attrition* = 消耗戦）" },
      { w: "cerulean", pos: "形", m: "濃青色の、青碧の" },
      { w: "asphyxiation", pos: "名", m: "窒息、仮死状態" },
      { w: "incorrigibly", pos: "副", m: "救いようがないほど、手に負えないほど" },
      { w: "choreography", pos: "名", m: "振り付け、舞踊構成" }
    ],
    grammar: [
      { title: "induce + O + to do", exp: "「Oを誘導して〜させる、引き起こす」。*cause* や *lead to* の洗練語です。" },
      { title: "infuriated by + 名詞, S + V", exp: "過去分詞による感情の分詞構文。「〜に激怒して、Sは…した」。" }
    ],
    tips: [
      "市場の需要期を無視したプロモーションの失敗について、*Marketing campaigns launched out of season represent the piper's flute, eliciting engagement only after profitability has terminated.* と批評できます。"
    ]
  },
  {
    num: 59,
    key: "bear_and_bees",
    titleEn: "The Bear and the Bees",
    titleJa: "蜂と熊",
    imgFile: "images/vol2_bear_and_bees.png",
    targetPre2: `A colossal grizzly bear navigated a subalpine conifer forest during an exhaustive quest for caloric sustenance. Brushing inadvertently against a desiccated, fallen timber, the mammal disturbed an indigenous apiary colony. Interpreting the vibration as an imminent existential assault, a solitary sentinel bee deployed from the entrance and administered a sharp venomous puncture upon the tender epithelium of the bear's snout.

The instantaneous neurological shock provoked an immediate collapse of the bear's emotional equilibrium. Rather than dismissing the negligible localized pain and continuing his nomadic trajectory, the apex predator allowed injured narcissism to extinguish every trace of rational forbearance.

Vocalizing a ferocious acoustic roar of indignity, the carnivore initiated a violent, retaliatory siege against the wooden redoubt. Deploying curved claws of hardened keratin and exerting kinetic compressive pressure, he pulverized the decayed bark into kindling, fanatically determined to eradicate the entire hive.

However, this unmeasured escalation unleashed an immediate military catastrophe. Galvinized by the physical violation of their sanctum, the mobilized swarm—an overwhelming contingent numbering tens of thousands of venomous combatants—erupted from the subterranean cavity like a billowing cloud of toxic shrapnel.

Before the lumbering quadruped could coordinate a retreat, the airborne legion colonized his cephalic zone. The insects systematically penetrated his ocular margins, inner auricular passages, nasal membranes, and every cutaneous vulnerability across his frame.

Convulsed by agonizing pain, the panic-stricken giant stampeded recklessly through the woodland biome, crashing against obstacles and lacerating his pelt on tangled briars. Ultimately, the battered predator precipitated into a deep alpine torrent, incarcerating his swollen head beneath the icy current to escape absolute biological liquidation.

Shivering in the glacial waters, adorned with hundreds of pulsating dermal inflammations, the chastised carnivore recognized his catastrophic disproportionality: "What unmitigated folly! In executing a disproportionate campaign of vengeance for a single negligible sting, I provoked an entire syndicate and engineered my own near-fatal ruin."`,
    transJa: `巨大なハイイログマが、カロリー補給（食料）の徹底的な探求の最中に、亜高山帯の針葉樹林を徘徊していました。乾燥して倒れた材木に不注意に体を擦りつけたとき、その哺乳類はそこに自生していた養蜂コロニー（野生の蜂の巣）を刺激してしまいました。その振動を切迫した実存的急襲と解釈した一匹の見張り蜂が入口から展開し、クマの鼻腔の柔らかい上皮の上に鋭い有毒の刺傷を加えました。

瞬間的な神経学的ショックが、クマの感情的平衡の即座の崩壊を引き起こしました。無視できる局所的な痛みを退けて自らの放浪の軌道を継続するどころか、頂点捕食者は傷つけられた自己愛によって、理性的忍耐のあらゆる痕跡を消し去ってしまったのです。

屈辱の獰猛な音響的咆哮を轟かせながら、その肉食獣は木造の拠点に対する暴力的で報復的な包囲攻撃を開始しました。硬化したケラチンの曲がった爪を展開し、運動圧縮圧力を発揮して、彼は腐った樹皮を焚き付けの木屑へと粉砕し、巣全体を根絶やしにしようと狂信的に決意しました。

しかしながら、この節度のないエスカレーションは、即座の軍事的破滅を解き放ちました。聖域の物理的侵害によって刺激された動員軍（数万匹の有毒な戦闘員からなる圧倒的な分遣隊）が、有毒な榴散弾の渦巻く雲のように地下の空洞から噴出したのです。

鈍重な四足獣が退却を組織する暇もなく、空中の軍団はその頭部領域を植民地化（完全包囲）しました。昆虫たちは彼の眼の縁、内耳の通路、鼻の粘膜、そしてその体中のあらゆる保護されていない皮膚の脆弱性を組織的に貫通していきました。

耐え難い苦痛によって痙攣したパニック状態の巨獣は、森林生態系の中を向こう見ずに暴走し、障害物に衝突し、絡み合った野ばらの茂みで自らの毛皮を切り裂きました。最終的に、打ちのめされた捕食者は深い高山急流の中へと身を投げ、完全な生物学的清算（死）から逃れるために、氷のような水流の下へと腫れ上がった頭部を幽閉（潜水）させました。

氷河の水の中で震え、何百もの脈動する皮膚の炎症に覆われながら、懲罰を受けた肉食獣は自らの破滅的な不釣り合い（過剰報復）を認識しました。「なんと純然たる愚行だろう！ たった一つの無視できる一刺しに対する不釣り合いな復讐作戦を実行したばかりに、私は組織全体を挑発し、自らの瀕死の破滅を自ら設計してしまったのだ。」`,
    moral: "Blind rage inflames a minor sting into catastrophic destruction.（些細な一刺しの痛みに我を忘れて過剰な報復戦争を仕掛ける者は、相手の組織的防衛力を総動員させ、自らを瀕死の重傷と破滅へと追い込む。）",
    cards: [
      {
        header: "フレーズ 1：感情の平衡崩壊と理性的忍耐の完全消滅",
        g3: "Afflicted by the sting, he allowed wounded pride to overpower his judgment.",
        pre2: "The neurological shock provoked a collapse of equilibrium, extinguishing rational forbearance.",
        note: "「collapse of emotional equilibrium（感情的平衡の崩壊）」「extinguish rational forbearance（理性的自制・忍耐を消滅させる）」の高度な文体です。"
      },
      {
        header: "フレーズ 2：不釣り合いな過剰エスカレーションによる軍事的大惨事",
        g3: "His violent vandalism triggered an immediate catastrophe.",
        pre2: "This unmeasured escalation unleashed an immediate military catastrophe.",
        note: "地政学・軍事用語「unmeasured escalation（節度のない・無制限のエスカレーション）」の卓越した用例です。"
      },
      {
        header: "フレーズ 3：数万の有毒戦闘員が榴散弾のように噴出する",
        g3: "Tens of thousands of defenders surged out like an ominous storm cloud.",
        pre2: "An overwhelming contingent of toxic combatants erupted like a billowing cloud of shrapnel.",
        note: "軍事用語「contingent of combatants（戦闘員の分遣隊）」「billowing cloud of shrapnel（渦巻く榴散弾の雲）」の比喩です。"
      },
      {
        header: "フレーズ 4：些細な一撃への不釣り合いな報復が招いた自滅",
        g3: "In seeking reckless vengeance for a single prick, I provoked an entire army.",
        pre2: "In executing a disproportionate campaign of vengeance for a negligible sting, I provoked an entire syndicate.",
        note: "安全保障論文の白眉「disproportionate campaign of vengeance（不釣り合いな復讐作戦）」と「provoked an entire syndicate」の結実です。"
      }
    ],
    vocab: [
      { w: "subalpine", pos: "形", m: "亜高山帯の" },
      { w: "conifer", pos: "名", m: "針葉樹" },
      { w: "forbearance", pos: "名", m: "忍耐、自制、寛容" },
      { w: "pulverize", pos: "動", m: "〜を粉砕する、粉にする" },
      { w: "shrapnel", pos: "名", m: "榴散弾、爆発の破片" },
      { w: "cephalic", pos: "形", m: "頭部の、頭の（解剖学用語）" },
      { w: "disproportionality", pos: "名", m: "不均衡、過大性、不釣り合い" },
      { w: "syndicate", pos: "名", m: "企業連合、組織、シンジケート" }
    ],
    grammar: [
      { title: "extinguish + trace of + 名詞", exp: "「〜の痕跡を完全に消し去る」。論理的崩壊を語る表現です。" },
      { title: "In executing + 名詞, S + V", exp: "「〜を実行するにあたって、〜の過程で」。" }
    ],
    tips: [
      "国際安全保障における過剰報復とエスカレーション・スパイラルについて、*Disproportionate military retaliation against isolated border skirmishes frequently galvanizes entire hostile syndicates into total warfare.* と展開できます。"
    ]
  },
  {
    num: 60,
    key: "traveler_and_fortune",
    titleEn: "The Traveler and Fortune",
    titleJa: "旅人と運命の女神",
    imgFile: "images/vol2_traveler_and_fortune.png",
    targetPre2: `A fatigued wayfarer traversed an inhospitable arid wasteland during an extended continental pilgrimage. Deprived of essential hydration, burdened by physical exhaustion, and suffering acute sensory disorientation, the traveler encountered an ancient subterranean cistern situated contiguous to the highway.

Seeking immediate relief from atmospheric exposure, the wanderer collapsed directly upon the crumbling masonry framing the abyss. The architecture was profoundly precarious: decades of structural degradation had eroded the mortar, leaving an unreinforced lip suspended immediately above a fifty-foot vertical drop into freezing subterranean waters.

Completely subordinating self-preservation to physical fatigue, the nomad lapsed into profound, comatose unconsciousness. His cranium hovered perilous inches over the void; an inadvertent nocturnal spasm would inevitably cause his center of gravity to shift, precipitating an irreversible plunge to oblivion.

At that fateful interlude, the divine personification of Fortune materialized upon the desert wind, illuminated by an ethereal celestial luminescence.

Extending a slender hand, the deity agitated the traveler's shoulder, forcibly arresting his dangerous slumber: "Rouse your faculties, reckless mortal, and vacate this lethal ledge!"

Startled into acute wakefulness, the traveler peered into the subterranean chasm and recoiled in visceral horror, perceiving how narrowly he had skirted catastrophic liquidation.

Before the bewildered wanderer could articulate clumsy gratitude, Fortune addressed him with devastating analytical insight:

"Absorb this deliverance, naive nomad, but meditate upon the chronic duplicity of human psychology. Had you shifted in your sleep and plummeted to an aqueous grave, your grieving relatives would never have imputed the catastrophe to your own gross negligence. Uniformly, they would have anathematized Fortune, proclaiming that malevolent destiny had snuffed out an innocent soul. Mankind perpetually monopolizes credit for their triumphs, attributing prosperity to personal virtue, yet ruthlessly scapegoats Fortune for the natural consequences of their unmitigated idiocy."`,
    transJa: `疲労困憊した旅人が、長期にわたる大陸巡礼の途上、過酷で乾燥した荒野を横断していました。不可欠な水分補給を奪われ、肉体的疲労に圧迫され、急性の感覚喪失に苦しみながら、その旅人は街道に隣接して位置していた古代の地下貯水槽（井戸）に遭遇しました。

大気への暴露（直射日光や熱風）からの即座の救済を求め、放浪者は深淵を縁取る崩れかけた石造りの構造物の上に直接倒れ込みました。その建築構造は深刻なほど不安定でした。何十年もの構造的劣化がモルタルを侵食し、氷のように冷たい地下水の中へと向かう50フィートの垂直落下の真上に、補強されていない縁が宙づりのまま残されていたのです。

自己保存を肉体的疲労へと完全に従属させ、放浪者は昏睡状態のような深い無意識へと沈んでいきました。彼の頭部は虚空のわずか数インチ上を危うく漂っていました。眠りの中でのうっかりした不随意の痙攣一つが、必然的に彼の重心を移動させ、忘却（死）への不可逆的な転落を引き起こす状況だったのです。

その運命的な合間に、運命の女神フォーチュンの神聖な擬人化された姿が、霊妙な天上の光彩に照らされながら、砂漠の風の上に具現化しました。

ほっそりとした手を差し伸べ、女神は旅人の肩を揺すり、その危険な眠りを力強く制止しました。「知性を奮い立たせなさい、無謀な定命の者よ、そしてこの致死的な岩棚から退くのです！」

鋭い覚醒へと叩き起こされた旅人は、地下の裂け目を覗き込み、自らがいかに紙一重で壊滅的な死を免れたかを知覚して、本能的な恐怖のあまり後ずさりしました。

困惑した放浪者が不器用な感謝の言葉を口にする間もなく、運命の女神は壊滅的な分析的洞察をもって彼に語りかけました。

「この救済を受け止めなさい、世間知らずの放浪者よ。しかし人間の心理の慢性的な二面性（自己欺瞞）を深く思索するのです。もしあなたが眠りの中で身じろぎし、水底の墓場へと急落していたなら、あなたの悲嘆に暮れる親族たちは、決してその大惨事をあなた自身の甚だしい過失に帰することはなかったでしょう。判で押したように、彼らは運命の女神を呪詛し、邪悪な運命が無実の魂を奪い去ったと宣言したはずです。人類は常に自らの勝利に対する功績を独占し、繁栄を自らの美徳に帰属させるくせに、自らの純然たる白痴（愚行）の自然な結末については、無慈悲にも運命をスケープゴート（身代わり）にするものなのですから。」`,
    moral: "Men credit themselves with triumph, but curse Fortune for their own folly.（人間は自らの成功を個人の才能や努力の賜物として独占して誇る一方、自らの怠慢や不注意による過失の破滅については、すべて運命や不運のせいにして責任転嫁する。）",
    cards: [
      {
        header: "フレーズ 1：自己保存を疲労に従属させて昏睡状態に陥る",
        g3: "Disregarding all instincts of self-preservation, he drifted into slumber.",
        pre2: "Subordinating self-preservation to fatigue, the nomad lapsed into comatose unconsciousness.",
        note: "分詞構文「Subordinating A to B」と医学用語「comatose unconsciousness（昏睡状態の無意識）」の洗練表現です。"
      },
      {
        header: "フレーズ 2：わずかな重心移動が不可逆の転落を招く危機",
        g3: "The slightest movement would cause him to plunge to his doom.",
        pre2: "An inadvertent spasm would cause his center of gravity to shift, precipitating an irreversible plunge.",
        note: "物理学用語「center of gravity to shift（重心の移動）」「precipitating an irreversible plunge」の迫真描写です。"
      },
      {
        header: "フレーズ 3：過失を顧みず運命を呪詛する親族たちの偽善",
        g3: "Relatives would never have attributed disaster to negligence, but would have reviled Fortune.",
        pre2: "Relatives would never have imputed catastrophe to negligence, but would have anathematized Fortune.",
        note: "神学・修辞学用語「anathematized Fortune（運命を呪詛した・破門宣告した）」を用いた格調高い文体です。"
      },
      {
        header: "フレーズ 4：勝利の功績は独占し、愚行は運命に責任転嫁する",
        g3: "Mortals ascribe successes to personal genius, yet blame Fortune for their own folly.",
        pre2: "Mankind perpetually monopolizes credit for triumphs, yet ruthlessly scapegoats Fortune for idiocy.",
        note: "「monopolizes credit for triumphs（勝利の功績を独占する）」と「scapegoats Fortune for idiocy（愚行を運命に責任転嫁する）」の対比です。"
      }
    ],
    vocab: [
      { w: "inhospitable", pos: "形", m: "過酷な、住むのに適さない、不親切な" },
      { w: "contiguous", pos: "形", m: "隣接する、接触している（*contiguous to*）" },
      { w: "comatose", pos: "形", m: "昏睡状態の、無感覚な" },
      { w: "inadvertent", pos: "形", m: "不注意な、うっかりした、不随意の" },
      { w: "anathematize", pos: "動", m: "〜を呪う、破門する、厳しく糾弾する" },
      { w: "monopolize", pos: "動", m: "〜を独占する、独り占めにする" },
      { w: "scapegoat", pos: "動", m: "〜を身代わり・生贄にする [名] スケープゴート" },
      { w: "duplicity", pos: "名", m: "二面性、二枚舌、自己欺瞞" }
    ],
    grammar: [
      { title: "scapegoat + A + for + B", exp: "「B（失敗など）の責任をAに転嫁する、身代わりに仕立てる」。" },
      { title: "precipitate + 名詞", exp: "「〜（急落・大惨事）を引き起こす、早める」。" }
    ],
    tips: [
      "経営破綻や投資失敗における「運のせい」にする経営者責任について、*Corporate executives often monopolize praise during macro booms yet scapegoat market fortune for insolvency.* と批判できます。"
    ]
  }
];

// Combine benchmark from vol 21 with pre2Data
console.log("Compiling Volume 22 files...");
pre2Data.forEach(ch => {
  // Read targetG3 from vol21 file
  const v21Path = path.join(kindleDir, `chapter${ch.num}_${ch.key}.md`);
  const v21Content = fs.readFileSync(v21Path, 'utf8');
  
  // Extract Target Level: Eiken Grade 3 section
  const g3Match = v21Content.match(/## 2\. Target Level: Eiken Grade 3 \(英検3級レベル本文\)\s*\n\*[^\n]+\*\s*\n\n([\s\S]*?)\n\n---/);
  const benchmarkG3 = g3Match ? g3Match[1] : '';

  // Extract Townsend
  const townMatch = v21Content.match(/## 3\. Classic Original English Text \(イソップ寓話クラシック原文\)\s*\n\*[^\n]+\*\s*\n\n([\s\S]*?)\n\n---/);
  const townsend = townMatch ? townMatch[1] : '';

  const fileName = `vol2_chapter${ch.num}_${ch.key}.md`;
  const filePath = path.join(kindleDir, fileName);

  let md = `# Chapter ${ch.num}: ${ch.titleEn} (${ch.titleJa})

<!-- Kindle Page Break & Image Header -->
<div style="text-align: center; margin-bottom: 20px;">
  <img src="${ch.imgFile}" alt="${ch.titleEn} Illustration" style="max-width: 100%; height: auto;" />
</div>

<div style="page-break-before: always;"></div>

## 1. Benchmark Level: Eiken Grade 3 (英検3級レベル本文)
*Read in ~2 to 2.5 minutes. Baseline vocabulary and basic syntax.*

${benchmarkG3}

---
<div style="page-break-before: always;"></div>

## 2. Target Level: Eiken Grade Pre-2 (英検準2級レベル本文)
*Read in ~2 to 2.5 minutes. Richer idioms, participle clauses, and compound sentences.*

${ch.targetPre2}

---
<div style="page-break-before: always;"></div>

## 3. Classic Original English Text (イソップ寓話クラシック原文)
*Translated by George Fyler Townsend (1867)*

${townsend}

---
<div style="page-break-before: always;"></div>

## 4. Japanese Translation & Moral (日本語訳と教訓)

### 【日本語全訳：英検準2級レベル本文】
${ch.transJa}

### 【教訓（Moral）】
**${ch.moral.split('（')[0]}**  
（${ch.moral.split('（')[1]}

---
<div style="page-break-before: always;"></div>

## 5. Recite & Compare: そらんじたいキーフレーズ対比カード

`;

  ch.cards.forEach(card => {
    md += `<div class="comparison-card">
  <div class="card-header">${card.header}</div>
  <div class="card-row-g3-base"><span class="card-badge-g3-base">3級</span>${card.g3}</div>
  <div class="card-row-pre2"><span class="card-badge-pre2">準2級</span>${card.pre2}</div>
  <div class="card-note"><strong>解説：</strong>${card.note}</div>
</div>\n\n`;
  });

  md += `---
<div style="page-break-before: always;"></div>

## 6. Key Vocabulary & Exam Notes (英検準2級 重要語彙・文法・面接対策)

### 1. 英検準2級 必須ボキャブラリー
`;
  ch.vocab.forEach(v => {
    md += `* **${v.w}** [${v.pos}] ${v.m}\n`;
  });

  md += `\n### 2. 文法・構文のチェックポイント\n`;
  ch.grammar.forEach(g => {
    md += `* **${g.title}**:\n  * ${g.exp}\n`;
  });

  md += `\n### 3. スピーキング（面接）＆ライティング活用ヒント\n`;
  ch.tips.forEach(t => {
    md += `* ${t}\n`;
  });
  md += `\n`;

  fs.writeFileSync(filePath, md, 'utf8');
  console.log(`Created ${fileName}`);
});

console.log("SUCCESS: All 10 Volume 22 Chapters generated!");

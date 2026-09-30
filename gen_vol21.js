const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;

const chapters = [
  {
    num: 51,
    key: "eagle_and_arrow",
    titleEn: "The Eagle and the Arrow",
    titleJa: "鷲と矢",
    imgFile: "images/vol1_eagle_and_arrow.png",
    benchmarkG4: `A proud eagle lived high on a tall mountain cliff. Every morning, he looked down at the green valley. He had strong wings and very sharp eyes. He could see small rabbits moving in the grass from far away.

One sunny afternoon, the eagle flew down and sat on a high rock. He wanted to catch a hare for dinner. He looked around carefully. He did not hear a hunter walking quietly in the bushes below.

The hunter saw the big eagle on the rock. He put a sharp wooden arrow on his bow. He pulled the bowstring back with all his strength and let the arrow fly.

Whiz! The arrow flew through the air and hit the eagle right in his side. The eagle felt terrible pain. He lost his balance and fell off the rock. He landed on the dusty ground, breathing weakly.

As the dying eagle looked down at his wound, he saw the back of the arrow. The feathers on the arrow were smooth and brown. He knew those feathers very well. They were his own feathers! A few days ago, he had dropped them from his wing into the forest.

The eagle closed his eyes in great sadness. He whispered with his last breath: "How painful this is! I gave my own feathers to the earth, and now humans have used them on an arrow to kill me."`,
    targetG3: `A majestic eagle made his home on the highest cliff of a rugged mountain. Every morning, he surveyed the vast valley below because he possessed extraordinary eyesight. From high above the clouds, he could easily spot small animals that were hiding among the green bushes.

One calm afternoon, the eagle descended and perched upon a solitary boulder. He was waiting patiently to catch a hare for his evening meal. While he was concentrating on the grassy fields, an experienced hunter approached silently through the thick forest.

The hunter instantly recognized the great bird and prepared his weapon. Taking a sharp wooden arrow, he fitted it to his bowstring. He pulled the bow with great power and released the arrow toward the cliff.

The arrow soared swiftly through the air and pierced deep into the eagle's body. Overcome by sudden shock and intense pain, the monarch of the skies lost his balance and tumbled down to the rocky earth below.

As he lay dying on the ground, the eagle glanced down at the fatal shaft sticking out of his breast. To his astonishment and horror, he noticed the feathers that guided the arrow through the air. They were unmistakable brown flight feathers that had fallen from his own wings during his last molt.

Tears welled in the dying eagle's eyes as he spoke his final words: "It is a double sorrow to lose my life, but it is far more bitter to know that my own feathers provided the very wings that brought death to my heart."`,
    townsend: `An Eagle sat on a high rock, looking for hares. A hunter shot an arrow at him and hit him. As the Eagle fell dying, he looked at the arrow and saw that its feathers were plucked from an eagle's own wing. "Alas," he cried, "it is a double grief to me that I must die by an arrow feathered with my own plumage!"`,
    transJa: `威風堂々たるワシが、険しい山の最も高い崖の上に巣を作っていました。並外れた視力を持っていたため、彼は毎朝、眼下に広がる広大な谷を見渡していました。雲のはるか上空からでも、緑の茂みの中に隠れている小さな動物たちを容易に見つけることができたのです。

ある穏やかな午後、ワシは舞い降りて、一本の孤立した巨岩の上に止まりました。夕食のための野ウサギを捕まえようと、じっと辛抱強く待っていたのです。草むらに全神経を集中させていたため、彼は経験豊富な狩人が鬱蒼とした森の中を音もなく近づいてきていることに気づきませんでした。

狩人は即座にその大きな鳥の姿を認め、武器を構えました。鋭い木の矢を手に取り、弓の弦へと番えました。彼は怪力で弓を引き絞り、崖に向かって矢を解き放ちました。

矢は空を素早く切り裂き、ワシの胴体深くへと突き刺さりました。突然の衝撃と激痛に圧倒され、空の王者はバランスを崩し、眼下の岩だらけの地面へと転落してしまいました。

地面に横たわり死にかけていたワシは、自らの胸から突き出ている致命的な矢の柄を見下ろしました。驚愕と恐怖の中で、彼は矢が空中を飛ぶのを誘導していた羽根に目を留めました。それは、彼が前回の換羽期に自らの翼から抜け落ちた、紛れもない彼自身の茶色い風切羽だったのです。

息絶えゆくワシの目に涙が浮かび、彼は最後の言葉を絞り出しました。「命を失うことだけでも深い悲しみだが、自分自身の羽が、自らの心臓に死をもたらす矢に翼を与えていたと知ることは、遥かに耐えがたい苦痛である。」`,
    moral: "We often supply the means of our own destruction.（人間はしばしば、自らが提供した技術・武器・情報によって、皮肉にも自らを破滅へと追い込む道具を作り出してしまう。）",
    cards: [
      {
        header: "フレーズ 1：雲の上から獲物を見つけ出す視力",
        g4: "He had strong wings and very sharp eyes.",
        g3: "Because he possessed extraordinary eyesight, he could easily spot small animals.",
        note: "3級必須の接続詞「because」と知覚動詞「spot（見つけ出す）」による複文構成です。"
      },
      {
        header: "フレーズ 2：獲物に集中している間に敵が接近する",
        g4: "He did not hear a hunter walking quietly below.",
        g3: "While he was concentrating on the fields, an experienced hunter approached silently.",
        note: "「While + 過去進行形」を用いて、背景の動作と新たな出来事の対比を鮮やかに表現しています。"
      },
      {
        header: "フレーズ 3：自らの翼から落ちた羽根だと気づく",
        g4: "They were his own feathers that he had dropped from his wing.",
        g3: "He noticed the feathers that had fallen from his own wings during his last molt.",
        note: "関係代名詞「that」と過去完了形「had fallen」を組み合わせた3級合格の必修構文です。"
      },
      {
        header: "フレーズ 4：自らの羽が自らに死をもたらした悲哀",
        g4: "Humans have used my own feathers to kill me.",
        g3: "My own feathers provided the very wings that brought death to my heart.",
        note: "強調の「the very + 名詞（まさにその〜）」と関係代名詞「that」を用いた名文句です。"
      }
    ],
    vocab: [
      { w: "survey", pos: "動", m: "〜を見渡す、調査する" },
      { w: "extraordinary", pos: "形", m: "並外れた、異常な（*extraordinary eyesight*）" },
      { w: "spot", pos: "動", m: "〜を見つけ出す、発見する" },
      { w: "descend", pos: "動", m: "降りる、舞い降りる（⇔ *ascend* 登る）" },
      { w: "solitary", pos: "形", m: "孤立した、孤独な" },
      { w: "boulder", pos: "名", m: "大きな岩、丸石" },
      { w: "pierce", pos: "動", m: "〜を突き刺す、貫通する" },
      { w: "plumage", pos: "名", m: "羽毛、羽（集合的）" }
    ],
    grammar: [
      { title: "While + 過去進行形", exp: "「〜している間に…が起こった」。時間の幅を持つ背景行動を表す重要構文です。" },
      { title: "the very + 名詞", exp: "「まさにその〜」。関係代名詞節の先行詞を強く強調する表現です。" }
    ],
    tips: [
      "自らの情報提供や不用意な発言が後で自分を苦しめるリスクについて、*We must be cautious not to provide tools for our own ruin.* と論述できます。"
    ]
  },
  {
    num: 52,
    key: "monkey_as_judge",
    titleEn: "The Monkey as Judge",
    titleJa: "猿の裁判長",
    imgFile: "images/vol1_monkey_as_judge.png",
    benchmarkG4: `Two hungry cats were walking down a country road together. Suddenly, they found a big piece of yellow cheese on the grass. Both cats shouted with joy and ran to grab it.

However, a big quarrel began between them. "I saw the cheese first!" cried the black cat. "No, I picked it up with my paws first!" argued the white cat. They could not agree on how to divide the cheese fairly.

Just then, a clever monkey walked past them. The monkey smiled and said: "Do not fight, my friends. I am an honest judge. I can divide your cheese into two equal pieces." The two simple cats were very glad and gave him the cheese.

The monkey brought out a pair of wooden scales. He broke the cheese into two pieces and put one on each side. The right side went down because it was slightly heavier.

"Look, this piece is too big," said the monkey. He quickly bit off a large chunk and chewed it happily. Now the left side was heavier! So the monkey took a big bite out of the left piece.

He kept biting from side to side for a long time. The cats watched their delicious cheese become smaller and smaller. Finally, only two tiny crumbs were left on the scales.

"Please stop!" cried the frightened cats. "Give us what is left! We are satisfied now."

"No," replied the smiling monkey. "Justice requires hard work. These last two crumbs belong to me as my fee for judging your case." With that, the monkey swallowed the rest of the cheese and ran away.`,
    targetG3: `Two hungry cats were wandering along a quiet village path when they discovered a delicious piece of rich cheese. At first, both animals were delighted by their wonderful good fortune, but a bitter dispute soon arose between them.

Neither cat was willing to share the cheese equally. The black cat insisted that he had spotted the treasure first, while the white cat claimed that his claws had touched it before anyone else. Unable to resolve their disagreement peacefully, they decided to find an impartial judge.

At that moment, a cunning monkey appeared from behind an oak tree. Observing their predicament, the monkey offered his services with a polite bow. "Please do not worry, neighbors. I have served as a judge for many years, and I can ensure that justice is served between you." Relieved by his words, the two naive cats entrusted their cheese to the monkey.

The monkey immediately produced a pair of balance scales. He divided the cheese into two irregular pieces and placed one on each pan. Because the right piece was heavier, the balance tilted downward.

"This will never do," muttered the monkey thoughtfully. "We must make both sides completely equal." He took a generous bite from the larger piece, but now the other side was heavier. Therefore, the monkey took another bite from the second piece.

Back and forth the process continued while the anxious cats watched their treasure dwindle to almost nothing. Realizing their mistake, they begged the arbiter to stop. "Please give us whatever remains! We will settle the dispute ourselves!"

"That is impossible," chuckled the greedy monkey as he placed the remaining morsels into his mouth. "An honorable magistrate must always receive compensation for his professional services." Having consumed the entire cheese, the monkey bounded up into the trees, leaving the two foolish cats hungry and empty-handed.`,
    townsend: `Two Cats found a piece of cheese and could not agree on dividing it. They went to a Monkey to arbitrate. The Monkey brought a balance scale and broke the cheese into two pieces. One was heavier, so he bit a piece off it. Then the other side was heavier, so he bit a piece off that. He kept eating from each side until the Cats pleaded: "Give us what is left!" The Monkey said: "The rest is my fee for judging," and devoured it all.`,
    transJa: `二匹の飢えた猫が静かな村の小道を歩いていたところ、濃厚で美味しそうな一切れのチーズを発見しました。最初、二匹とも自らの素晴らしい幸運に大喜びしましたが、すぐに激しい口論が二匹の間に巻き起こりました。

どちらの猫も、チーズを公平に分け合う意志がありませんでした。黒猫は自分が最初に宝物を見つけたと主張し、白猫は他の誰よりも早く自分の爪がそれに触れたと言い張りました。平和的に不一致を解決することができなかった二匹は、公平な裁判官を探すことに決めました。

その瞬間、狡猾な猿がカシの木の後ろから姿を現しました。二匹の窮状を観察した猿は、丁寧なお辞儀とともに自らの調停サービスを申し出ました。「ご近所さん、心配には及びませんよ。私は長年裁判官を務めており、あなた方の間で正義が執行されるよう保証できます。」その言葉に安堵した世間知らずの二匹の猫は、自分たちのチーズを猿に預けてしまいました。

猿は即座に天秤ばかりを取り出しました。彼はチーズを不揃いな二つに割り、それぞれの皿の上に置きました。右の破片の方が重かったため、天秤は右へと傾きました。

「これではいけませんな」と猿は思慮深そうにつぶやきました。「両方を完全に等しくせねばなりません。」彼は大きな方の破片から惜しげもなく一口かじり取りましたが、今度はもう一方の皿の方が重くなりました。そのため、猿は二つ目の破片からももう一口かじり取りました。

不安がる猫たちが自分たちの宝物がほとんどゼロにまで縮んでいくのを見守る中、この往復プロセスは延々と続きました。過ちに気づいた猫たちは、調停をやめるよう懇願しました。「お願いです、残っているものを返してください！ あとは自分たちで争いを解決しますから！」

「それは不可能ですな」と貪欲な猿は残りの破片を口の中に放り込みながら笑いました。「名誉ある治安判事は、その専門的職務に対して常に報酬を受け取る権利があるのです。」チーズをすべて平らげると、猿は木々の上へと跳び去り、二匹の愚かな猫たちを飢えと徒手空拳のまま置き去りにしました。`,
    moral: "In petty disputes, the arbiter consumes the prize.（些細な私利私欲の争いで第三者に安易な調停を求めると、仲裁者に手数料として全てを巻き上げられ、当事者双方が共倒れになる。）",
    cards: [
      {
        header: "フレーズ 1：平和的に解決できず裁判官を探す",
        g4: "They could not agree on how to divide the cheese fairly.",
        g3: "Unable to resolve their disagreement peacefully, they decided to find an impartial judge.",
        note: "分詞構文的な「Unable to...」と形容詞「impartial（偏らない、公平な）」を用いた洗練表現です。"
      },
      {
        header: "フレーズ 2：不揃いな二つに割って天秤に載せる",
        g4: "He broke the cheese into two pieces and put one on each side.",
        g3: "He divided the cheese into two irregular pieces and placed one on each pan.",
        note: "「divide A into B」と天秤の皿を表す「pan」を使った具体的な英語表現です。"
      },
      {
        header: "フレーズ 3：宝物がほとんどゼロに縮んでいく",
        g4: "The cats watched their delicious cheese become smaller and smaller.",
        g3: "The anxious cats watched their treasure dwindle to almost nothing.",
        note: "知覚動詞「watch + O + 原形」と「dwindle（次第に減少する）」の組み合わせです。"
      },
      {
        header: "フレーズ 4：調停の手数料としてすべて平らげる",
        g4: "These last crumbs belong to me as my fee for judging your case.",
        g3: "A magistrate must always receive compensation for his professional services.",
        note: "社会・法律用語「magistrate（治安判事）」「compensation（報酬・補償）」を用いた高度な文体です。"
      }
    ],
    vocab: [
      { w: "dispute", pos: "名", m: "紛争、論争、口論" },
      { w: "impartial", pos: "形", m: "偏らない、公平な（*impartial judge*）" },
      { w: "predicament", pos: "名", m: "窮状、苦境" },
      { w: "irregular", pos: "形", m: "不揃いな、不規則な" },
      { w: "dwindle", pos: "動", m: "だんだん小さくなる、衰退する" },
      { w: "arbiter", pos: "名", m: "仲裁人、調停者" },
      { w: "magistrate", pos: "名", m: "裁判官、治安判事" },
      { w: "compensation", pos: "名", m: "報酬、埋め合わせ、補償金" }
    ],
    grammar: [
      { title: "Neither + 単数名詞 + was willing to ...", exp: "「どちらの〜も…しようとしなかった」。2者を同時に否定する重要構文です。" },
      { title: "watch + O + 原形動詞", exp: "知覚動詞の構文。「Oが〜するのを見守る、眺める」。" }
    ],
    tips: [
      "無用な訴訟や社内対立のリスクを論じる際、*Excessive litigation often benefits only external arbiters while bankrupting both parties.* と展開できます。"
    ]
  },
  {
    num: 53,
    key: "miller_son_and_donkey",
    titleEn: "The Miller, His Son and the Donkey",
    titleJa: "ロバを売る親子",
    imgFile: "images/vol1_miller_son_and_donkey.png",
    benchmarkG4: `An old miller and his young son were walking to a market town. They were taking their gray donkey with them to sell him. Because they wanted to keep the animal fresh and clean, they both walked on foot.

Soon, they met a group of young women near a well. "Look at those silly fools!" one woman laughed loudly. "Why are they walking in the hot dust when they have a donkey to ride?"

The old miller did not like being laughed at. He quickly told his son to climb onto the donkey's back while he walked beside them.

A little later, they passed three old men resting under a tree. "What an impolite world we live in!" one old man shouted angrily. "Look at that lazy boy riding in comfort while his poor old father must walk on tired legs!"

The boy felt deeply ashamed. He climbed down immediately and told his father to ride. The miller sat on the donkey, and the boy walked behind.

Further down the road, they met some farmers returning from the fields. "You selfish old man!" the farmers called out. "Why do you make that young child run in the heat while you sit like a king?"

The miller wanted to please everyone. So he pulled his son up onto the donkey, and they both rode together.

As they entered the town, the townspeople began to point and yell: "What cruel monsters! Two heavy people riding on one small donkey! You should carry the poor beast instead!"

The confused miller and his son got off. They tied the donkey's legs to a strong wooden pole. Raising the pole onto their shoulders, they carried the heavy donkey across a bridge.

The townspeople burst into roaring laughter at the strange sight. The frightened donkey struggled, broke the ropes, fell into the swift river, and drowned.

The sad miller walked home with nothing.`,
    targetG3: `An elderly miller and his youthful son set out early one morning to sell their donkey at a busy market town. In order to preserve the animal's strength and keep its coat clean, the father and son chose to walk patiently beside the beast.

As they proceeded along the dusty highway, they passed a group of young girls who were drawing water from a village well. "What preposterous fools those travelers are!" exclaimed one girl with a mocking laugh. "Why should they trudge through the summer heat when their donkey carries no load at all?"

Sensitive to public criticism, the miller instructed his son to mount the donkey while he continued to walk on foot.

Before long, they encountered an assemblage of elders who were engaged in serious conversation. One of the old men frowned severely and criticized the travelers: "Look at the deplorable lack of respect among youth today! That healthy boy lounges lazily on the animal, while his aged father is forced to endure the exhaustion of the road."

Blushing with embarrassment, the boy quickly dismounted and insisted that his father take his place. The miller climbed onto the saddle, feeling satisfied that they had corrected their behavior.

However, their satisfaction was short-lived. A group of women carrying heavy baskets soon crossed their path. "What a callous and selfish parent!" they cried indignantly. "You comfortably ride ahead while your little son struggles to keep pace with your footsteps!"

Desperate to avoid further disapproval, the miller hoisted his son up behind him so that both could ride together.

Yet when they approached the town gates, the citizens shouted in moral outrage: "Have you no mercy for that exhausted creature? You are far better suited to carry the beast than the beast is to carry you!"

Thoroughly bewildered by the conflicting opinions of strangers, the father and son dismounted once more. Finding a stout timber, they tied the donkey's legs securely to the pole and lifted the struggling animal onto their shoulders.

When the townsfolk witnessed this absurd spectacle on the municipal bridge, they erupted in uncontrollable hilarity. Startled by the commotion, the donkey kicked violently, snapped the binding cords, plunged into the deep river, and tragically drowned.

The miller returned home empty-handed, having learned that he who attempts to please everybody pleases nobody.`,
    townsend: `A Miller and his Son were leading their Donkey to market. A passerby said: "Why walk when you have a beast to ride?" So the Miller put his Son on the Donkey. Another criticized the boy for riding while his old father walked, so the Miller took his place. A third cried shame that the poor donkey carried the heavy man, so both rode. A fourth called them cruel to overload the animal, so they tied the donkey's feet to a pole and carried him. As they crossed a bridge, the crowd laughed, the donkey kicked, broke loose, fell into the river, and drowned.`,
    transJa: `年老いた粉屋とその幼い息子が、ある朝早く、賑やかな市場の町でロバを売るために出発しました。動物の体力を温存し、その毛並みを清潔に保つために、父と子は獣の隣を辛抱強く歩くことを選んだのです。

埃っぽい街道を進んでいくと、村の井戸から水を汲んでいた少女たちの一団のそばを通りかかりました。「あの旅人たちはなんて突拍子もない愚か者なんでしょう！」一人の少女が嘲笑とともに叫びました。「ロバが何の荷物も運んでいないのに、なぜ夏の暑さの中をとぼとぼ歩いているのかしら？」

世間の批判に敏感だった粉屋は、自らは徒歩を続けながら、息子にロバに乗るよう指示しました。

まもなく、真剣な会話を交わしていた長老たちの一団に出くわしました。一人の老人が厳しく眉をひそめ、旅人たちを非難しました。「最近の若者の嘆かわしい敬意の欠如を見てみろ！ あの健康な少年が動物の上でだらしなくくつろぎ、老いた父親が過酷な道の疲労に耐えることを強いられているではないか。」

恥ずかしさで顔を赤らめながら、少年は素早くロバから降り、父親が代わりに座るよう主張しました。粉屋は鞍の上に跨り、自分たちの行動を正したことに満足感を覚えました。

しかし、彼らの満足は長続きしませんでした。重い籠を運んでいた女性たちの一団がすぐに彼らの進路を横切りました。「なんて冷酷で利己的な親でしょう！」彼女たちは憤慨して叫びました。「小さな息子があなたの足取りについていくのに必死になっているというのに、自分だけ優雅にロバに乗っているなんて！」

これ以上の非難を避けることに必死になった粉屋は、二人で一緒に乗れるよう、自分の後ろへと息子を引き上げました。

しかし町の門に近づくと、市民たちが道徳的憤りを込めて叫びました。「あの疲れ果てた動物への慈悲はないのか！ お前たちがその獣を背負う方が、その獣がお前たちを背負うよりも遥かに似つかわしいぞ！」

見知らぬ人々の矛盾した意見に完全に混乱した父と子は、再びロバから降りました。頑丈な材木を見つけると、彼らはロバの足を棒にしっかりと縛り付け、もがく動物を自分たちの肩の上へと持ち上げました。

町の橋の上でこの不条理な光景を目撃した町民たちは、抑えきれない大爆笑を巻き起こしました。騒音に驚いたロバが激しく暴れ、縛られていた紐を引きちぎり、深い川の中へと転落して悲劇的にも溺死してしまいました。

全ての人を喜ばせようとする者は誰をも喜ばせることができないという教訓を骨身に刻み、粉屋は手ぶらで家へと帰っていきました。`,
    moral: "Please all, and you will please none.（万人の意見や評価に振り回されて全員を満足させようとする者は、自らの判断の軸を失い、誰をも満足させられずに破滅する。）",
    cards: [
      {
        header: "フレーズ 1：批判を気にして息子をロバに乗せる",
        g4: "He quickly told his son to climb onto the donkey's back.",
        g3: "Sensitive to public criticism, the miller instructed his son to mount the donkey.",
        note: "形容詞句「Sensitive to public criticism（世評に過敏な）」を用いた格調高い導入です。"
      },
      {
        header: "フレーズ 2：不評を恐れて二人で同時に乗る",
        g4: "He pulled his son up onto the donkey, and they both rode together.",
        g3: "Desperate to avoid further disapproval, the miller hoisted his son up behind him.",
        note: "「Desperate to avoid disapproval（不興を買うことを避けるのに必死で）」という心理描写です。"
      },
      {
        header: "フレーズ 3：矛盾する意見に完全に困惑する",
        g4: "The confused miller and his son got off.",
        g3: "Thoroughly bewildered by the conflicting opinions of strangers, they dismounted once more.",
        note: "分詞形容詞「bewildered」と「conflicting opinions（相反する意見）」の連語です。"
      },
      {
        header: "フレーズ 4：万人に阿る者は誰をも喜ばせられない",
        g4: "The sad miller walked home with nothing.",
        g3: "He who attempts to please everybody pleases nobody.",
        note: "英語圏で最も有名な普遍の格言「He who attempts to please everybody pleases nobody.」です。"
      }
    ],
    vocab: [
      { w: "preposterous", pos: "形", m: "不合理な、常軌を逸した、ばかげた" },
      { w: "trudge", pos: "動", m: "重い足取りでとぼとぼ歩く" },
      { w: "deplorable", pos: "形", m: "嘆かわしい、哀れな、ひどい" },
      { w: "callous", pos: "形", m: "冷酷な、無神経な" },
      { w: "disapproval", pos: "名", m: "不賛成、非難、不興" },
      { w: "bewildered", pos: "形", m: "途方に暮れた、当惑した" },
      { w: "hilarity", pos: "名", m: "大笑い、陽気な騒ぎ" },
      { w: "drown", pos: "動", m: "溺れ死ぬ、溺死する" }
    ],
    grammar: [
      { title: "He who + 動詞", exp: "「〜する人は（誰でも）」。ことわざや教訓で頻出する関係代名詞の古典的表現です。" },
      { title: "In order to + 原形動詞", exp: "「〜するために」。明確な目的を示す重要熟語です。" }
    ],
    tips: [
      "他人の目や同調圧力に囚われない主体的な意思決定について、*Leaders who attempt to satisfy every conflicting demand inevitably undermine their organizational vision.* と主張できます。"
    ]
  },
  {
    num: 54,
    key: "bee_and_zeus",
    titleEn: "The Bee and Zeus",
    titleJa: "蜜蜂とゼウス",
    imgFile: "images/vol1_bee_and_zeus.png",
    benchmarkG4: `A little queen bee lived in a big wooden beehive. Her worker bees made sweet golden honey every day. Many animals and humans loved honey, so they often came to steal it.

The queen bee was very angry. She wanted a strong weapon to protect her honey. She decided to fly to Mount Olympus to speak with Zeus, the king of the gods.

When she arrived, she gave Zeus a bowl of fresh, sweet honey. Zeus tasted the honey and was very pleased. He said: "Thank you for this delicious gift, little bee. I will grant you one wish. What do you want?"

The bee answered with hate in her heart: "Great Zeus, please give me a sharp needle with poison. Whenever a human or animal tries to touch my honey, I want to sting them and kill them instantly!"

Zeus was very sad and angry to hear such a cruel wish. He loved humans and did not want them to die. However, because he was a king, he could not break his promise.

So Zeus said: "I will give you a sharp stinger as you requested. But listen to my law: when you sting someone, the stinger will stay stuck in their flesh. When you pull away, your body will break, and you will die immediately. Your weapon will take your own life."

The queen bee flew back to earth with regret.`,
    targetG3: `A queen bee ruled over a flourishing colony inside a hollow oak tree. Throughout the spring and summer, her industrious workers gathered nectar and produced combs of pure, golden honey. However, because both humans and wild beasts frequently plundered the hive, the queen grew bitter and resentful.

Desiring a lethal weapon to defend her property, the bee undertook a long pilgrimage to Mount Olympus. Upon reaching the celestial palace, she presented a comb of freshly harvested honey to Zeus, the supreme king of the gods.

Delighted by the sweet offering, Zeus praised the bee's craftsmanship and made a solemn vow: "In return for this marvelous gift, I promise to grant whatever request you formulate."

Seizing the opportunity, the bee revealed the dark malice in her heart. "Almighty Zeus," she petitioned, "endow my body with a venomous needle. Whenever an intruder attempts to approach my honeycombs, I wish to inflict a fatal sting so that they will perish on the spot."

Zeus was deeply displeased by this spiteful prayer because he cherished mortal mankind. Nevertheless, because he had sworn a divine oath, he could not revoke his word.

Instead, Zeus pronounced a just condition: "Your request shall be granted, and you shall possess a sharp stinger. However, whenever you discharge your venom into an enemy, your barbed weapon shall remain embedded in the wound. As you attempt to withdraw, your vital organs shall tear away, and you shall forfeit your own life. The very instrument of your malice shall seal your destruction."`,
    townsend: `A Bee went to Mount Olympus to offer fresh honey to Zeus. Zeus was pleased and promised her whatever she asked. The Bee requested a stinger so that she might kill anyone who tried to take her honey. Zeus was displeased with her malicious wish, yet kept his promise; but he decreed that whenever she stung someone, the stinger should remain in the wound, and she should lose her life.`,
    transJa: `女王蜂がうろのあるカシの木の内部で、繁栄するコロニーを統率していました。春から夏にかけて、彼女の勤勉な働き蜂たちは蜜を集め、純粋な黄金の蜂蜜の巣房を作り上げました。しかしながら、人間も野獣もしばしば巣を略奪したため、女王蜂は次第に苦々しさと怨恨を募らせていきました。

自らの財産を防衛するための致死的な武器を渇望した蜂は、オリュンポス山への長い巡礼の旅に出ました。天上の宮殿に到着すると、彼女は神々の最高権力者であるゼウスに、収穫したばかりの蜂蜜の巣を献上しました。

甘い贈り物に喜んだゼウスは、蜂の職人芸を称賛し、厳粛な誓いを立てました。「この素晴らしい贈り物に報いるため、お前が述べるいかなる願いも叶えてやると約束しよう。」

この好機を捉えた蜂は、その心に潜む暗い悪意を露わにしました。「全能のゼウスよ」と彼女は嘆願しました。「私の体に有毒な針をお授けください。侵入者が私の巣房に近づこうと試みたときにはいつでも、致命的な一刺しを浴びせ、その場で絶命させたいのでございます。」

死すべき人間たちを慈しんでいたゼウスは、この悪意に満ちた祈りに深く不快感を覚えました。それにもかかわらず、神聖な誓いを立ててしまっていたため、自らの言葉を取り消すことはできませんでした。

その代わり、ゼウスは公正な条件を言い渡しました。「お前の願いは叶えられ、お前は鋭い針を手に入れるだろう。しかしながら、お前が敵に毒を放つときにはいつでも、その逆棘のある武器は傷口の中に埋め込まれたまま残るであろう。お前が飛び去ろうと試みるとき、お前の内臓は引き裂かれ、お前は自らの命を失うことになる。お前の悪意のまさにその道具こそが、お前自身の破滅を決定づけるのだ。」`,
    moral: "Weapons forged in malice exact the ultimate price from the wielder.（他者を害し殺傷するために願った悪意の武器は、必ずその所有者自身に最大の代償を請求し、自らを破滅へと導く。）",
    cards: [
      {
        header: "フレーズ 1：略奪に苦しみ怨恨を募らせる",
        g4: "Many animals loved honey, so they often came to steal it.",
        g3: "Because intruders frequently plundered the hive, the queen grew bitter and resentful.",
        note: "3級最頻出の動詞「plunder（略奪する）」と形容詞「bitter and resentful」の表現です。"
      },
      {
        header: "フレーズ 2：いかなる願いも叶えるという厳粛な誓約",
        g4: "I will grant you one wish. What do you want?",
        g3: "I promise to grant whatever request you formulate.",
        note: "複合関係代名詞「whatever（いかなる〜でも）」を用いた格調高い約束の表現です。"
      },
      {
        header: "フレーズ 3：他者をその場で絶命させたいという悪意",
        g4: "I want to sting them and kill them instantly!",
        g3: "I wish to inflict a fatal sting so that they will perish on the spot.",
        note: "「inflict a fatal sting（致命的な一刺しを加える）」と目的の「so that ... will」の構文です。"
      },
      {
        header: "フレーズ 4：悪意の道具が己の命を奪うという神託",
        g4: "When you pull away, your body will break, and you will die.",
        g3: "The very instrument of your malice shall seal your destruction.",
        note: "格言的な名文「The very instrument of your malice shall seal your destruction.」です。"
      }
    ],
    vocab: [
      { w: "industrious", pos: "形", m: "勤勉な、よく働く" },
      { w: "plunder", pos: "動", m: "〜を略奪する、奪う" },
      { w: "pilgrimage", pos: "名", m: "巡礼の旅、長旅" },
      { w: "solemn", pos: "形", m: "厳粛な、荘重な（*solemn vow*）" },
      { w: "formulate", pos: "動", m: "〜を述べる、明確に表現する" },
      { w: "intruder", pos: "名", m: "侵入者、邪魔者" },
      { w: "inflict", pos: "動", m: "（損害・打撃を）加える、負わせる" },
      { w: "perish", pos: "動", m: "死ぬ、滅びる（文語）" }
    ],
    grammar: [
      { title: "so that + S + will/may ...", exp: "「Sが〜できるように」。目的を表す副詞節を導く重要接続詞です。" },
      { title: "inflict + 損害 + on ...", exp: "「〜に損害や苦痛を与える」。社会・論述問題で頻出のコロケーションです。" }
    ],
    tips: [
      "他害的な兵器開発やサイバー攻撃のブーメラン効果について、*Malicious offensive tools inevitably expose the attacker to self-destruction.* と論証できます。"
    ]
  },
  {
    num: 55,
    key: "pig_sheep_and_goat",
    titleEn: "The Pig, the Sheep and the Goat",
    titleJa: "豚と羊と山羊",
    imgFile: "images/vol1_pig_sheep_and_goat.png",
    benchmarkG4: `On a warm green farm, a pig, a sheep, and a goat lived together in the same grassy field. They ate grass, rested in the shade, and were peaceful neighbors.

One morning, the farmer walked into the meadow. He walked past the sheep and the goat. Suddenly, he grabbed the fat young pig by his hind legs!

The pig became terrified. He began to kick violently. He squealed and screamed with all his might: "Weee! Weee! Help me!" His loud cries could be heard all across the valley.

The farmer held the pig tightly and carried him toward a wooden cart.

The sheep and the goat watched the pig struggle. They shook their heads and felt annoyed by the loud noise.

"Why are you making such a terrible noise, pig?" said the sheep calmly. "The farmer catches us all the time. He takes our warm wool every summer, but we never scream like babies."

"That is true," added the goat. "The farmer catches me every morning to take my milk. I never kick or cry. You should learn to be quiet and brave like us."

The pig looked at them with tears in his eyes as the farmer carried him away. He gasped: "You foolish animals! You do not understand anything! When the farmer catches you, he only wants your wool or your milk. But when he catches me, he does not want wool or milk. He wants my bacon! He is going to kill me!"

The sheep and the goat fell completely silent.`,
    targetG3: `In a quiet pastoral meadow, a young pig, a gentle sheep, and a horned goat shared the same pasture in apparent harmony. They grazed upon the sweet clover and enjoyed the peaceful life of domestic livestock.

One crisp morning, the shepherd entered the enclosure carrying a sturdy hemp sack. Ignoring the sheep and the goat, he lunged forward and seized the plump pig by his hind leg.

Instantly, the pig erupted in wild terror. He thrashed against the shepherd's grasp, squealing at the top of his lungs with piercing screams that echoed across the surrounding hills.

The shepherd dragged the captive beast firmly toward the butcher's wagon.

Observing this chaotic scene, the sheep and the goat felt irritated by the pig's undignified behavior. They approached the fence and criticized their companion for his lack of composure.

"What a shameful display of cowardice!" bleated the sheep condescendingly. "The shepherd captures us regularly, shearing my heavy fleece every spring, yet I never disturb the peace with hysterical shrieks."

"Indeed," agreed the goat with self-righteous pride. "The master corners me twice daily to milk me, and I submit quietly without resistance. Why can you not endure a routine capture with patient dignity?"

The doomed pig turned his sorrowful gaze toward his naive companions and offered a chilling clarification: "How easy it is for you to preach composure when your lives are never at risk! When the shepherd captures you, he seeks merely your renewable fleece or your morning milk. But when he seizes me, he seeks neither wool nor dairy—he demands my lifeblood! You risk only a haircut, but I face the butcher's knife!"

Hearing these words, the sheep and goat fell into horrified silence, recognizing their moral blindness.`,
    townsend: `A Pig, a Sheep, and a Goat were kept in the same meadow. One day the shepherd seized the Pig, which began to squeal and struggle furiously. The Sheep and Goat rebuked him: "The shepherd takes us constantly, and we never make such an outcry." The Pig replied: "Your capture and mine are very different matters: he wants you for your wool and milk, but he takes me for my life."`,
    transJa: `静かな牧歌的な草地で、若い豚、穏やかな羊、そして角のある山羊が、外見上は何の不和もなく同じ放牧地を共有していました。彼らは甘いクローバーを食み、家畜としての平和な生活を楽しんでいました。

ある爽やかな朝、羊飼いが頑丈な麻袋を抱えて囲い地の中に入ってきました。羊と山羊には目もくれず、彼は前へと踏み出し、丸々と太った豚の後ろ足を掴みました。

瞬時にして、豚は猛烈な恐怖を爆発させました。彼は羊飼いの拘束に激しく抵抗し、周囲の丘にこだまするほどの甲高い金切り声で、喉も張り裂けんばかりに悲鳴を上げました。

羊飼いは捕らえた獣を、肉屋の荷車へとしっかりと引きずっていきました。

この混沌とした光景を目撃した羊と山羊は、豚の威厳のない振る舞いに苛立ちを覚えました。彼らは柵に歩み寄り、落ち着きのなさを理由に仲間を非難しました。

「なんて恥知らずな臆病の見世物でしょう！」と羊が見下すように鳴きました。「羊飼いは私たちを定期的に捕まえ、毎年春に私の重い羊毛を刈り取りますが、私がヒステリックな叫び声で平穏を乱したことなど一度もありませんよ。」

「その通りだ」と山羊も独善的な誇りをもって同意しました。「主人は私から乳を搾るために一日に二度私を追い詰めるが、私は抵抗することなく静かに服従している。なぜ君はもっと辛抱強い威厳をもって、日常的な捕獲に耐えることができないのかね？」

破滅を宣告された豚は、世間知らずな仲間たちへと悲哀に満ちた視線を向け、背筋も凍るような明確化を告げました。「自分たちの生命が微塵も脅かされていないときに、冷静さを説教することがどれほど容易であることか！ 羊飼いがあなた方を捕まえるとき、彼が求めているのは再生可能な羊毛か、朝のミルクに過ぎない。しかし彼が私を掴むとき、彼が求めているのは毛でも乳でもない——彼は私の命の血を要求しているのだ！ あなた方が失うリスクは散髪に過ぎないが、私が直面しているのは肉屋の包丁なのだ！」

この言葉を聞いた羊と山羊は、自らの道徳的盲目を思い知り、恐怖の沈黙へと沈んでいきました。`,
    moral: "Empathy falters when stakes of peril are unequal.（自らの失うリスクが極小である者が、命の危険に直面している他者の恐怖や叫びを『取り乱している』と傲慢に批判してはならない。）",
    cards: [
      {
        header: "フレーズ 1：平和な牧場で外見上は調和して暮らす",
        g4: "A pig, a sheep, and a goat lived together in the field.",
        g3: "They shared the pasture in apparent harmony, enjoying peaceful life.",
        note: "「in apparent harmony（外見上は調和して）」という深みのある導入表現です。"
      },
      {
        header: "フレーズ 2：取り乱した臆病な振る舞いを非難する",
        g4: "The sheep and the goat watched the pig struggle and felt annoyed.",
        g3: "The sheep and goat criticized their companion for his lack of composure.",
        note: "名詞「composure（冷静さ、落ち着き）」と「lack of composure」の重要フレーズです。"
      },
      {
        header: "フレーズ 3：生命の危険がない時の説教の容易さ",
        g4: "You do not understand anything! He wants to kill me!",
        g3: "How easy it is for you to preach composure when your lives are never at risk!",
        note: "感嘆文「How easy it is to...」と条件節「when your lives are never at risk」の構文です。"
      },
      {
        header: "フレーズ 4：散髪のリスクと包丁のリスクの圧倒的な差",
        g4: "He only wants your wool, but he wants my life.",
        g3: "You risk only a haircut, but I face the butcher's knife!",
        note: "「risk only a haircut」と「face the butcher's knife」という鮮烈なコントラストです。"
      }
    ],
    vocab: [
      { w: "pastoral", pos: "形", m: "牧歌的な、羊飼いの" },
      { w: "enclosure", pos: "名", m: "囲い地、構内" },
      { w: "composure", pos: "名", m: "落ち着き、沈着、平静（*keep one's composure*）" },
      { w: "condescendingly", pos: "副", m: "見下すように、恩着せがましく" },
      { w: "self-righteous", pos: "形", m: "独善的な、自分だけが正しいと思っている" },
      { w: "renewable", pos: "形", m: "再生可能な（*renewable resource*）" },
      { w: "butcher", pos: "名", m: "肉屋、屠殺業者" },
      { w: "blindness", pos: "名", m: "盲目、無知（*moral blindness*）" }
    ],
    grammar: [
      { title: "How + 形容詞 + it is + for 人 + to do", exp: "感嘆文。「〜にとって…することはなんと〜なことか！」感情を強く訴える表現です。" },
      { title: "at risk", exp: "イディオム。「危険にさらされて」。*lives at risk*（危機に瀕した命）。" }
    ],
    tips: [
      "特権階級と弱者の立場の断絶について、*Those who face no existential threat must not preach patience to marginalized groups facing annihilation.* と論評できます。"
    ]
  },
  {
    num: 56,
    key: "sick_raven",
    titleEn: "The Sick Raven",
    titleJa: "病気のカラスと母",
    imgFile: "images/vol1_sick_raven.png",
    benchmarkG4: `A black raven lived in an old tall pine tree. He had lived a bad life. Whenever he saw humans offering bread and meat to the gods on stone altars, he flew down and stole the food. He never cared about the gods.

One cold winter, the raven became terribly sick. His feathers fell out, his eyes grew cloudy, and his throat was burning. He could not stand up on his branch. He felt that death was near.

His mother sat beside him on the nest, weeping softly.

The sick raven looked at his mother and whispered: "Mother, please help me! Fly quickly to the sacred temples in the city. Pray to Apollo and the great gods for my recovery. Promise them that if I live, I will offer a grand sacrifice on their altars!"

The mother raven looked at her dying son with deep sorrow. She shook her head sadly and replied:

"My dear son, which of the gods do you think will listen to my prayers? Is there a single altar in the whole country from which you have not stolen sacred food? You have insulted every god during your healthy years. How can we expect them to show mercy now that you are dying?"

The sick raven had no answer. He closed his eyes in deep regret.`,
    targetG3: `A wild raven perched upon the gnarled branch of an ancient pine tree, suffering from an acute and debilitating illness. Throughout his youthful days, the reckless scavenger had lived an unprincipled existence. Whenever pious villagers placed roasted meats and honeyed cakes upon the sacred altars of the gods, the raven would swoop down audacity and steal the consecrated offerings.

Now, afflicted by violent fevers and failing strength, the bird lay trembling in his nest. Sensing that his life was rapidly slipping away, he called out to his mother, who was perched beside him in mourning.

"Dearest mother," the stricken bird pleaded in agony, "I implore you to fly immediately to the sacred sanctuaries of Apollo and the Olympian gods! Prostrate yourself before their shrines and petition for my physical restoration. Promise them that if they spare my life, I will dedicate a magnificent sacrifice to honor their names!"

The mother raven gazed down upon her wretched offspring with tears of profound grief. She sighed mournfully and delivered a piercing reality check:

"Alas, my foolish child, upon which deity can you possibly call for salvation? Can you name a single celestial patron whose sacred precinct you have not desecrated, or from whose holy altar you have not purloined consecrated flesh? You systematically mocked the gods throughout your prosperous health. It is preposterous to expect divine compassion now that you face the threshold of mortality."

Stricken by the truth of her indictment, the dying bird remained silent as darkness enveloped his sight.`,
    townsend: `A Raven was taken very ill and expected to die. He said to his Mother: "Pray to the gods for my recovery, and promise them a sacrifice." The Mother replied: "Alas, my son, which of the gods will have pity on you? For is there any god from whose altar you have not stolen offerings?"`,
    transJa: `野生のカラスが古代のマツの木の節くれだった枝の上で、急性の衰弱性の病気に苦しんでいました。若き日々を通じて、この無謀な腐肉食者は節操のない自堕落な生活を送っていました。信心深い村人たちが神々の神聖な祭壇の上に焼き肉や蜂蜜のケーキを供えるたびに、カラスは厚かましくも急降下し、奉納された捧げ物を盗み去っていたのです。

今や激しい高熱と衰えゆく体力に苛まれ、その鳥は巣の中で震えながら横たわっていました。自らの生命が急速に失われつつあるのを感じ取り、彼は喪に服すように隣に止まっていた母親に向かって声を絞り出しました。

「愛するお母さん」と打ちのめされた鳥は苦悶の中で懇願しました。「お願いだから今すぐアポロンやオリュンポスの神々の神聖な神殿へと飛んでいってほしい！ 神殿の前にひれ伏し、私の肉体的回復を請い求めてください。もし私の命を助けてくださるならば、神々の名を称える壮大な生贄を捧げると約束してください！」

母ガラスは深い悲しみの涙を浮かべながら、哀れなわが子を見つめました。彼女は嘆かわしそうにため息をつき、痛烈な現実を突きつけました。

「ああ、私の愚かな子よ、いったいどの神にあなたが救済を求めることができるというのですか？ あなたが冒涜しなかった神聖な境内を持つ天の守護神、あるいはあなたがその清らかな祭壇から捧げ物の肉をかすめ取らなかった神が、一人でもいるというのですか？ あなたは健康で栄えていた間、神々を組織的に侮辱し続けてきました。死の淵に直面した今になって神の慈悲を期待するなど、言語道断な思い上がりです。」

母親の告発の正しさに打ちのめされ、死にゆく鳥は沈黙したまま、視界を闇に包まれていきました。`,
    moral: "Vows made only in mortal crisis win no divine favor.（平時において道徳や信義を蔑ろにし、私利私欲のために神仏や他者を冒涜してきた者が、自らが死の危機に瀕した時だけ慌てて立てる誓言や神頼みは、誰の心にも届かず空しく消え去る。）",
    cards: [
      {
        header: "フレーズ 1：神聖な祭壇から捧げ物をかすめ取る",
        g4: "He flew down and stole the food from stone altars.",
        g3: "The raven would swoop down with audacity and steal the consecrated offerings.",
        note: "「swoop down（急降下する）」と「consecrated offerings（神聖な捧げ物）」の表現です。"
      },
      {
        header: "フレーズ 2：生命を助けてくれるなら生贄を捧げると約束する",
        g4: "Promise them that if I live, I will offer a sacrifice.",
        g3: "Promise them that if they spare my life, I will dedicate a magnificent sacrifice.",
        note: "条件節「if they spare my life」と「dedicate a sacrifice」を用いた本格構文です。"
      },
      {
        header: "フレーズ 3：一度も盗みを働かなかった祭壇がどこにあるのか",
        g4: "Which god has not had his food stolen by you?",
        g3: "Can you name a single celestial patron whose holy altar you have not purloined?",
        note: "関係代名詞の所有格「whose」を用いた、3級から準2級への最重要ステップアップ構文です。"
      },
      {
        header: "フレーズ 4：危機においてのみ慈悲を期待する不条理",
        g4: "How can we expect them to show mercy now that you are dying?",
        g3: "It is preposterous to expect divine compassion now that you face mortality.",
        note: "接続詞「now that（今や〜なのだから）」と「preposterous（常軌を逸した）」の組み合わせです。"
      }
    ],
    vocab: [
      { w: "debilitating", pos: "形", m: "衰弱させる、衰えさせる" },
      { w: "scavenger", pos: "名", m: "腐肉食動物、清掃動物" },
      { w: "consecrated", pos: "形", m: "神聖化された、奉納された" },
      { w: "sanctuary", pos: "名", m: "聖域、神殿、避難所" },
      { w: "prostrate", pos: "動", m: "ひれ伏す、平伏する" },
      { w: "desecrate", pos: "動", m: "〜を冒涜する、神聖を汚す" },
      { w: "purloin", pos: "動", m: "〜を盗む、くすねる（*steal* の文語）" },
      { w: "mortality", pos: "名", m: "死すべき運命、死亡率" }
    ],
    grammar: [
      { title: "whose + 名詞", exp: "関係代名詞の所有格。「〜の…であるところの」。先行詞の人や神の所有関係を説明します。" },
      { title: "now that + S + V", exp: "接続詞句。「今や〜である以上は、〜なのだから」。原因・理由を強調する表現です。" }
    ],
    tips: [
      "平時の信頼構築と非常時の協力について、*One cannot expect institutional support during crises if one has systematically violated organizational trust during prosperity.* と論述できます。"
    ]
  },
  {
    num: 57,
    key: "spider_and_swallow",
    titleEn: "The Spider and the Swallow",
    titleJa: "クモとツバメ",
    imgFile: "images/vol1_spider_and_swallow.png",
    benchmarkG4: `A proud black spider lived under the roof of a stone house. She was very proud of her shiny silk web. Every morning, small flies and mosquitoes flew into her sticky threads. The spider wrapped them up and ate them.

One summer day, a fast swallow flew into the garden. The swallow had long blue wings. She flew through the air like an arrow, catching flies with her open beak.

The spider watched the swallow from her corner. She felt very jealous. "That bird is stealing my flies!" thought the spider. "I am a master hunter. My web is strong. I will catch that bird and eat her!"

The foolish spider worked all afternoon. She spun a large web across the open window where the swallow often flew. She smiled and waited in the middle of her net.

Soon, the swallow came flying back toward the window at top speed.

Whoosh! The swallow did not even see the spider's web. She flew right through it. The tiny silk threads snapped instantly like thin dust.

The swallow did not even slow down. But the broken web and the spider stuck to her feathers. The swallow carried the web and the helpless spider high up into the clouds.

As the wind blew her away, the dying spider cried: "I was so proud of catching tiny flies that I forgot how weak I am against a giant bird!"`,
    targetG3: `A spider had established her residence beneath the eaves of an ancient courtyard. Possessing an abundant supply of sticky silk, she constructed intricate geometric webs that were exceptionally effective at capturing small insects. Day after day, she gorged herself on gnats and flies, which fostered a dangerous sense of supreme arrogance.

During midsummer, an agile swallow began frequenting the courtyard. Endowed with aerodynamic wings and incredible speed, the migratory bird soared gracefully through the atmosphere, effortlessly capturing insects mid-flight.

Watching this aerial master from her corner, the spider was consumed by bitter envy. "That creature dares to deplete my private hunting grounds," she grumbled indignantly. "Humans praise the swallow, but my engineering skills are superior. I shall construct a net so formidable that it will ensnare the intruder herself."

Driven by megalomaniacal ambition, the spider labored tirelessly for hours, spinning an expansive web across the courtyard gateway where the bird routinely passed. Confident in the tensile strength of her creation, the arachnid stationed herself proudly in the center.

Presently, the swallow returned, diving toward the archway with tremendous velocity.

In a fraction of a second, the collision occurred. Far from arresting the avian raptor, the fragile silk filaments disintegrated instantly upon impact. The swallow did not even register the trivial obstruction. However, the ruptured web, along with the spider herself, adhered to the bird's tail feathers.

Carried miles into the stratosphere by the unstoppable momentum of the swallow, the battered spider acknowledged her fatal delusion: "Woe is me! In my petty vanity over trapping helpless flies, I foolishly imagined my frail apparatus could withstand the sovereign forces of the sky!"`,
    townsend: `A Spider watched a Swallow catching flies in the air and felt bitter jealousy. Thinking she could trap the bird, the Spider spun a web across a courtyard where the Swallow flew. The Swallow swept past at full speed, tore right through the frail web without feeling it, and carried off the web and the Spider together.`,
    transJa: `あるクモが、古い中庭の軒下に居を構えていました。粘着性のある糸を豊富に備えていた彼女は、小さな昆虫を捕らえるのに極めて効果的な、複雑で幾何学的な網を構築していました。来る日も来る日も、彼女はブヨやハエを満腹になるまで貪り食い、それが彼女の中に絶対的な傲慢という危険な感覚を育てていきました。

真夏の間、敏捷なツバメがその中庭を頻繁に訪れるようになりました。空気力学的な翼と信じられないスピードを授かったこの渡り鳥は、大気の中を優雅に飛翔し、飛んでいる昆虫をいとも簡単に捕獲していました。

自らの巣の片隅からこの空の達人を観察しながら、クモは激しい嫉妬に苛まれました。「あの生き物は、あつかましくも私の私的な狩場を食い荒らしている」と彼女は憤慨して愚痴をこぼしました。「人間たちはツバメを賞賛するが、私の工学技術の方が遥かに優れている。あの侵入者自身を罠にかけるほどの恐るべき網を構築してやるわ。」

誇大妄想的な野心に駆られたクモは、鳥が日常的に通過する中庭の通路を横切るように広大な網を張り巡らせ、何時間も休みなく働き続けました。自らの作品の引っ張り強度に自信を深めたクモは、その中央に誇らしげに陣取りました。

やがてツバメが戻り、凄まじい速度をもってアーチ型の通路へと急降下してきました。

ほんの一瞬のうちに衝突が起こりました。鳥類の捕食者を拘束するどころか、脆い絹の繊維は衝撃の瞬間に粉々に分解してしまいました。ツバメはその些細な障害物に気づきさえしませんでした。しかしながら、破断した網は、クモ自身とともに鳥の尾羽へと付着してしまったのです。

ツバメの止められない勢いによって成層圏（上空）へ何マイルも連れ去られながら、打ちのめされたクモは自らの致命的な妄想を認めました。「ああ、何と浅ましいことか！ 無力なハエを捕まえた些細な虚栄心に目を奪われ、私は自らの脆弱な仕掛けが、空の主権的な力に対抗できるなどと愚かにも妄想してしまったのだ！」`,
    moral: "Frail stratagems are shattered in an instant by superior forces.（弱小な者が小手先の罠や策略に過信し、自らの能力を遥かに超える巨大な実力者に戦いを挑めば、仕掛けた罠ごと一撃で粉砕され連れ去られる。）",
    cards: [
      {
        header: "フレーズ 1：小虫を捕獲して危険な傲慢を育てる",
        g4: "Small flies flew into her sticky threads and she ate them.",
        g3: "She gorged herself on flies, which fostered a dangerous sense of supreme arrogance.",
        note: "関係代名詞の非制限用法「, which」を用いた原因結果の表現です。"
      },
      {
        header: "フレーズ 2：鳥自身を罠にかける恐るべき網を張る",
        g4: "I will catch that bird and eat her!",
        g3: "I shall construct a net so formidable that it will ensnare the intruder herself.",
        note: "「so ... that構文」を用いた意図・強度の強調表現です。"
      },
      {
        header: "フレーズ 3：衝突の瞬間に脆い繊維が粉々になる",
        g4: "The tiny silk threads snapped instantly like dust.",
        g3: "The fragile silk filaments disintegrated instantly upon impact.",
        note: "「filaments（極細の糸）」と「disintegrate（分解する、崩壊する）」のアカデミックな動詞です。"
      },
      {
        header: "フレーズ 4：脆弱な仕掛けが巨大な力に対抗できるという妄想",
        g4: "I forgot how weak I am against a giant bird!",
        g3: "I foolishly imagined my frail apparatus could withstand the sovereign forces of the sky!",
        note: "「frail apparatus（脆弱な仕掛け）」と「withstand（〜に耐える）」の重要表現です。"
      }
    ],
    vocab: [
      { w: "intricate", pos: "形", m: "入り組んだ、複雑な（*intricate design*）" },
      { w: "arrogance", pos: "名", m: "傲慢、尊大（*supreme arrogance*）" },
      { w: "aerodynamic", pos: "形", m: "空気力学的な、流線型の" },
      { w: "deplete", pos: "動", m: "〜を激減させる、枯渇させる" },
      { w: "ensnare", pos: "動", m: "〜を罠にかける、陥れる" },
      { w: "filament", pos: "名", m: "細い糸、フィラメント" },
      { w: "disintegrate", pos: "動", m: "崩壊する、粉々になる" },
      { w: "withstand", pos: "動", m: "〜に耐える、抵抗する" }
    ],
    grammar: [
      { title: "so + 形容詞 + that + S + V", exp: "「非常に〜なので…である」。程度や結果を表す頻出構文です。" },
      { title: "upon + 名詞", exp: "「〜の瞬間に、〜するとすぐに」。*upon impact*（衝突の瞬間に）。" }
    ],
    tips: [
      "中小の競合企業が大企業やグローバルな市場の力学に無謀に立ち向かうリスクについて、*Frail market stratagems inevitably disintegrate when confronted by macro-industrial forces.* と論証できます。"
    ]
  },
  {
    num: 58,
    key: "fisherman_piping",
    titleEn: "The Fisherman Piping",
    titleJa: "笛を吹く漁師",
    imgFile: "images/vol1_fisherman_piping.png",
    benchmarkG4: `A young fisherman lived in a small house near the blue sea. He loved music very much. He played a small wooden flute beautifully every evening. He was also a fisherman who caught fish to sell at the village market.

One morning, he had a strange idea. "Fish love dancing," he thought. "If I play my sweet music, they will hear it and jump out of the water onto the sand. Then I will not need to pull heavy wet nets all day!"

So he took his flute and a wicker basket to the seashore. He stood on a high rock above the clear blue water.

He put the flute to his lips and began to play. He played merry tunes, soft songs, and lively dance music. He played for hours under the warm sun, tapping his feet.

However, not a single fish jumped onto the shore. The ocean remained calm, and the fish swam peacefully deep in the water, ignoring his songs.

The fisherman grew tired and angry. He put his flute away into his pocket. He picked up his large, heavy net and cast it far into the waves. In a few minutes, he pulled the net back. It was filled with dozens of flapping, jumping fish!

He dumped the fish out onto the dry sand. The fish began to flip and bounce desperately in the air.

The fisherman looked at them and laughed bitterly: "You foolish creatures! When I played music for you, you refused to dance. But now that I have stopped playing, you dance with all your might!"`,
    targetG3: `A coastal fisherman who was renowned throughout his village as a talented piper journeyed to the rocky seashore one morning. Carrying both his musical pipe and his fishing gear, he conceived an eccentric experiment.

Having heard ancient myths that marine creatures were charmed by acoustic harmonies, he believed he could entice the fish to beach themselves voluntarily. "Why should I exhaust my strength casting and hauling heavy nets," he mused, "when I can simply charm them into leaping into my basket?"

Perching upon a rocky promontory overlooking the azure tide, the fisherman placed the instrument to his lips. He played lively pastoral melodies, followed by festive dance tunes that echoed across the waves. For hours he performed under the blazing sun, watching the transparent water with eager anticipation.

Yet the ocean remained utterly indifferent. The fish swam languidly through the kelp forests below, completely oblivious to his musical serenades.

Frustrated by his total failure, the piper finally recognized the futility of his approach. Relinquishing his instrument, he gathered his heavy casting net, hurled it into the surf, and hauled it ashore with practiced vigor. The mesh teemed with an abundant harvest of gasping, thrashing fish.

As he emptied the catch onto the dry gravel, the fish flopped frantically beneath the sun, leaping and convulsing in desperate bids for survival.

Observing their chaotic spasms, the fisherman addressed them with sarcastic irony: "What contrary and unreasonable creatures you are! When I piped delightful tunes to invite your merriment, you stubbornly refused to dance. Yet now that the music has ceased, you perform the most energetic dance of your lives!"`,
    townsend: `A Fisherman who was also a flute player took his pipes and nets to the seashore. Standing on a rock, he played beautiful tunes, hoping the fish would be charmed by his music and jump out onto the shore. When not a single fish appeared, he put down his pipe, cast his net, and hauled in a great catch. Throwing the flopping fish onto the sand, he said: "O foolish creatures, you would not dance when I piped, but now that I have stopped, you dance merrily!"`,
    transJa: `才能豊かな笛吹きとして村中で知られていた沿岸の漁師が、ある朝、岩だらけの海岸へと出かけました。楽器の笛と漁具の両方を携えて、彼は奇妙な実験を思いついたのです。

海の生き物たちは音響的なハーモニー（美しい音楽）に魅了されるという古代の神話を聞いていた彼は、魚たちを誘惑して自発的に浜辺へと飛び上がらせることができると信じ込んでいました。「甘美な音楽でカゴの中へと魚たちを飛び込ませることができるというのに、なぜ重い網を投げて引き揚げることに体力を消耗させねばならないのか」と彼は思案したのです。

青い潮を見下ろす岩がちの岬の上に腰掛け、漁師は楽器を唇に当てました。彼は陽気な牧歌的メロディを奏で、続いて波間にこだまする華やかなダンス曲を演奏しました。熱い太陽の下で何時間も演奏を続け、彼は熱心な期待をもって透明な水面を見つめていました。

しかしながら、大洋は完全に無関心なままでした。魚たちは下の昆布の森を物憂げに泳ぎ回り、彼の音楽的セレナーデにまったく気づきもしませんでした。

完全な失敗に苛立った笛吹きは、ついに自らの手法の無益さを認めました。楽器を手放すと、彼は重い投網をかき集めて波打ち際へと投げ込み、熟練した力強さでそれを岸へと引き揚げました。網の目は、あえぎ暴れる魚たちの豊饒な収穫で満ち溢れていました。

乾いた砂利の上に獲物をぶちまけると、魚たちは太陽の下で必死にのたうち回り、生存をかけた捨て身の試みとして飛び跳ね、痙攣しました。

彼らの混沌とした痙攣を観察しながら、漁師は皮肉な皮肉を込めて彼らに語りかけました。「なんと天邪鬼（あまのじゃく）で理不尽な生き物たちだろう！ 私がお前たちの歓喜を誘うために素晴らしい曲を奏でていたときには、お前たちは頑として踊ることを拒んだ。それなのに音楽が終わった今になって、お前たちは生涯で最も精力的なダンスを披露しているではないか！」`,
    moral: "Action out of season yields no fruit; timely vigor is everything.（時機を逸した行動は何の意味も持たない。求められている時に動かず、手遅れになってから慌てて跳ね回っても、もはや何の成果も得られず破滅を免れない。）",
    cards: [
      {
        header: "フレーズ 1：音楽で魚を飛び上がらせる奇妙な思いつき",
        g4: "If I play my sweet music, they will jump out of the water.",
        g3: "He believed he could entice the fish to beach themselves voluntarily.",
        note: "動詞「entice（誘惑する）」と「beach themselves（自ら浜に乗り上げる）」の洗練表現です。"
      },
      {
        header: "フレーズ 2：音楽のセレナーデに完全に気づかない魚たち",
        g4: "The fish swam peacefully deep in the water, ignoring his songs.",
        g3: "The fish swam languidly below, completely oblivious to his musical serenades.",
        note: "「oblivious to ...（〜に完全に気づいていない）」を用いた格調高い客観描写です。"
      },
      {
        header: "フレーズ 3：手法の無益さを悟り網を放り投げる",
        g4: "The fisherman grew tired. He picked up his net and cast it.",
        g3: "Recognizing the futility of his approach, he hurled his casting net into the surf.",
        note: "分詞構文「Recognizing the futility of...（手法の無益さを認識して）」の重要構文です。"
      },
      {
        header: "フレーズ 4：演奏中は踊らず、終わってから踊り出す皮肉",
        g4: "When I played, you refused to dance. Now that I stopped, you dance!",
        g3: "When I piped to invite your merriment, you refused. Yet now that the music ceased, you dance!",
        note: "対比の接続詞「when」と「now that」を呼応させた修辞的クライマックスです。"
      }
    ],
    vocab: [
      { w: "eccentric", pos: "形", m: "風変わりな、奇妙な" },
      { w: "entice", pos: "動", m: "〜を誘惑する、おびき寄せる" },
      { w: "promontory", pos: "名", m: "岬、突き出た崖" },
      { w: "languidly", pos: "副", m: "物憂げに、だるそうに" },
      { w: "oblivious", pos: "形", m: "気づいていない、忘れている（*oblivious to*）" },
      { w: "futility", pos: "名", m: "無益、無駄、効果のないこと" },
      { w: "contrary", pos: "形", m: "天邪鬼な、正反対の" },
      { w: "cease", pos: "動", m: "終わる、やむ、中止する" }
    ],
    grammar: [
      { title: "entice + O + to do", exp: "「Oを誘惑して〜させる」。*persuade* や *encourage* の誘惑版として重要です。" },
      { title: "Recognizing + 名詞, S + V", exp: "分詞構文（時・理由）。「〜を認識して、Sは…した」。" }
    ],
    tips: [
      "タイミングを逃した投資や危機対応の遅れについて、*Delayed compliance that occurs after catastrophic failure resembles the fish dancing only after the net has landed.* と比喩的に展開できます。"
    ]
  },
  {
    num: 59,
    key: "bear_and_bees",
    titleEn: "The Bear and the Bees",
    titleJa: "蜂と熊",
    imgFile: "images/vol1_bear_and_bees.png",
    benchmarkG4: `A big brown bear was walking through a quiet green forest. He was hungry and looking for sweet wild berries.

As he walked past an old hollow log, a small worker bee flew out. The bee was nervous because the bear was so close. The bee buzzed angrily and stung the bear right on the tip of his nose!

Ouch! The bear felt a sharp, burning pain on his nose. He rubbed his face with his paw, but the pain did not go away.

Instead of walking away calmly, the bear lost his temper completely. He roared in fury. He opened his big mouth and showed his sharp teeth.

"You tiny bug!" shouted the angry bear. "How dare you sting my royal nose! I will smash your home to pieces!"

The bear jumped on the hollow log. He used his giant claws and heavy weight to tear the wood apart. He smashed the honeycomb and broke the entrance.

Immediately, thousands of angry bees poured out of the log like a black cloud. They were furious that their home was destroyed.

The bees attacked the bear from all sides. They stung him in his ears, on his eyelids, around his mouth, and on his neck.

The screaming bear ran blindly through the forest, jumping into bushes and rolling in the dirt. He barely reached a deep river and jumped into the water to save his life.

Lying in the cold water with hundreds of painful stings, the miserable bear cried: "How foolish I was! Because of one tiny sting, I became mad with anger, and now my whole body is on fire!"`,
    targetG3: `A massive brown bear was foraging for nourishment through a dense pine forest. As he brushed past a fallen, hollow timber, an agitated honeybee emerged from the darkness. Perceiving the colossal mammal as a hostile threat to the hive, the bee darted forward and planted a painful sting directly on the tip of the bear's sensitive nose.

Afflicted by the sharp sting, the bear was seized by an uncontrollable paroxysm of rage. Rather than ignoring the minor inconvenience and continuing his journey, he allowed wounded pride to overpower his rational judgment.

Growling with savage indignation, the bear launched a ferocious assault upon the hollow log. With his formidable claws and immense physical strength, he began tearing the rotting bark to splinters, intent on annihilating the entire nest.

However, his violent vandalism triggered an immediate catastrophe. Aroused by the destruction of their sanctuary, the entire colony—tens of thousands of aggressive defenders—surged out of the shattered log like an ominous storm cloud.

Before the bear could retreat, the furious swarm engulfed his massive head. The insects stung him mercilessly in his nostrils, across his tender eyelids, inside his ears, and upon every unprotected patch of skin.

Howling in excruciating agony, the frantic beast galloped blindly through the forest, crashing through brambles and thrashing against trees. He finally plunged into the freezing waters of a mountain stream, submerging his swollen head beneath the surface to escape total extermination.

Exhausted, battered, and covered in hundreds of throbbing welts, the chastened bear lamented his catastrophic error: "What utter madness! In seeking reckless vengeance for a single insignificant prick, I provoked an entire army and brought overwhelming torment upon myself."`,
    townsend: `A Bear was stung by a single bee that flew out of a hollow tree. Enraged by the pain, the Bear attacked the hive with claws and teeth, tearing it apart. Thereupon the whole swarm poured out and attacked him, stinging him mercilessly about the eyes, ears, and nose. The Bear barely escaped with his life, lamenting that a moment's rage over one tiny sting had brought him hundreds of painful wounds.`,
    transJa: `巨大なヒグマが鬱蒼としたマツの森の中を、食料を求めて徘徊していました。彼が倒れてうろのできた材木のそばをかすめて通り過ぎたとき、興奮した一匹のミツバチが暗闇から飛び出してきました。その巨大な哺乳類を巣に対する敵対的な脅威と認識した蜂は、前へと突進し、クマの敏感な鼻の頭に直接、痛烈な一刺しを浴びせました。

鋭い痛みに苛まれ、クマは制御不能な激怒の発作に襲われました。些細な不快感を無視して旅を続けるどころか、彼は傷つけられたプライドによって理性的判断を圧倒させてしまったのです。

獰猛な憤怒とともに唸り声を上げながら、クマはうろのある丸太に対する激しい急襲を開始しました。その恐るべき爪と巨大な物理的怪力をもって、彼は巣全体を壊滅させようと意図し、腐りかけた樹皮を木っ端微塵に引き裂き始めました。

しかしながら、彼の暴力的な破壊行為は即座の破滅を引き起こしました。聖域の破壊によって怒り狂ったコロニー全体（何万匹もの攻撃的な防衛軍）が、不吉な嵐の雲のように粉々になった丸太から押し寄せてきたのです。

クマが退却する暇もなく、猛り狂った大群がその巨大な頭部を包み込みました。昆虫たちは彼の鼻孔、繊細なまぶた、耳の内部、そしてあらゆる保護されていない皮膚の隙間を容赦なく刺し続けました。

耐え難い苦痛のあまり遠吠えを上げながら、狂乱した獣は森の中を盲目的に疾走し、野ばらの茂みを突き破り、木々に体を激突させました。彼は最終的に山あいの小川の凍てつく水の中へと飛び込み、完全な殺戮から逃れるために腫れ上がった頭部を水面下へと沈めました。

疲労困憊し、打ちのめされ、何百もの疼く腫れ物に覆われながら、懲らしめられたクマは自らの破滅的な過ちを嘆きました。「なんという純然たる狂気だろう！ たった一刺しの些細な傷に対する見境なき復讐を求めたばかりに、私は軍隊全体を挑発し、自らに圧倒的な苦痛を招き寄せてしまったのだ。」`,
    moral: "Blind rage inflames a minor sting into catastrophic destruction.（一時の些細な痛手や侮辱に対して理性を失って激怒し、過剰な報復を仕掛ける者は、相手の組織全体を敵に回して何百倍もの壊滅的打撃を自らに招く。）",
    cards: [
      {
        header: "フレーズ 1：些細な不快感を無視できず理性を失う",
        g4: "Instead of walking away calmly, the bear lost his temper.",
        g3: "Rather than ignoring the minor inconvenience, he allowed wounded pride to overpower his judgment.",
        note: "「Rather than + 動名詞」と「overpower rational judgment」を用いた高度な心理描写です。"
      },
      {
        header: "フレーズ 2：巣全体を壊滅させようと暴力を振るう",
        g4: "He used his giant claws to tear the wood apart.",
        g3: "With his formidable claws, he began tearing bark to splinters, intent on annihilating the nest.",
        note: "「tear A to splinters（Aを粉々に引き裂く）」と「intent on + 動名詞（〜を企図して）」の表現です。"
      },
      {
        header: "フレーズ 3：何万匹もの防衛軍が嵐のように湧き出す",
        g4: "Thousands of angry bees poured out of the log like a cloud.",
        g3: "Tens of thousands of defenders surged out of the shattered log like an ominous storm cloud.",
        note: "比喩表現「surged out ... like an ominous storm cloud」の迫力ある英文です。"
      },
      {
        header: "フレーズ 4：一匹の蜂への復讐が軍隊全体を挑発した",
        g4: "Because of one tiny sting, my whole body is on fire!",
        g3: "In seeking reckless vengeance for a single prick, I provoked an entire army.",
        note: "「seeking reckless vengeance（見境のない復讐を求めて）」という決定的な教訓フレーズです。"
      }
    ],
    vocab: [
      { w: "agitated", pos: "形", m: "動揺した、興奮した" },
      { w: "paroxysm", pos: "名", m: "（感情・病気の）激発、発作（*paroxysm of rage*）" },
      { w: "vandalism", pos: "名", m: "器物破損、蛮行" },
      { w: "annihilate", pos: "動", m: "〜を全滅させる、壊滅させる" },
      { w: "ominous", pos: "形", m: "不吉な、険悪な" },
      { w: "excruciating", pos: "形", m: "耐え難い、極痛の（*excruciating pain*）" },
      { w: "chastened", pos: "形", m: "懲らしめられた、反省した" },
      { w: "vengeance", pos: "名", m: "復讐、報復（*revenge* の重い語）" }
    ],
    grammar: [
      { title: "Rather than + 動名詞 ..., S + V", exp: "「〜するのではなくむしろ…した」。対照的な選択肢を比較する重要構文です。" },
      { title: "intent on + 動名詞 / 名詞", exp: "「〜に専念して、〜を目論んで」。強い意志や執念を表します。" }
    ],
    tips: [
      "些細な挑発に対する過剰反応の自滅リスクについて、*Emotional overreaction to minor slights frequently triggers disproportionate institutional blowback.* と論証できます。"
    ]
  },
  {
    num: 60,
    key: "traveler_and_fortune",
    titleEn: "The Traveler and Fortune",
    titleJa: "旅人と運命の女神",
    imgFile: "images/vol1_traveler_and_fortune.png",
    benchmarkG4: `A tired traveler was walking along a lonely mountain road. He had been walking for many days under the hot sun. His boots were worn out, and his legs felt like heavy stones.

Near the road, he found an old stone well. The well was very deep, and the stone walls were broken and slippery.

The foolish traveler sat down right on the edge of the well. He closed his eyes and immediately fell into a deep sleep. His head leaned over the dark hole. If he moved even one inch in his sleep, he would fall into the water and die!

Just at that dangerous moment, the goddess Fortune appeared in the air. She wore a bright golden robe and had wings like light.

Fortune looked at the sleeping man and tapped him gently on his shoulder.

"Wake up, my friend!" whispered the goddess softly.

The traveler woke up with a start. He looked down into the dark abyss and jumped backward in terror.

The goddess Fortune smiled calmly and said to him:

"You should thank me for waking you. But remember this lesson: if you had fallen into that deep well and drowned, your friends and family would not blame your own foolish laziness. Instead, they would point their fingers at me and cry: 'Oh, cruel Fortune! Bad luck killed him!' Humans always take credit for their good luck, but they always blame Fortune for their own stupid mistakes."

With those wise words, the goddess vanished into the clouds.`,
    targetG3: `A weary traveler had journeyed for many exhausting days across an arid and desolate plateau. His provisions were nearly depleted, his garments were stained with road dust, and his limbs trembled with profound fatigue.

Stumbling upon an ancient stone cistern situated beside the road, the exhausted wayfarer sought immediate repose. The well was perilous: its brick rim had partially collapsed, and the dark shaft descended vertically into cold, bottomless water.

Disregarding all rudimentary instincts of self-preservation, the reckless traveler sat down directly on the precipitous ledge and drifted into an unconscious slumber. His torso swayed precarious above the abyss; the slightest inadvertent movement would cause him to plunge headlong to his doom.

At that critical juncture, the personification of Fortune materialized before the sleeping mortal, enveloped in radiant celestial splendor.

Approaching the brink with graceful footsteps, the goddess shook the traveler's shoulder and summoned him back to consciousness: "Awake, heedless mortal, and retreat from this lethal precipice!"

The traveler gasped in horror as he recognized that he had been slumbering inches from absolute catastrophe.

Before the trembling wanderer could utter an apology, Fortune addressed him with piercing philosophical clarity:

"Recognize your deliverance, foolish traveler. Yet reflect upon human hypocrisy: had you plummeted into that aqueous chasm, your acquaintances would never have attributed the disaster to your own gross negligence. Invariably, they would have reviled Fortune, lamenting that ill luck had claimed an innocent victim. Mortals perpetually ascribe their successes to personal genius, yet stubbornly blame Fortune for the inevitable consequences of their own folly."`,
    townsend: `A tired Traveler lay down and fell asleep right at the slippery edge of a deep well. Fortune appeared beside him, woke him, and said: "Rise, my friend, and depart. For if you had fallen into the well, men would not have blamed your own reckless carelessness, but would have cursed Fortune for your death!"`,
    transJa: `疲労困憊した旅人が、乾燥して荒涼とした高原を何日も過酷な旅を続けていました。彼の食料はほぼ枯渇し、衣服は街道の埃で汚れ、その手足は深い疲労のために震えていました。

街道のそばに位置していた古い石造りの貯水井戸に偶然出くわした疲れた旅人は、即座の休息を求めました。その井戸は危険極まりないものでした。レンガの縁は部分的に崩壊し、暗い立て坑が冷たく底知れない水の中へと垂直に降下していたのです。

自己保存の初歩的な本能をすべて無視して、無謀な旅人は切り立った崖のような井戸の縁に直接腰を下ろし、無意識の眠りへと落ちていきました。彼の胴体は深淵の上で不安定に揺れ動いていました。眠りの中でのほんのわずかな不注意な身動き一つが、彼を自らの破滅へと真っ逆さまに転落させる状況だったのです。

その危機的な瞬間、輝かしい天上の光彩に包まれながら、運命の女神フォーチュンの擬人化された姿が、眠れる定命の人間の前に出現しました。

優雅な足取りで縁へと近づいた女神は、旅人の肩を揺さぶり、彼を意識へと呼び戻しました。「目を覚ましなさい、軽率な定命の者よ。そしてこの致死的な断崖から退きなさい！」

旅人は、自分が絶対的な大惨事からわずか数インチのところで眠りこけていたことを認識し、恐怖のあまり息を呑みました。

震える放浪者が謝罪を口にする間もなく、運命の女神は鋭い哲学的明晰さをもって彼に語りかけました。

「自らが救われたことを認識しなさい、愚かな旅人よ。そして人間の偽善を省みるのです。もしあなたがその水底の裂け目へと急落していたなら、あなたの知人たちは決してその惨事をあなた自身の甚だしい過失に帰することはなかったでしょう。彼らは決まって運命を罵倒し、悪運が無実の犠牲者を奪ったと嘆いたはずです。人間は自らの成功を常に個人の才能に帰属させるくせに、自らの愚行の不可避の結末については、頑固に運命のせいにするものなのですから。」`,
    moral: "Men credit themselves with triumph, but curse Fortune for their own folly.（人間は自らの成功や幸運を『自分の実力と才能』の賜物だと誇る一方で、自らの怠慢や過失による失敗については『運が悪かった、運命のいたずらだ』と責任転嫁する身勝手な生き物である。）",
    cards: [
      {
        header: "フレーズ 1：自己保存の本能を無視して井戸の縁で眠る",
        g4: "He sat down on the edge of the well and fell asleep.",
        g3: "Disregarding all instincts of self-preservation, he drifted into slumber on the ledge.",
        note: "分詞構文「Disregarding all instincts of self-preservation」による高度な導入です。"
      },
      {
        header: "フレーズ 2：不注意なわずかな動きが転落死を招く",
        g4: "If he moved even one inch, he would fall and die.",
        g3: "The slightest inadvertent movement would cause him to plunge to his doom.",
        note: "仮定法的なニュアンスを持つ主語「The slightest inadvertent movement」を用いた無生物主語構文です。"
      },
      {
        header: "フレーズ 3：過失を顧みず運命のせいにする人間の偽善",
        g4: "They would not blame your laziness, but would cry: 'Bad luck killed him!'",
        g3: "They would never have attributed disaster to negligence, but would have reviled Fortune.",
        note: "仮定法過去完了「would have attributed A to B（AをBのせいにしただろう）」の重要構文です。"
      },
      {
        header: "フレーズ 4：成功は己の功、失敗は運のせいにする身勝手さ",
        g4: "Humans take credit for good luck, but blame Fortune for stupid mistakes.",
        g3: "Mortals ascribe successes to personal genius, yet blame Fortune for their own folly.",
        note: "格言の対比構造「ascribe A to B, yet blame C for D」を用いた最高格式の結びです。"
      }
    ],
    vocab: [
      { w: "arid", pos: "形", m: "乾燥した、不毛の（*arid climate*）" },
      { w: "cistern", pos: "名", m: "貯水槽、井戸" },
      { w: "precipitous", pos: "形", m: "険しい、切り立った、急な" },
      { w: "inadvertent", pos: "形", m: "うっかりした、不注意な、偶然の" },
      { w: "plunge", pos: "動", m: "突っ込む、急落する、身を投げる" },
      { w: "negligence", pos: "名", m: "怠慢、過失（*gross negligence* = 重過失）" },
      { w: "ascribe", pos: "動", m: "〜を（…のせいに）帰する（*ascribe A to B*）" },
      { w: "folly", pos: "名", m: "愚行、愚かさ" }
    ],
    grammar: [
      { title: "ascribe + A + to + B", exp: "「AをBの成果・原因とみなす」。学術・評論で *attribute A to B* と並ぶ最重要動詞です。" },
      { title: "The slightest + 名詞 + would ...", exp: "無生物主語による仮定表現。「ほんのわずかな〜でも…だろう」。" }
    ],
    tips: [
      "自己帰属バイアス（成功は内因、失敗は外因に帰する心理）について、*Behavioral psychologists note that individuals routinely exhibit self-serving bias, ascribing victories to merit while blaming fortune for negligence.* と論述できます。"
    ]
  }
];

console.log("Writing Volume 21 Chapters...");
chapters.forEach(ch => {
  const fileName = `chapter${ch.num}_${ch.key}.md`;
  const filePath = path.join(kindleDir, fileName);

  let md = `# Chapter ${ch.num}: ${ch.titleEn} (${ch.titleJa})

<!-- Kindle Page Break & Image Header -->
<div style="text-align: center; margin-bottom: 20px;">
  <img src="${ch.imgFile}" alt="${ch.titleEn} Illustration" style="max-width: 100%; height: auto;" />
</div>

<div style="page-break-before: always;"></div>

## 1. Benchmark Level: Eiken Grade 4 (英検4級レベル本文)
*Read in ~1.5 to 2 minutes. Simple vocabulary and basic syntax.*

${ch.benchmarkG4}

---
<div style="page-break-before: always;"></div>

## 2. Target Level: Eiken Grade 3 (英検3級レベル本文)
*Read in ~2 to 2.5 minutes. Richer vocabulary and natural sentence flow.*

${ch.targetG3}

---
<div style="page-break-before: always;"></div>

## 3. Classic Original English Text (イソップ寓話クラシック原文)
*Translated by George Fyler Townsend (1867)*

${ch.townsend}

---
<div style="page-break-before: always;"></div>

## 4. Japanese Translation & Moral (日本語訳と教訓)

### 【日本語全訳：英検3級レベル本文】
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
  <div class="card-row-g4"><span class="card-badge-g4">4級</span>${card.g4}</div>
  <div class="card-row-g3"><span class="card-badge-g3">3級</span>${card.g3}</div>
  <div class="card-note"><strong>解説：</strong>${card.note}</div>
</div>\n\n`;
  });

  md += `---
<div style="page-break-before: always;"></div>

## 6. Key Vocabulary & Exam Notes (英検3級 重要語彙・文法・面接対策)

### 1. 英検3級 必須ボキャブラリー
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
console.log("SUCCESS: All 10 Volume 21 Chapters generated!");

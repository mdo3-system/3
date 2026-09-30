# 電子書籍（電子書籍 / 楽天Kobo）全自動出版・制作ロジック・完全仕様マニュアル

本書は、『英検ステップアップ多読：イソップ寓話編』シリーズ（全4巻）を電子書籍化し、**電子書籍ストア（KDP）** および **楽天Kobo（KWL）** の両プラットフォームへエラーなく全自動出稿・出版するための**完全制作ロジック規定書**です。

---

## 1. 全制作ロジック ＆ ビルドワークフロー（Build Architecture）

当プロジェクトにおけるテキスト変換、CSS構築、レイアウト最適化、パッケージングの全ロジックは以下の設計思想に従って自動化されています。

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. 各章マークダウン原稿 (.md)                                                 │
│    ├─ 章前半: 純英文セクション (ステップ1〜3: 朗読・TTS最優先)                    │
│    └─ 章後半: 日本語訳・対比カード・解説ノート (解説・暗唱学習)                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. ビルドスクリプト処理 (Node.js & PowerShell)                               │
│    ├─ 表構造変換: 4列Markdown/HTML表 ➔ <div class="comparison-card"> カード化   │
│    ├─ 改ページ処理: 手動改ページタグ (<div style="page-break...">) の完全除去       │
│    ├─ 画像参照置換: 級別専用イラスト (images/volX_story.png) への自動紐付け          │
│    └─ メタデータ注入: dc:language (KDP=en/ja, Kobo=ja) & TOC (NCX/NAV) 自動生成   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. 出力成果物                                                               │
│    ├─ Amazon KDP用: eiken3_fables_vol1.epub / eiken3_fables_vol1_kdp.zip    │
│    └─ 楽天Kobo用  : eiken3_fables_vol1_kobo.epub + kobo_vol1_cover.jpg        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ⚙️ 核心ビルドロジック仕様
1. **改ページ記述の完全排除（No Page Breaks）**:  
   原稿マークダウンおよびHTML内に `<div style="page-break-before: always;"></div>` や `↓（改ページ）` などの手動改ページタグ・注釈テキストを**一切記述しない**。リフロー端末表示、画面サイズ変更、連続朗読（TTS）の安定化を図ります。
2. **Markdown/HTML表のレスポンシブカード化（No Wide Tables）**:  
   KDPの Enhanced Typesetting (KFX) 審査エラー「お客様のファイルを正常に変換できませんでした」を防止するため、4列テーブルをすべて以下のレスポンシブカード構造へ全自動変換します。
   ```html
   <div class="comparison-card">
     <div class="card-header">■ 場面：[シーン説明]</div>
     <div class="card-row-g4"><span class="card-badge-g4">【基礎レベル】</span> [基礎英文]</div>
     <div class="card-row-g3"><span class="card-badge-g3">【暗唱レベル】</span> <strong>[ターゲット高度英文]</strong></div>
     <div class="card-note">【ポイント】 <strong>解説・試験活用</strong>：[解説テキスト]</div>
   </div>
   ```
3. **音声読み上げ機能 (TTS) ＆ OS朗読最適化構造**:  
   各章の前半（ステップ1〜3）は純英文のみで構成し、日本語訳や解説・注釈は章後半に配置します。これにより、音声読み上げ機能 (TTS) やスマホOS（iOS画面読み上げ/Android TalkBack）を起動した際、日本語に邪魔されることなくネイティブ発音の英文ストーリーが連続朗読されます。

---

## 2. 級別（レベル別）挿絵・画像生成のアートディレクション規定

挿絵は単なる飾りではなく、**「対象読者の精神年齢・発達段階・学習世界観」** に合致させた新規生成を行う規定としています。

### 🎨 対象級別の挿絵スタイル・プロンプト設計方針

| 巻 | 対象レベル | ターゲット読者層 | 挿絵のアートスタイル・世界観 | プロンプト設計キーワード |
| :--- | :--- | :--- | :--- | :--- |
| **第1巻** | 4級 ➔ 3級 | 小中学生〜英語初学者 | **ファンタジー絵本タッチ**<br>(Vibrant Fairy Tale Storybook) | *vibrant colors, friendly storybook art, warm lighting, approachable fantasy illustration, clear character expressions* |
| **第2巻** | 3級 ➔ 準2級 | 中高生〜日常英語学習者 | **温かみのある水彩画風寓話アート**<br>(Warm Watercolor Fable Art) | *artistic watercolor painting, expressive brushstrokes, natural outdoor scenery, soft pastel tones, classic fable aesthetic* |
| **第3巻** | 準2級 ➔ 2級 | 高校生〜社会人・フォーマル英語 | **西洋古典油絵・絵画タッチ**<br>(Classic European Oil Painting) | *rich oil painting texture, dramatic chiaroscuro lighting, elegant European fable fine art, sophisticated details, dark rich tones* |
| **第4巻** | 2級 ➔ 準1級 | 大学生・社会人・最高峰アカデミック層 | **格調高き西洋古典版画・エッチング**<br>(Vintage Fine Art Woodcut / Etching) | *intricate vintage line engraving, classic woodcut fine art, deep sepia/muted tones, academic literary aesthetic, museum quality* |

### 🖼️ 表紙画像（Cover）の完全規格
* **寸法・アスペクト比**: **幅 1600 px × 高さ 2560 px** (縦横比 1 : 1.6)。
* **フォーマット**: **JPEG (`.jpg`) / 24bit RGB (sRGB)**。
* **トリミング防止（Aspect Fit）**: 画像全体をキャンバス内に納め、タイトル文字や枠線が端末画面端で削られない保護マージンを適用。
* **レベル別カラーコード**:
  * 第1巻（3級）: スカイブルー (`#3498DB`) — 王道学習感
  * 第2巻（準2級）: エメラルドグリーン (`#16A085`) — 成長とステップアップ
  * 第3巻（2級）: ロイヤルパープル (`#8E44AD`) — フォーマル・エレガンス
  * 第4巻（準1級）: ディープレッド (`#C0392B`) — 最高峰アカデミック

---

## 3. プラットフォーム別（電子書籍 KDP vs 楽天Kobo KWL）出稿仕様

### 1. 電子書籍 (KDP) 仕様
* **受入フォーマット**: EPUB3 (`.epub`) または KDP原稿パッケージ (`.zip`)。
* **音声朗読**: 音声読み上げ機能 (TTS) / VoiceView 自動適合。
* **組版エンジン**: Enhanced Typesetting (KFX) 全自動変換。

### 2. 楽天Kobo (KWL: Kobo Writing Life) 仕様
* **受入フォーマット**: EPUB3 (`.epub`) 原稿 ＋ 独立表紙画像 (`.jpg`)。
* **言語指定**: **`<dc:language>ja</dc:language>`** （※日本のKoboストアの語学・英語学習カテゴリーに自動分類されます）。
* **音声朗読**: Kobo端末自体は自動TTS非搭載。ただしiPhone / Androidの「Koboアプリ」にてOS標準読み上げ（iOS画面読み上げ / Android TalkBack）を起動することで、章前半の英文が連続朗読可能。

---

## 4. 全作成ファイル ＆ ビルドスクリプト・インデックス

プロジェクトディレクトリ (`c:\Users\kokim\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle`) 内の主要成果物一覧です。

### ■ 各巻マークダウン原稿ファイル
* **第1巻**: `00_introduction.md`, `chapter01_*.md` 〜 `chapter10_*.md`, `99_epilogue_and_next_volume.md`
* **第2巻**: `vol2_00_introduction.md`, `vol2_chapter01_*.md` 〜 `vol2_chapter10_*.md`, `vol2_99_epilogue_and_next_volume.md`
* **第3巻**: `vol3_00_introduction.md`, `vol3_chapter01_*.md` 〜 `vol3_chapter10_*.md`, `vol3_99_epilogue_and_next_volume.md`
* **第4巻**: `vol4_00_introduction.md`, `vol4_chapter01_*.md` 〜 `vol4_chapter10_*.md`, `vol4_99_epilogue_and_next_volume.md`

### 📦 出力パッケージ（電子書籍用 ＆ 楽天Kobo用）
* **第1巻（3級編）**: 
  * 電子書籍用: [eiken3_fables_vol1.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eiken3_fables_vol1.epub) / [eiken3_fables_vol1_kdp.zip](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eiken3_fables_vol1_kdp.zip)
  * Kobo用  : [eiken3_fables_vol1_kobo.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eiken3_fables_vol1_kobo.epub) ｜ 表紙: [images/kobo_vol1_cover.jpg](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/images/kobo_vol1_cover.jpg)
* **第2巻（準2級編）**: 
  * 電子書籍用: [eikenPre2_fables_vol2.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eikenPre2_fables_vol2.epub) / [eikenPre2_fables_vol2_kdp.zip](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eikenPre2_fables_vol2_kdp.zip)
  * Kobo用  : [eikenPre2_fables_vol2_kobo.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eikenPre2_fables_vol2_kobo.epub) ｜ 表紙: [images/kobo_vol2_cover.jpg](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/images/kobo_vol2_cover.jpg)
* **第3巻（2級編）**: 
  * 電子書籍用: [eiken2_fables_vol3.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eiken2_fables_vol3.epub) / [eiken2_fables_vol3_kdp.zip](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eiken2_fables_vol3_kdp.zip)
  * Kobo用  : [eiken2_fables_vol3_kobo.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eiken2_fables_vol3_kobo.epub) ｜ 表紙: [images/kobo_vol3_cover.jpg](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/images/kobo_vol3_cover.jpg)
* **第4巻（準1級編）**: 
  * 電子書籍用: [eikenPre1_fables_vol4.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eikenPre1_fables_vol4.epub) / [eikenPre1_fables_vol4_kdp.zip](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eikenPre1_fables_vol4_kdp.zip)
  * Kobo用  : [eikenPre1_fables_vol4_kobo.epub](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/eikenPre1_fables_vol4_kobo.epub) ｜ 表紙: [images/kobo_vol4_cover.jpg](file:///c:/Users/kokim/Dropbox/%E2%96%A0%E8%A8%AD%E8%A8%88%EF%BD%BB%EF%BE%8E%EF%BE%9F%EF%BD%B0%EF%BE%84/%E2%96%A0note/antigravity/kindle/images/kobo_vol4_cover.jpg)

### 🛠️ 自動化ビルド＆挿絵生成スクリプト
* **`create_level_illustrations.ps1`**: 全40枚の級別挿絵（絵本/水彩/油絵/古典版画）のフレーム・バッジ全自動合成
* **`rebuild_all_volumes.js`**: 全4巻のマークダウン解析・EPUB/ZIPパッケージング一括自動再構築
* **`build_kobo_epubs.js`**: 楽天Kobo専用EPUB3 ＆ 独立表紙画像生成スクリプト

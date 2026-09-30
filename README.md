# DAILY HERO & EIKEN STUDIO (長男専用 学習＆日課ポータル)

長男向けの自律学習・生活習慣化・英検学習・資産形成シミュレーションを統合したPWA対応Webアプリケーションです。

---

## 1. プロジェクト基本情報 & インフラ構成

| 項目 | 設定値 / URL |
| :--- | :--- |
| **GitHub リポジトリ** | `git@github.com:mdo3-system/3.git` |
| **本番公開URL** | [https://3.mdo3.com](https://3.mdo3.com) |
| **本番サーバー (Xserver)** | `mdo3@mdo3.xsrv.jp` (ポート: `10022`) |
| **本番サーバー配置ディレクトリ** | `mdo3/public_html/3` |

---

## 2. デプロイ手順 (本番反映フロー)

GitHubの `main` ブランチに変更をプッシュした後、以下のSSHコマンドを実行してXserverへ即時デプロイします。

```bash
ssh -o BatchMode=yes -p 10022 mdo3@mdo3.xsrv.jp "cd mdo3/public_html/3 && git pull origin main"
```

---

## 3. バージョン管理 & 運用ルール

### 3.1 原則
- **パッチバージョンの自動インクリメント:** コードを修正・機能追加・微調整する際は、必ずパッチバージョンをインクリメント（`*.*.+1`）します。
- **`Version.js` の更新:** 変更を加えるたびに、変更内容の履歴コメントを追記し、`APP_VERSION` を更新してユーザーへ提示します。

### 3.2 `Version.js` テンプレート
```javascript
/**
 * Application Version Management
 * 
 * [Changelog]
 * - v1.0.0 (2026-09-30): Initial Release - DAILY HERO & EIKEN STUDIO
 */
const APP_VERSION = "1.0.0";

if (typeof window !== "undefined") {
  window.APP_VERSION = APP_VERSION;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = { APP_VERSION };
}
```

---

## 4. 長男用ツールの完成度と機能概要

### 4.1 現在の完成状況
**【完成度：約95%（基幹機能・コンテンツ60話・UI/UX実装完了）】**
現在、スタンドアロンHTML（`study_portal_for_son.html`）およびPythonビルドパイプライン（`build_son_study_portal.py`）により、全機能が動作する状態になっています。

### 4.2 提供機能・システム詳細

```mermaid
graph TD
    A[DAILY HERO & EIKEN STUDIO] --> B[1. 日課・クエスト管理]
    A --> C[2. イソップ英検スタジオ (全60話)]
    A --> D[3. 報酬・資産成長ダッシュボード]
    
    B --> B1[タスクチェック & 連続ボーナス]
    B --> B2[Google Drive写真提出 & Gemini AI確認テスト]
    B --> B3[未達成ペナルティ & 倍率システム]
    
    C --> C1[5段階グレード切替 (4級/3級/準2級/2級/準1級/Classic)]
    C --> C2[Web Speech API 英語ネイティブ音声再生]
    C --> C3[暗記用 赤シート機能 (単語/文法)]
    C --> C4[教訓・試験ポイント解説]
    C --> C5[Veo 3 / YouTube 動画プレイヤー]
    
    D --> D1[報酬50% 即時利用 (Suica / 楽天キャッシュ)]
    D --> D2[報酬50% 投資信託シミュレーション]
```

#### ① 日課・習慣化クエスト（Daily Routine & Quests）
- **朝・夕・夜のタスクチェックリスト:** 部屋の整理整頓、宿題、学習日課の達成管理。
- **Google Drive提出 & AI確認テスト:** 宿題や学習ノートの写真をDriveにアップロードし、Gemini AIが内容を判定・確認クイズを出題してクリア判定。
- **ペナルティ＆連続達成倍率:**
  - 連続達成で報酬倍率がアップ（最大2.0倍）。
  - 未達成が続くと警告・ペナルティモードが発動し、緊張感を持って習慣化を促す。

#### ② イソップ英検スタジオ（Aesop Fables Eiken Studio - 全60話）
- **全60話のイソップ寓話マスターデータ:** 
  - **4級 (Grade 4)**
  - **3級 (Grade 3)**
  - **準2級 (Grade Pre-2)**
  - **2級 (Grade 2)**
  - **準1級 (Grade Pre-1)**
  - **クラシック原文 (Classic Original Text - Townsend/Jacobs版)**
- **インタラクティブ赤シート機能:**
  - 赤シートボタンをONにすると、重要単語・構文がマスキングされ、クリックでめくりながら暗記学習が可能。
- **ネイティブ音声読み上げ（TTS）:**
  - ブラウザ標準の Web Speech API を活用し、自然な発音・速度調整付きでリスニング＆シャドーイング学習が可能。
- **教訓・英検ライティング/スピーキング解説:**
  - 各話の最後に、英検の英作文や面接で使える重要表現と人生の教訓（Moral）を掲載。
- **Veo 3 / YouTube連動:**
  - 生成AI動画（Google Veo 3）やYouTube動画を埋め込み再生。

#### ③ 報酬・資産形成シミュレーション（Asset & Growth Dashboard）
- **報酬の5:5スプリット配分システム:**
  - **50%:** Suica / 楽天キャッシュ（日常のお小遣い・即時利用分）
  - **50%:** 投資信託（長期複利運用シミュレーション）
- 日々の努力が将来どれだけの資産価値になるかを視覚化し、金融教育・自律的な学習意欲を育む仕組み。

---

## 5. ファイル構成

- [study_portal_for_son.html](file:///d:/Dropbox/■設計ｻﾎﾟｰﾄ/■note/antigravity/kindle/study_portal_for_son.html) : 本番用ポータルHTML（単一ファイルで完全動作）
- [build_son_study_portal.py](file:///d:/Dropbox/■設計ｻﾎﾟｰﾄ/■note/antigravity/kindle/build_son_study_portal.py) : 全60話のMD・JSONからポータルHTMLを自動ビルドするPythonスクリプト
- [Version.js](file:///d:/Dropbox/■設計ｻﾎﾟｰﾄ/■note/antigravity/kindle/Version.js) : バージョン管理・リリース履歴定義ファイル
- [README.md](file:///d:/Dropbox/■設計ｻﾎﾟｰﾄ/■note/antigravity/kindle/README.md) : 本ドキュメント

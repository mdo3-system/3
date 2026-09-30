import os
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
VEO3_JSON = os.path.join(BASE_DIR, "veo3_production", "veo3_prompts_master.json")
SNS_JSON = os.path.join(BASE_DIR, "sns_posts", "all_sns_posts_master.json")
YT_REGISTRY_JSON = os.path.join(BASE_DIR, "youtube_urls_registry.json")
PORTAL_FILE = os.path.join(BASE_DIR, "video_production_portal.html")

with open(VEO3_JSON, "r", encoding="utf-8") as f:
    veo3_data = json.load(f)

with open(SNS_JSON, "r", encoding="utf-8") as f:
    sns_data = json.load(f)

yt_registry = {}
if os.path.exists(YT_REGISTRY_JSON):
    with open(YT_REGISTRY_JSON, "r", encoding="utf-8") as f:
        yt_registry = json.load(f)

# Merge story data (Support all 60 chapters)
veo3_map = {item["chapter"]: item for item in veo3_data.get("stories", [])}
combined_stories = []

for ch_num in range(1, 61):
    ch_key = f"chapter{ch_num:02d}"
    veo3_item = veo3_map.get(ch_num, {})
    sns_item = sns_data.get(ch_key, {})
    ch_yt_urls = yt_registry.get(ch_key, {})
    
    title_en = sns_item.get("title_en") or veo3_item.get("titleEn") or f"Chapter {ch_num}"
    title_ja = sns_item.get("title_ja") or veo3_item.get("titleJa") or f"第{ch_num}話"
    key = veo3_item.get("key") or ch_key
    ref_img = veo3_item.get("referenceImage") or f"images/chapter{ch_num:02d}.png"
    clips = veo3_item.get("clips", [])
    
    combined_stories.append({
        "chapter": ch_num,
        "key": key,
        "titleEn": title_en,
        "titleJa": title_ja,
        "referenceImage": ref_img,
        "clips": clips,
        "youtubeUrls": ch_yt_urls,
        "sns": sns_item
    })

combined_json_str = json.dumps(combined_stories, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MDO3出版 Video Automation Studio | 英語古典多読スタジオ</title>
  <!-- Google Fonts & Lucide Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <style>
    :root {{
      --bg-dark: #0b0f19;
      --card-bg: rgba(22, 30, 49, 0.75);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover: rgba(30, 41, 67, 0.9);
      --accent-primary: #38bdf8;
      --accent-gradient: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent-green: #10b981;
      --accent-gold: #fbbf24;
      --accent-rose: #f43f5e;
      --red-sheet-color: #d90429;
      --radius-lg: 16px;
      --radius-md: 10px;
      --radius-sm: 6px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      display: flex;
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(192, 132, 252, 0.12) 0px, transparent 50%);
      background-attachment: fixed;
    }}

    /* Sidebar */
    .sidebar {{
      width: 280px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(20px);
      border-right: 1px solid var(--card-border);
      display: flex;
      flex-direction: column;
      padding: 24px 16px;
      position: fixed;
      height: 100vh;
      z-index: 100;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 0 8px 24px;
      border-bottom: 1px solid var(--card-border);
    }}

    .brand-icon {{
      width: 42px;
      height: 42px;
      border-radius: var(--radius-md);
      background: var(--accent-gradient);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #0b0f19;
      box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }}

    .brand-text h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}

    .brand-text span {{
      font-size: 0.72rem;
      color: var(--accent-primary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
    }}

    .nav-links {{
      margin-top: 24px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      flex-grow: 1;
    }}

    .nav-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 16px;
      border-radius: var(--radius-md);
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: all 0.2s ease;
      cursor: pointer;
      border: 1px solid transparent;
    }}

    .nav-item:hover {{
      color: var(--text-main);
      background: var(--card-bg);
      border-color: var(--card-border);
    }}

    .nav-item.active {{
      color: #fff;
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.4);
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.15);
    }}

    .nav-badge {{
      margin-left: auto;
      background: var(--accent-green);
      color: #0b0f19;
      font-size: 0.68rem;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 10px;
    }}

    .social-channels-card {{
      margin-top: auto;
      padding: 14px;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      font-size: 0.75rem;
    }}

    .social-channels-title {{
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 8px;
      text-transform: uppercase;
      display: flex;
      justify-content: space-between;
    }}

    .social-channel-list {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      color: #cbd5e1;
    }}

    /* Main Content */
    .main-wrapper {{
      margin-left: 280px;
      flex-grow: 1;
      padding: 28px 36px;
      max-width: 1440px;
    }}

    /* Top Chapter Bar */
    .chapter-bar {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 14px 20px;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      backdrop-filter: blur(16px);
    }}

    .chapter-select-group {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .chapter-select {{
      background: rgba(11, 15, 25, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #fff;
      font-family: inherit;
      font-size: 0.95rem;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: var(--radius-md);
      cursor: pointer;
      outline: none;
    }}

    .btn-nav {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--card-border);
      color: #fff;
      font-weight: 700;
      font-size: 0.82rem;
      padding: 8px 14px;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-nav:hover {{
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-primary);
    }}

    /* Top Header */
    .top-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 24px;
    }}

    .page-title h2 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.6rem;
      font-weight: 800;
      margin-bottom: 4px;
    }}

    .page-title p {{
      color: var(--text-muted);
      font-size: 0.9rem;
    }}

    .header-actions {{
      display: flex;
      gap: 12px;
    }}

    .btn {{
      padding: 10px 18px;
      border-radius: var(--radius-md);
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      text-decoration: none;
      border: 1px solid transparent;
    }}

    .btn-red-sheet {{
      background: rgba(217, 4, 41, 0.15);
      border-color: rgba(217, 4, 41, 0.4);
      color: #ff4d6d;
    }}

    .btn-red-sheet.active {{
      background: #d90429;
      color: #fff;
      box-shadow: 0 0 20px rgba(217, 4, 41, 0.5);
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--card-border);
      color: var(--text-main);
    }}

    /* Tab Content */
    .tab-content {{ display: none; }}
    .tab-content.active {{ display: block; }}

    /* Video Player Components */
    .grade-bar {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}

    .grade-tab-btn {{
      padding: 8px 14px;
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .grade-tab-btn:hover {{
      color: var(--text-main);
      background: var(--card-hover);
    }}

    .grade-tab-btn.active {{
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-primary);
      color: #fff;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
    }}

    .grade-tab-btn.gold.active {{
      background: rgba(251, 191, 36, 0.2);
      border-color: var(--accent-gold);
      box-shadow: 0 0 12px rgba(251, 191, 36, 0.3);
    }}

    .video-showcase {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 24px;
    }}

    .video-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .video-player-wrapper {{
      position: relative;
      width: 100%;
      background: #000;
      aspect-ratio: 16 / 9;
    }}

    .video-player-wrapper video {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .video-meta-box {{
      padding: 20px;
    }}

    .meta-badges {{
      display: flex;
      gap: 8px;
      margin: 12px 0;
      flex-wrap: wrap;
    }}

    .badge-chip {{
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
    }}

    .badge-chip.active {{
      background: rgba(56, 189, 248, 0.2);
      border-color: rgba(56, 189, 248, 0.4);
      color: var(--accent-primary);
    }}

    .badge-chip.purple {{
      background: rgba(192, 132, 252, 0.15);
      border-color: rgba(192, 132, 252, 0.4);
      color: #c084fc;
    }}

    .clip-prompt-text {{
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      padding: 14px;
      font-size: 0.84rem;
      line-height: 1.6;
      color: #cbd5e1;
      margin-bottom: 12px;
      overflow-y: auto;
    }}

    .btn-copy {{
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--accent-primary);
      font-weight: 700;
      font-size: 0.78rem;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-copy:hover {{
      background: rgba(56, 189, 248, 0.25);
      border-color: var(--accent-primary);
      color: #fff;
    }}

    /* Red Sheet Simulation Styles */
    .red-sheet-container {{
      position: relative;
      background: #ffffff;
      color: #1e293b;
      border-radius: var(--radius-lg);
      padding: 32px;
      font-size: 0.95rem;
      line-height: 1.7;
      overflow: hidden;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
    }}

    .red-sheet-container table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
    }}

    .red-sheet-container th, .red-sheet-container td {{
      padding: 10px 14px;
      border: 1px solid #e2e8f0;
      font-size: 0.88rem;
    }}

    .red-sheet-container th {{
      background-color: #f1f5f9;
      color: #334155;
      font-weight: 700;
    }}

    .red-sheet-container .vocab-red {{
      color: #d90429 !important;
      font-weight: bold;
      transition: opacity 0.3s;
    }}

    .red-sheet-active::after {{
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(217, 4, 41, 0.82);
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 10;
    }}

    .red-sheet-active .vocab-red {{
      opacity: 0 !important;
      background-color: #d90429;
      user-select: none;
    }}

    .red-sheet-active .vocab-red:hover {{
      opacity: 1 !important;
      background-color: transparent;
    }}

    .toast {{
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: #10b981;
      color: #0b0f19;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: var(--radius-md);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toast.show {{ transform: translateY(0); opacity: 1; }}
  </style>
</head>
<body>

  <!-- Sidebar -->
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-icon">
        <i data-lucide="clapperboard"></i>
      </div>
      <div class="brand-text">
        <h1>MDO3出版</h1>
        <span>Automation Suite</span>
      </div>
    </div>

    <nav class="nav-links">
      <div class="nav-item" onclick="switchTab('veo3')">
        <i data-lucide="copy"></i>
        <span>1. プロンプト投入</span>
      </div>
      <div class="nav-item active" onclick="switchTab('player')">
        <i data-lucide="play-circle"></i>
        <span>2. 完成動画を再生</span>
        <span class="nav-badge">全6版対応</span>
      </div>
      <div class="nav-item" onclick="switchTab('vocab')">
        <i data-lucide="sparkles"></i>
        <span>3. 赤シート単語帳</span>
        <span class="nav-badge" style="background:#d90429; color:#fff;">NEW</span>
      </div>
      <div class="nav-item" onclick="switchTab('social')">
        <i data-lucide="share-2"></i>
        <span>4. SNSマルチ発信</span>
        <span class="nav-badge" style="background:var(--accent-rose); color:#fff;">再生特化</span>
      </div>
      <div class="nav-item" onclick="switchTab('kindle')">
        <i data-lucide="book-open"></i>
        <span>5. Kindle同期状態</span>
      </div>
      <div class="nav-item" onclick="switchTab('brand')">
        <i data-lucide="palette"></i>
        <span>6. ブランド画像・プロフ</span>
        <span class="nav-badge" style="background:var(--accent-gold); color:#0b0f19;">READY</span>
      </div>
    </nav>

    <!-- Social Channels Info -->
    <div class="social-channels-card">
      <div class="social-channels-title">
        <span>公式アカウント一覧</span>
        <i data-lucide="check" style="width:14px; color:var(--accent-green);"></i>
      </div>
      <div class="social-channel-list">
        <div>🎬 <b>YouTube:</b> @mdo3_english</div>
        <div>🐦 <b>𝕏:</b> 上善如水出版 (@mdo3_english)</div>
        <div>📸 <b>IG:</b> mdo3_english</div>
        <div>📝 <b>note:</b> mdo3_english</div>
      </div>
    </div>
  </aside>

  <!-- Main Content -->
  <main class="main-wrapper">
    
    <!-- Top Chapter Bar -->
    <div class="chapter-bar">
      <div class="chapter-select-group">
        <span style="font-size:0.85rem; font-weight:700; color:var(--text-muted); text-transform:uppercase;">📖 対象寓話 (全60話):</span>
        <select id="storySelect" class="chapter-select" onchange="onChapterChange(this.value)">
          <!-- Options dynamically injected -->
        </select>
      </div>
      <div style="display:flex; gap:8px;">
        <button class="btn-nav" onclick="navigateChapter(-1)"><i data-lucide="chevron-left"></i> 前の話</button>
        <button class="btn-nav" onclick="navigateChapter(1)">次の話へ進む <i data-lucide="chevron-right"></i></button>
      </div>
    </div>

    <!-- Top Header -->
    <header class="top-header">
      <div class="page-title">
        <h2 id="pageTitleText">完成動画プレイヤー & 聴き比べ</h2>
        <p id="pageSubtitleText">共通のVeo 3映像（3カット）をベースに、4級〜準1級＋クラシック原文まで全6バリエーション完成！</p>
      </div>
      <div class="header-actions">
        <button class="btn btn-red-sheet" id="redSheetToggleBtn" onclick="toggleRedSheet()">
          <i data-lucide="eye-off"></i> 🔴 赤シートをかぶせる (OFF)
        </button>
        <button class="btn btn-secondary" onclick="reloadVideo()">
          <i data-lucide="refresh-cw"></i> 再読み込み
        </button>
      </div>
    </header>

    <!-- Tab 1: Veo 3 Prompts -->
    <section id="tab-veo3" class="tab-content">
      <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:24px; margin-bottom:24px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
          <div>
            <h3 style="font-size:1.15rem; font-weight:700;" id="veo3StoryTitleHeader">🎬 第1話: ウサギとカメ (The Tortoise and the Hare)</h3>
            <span style="font-size:0.82rem; color:var(--text-muted);">Geminiに参照画像を添付し、以下の起・承・結プロンプトを順に送信してください（1日3クリップ）</span>
          </div>
          <a href="https://gemini.google.com" target="_blank" class="btn btn-secondary" style="padding:8px 16px; font-size:0.82rem;">
            <i data-lucide="external-link"></i> Geminiを開く
          </a>
        </div>

        <!-- Gemini Reference Image Quick Guide Box -->
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-bottom:18px;">
          <div style="background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.3); border-radius:var(--radius-md); padding:12px 16px; display:flex; justify-content:space-between; align-items:center;">
            <div style="font-size:0.82rem; overflow:hidden;">
              <div style="color:var(--accent-primary); font-weight:700; margin-bottom:2px;"><i data-lucide="image"></i> ① Gemini添付用 参照画像:</div> 
              <code id="veo3_img_target_name" style="color:#fff; font-weight:700; font-family:'JetBrains Mono', monospace; font-size:0.75rem; word-break:break-all;">gemini_upload_images/00_全60話_番号順_Veo3投入用/第01話_ウサギとカメ.png</code>
            </div>
            <button class="btn-copy" style="padding:4px 10px; font-size:0.72rem; margin-left:8px; white-space:nowrap;" onclick="copyPrompt('veo3_img_target_name', this)">
              <i data-lucide="copy"></i> コピー
            </button>
          </div>

          <div style="background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.3); border-radius:var(--radius-md); padding:12px 16px; display:flex; justify-content:space-between; align-items:center;">
            <div style="font-size:0.82rem; overflow:hidden;">
              <div style="color:var(--accent-green); font-weight:700; margin-bottom:2px;"><i data-lucide="download"></i> ② 生成動画（mp4）の保存先フォルダ:</div> 
              <code id="veo3_inbox_path_text" style="color:#fff; font-weight:700; font-family:'JetBrains Mono', monospace; font-size:0.75rem; word-break:break-all;">veo3_inbox/</code>
            </div>
            <button class="btn-copy" style="padding:4px 10px; font-size:0.72rem; margin-left:8px; white-space:nowrap;" onclick="copyPrompt('veo3_inbox_path_text', this)">
              <i data-lucide="copy"></i> コピー
            </button>
          </div>
        </div>

        <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:16px;" id="veo3ClipsGrid">
          <!-- Dynamically populated -->
        </div>

        <!-- Chat Automation Guidance Banner -->
        <div style="margin-top:20px; background:linear-gradient(135deg, rgba(56,189,248,0.15) 0%, rgba(192,132,252,0.15) 100%); border:1px solid rgba(56,189,248,0.4); border-radius:var(--radius-md); padding:18px 22px; display:flex; align-items:center; justify-content:space-between; gap:20px;">
          <div>
            <div style="font-weight:800; font-size:0.95rem; color:#38bdf8; margin-bottom:6px; display:flex; align-items:center; gap:8px;">
              <i data-lucide="message-square"></i> チャットで指示するだけ（推奨・一番手軽）
            </div>
            <div style="font-size:0.85rem; color:#f8fafc; line-height:1.6;">
              動画（3本）をブラウザから <code>veo3_inbox/</code> フォルダに保存したら、<b>Google Antigravity IDEのチャットで：</b><br>
              <span style="display:inline-block; background:rgba(0,0,0,0.5); padding:4px 10px; border-radius:4px; margin-top:4px; border:1px solid rgba(251,191,36,0.4); color:var(--accent-gold); font-weight:700;">
                「第2話の動画を入れたので作って」 / 「第3話をビルドして」
              </span>
              <span style="color:var(--text-muted); font-size:0.8rem; margin-left:8px;">と伝えるだけで、全6級動画＋縦型ショート3本が完全自動生成されます。</span>
            </div>
          </div>
          <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1); border-radius:var(--radius-sm); padding:10px 14px; font-size:0.75rem; color:var(--text-muted); text-align:right; white-space:nowrap;">
            <div style="color:var(--accent-green); font-weight:700; margin-bottom:2px;">📁 保存先フォルダ:</div>
            <code style="color:#fff; font-family:'JetBrains Mono', monospace; font-weight:700;">veo3_inbox/</code>
          </div>
        </div>
      </div>
    </section>

    <!-- Tab 2: Video Player -->
    <section id="tab-player" class="tab-content active">
      <div class="grade-bar">
        <div class="grade-bar-label"><i data-lucide="layers"></i> バリエーション切替:</div>
        <button class="grade-tab-btn active" onclick="switchGradeVideo('Grade_4', '英検4級', '1分09秒', '135語 (基礎構文・ゆったり朗読)', this)">🥉 英検4級 版</button>
        <button class="grade-tab-btn" onclick="switchGradeVideo('Grade_3', '英検3級', '1分19秒', '195語 (関係代名詞・接続詞)', this)">🥈 英検3級 版</button>
        <button class="grade-tab-btn" onclick="switchGradeVideo('Grade_Pre2', '英検準2級', '1分34秒', '275語 (分詞構文・フォーマル表現)', this)">🥇 英検準2級 版</button>
        <button class="grade-tab-btn" onclick="switchGradeVideo('Grade_2', '英検2級', '1分53秒', '360語 (論理展開・アカデミック語彙)', this)">🏆 英検2級 版</button>
        <button class="grade-tab-btn" onclick="switchGradeVideo('Grade_Pre1', '英検準1級', '1分43秒', '460語 (高度な修辞・高度語彙・ナチュラルスピード)', this)">👑 英検準1級 版</button>
        <button class="grade-tab-btn gold" onclick="switchGradeVideo('Classic_Original', 'クラシック原文', '43秒', 'Townsend版 古典原文 (格調高いイギリス英語ナレーション)', this)">🏛️ クラシック原文 (Townsend版)</button>
      </div>

      <div class="video-showcase">
        <div class="video-card">
          <div class="video-player-wrapper">
            <video id="mainVideoPlayer" controls autoplay muted poster="video_output/preview_v2.jpg">
              <source id="videoSource" src="video_output/chapter01_tortoise_and_hare/chapter01_Grade_4.mp4" type="video/mp4">
              お使いのブラウザは動画タグに対応していません。
            </video>
          </div>
          <div class="video-meta-box">
            <h3 id="currentGradeTitle">🎬 Chapter 01: The Tortoise and the Hare 【英検4級 版】</h3>
            <div class="meta-badges">
              <span class="badge-chip active" id="currentGradeBadge">英検4級 レベル</span>
              <span class="badge-chip purple">🌟 共通Veo 3映像 (3カット結合済)</span>
              <span class="badge-chip" id="currentDurationBadge">尺: 1分09秒</span>
              <span class="badge-chip">1920x1080 Full HD</span>
            </div>
            <p id="currentGradeDesc" style="color:var(--text-muted); font-size:0.88rem; line-height:1.6;">
              <b>【レベル特徴】</b> 135語 (基礎構文・ゆったり朗読)<br>
              ・<b>0:00〜0:24</b>: 挑発とレースのスタート（Veo Clip 1）<br>
              ・<b>0:24〜0:48</b>: 昼寝と着実な前進（Veo Clip 2）<br>
              ・<b>0:48〜1:09</b>: 飛び起きる焦りとゴール（Veo Clip 3）
            </p>
          </div>
        </div>

        <!-- Right Side: Workflow & Shortcuts -->
        <div style="display:flex; flex-direction:column; gap:16px;">
          <!-- Shorts Promotion Card (3 Variants) -->
          <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:20px;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
              <i data-lucide="smartphone" style="color:var(--accent-rose);"></i>
              <h4 style="font-size:0.95rem; font-weight:700;">縦型ショート (9:16) 全3本完成済</h4>
            </div>
            <p style="font-size:0.78rem; color:var(--text-muted); line-height:1.5; margin-bottom:12px;">
              訴求ターゲットに合わせて3本の縦型ショート動画から選んで投稿できます。
            </p>
            <div style="display:flex; flex-direction:column; gap:6px;">
              <a id="player_shorts_link_g4" href="video_output/shorts_reels/chapter01_shorts_Grade4_9x16.mp4" target="_blank" class="btn" style="background:rgba(244,63,94,0.15); border-color:rgba(244,63,94,0.4); color:#ff4d6d; font-size:0.78rem; justify-content:space-between;">
                <span>📖 4級 基礎ショート (9:16)</span> <i data-lucide="play"></i>
              </a>
              <a id="player_shorts_link_g3" href="video_output/shorts_reels/chapter01_shorts_Grade3_9x16.mp4" target="_blank" class="btn" style="background:rgba(56,189,248,0.15); border-color:rgba(56,189,248,0.4); color:#38bdf8; font-size:0.78rem; justify-content:space-between;">
                <span>🎯 3級 ステップアップ (9:16)</span> <i data-lucide="play"></i>
              </a>
              <a id="player_shorts_link_classic" href="video_output/shorts_reels/chapter01_shorts_Classic_9x16.mp4" target="_blank" class="btn" style="background:rgba(251,191,36,0.15); border-color:rgba(251,191,36,0.4); color:#fbbf24; font-size:0.78rem; justify-content:space-between;">
                <span>🏛️ クラシック原文 教訓 (9:16)</span> <i data-lucide="play"></i>
              </a>
            </div>
          </div>

          <!-- YouTube & Sync Status -->
          <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:20px; flex-grow:1;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
              <i data-lucide="youtube" style="color:#f43f5e;"></i>
              <h4 style="font-size:0.95rem; font-weight:700;">YouTube ＆ Kindle 同期台帳</h4>
            </div>
            <div style="font-size:0.8rem; color:var(--text-muted); line-height:1.6;">
              <div><b>公開YouTube URL:</b> <a id="sync_yt_url_link" href="https://youtu.be/oCB_BcSUVbw" target="_blank" style="color:var(--accent-primary); font-weight:700;">https://youtu.be/oCB_BcSUVbw</a></div>
              <div><b>Kindle連動:</b> 全120個の原稿に動画リンク挿入済</div>
              <div><b>note / 𝕏 連動:</b> 実URL埋め込み完了</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tab 3: Vocab Builder & Red Sheet -->
    <section id="tab-vocab" class="tab-content">
      <div class="red-sheet-container" id="vocabContainer">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; border-bottom:2px solid #e2e8f0; padding-bottom:14px;">
          <div>
            <h3 style="font-size:1.3rem; font-weight:800; color:#0f172a;" id="vocabStoryTitle">Chapter 01: The Tortoise and the Hare</h3>
            <span style="font-size:0.85rem; color:#64748b;">赤シート対応 重要単語・熟語チェック表（Kindle原稿・note共有）</span>
          </div>
          <div style="font-size:0.85rem; font-weight:700; color:#d90429; display:flex; align-items:center; gap:6px;">
            <i data-lucide="shield-alert"></i> 赤字 (#d90429) は物理赤シートで消えます
          </div>
        </div>

        <div id="vocabTableBody">
          <!-- Dynamically populated -->
        </div>
      </div>
    </section>

    <!-- Tab 4: Social Hub -->
    <section id="tab-social" class="tab-content">
      <!-- Sub-tabs bar: YouTube FIRST workflow -->
      <div style="display:flex; gap:12px; margin-bottom:20px; border-bottom:1px solid var(--card-border); padding-bottom:12px;">
        <button class="grade-tab-btn active" id="btn-sub-yt" onclick="switchSocialSubTab('youtube')" style="font-size:0.88rem; display:flex; align-items:center; gap:8px;">
          <i data-lucide="youtube" style="color:#f43f5e;"></i> ① 🎬 YouTube (動画UP ＆ URL取得)
        </button>
        <button class="grade-tab-btn" id="btn-sub-note" onclick="switchSocialSubTab('note')" style="font-size:0.88rem; display:flex; align-items:center; gap:8px;">
          <i data-lucide="file-text" style="color:#10b981;"></i> ② 📝 note (完全版ブログ / 動画埋込)
        </button>
        <button class="grade-tab-btn" id="btn-sub-x" onclick="switchSocialSubTab('x')" style="font-size:0.88rem; display:flex; align-items:center; gap:8px;">
          <i data-lucide="twitter" style="color:#38bdf8;"></i> ③ 🐦 𝕏 (スレッド投稿 / 動画埋込)
        </button>
        <button class="grade-tab-btn" id="btn-sub-ig" onclick="switchSocialSubTab('instagram')" style="font-size:0.88rem; display:flex; align-items:center; gap:8px;">
          <i data-lucide="instagram" style="color:#c084fc;"></i> ④ 📸 Instagram (リール・キャプション)
        </button>
      </div>

      <!-- 1. YouTube Content Area (Step 1) -->
      <div id="social-content-youtube" class="social-sub-content">
        <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:24px;">
          
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
            <div>
              <h3 style="font-size:1.1rem; font-weight:700; color:#f43f5e; display:flex; align-items:center; gap:8px;">
                <i data-lucide="youtube"></i> ① YouTube 動画メタデータ ＆ URL登録ハブ
              </h3>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:2px;">
                まずYouTubeに動画をアップロードし、発行されたURLを登録すると、note・𝕏などの投稿文に自動反映されます。
              </p>
            </div>
            <a href="https://studio.youtube.com" target="_blank" class="btn" style="background:#f43f5e; color:#fff; font-weight:800; padding:8px 16px; font-size:0.82rem;">
              <i data-lucide="external-link"></i> YouTube Studio を開く
            </a>
          </div>

          <!-- YouTube Live URL Paste & Sync Box (Grade Specific Slots) -->
          <div style="background:linear-gradient(135deg, rgba(244,63,94,0.15) 0%, rgba(56,189,248,0.15) 100%); border:1px solid rgba(244,63,94,0.4); border-radius:var(--radius-md); padding:18px; margin-bottom:24px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <div style="font-weight:800; font-size:0.92rem; color:#fff; display:flex; align-items:center; gap:8px;">
                <i data-lucide="link" style="color:var(--accent-rose);"></i> <span id="yt_slot_active_title">【英検4級 版】アップロードした YouTube 動画のURLを登録</span>
              </div>
              <span class="badge-chip active" id="yt_slot_active_badge" style="font-size:0.75rem;">現在選択中: 4級</span>
            </div>
            <p style="font-size:0.78rem; color:var(--text-muted); margin-bottom:12px;">
              下記の「級別メタデータ切替」で選択している級のURLを登録します。登録したURLは他SNS（note・𝕏）に自動連携されます。
            </p>
            <div style="display:flex; gap:10px; align-items:center; margin-bottom:14px;">
              <input type="text" id="yt_live_url_input" placeholder="https://youtu.be/... (英検4級のURL)" style="flex-grow:1; background:rgba(11,15,25,0.85); border:1px solid var(--accent-primary); border-radius:var(--radius-sm); color:#fff; padding:10px 14px; font-size:0.9rem; font-family:'JetBrains Mono', monospace; outline:none;">
              <button onclick="applyAndSaveYoutubeUrl()" class="btn" style="background:var(--accent-primary); color:#0b0f19; font-weight:800; font-size:0.85rem; padding:10px 18px; white-space:nowrap;">
                <i data-lucide="check"></i> この級のURLを保存
              </button>
              <button onclick="switchSocialSubTab('note')" class="btn btn-secondary" style="font-size:0.85rem; padding:10px 16px; white-space:nowrap;">
                ② note投稿へ進む <i data-lucide="arrow-right"></i>
              </button>
            </div>

            <!-- Grade Slots Overview Table -->
            <div style="background:rgba(0,0,0,0.35); border:1px solid var(--card-border); border-radius:var(--radius-sm); padding:12px;">
              <div style="font-size:0.75rem; font-weight:700; color:var(--accent-gold); margin-bottom:8px; display:flex; align-items:center; gap:6px;">
                <i data-lucide="list"></i> 本話の各級 YouTube 公開URL 登録スロット一覧（全7枠）
              </div>
              <div id="yt_all_grade_slots_grid" style="display:grid; grid-template-columns: repeat(2, 1fr); gap:8px; font-size:0.78rem;">
                <!-- Dynamically rendered slots for 4級, 3級, 準2, 2, 準1, 原文, Shorts -->
              </div>
            </div>
          </div>

          <!-- YouTube Grade Selector Bar -->
          <div style="display:flex; gap:8px; margin-bottom:18px; flex-wrap:wrap;">
            <button class="grade-tab-btn active" id="yt-btn-Grade_4" onclick="switchYtGrade('Grade_4', '英検4級', '基礎多読')">🥉 4級 メタデータ</button>
            <button class="grade-tab-btn" id="yt-btn-Grade_3" onclick="switchYtGrade('Grade_3', '英検3級', '中学英語')">🥈 3級 メタデータ</button>
            <button class="grade-tab-btn" id="yt-btn-Grade_Pre2" onclick="switchYtGrade('Grade_Pre2', '英検準2級', '高校初級')">🥇 準2級 メタデータ</button>
            <button class="grade-tab-btn" id="yt-btn-Grade_2" onclick="switchYtGrade('Grade_2', '英検2級', '大人の教養')">🏆 2級 メタデータ</button>
            <button class="grade-tab-btn" id="yt-btn-Grade_Pre1" onclick="switchYtGrade('Grade_Pre1', '英検準1級', '上級多読')">👑 準1級 メタデータ</button>
            <button class="grade-tab-btn gold" id="yt-btn-Classic_Original" onclick="switchYtGrade('Classic_Original', 'クラシック原文', 'イギリス英語古典')">🏛️ クラシック原文</button>
            <button class="grade-tab-btn" id="yt-btn-Shorts" onclick="switchYtGrade('Shorts', 'Shorts縦型', '1分ショート')" style="background:rgba(244,63,94,0.15); border-color:rgba(244,63,94,0.4); color:#ff4d6d;">📱 Shorts用</button>
          </div>

          <!-- YT Title -->
          <div style="margin-bottom:18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">① 動画タイトル (Video Title / クリック率特化)</label>
              <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('yt_field_title', this)"><i data-lucide="copy"></i> タイトルをコピー</button>
            </div>
            <div class="clip-prompt-text" id="yt_field_title" style="height:auto; min-height:42px; font-weight:700; font-size:0.95rem; color:#fff;"></div>
          </div>

          <!-- YT Description -->
          <div style="margin-bottom:18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">② 説明文・概要欄 (Description / タイムスタンプ・英文スクリプト完備)</label>
              <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('yt_field_desc', this)"><i data-lucide="copy"></i> 説明文を全コピー</button>
            </div>
            <div class="clip-prompt-text" id="yt_field_desc" style="height:250px; font-family:'JetBrains Mono', monospace; font-size:0.82rem; white-space:pre-wrap; line-height:1.6;"></div>
          </div>

          <!-- YT Tags & Pinned -->
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-bottom:18px;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">③ カンマ区切りタグ (Tags)</label>
                <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('yt_field_tags', this)"><i data-lucide="copy"></i> タグをコピー</button>
              </div>
              <div class="clip-prompt-text" id="yt_field_tags" style="height:70px; font-size:0.8rem; color:#f43f5e;"></div>
            </div>
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">④ 固定コメント用 (Pinned Comment)</label>
                <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('yt_field_pinned', this)"><i data-lucide="copy"></i> コメントをコピー</button>
              </div>
              <div class="clip-prompt-text" id="yt_field_pinned" style="height:70px; font-size:0.8rem;"></div>
            </div>
          </div>

          <!-- Video File Storage Location & Upload Guide -->
          <div style="background:rgba(0,0,0,0.35); border:1px solid rgba(244,63,94,0.3); border-radius:var(--radius-md); padding:16px;">
            <div style="font-weight:800; font-size:0.9rem; color:#f43f5e; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
              <i data-lucide="hard-drive"></i> ⑤ 完成動画ファイル（.mp4）の保存先とアップロード手順
            </div>
            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.6;">
              <div><b>PCローカル/Dropbox保存先:</b> <code id="yt_video_folder_path">video_output/chapter01_tortoise_and_hare/</code></div>
              <div style="margin-top:4px;"><b>アップロード方法:</b> <a href="https://studio.youtube.com" target="_blank" style="color:var(--accent-primary); font-weight:700;">YouTube Studio</a> を開き、右上の「作成」➔「動画をアップロード」をクリックして、上記フォルダ内の <code>.mp4</code> をドラッグ＆ドロップしてください。</div>
            </div>
            
            <div style="display:flex; gap:10px; margin-top:12px; flex-wrap:wrap;" id="yt_download_links_bar">
              <!-- Dynamically populated with Grade 4, 3, etc download links -->
            </div>
          </div>
        </div>
      </div>

      <!-- 2. note Content Area (Step 2) -->
      <div id="social-content-note" class="social-sub-content" style="display:none;">
        <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:24px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
            <div>
              <h3 style="font-size:1.1rem; font-weight:700; color:#10b981; display:flex; align-items:center; gap:8px;">
                <i data-lucide="file-text"></i> ② note 投稿用 完全版記事パッケージ
              </h3>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:2px;">
                登録したYouTube動画リンクが本文中に自動挿入されています。コピーしてそのまま投稿できます。
              </p>
            </div>
            <a href="https://note.com/notes/new" target="_blank" class="btn" style="background:#10b981; color:#0b0f19; font-weight:800; padding:8px 16px; font-size:0.82rem;">
              <i data-lucide="external-link"></i> note 投稿画面を開く
            </a>
          </div>

          <!-- Note Header / Eyecatch Image Area -->
          <div style="background:rgba(0, 0, 0, 0.4); border:1px solid rgba(16, 185, 129, 0.3); border-radius:var(--radius-md); padding:18px; margin-bottom:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <div style="font-weight:800; font-size:0.95rem; color:#10b981; display:flex; align-items:center; gap:8px;">
                <i data-lucide="image"></i> ① note 記事用「見出し画像（アイキャッチ画像・リンク元）」
              </div>
              <span style="font-size:0.75rem; color:var(--text-muted);">noteエディタ最上部「見出し画像を追加」に設定</span>
            </div>
            
            <div style="display:grid; grid-template-columns: 280px 1fr; gap:18px; align-items:center;">
              <!-- Story Image Preview -->
              <div style="background:rgba(22, 30, 49, 0.8); border:1px solid var(--card-border); border-radius:var(--radius-sm); padding:12px; text-align:center;">
                <img id="note_image_preview" src="images/vol1_tortoise_and_hare.png" alt="見出し画像プレビュー" style="width:100%; height:140px; object-fit:cover; border-radius:var(--radius-sm); border:1px solid var(--card-border); margin-bottom:10px;">
                <div style="display:flex; gap:8px; justify-content:center;">
                  <a id="note_image_download_btn" href="images/vol1_tortoise_and_hare.png" download="note_eyecatch_chapter01.png" class="btn btn-secondary" style="font-size:0.75rem; padding:6px 12px; width:100%; justify-content:center;">
                    <i data-lucide="download"></i> 挿絵画像を保存 / ダウンロード
                  </a>
                </div>
              </div>

              <!-- Details & Paths -->
              <div style="display:flex; flex-direction:column; gap:10px;">
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="font-size:0.75rem; color:var(--accent-gold); font-weight:700;">📁 挿絵画像のリンク元ファイルパス:</span>
                    <button class="btn-copy" style="padding:2px 8px; font-size:0.7rem;" onclick="copyPrompt('note_img_path_text', this)"><i data-lucide="copy"></i> パスをコピー</button>
                  </div>
                  <div class="clip-prompt-text" id="note_img_path_text" style="height:auto; font-size:0.8rem; padding:8px; font-family:'JetBrains Mono', monospace; color:#38bdf8;">images/vol1_tortoise_and_hare.png</div>
                </div>

                <div style="background:rgba(0,0,0,0.25); border:1px solid var(--card-border); border-radius:var(--radius-sm); padding:10px; font-size:0.78rem; color:var(--text-muted); line-height:1.5;">
                  <b style="color:#fff;">💡 見出し画像の設定手順:</b><br>
                  1. 上記の <b>「挿絵画像を保存」</b> をクリックしてPCに保存（または表示パスの元ファイルを使用）<br>
                  2. note投稿画面の最上部にある <b>「見出し画像を追加」</b> アイコンをクリック<br>
                  3. <b>「画像をアップロード」</b> を選択し、本画像を適用してください。<br>
                  <span style="color:var(--text-muted); font-size:0.72rem;">※ 連載の共通バナーを使いたい場合は <code>sns_brand_assets/channel_banner.jpg</code> も利用できます。</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Note Title -->
          <div style="margin-bottom:18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">② 記事タイトル (Title / 公式30文字制限・SEO & クリック率特化)</label>
              <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('note_field_title', this)"><i data-lucide="copy"></i> タイトルをコピー</button>
            </div>
            <div class="clip-prompt-text" id="note_field_title" style="height:auto; min-height:42px; font-weight:700; font-size:0.95rem; color:#fff;"></div>
          </div>

          <!-- Note Body -->
          <div style="margin-bottom:18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">③ 記事本文 (Markdown / 英文・全訳・単語表・動画リンク完備)</label>
              <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('note_field_body', this)"><i data-lucide="copy"></i> 本文Markdownを全コピー</button>
            </div>
            <div class="clip-prompt-text" id="note_field_body" style="height:320px; font-family:'JetBrains Mono', monospace; font-size:0.82rem; white-space:pre-wrap; line-height:1.6;"></div>
          </div>

          <!-- Note Tags -->
          <div style="margin-bottom:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">④ ハッシュタグ (Tags / 公開設定の「ハッシュタグを追加」欄にペースト)</label>
              <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('note_field_tags', this)"><i data-lucide="copy"></i> タグをコピー</button>
            </div>
            <div class="clip-prompt-text" id="note_field_tags" style="height:auto; font-size:0.82rem; color:#10b981;"></div>
          </div>

          <!-- Note Magazine & Publish Settings Guide (Screenshot Integration) -->
          <div style="background:rgba(0, 0, 0, 0.4); border:1px solid rgba(16, 185, 129, 0.3); border-radius:var(--radius-md); padding:18px;">
            <div style="font-weight:800; font-size:0.95rem; color:#10b981; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
              <i data-lucide="settings-2"></i> ⑤ note「公開設定」画面の推奨チェックリスト ＆ 連載マガジン設定
            </div>

            <!-- Magazine Recommendation -->
            <div style="background:rgba(22, 30, 49, 0.8); border:1px solid var(--card-border); border-radius:var(--radius-sm); padding:14px; margin-bottom:14px;">
              <div style="font-weight:700; font-size:0.85rem; color:var(--accent-gold); margin-bottom:6px; display:flex; align-items:center; gap:6px;">
                <i data-lucide="folder-plus"></i> 【最重要】「連載マガジン」を作成して記事を追加しよう！
              </div>
              <p style="font-size:0.78rem; color:var(--text-muted); line-height:1.5; margin-bottom:10px;">
                マガジンに記事を追加すると、読者が全60話を本のようにまとめて読み進められ、マガジンごとフォロー（購読）してくれます。
              </p>
              <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="font-size:0.75rem; color:var(--text-muted); font-weight:700;">マガジン名:</span>
                    <button class="btn-copy" style="padding:2px 6px; font-size:0.7rem;" onclick="copyPrompt('mag_title_copy', this)"><i data-lucide="copy"></i> コピー</button>
                  </div>
                  <div class="clip-prompt-text" id="mag_title_copy" style="height:auto; font-size:0.78rem; margin:0; padding:8px;">【小中高〜大人】イソップ寓話で学ぶ英検＆英語多読</div>
                </div>
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="font-size:0.75rem; color:var(--text-muted); font-weight:700;">マガジンの説明:</span>
                    <button class="btn-copy" style="padding:2px 6px; font-size:0.7rem;" onclick="copyPrompt('mag_desc_copy', this)"><i data-lucide="copy"></i> コピー</button>
                  </div>
                  <div class="clip-prompt-text" id="mag_desc_copy" style="height:auto; font-size:0.78rem; margin:0; padding:8px;">小中高校生の英検・受験対策から大人の学び直しまで！ネイティブ朗読・光るカラオケ字幕動画・赤シート単語帳と連動した英語多読レッスン全60話をお届けします。</div>
                </div>
              </div>
              <div style="margin-top:8px; font-size:0.75rem; color:var(--text-muted);">
                ※ マガジンのカバー画像には <code>sns_brand_assets/channel_banner.jpg</code> を設定してください。
              </div>
            </div>

            <!-- Settings Field Checklist -->
            <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap:10px; font-size:0.8rem; color:#cbd5e1;">
              <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:var(--radius-sm); border:1px solid var(--card-border);">
                <div>🟢 <b>記事タイプ:</b> <code>無料</code> にチェック</div>
                <div style="font-size:0.72rem; color:var(--text-muted); margin-top:2px;">※ 多くの読者に届けるため無料公開にします。</div>
              </div>
              <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:var(--radius-sm); border:1px solid var(--card-border);">
                <div>🟢 <b>記事の追加（マガジン）:</b> <code>作成したマガジン</code> を追加</div>
                <div style="font-size:0.72rem; color:var(--text-muted); margin-top:2px;">※ 公開設定画面でマガジンの横の「追加」を押します。</div>
              </div>
              <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:var(--radius-sm); border:1px solid var(--card-border);">
                <div>🟢 <b>記事の自動翻訳:</b> <code>ON (有効)</code></div>
                <div style="font-size:0.72rem; color:var(--text-muted); margin-top:2px;">※ 海外の英語学習読者にも記事が届きます。</div>
              </div>
              <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:var(--radius-sm); border:1px solid var(--card-border);">
                <div>🟢 <b>クリエイターページに表示:</b> <code>ON (有効)</code></div>
                <div style="font-size:0.72rem; color:var(--text-muted); margin-top:2px;">※ あなたのnoteトップページに新着記事として並びます。</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. X (Twitter) Content Area -->
      <div id="social-content-x" class="social-sub-content" style="display:none;">
        <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:24px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
            <div>
              <h3 style="font-size:1.1rem; font-weight:700; color:#38bdf8; display:flex; align-items:center; gap:8px;">
                <i data-lucide="twitter"></i> 𝕏 (Twitter) スレッド投稿パッケージ (3パターン切替対応)
              </h3>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:2px;">
                用途に合わせて「王道・教育」「文法・対比」「教訓・大人」の3パターンから選択して投稿できます。
              </p>
            </div>
            <a id="xDirectTweetBtn" href="https://twitter.com/intent/tweet" target="_blank" class="btn" style="background:#1d9bf0; color:#fff; font-weight:800; padding:8px 16px; font-size:0.82rem;">
              <i data-lucide="send"></i> 1通目を𝕏でポスト
            </a>
          </div>

          <!-- X Pattern Selector Tabs -->
          <div style="display:flex; gap:10px; margin-bottom:18px;">
            <button class="grade-tab-btn active" id="x-pattern-btn-a" onclick="switchXPattern('a')" style="font-size:0.82rem; padding:8px 16px;">
              🅰️ パターンA (王道・教育ストーリー)
            </button>
            <button class="grade-tab-btn" id="x-pattern-btn-b" onclick="switchXPattern('b')" style="font-size:0.82rem; padding:8px 16px;">
              🅱️ パターンB (英文法・フレーズ対比)
            </button>
            <button class="grade-tab-btn" id="x-pattern-btn-c" onclick="switchXPattern('c')" style="font-size:0.82rem; padding:8px 16px;">
              🅲 パターンC (教訓・大人の学び直し)
            </button>
          </div>

          <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:16px;">
            <!-- Tweet 1 -->
            <div style="background:rgba(11,15,25,0.6); border:1px solid var(--card-border); border-radius:var(--radius-md); padding:16px; display:flex; flex-direction:column;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-weight:700; color:#38bdf8; font-size:0.82rem;">① 親ツイート (動画添付)</span>
                <button class="btn-copy" style="padding:2px 8px; font-size:0.72rem;" onclick="copyPrompt('x_field_t1', this)"><i data-lucide="copy"></i> コピー</button>
              </div>
              <div class="clip-prompt-text" id="x_field_t1" style="height:180px; font-size:0.82rem; line-height:1.5;"></div>
            </div>

            <!-- Tweet 2 -->
            <div style="background:rgba(11,15,25,0.6); border:1px solid var(--card-border); border-radius:var(--radius-md); padding:16px; display:flex; flex-direction:column;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-weight:700; color:#38bdf8; font-size:0.82rem;">② ツリー2 (表現対比・解説)</span>
                <button class="btn-copy" style="padding:2px 8px; font-size:0.72rem;" onclick="copyPrompt('x_field_t2', this)"><i data-lucide="copy"></i> コピー</button>
              </div>
              <div class="clip-prompt-text" id="x_field_t2" style="height:180px; font-size:0.82rem; line-height:1.5;"></div>
            </div>

            <!-- Tweet 3 -->
            <div style="background:rgba(11,15,25,0.6); border:1px solid var(--card-border); border-radius:var(--radius-md); padding:16px; display:flex; flex-direction:column;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-weight:700; color:#38bdf8; font-size:0.82rem;">③ ツリー3 (動画＆Kindleリンク)</span>
                <button class="btn-copy" style="padding:2px 8px; font-size:0.72rem;" onclick="copyPrompt('x_field_t3', this)"><i data-lucide="copy"></i> コピー</button>
              </div>
              <div class="clip-prompt-text" id="x_field_t3" style="height:180px; font-size:0.82rem; line-height:1.5;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. Instagram Content Area -->
      <div id="social-content-instagram" class="social-sub-content" style="display:none;">
        <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:24px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
            <div>
              <h3 style="font-size:1.1rem; font-weight:700; color:#c084fc; display:flex; align-items:center; gap:8px;">
                <i data-lucide="instagram"></i> Instagram リール＆フィード キャプション
              </h3>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:2px;">
                縦型ショート動画（9:16）投稿時のキャプションおよびハッシュタグ30選です。
              </p>
            </div>
            <a href="https://www.instagram.com/" target="_blank" class="btn" style="background:#c084fc; color:#0b0f19; font-weight:800; padding:8px 16px; font-size:0.82rem;">
              <i data-lucide="external-link"></i> Instagram を開く
            </a>
          </div>

          <!-- IG Caption -->
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <label style="font-weight:700; font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">キャプション本文 ＆ ハッシュタグ (Caption & Tags)</label>
              <button class="btn-copy" style="padding:4px 10px; font-size:0.75rem;" onclick="copyPrompt('ig_field_caption', this)"><i data-lucide="copy"></i> キャプションをコピー</button>
            </div>
            <div class="clip-prompt-text" id="ig_field_caption" style="height:220px; font-family:'JetBrains Mono', monospace; font-size:0.82rem; white-space:pre-wrap; line-height:1.6;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tab 5: Kindle Monitor -->
    <section id="tab-kindle" class="tab-content">
      <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:24px;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <span style="background:var(--accent-gradient); color:#0b0f19; font-weight:800; font-size:0.75rem; padding:4px 8px; border-radius:4px;">KINDLE EPUB SYNC</span>
          <div>
            <h3 style="font-size:1.1rem; font-weight:700;">Kindle 原稿内 動画リンク挿入状態</h3>
            <span style="font-size:0.82rem; color:var(--text-muted);">電子書籍内に自動反映されているリンクボタンのプレビュー</span>
          </div>
        </div>

        <div style="background: rgba(0,0,0,0.4); padding: 20px; border-radius: var(--radius-md); border: 1px dashed var(--card-border); margin-bottom: 20px;">
          <div style="text-align: center; margin: 10px 0; padding: 14px 16px; background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 8px; max-width: 600px; margin-left: auto; margin-right: auto;">
            <a href="https://youtu.be/mock_tortoise_and_hare_ch01" target="_blank" style="color: #0969da; font-weight: bold; text-decoration: none; font-size: 1.05em; display: inline-block;">
              🎬 【動画で聴く・シャドーイング】ネイティブ朗読＆カラオケ字幕付き動画（YouTube）▶
            </a>
            <div style="font-size: 0.82em; color: #57606a; margin-top: 4px;">
              ※ タップするとYouTubeが開き、発音に合わせて光るカラオケ字幕で学習できます。
            </div>
          </div>
        </div>

        <div style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
          現在、<b>全60話（Vol 1〜Vol 24）の各 Markdown 原稿</b> に動画リンクと赤シート対応単語表が反映されています。
        </div>
      </div>
    </section>

    <!-- Tab 6: Brand Assets & Profiles -->
    <section id="tab-brand" class="tab-content">
      <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:var(--radius-lg); padding:24px; margin-bottom:24px;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
          <div style="display:flex; align-items:center; gap:12px;">
            <span style="background:var(--accent-gold); color:#0b0f19; font-weight:800; font-size:0.75rem; padding:4px 8px; border-radius:4px;">OFFICIAL ASSETS</span>
            <h3 style="font-size:1.15rem; font-weight:700;">ブランド公式アイコン・バナー素材</h3>
          </div>
          <span style="font-size:0.8rem; color:var(--text-muted);">保存先: <code>sns_brand_assets/</code></span>
        </div>
        
        <div style="display:grid; grid-template-columns: 240px 1fr; gap:24px; align-items:center;">
          <!-- Profile Icon Preview -->
          <div style="text-align:center; background:rgba(0,0,0,0.35); padding:18px; border-radius:var(--radius-md); border:1px solid var(--card-border);">
            <img src="sns_brand_assets/profile_icon.jpg" alt="MDO3 Icon" style="width:140px; height:140px; border-radius:50%; border:3px solid var(--accent-gold); box-shadow:0 0 25px rgba(251,191,36,0.3); object-fit:cover; margin-bottom:12px;">
            <div style="font-weight:700; font-size:0.9rem; margin-bottom:4px;">公式アバターアイコン</div>
            <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:12px;">全SNS共通 (1:1 正方形)</div>
            <a href="sns_brand_assets/profile_icon.jpg" download="mdo3_profile_icon.jpg" class="btn btn-secondary" style="width:100%; font-size:0.78rem; justify-content:center; padding:6px;">
              <i data-lucide="download"></i> アイコンを保存
            </a>
          </div>

          <!-- Banner Preview -->
          <div style="background:rgba(0,0,0,0.35); padding:18px; border-radius:var(--radius-md); border:1px solid var(--card-border);">
            <div style="font-weight:700; font-size:0.9rem; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
              <span>公式チャンネルアート・ヘッダーバナー</span>
              <span style="font-size:0.75rem; color:var(--text-muted);">YouTube / 𝕏 / note (16:9)</span>
            </div>
            <img src="sns_brand_assets/channel_banner.jpg" alt="MDO3 Banner" style="width:100%; height:130px; object-fit:cover; border-radius:var(--radius-sm); border:1px solid var(--card-border); margin-bottom:12px;">
            <a href="sns_brand_assets/channel_banner.jpg" download="mdo3_channel_banner.jpg" class="btn btn-secondary" style="font-size:0.78rem; justify-content:center; padding:6px 16px; display:inline-flex;">
              <i data-lucide="download"></i> バナー画像を保存
            </a>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Toast -->
  <div id="toast" class="toast">
    <i data-lucide="check-circle"></i>
    <span id="toastMsg">クリップボードにコピーしました！</span>
  </div>

  <script>
    const ALL_STORIES = {combined_json_str};
    let currentStoryIndex = 0;
    let isRedSheetActive = false;
    let currentSelectedYtGrade = 'Grade_4';
    let currentXPattern = 'a';

    function initPortal() {{
      const select = document.getElementById('storySelect');
      if (select) {{
        select.innerHTML = '';
        ALL_STORIES.forEach((story, idx) => {{
          const opt = document.createElement('option');
          opt.value = idx;
          opt.innerText = `Chapter ${{story.chapter < 10 ? '0' + story.chapter : story.chapter}}: ${{story.titleJa}} (${{story.titleEn}})`;
          select.appendChild(opt);
        }});
      }}

      renderStory(0);
      lucide.createIcons();
    }}

    function onChapterChange(idxStr) {{
      currentStoryIndex = parseInt(idxStr, 10);
      renderStory(currentStoryIndex);
    }}

    function navigateChapter(delta) {{
      let newIdx = currentStoryIndex + delta;
      if (newIdx < 0) newIdx = 0;
      if (newIdx >= ALL_STORIES.length) newIdx = ALL_STORIES.length - 1;
      currentStoryIndex = newIdx;
      const select = document.getElementById('storySelect');
      if (select) select.value = newIdx;
      renderStory(newIdx);
      if (ALL_STORIES[newIdx]) {{
        showToast(`Chapter ${{ALL_STORIES[newIdx].chapter}}: ${{ALL_STORIES[newIdx].titleJa}} に切り替えました`);
      }}
    }}

    function renderStory(idx) {{
      const story = ALL_STORIES[idx];
      if (!story) return;

      const chStr = story.chapter < 10 ? '0' + story.chapter : story.chapter;

      // 1. Veo 3 Tab
      try {{
        const vHeader = document.getElementById('veo3StoryTitleHeader');
        if (vHeader) vHeader.innerText = `🎬 Chapter ${{chStr}}: ${{story.titleJa}} (${{story.titleEn}})`;
        
        const vImgTarget = document.getElementById('veo3_img_target_name');
        if (vImgTarget) {{
          vImgTarget.innerText = `gemini_upload_images/00_全60話_番号順_Veo3投入用/第${{chStr}}話_${{story.titleJa}}.png`;
        }}

        const clipsGrid = document.getElementById('veo3ClipsGrid');
        if (clipsGrid) {{
          clipsGrid.innerHTML = '';
          if (story.clips && story.clips.length > 0) {{
            story.clips.forEach((c, cIdx) => {{
              const div = document.createElement('div');
              div.style = "background:rgba(11,15,25,0.6); border:1px solid var(--card-border); border-radius:var(--radius-md); padding:16px; display:flex; flex-direction:column;";
              div.innerHTML = `
                <div style="font-size:0.75rem; font-weight:700; color:var(--accent-primary); margin-bottom:8px;">Clip ${{c.clipIndex}}: ${{c.sceneName}}</div>
                <div class="clip-prompt-text" id="p_clip_${{cIdx}}" style="height:140px;">${{c.prompt}}</div>
                <button class="btn-copy" onclick="copyPrompt('p_clip_${{cIdx}}', this)"><i data-lucide="copy"></i> プロンプトをコピー</button>
              `;
              clipsGrid.appendChild(div);
            }});
          }} else {{
            clipsGrid.innerHTML = `<div style="grid-column:1/-1; padding:20px; text-align:center; color:var(--text-muted); background:rgba(0,0,0,0.2); border-radius:var(--radius-md);">Chapter ${{chStr}} のVeo 3プロンプトは準備中です。SNS投稿データは下記のタブからご利用いただけます。</div>`;
          }}
        }}
      }} catch (e) {{ console.error("Veo3 render error:", e); }}

      // 2. Video Player Meta & Auto-Reload
      try {{
        const cgTitle = document.getElementById('currentGradeTitle');
        if (cgTitle) cgTitle.innerText = `🎬 Chapter ${{chStr}}: ${{story.titleJa}} (${{story.titleEn}}) 【英検4級 版】`;
        
        const player = document.getElementById('mainVideoPlayer');
        const source = document.getElementById('videoSource');
        const newSrc = `video_output/chapter${{chStr}}_${{story.key}}/chapter${{chStr}}_Grade_4.mp4`;
        if (source) source.src = newSrc;
        if (player) {{
          player.load();
        }}

        // Reset grade buttons in Player tab to Grade 4
        const gradeButtons = document.querySelectorAll('#tab-player .grade-tab-btn');
        gradeButtons.forEach((b, idx) => {{
          if (idx === 0) b.classList.add('active');
          else b.classList.remove('active');
        }});

        // Update player badges
        const gBadge = document.getElementById('currentGradeBadge');
        if (gBadge) gBadge.innerText = '英検4級 レベル';
        const dBadge = document.getElementById('currentDurationBadge');
        if (dBadge) dBadge.innerText = 'フル動画';
        const dDesc = document.getElementById('currentGradeDesc');
        if (dDesc) dDesc.innerHTML = `<b>【レベル特徴】</b> 基礎構文・ゆったり朗読（ネイティブ音声＋カラオケ字幕）`;

        // Update Shorts links on right sidebar
        const sLinkG4 = document.getElementById('player_shorts_link_g4');
        const sLinkG3 = document.getElementById('player_shorts_link_g3');
        const sLinkCl = document.getElementById('player_shorts_link_classic');
        if (sLinkG4) sLinkG4.href = `video_output/shorts_reels/chapter${{chStr}}_shorts_Grade4_9x16.mp4`;
        if (sLinkG3) sLinkG3.href = `video_output/shorts_reels/chapter${{chStr}}_shorts_Grade3_9x16.mp4`;
        if (sLinkCl) sLinkCl.href = `video_output/shorts_reels/chapter${{chStr}}_shorts_Classic_9x16.mp4`;
      }} catch (e) {{ console.error("Player render error:", e); }}

      // 3. Vocab Table
      try {{
        const vTitle = document.getElementById('vocabStoryTitle');
        if (vTitle) vTitle.innerText = `Chapter ${{chStr}}: ${{story.titleJa}} (${{story.titleEn}})`;
        const vocabBox = document.getElementById('vocabTableBody');
        if (vocabBox && story.sns && story.sns.note && story.sns.note.body) {{
          const parts = story.sns.note.body.split('## 🔴 4. 赤シート対応！重要単語・熟語チェック表');
          if (parts.length > 1) {{
            const tablePart = parts[1].split('---')[0].trim();
            vocabBox.innerHTML = renderMarkdownTable(tablePart);
          }} else {{
            vocabBox.innerHTML = '<p style="color:var(--text-muted);">単語表データを抽出中...</p>';
          }}
        }}
      }} catch (e) {{ console.error("Vocab render error:", e); }}

      // 4. SNS Tab
      try {{
        const bestYtUrl = getBestYoutubeUrl(story.chapter);
        const currentGradeUrl = getStoredGradeYoutubeUrl(story.chapter, currentSelectedYtGrade);
        const ytInput = document.getElementById('yt_live_url_input');
        if (ytInput) ytInput.value = currentGradeUrl;
        
        renderYoutubeSlotsGrid(story.chapter);

        if (story.sns && story.sns.youtube) {{
          const ytTitle = document.getElementById('yt_field_title');
          const ytDesc = document.getElementById('yt_field_desc');
          const ytTags = document.getElementById('yt_field_tags');
          const ytPinned = document.getElementById('yt_field_pinned');
          if (ytTitle) ytTitle.innerText = story.sns.youtube.title || '';
          if (ytDesc) ytDesc.innerText = story.sns.youtube.description || '';
          if (ytTags) ytTags.innerText = story.sns.youtube.tags || '';
          if (ytPinned) ytPinned.innerText = story.sns.youtube.pinned_comment || '';

          // Update folder path and download buttons
          const folderRel = `video_output/chapter${{chStr}}_${{story.key}}/`;
          const ytFolder = document.getElementById('yt_video_folder_path');
          if (ytFolder) ytFolder.innerText = folderRel;

          const linksBar = document.getElementById('yt_download_links_bar');
          if (linksBar) {{
            linksBar.innerHTML = `
              <a href="${{folderRel}}chapter${{chStr}}_Grade_4.mp4" download class="btn btn-secondary" style="font-size:0.75rem; padding:6px 10px;">
                <i data-lucide="download"></i> 4級動画 (.mp4)
              </a>
              <a href="${{folderRel}}chapter${{chStr}}_Grade_3.mp4" download class="btn btn-secondary" style="font-size:0.75rem; padding:6px 10px;">
                <i data-lucide="download"></i> 3級動画 (.mp4)
              </a>
              <a href="${{folderRel}}chapter${{chStr}}_Grade_Pre2.mp4" download class="btn btn-secondary" style="font-size:0.75rem; padding:6px 10px;">
                <i data-lucide="download"></i> 準2級動画 (.mp4)
              </a>
              <a href="${{folderRel}}chapter${{chStr}}_Grade_2.mp4" download class="btn btn-secondary" style="font-size:0.75rem; padding:6px 10px;">
                <i data-lucide="download"></i> 2級動画 (.mp4)
              </a>
              <a href="${{folderRel}}chapter${{chStr}}_Grade_Pre1.mp4" download class="btn btn-secondary" style="font-size:0.75rem; padding:6px 10px;">
                <i data-lucide="download"></i> 準1級動画 (.mp4)
              </a>
              <a href="video_output/shorts_reels/chapter${{chStr}}_shorts_Grade4_9x16.mp4" download class="btn" style="font-size:0.75rem; padding:6px 10px; background:rgba(244,63,94,0.15); border-color:rgba(244,63,94,0.4); color:#ff4d6d;">
                <i data-lucide="smartphone"></i> 4級ショート (.mp4)
              </a>
              <a href="video_output/shorts_reels/chapter${{chStr}}_shorts_Grade3_9x16.mp4" download class="btn" style="font-size:0.75rem; padding:6px 10px; background:rgba(56,189,248,0.15); border-color:rgba(56,189,248,0.4); color:#38bdf8;">
                <i data-lucide="smartphone"></i> 3級ショート (.mp4)
              </a>
              <a href="video_output/shorts_reels/chapter${{chStr}}_shorts_Classic_9x16.mp4" download class="btn" style="font-size:0.75rem; padding:6px 10px; background:rgba(251,191,36,0.15); border-color:rgba(251,191,36,0.4); color:#fbbf24;">
                <i data-lucide="smartphone"></i> 原文ショート (.mp4)
              </a>
            `;
          }}

          // Update YouTube sync link
          const actualYtUrl = bestYtUrl || `https://youtu.be/mock_chapter${{chStr}}`;
          const syncYtLink = document.getElementById('sync_yt_url_link');
          if (syncYtLink) {{
            syncYtLink.href = actualYtUrl;
            syncYtLink.innerText = actualYtUrl;
          }}
        }}

        // note with dynamic YouTube URL
        if (story.sns && story.sns.note) {{
          const noteTitle = document.getElementById('note_field_title');
          const noteBodyEl = document.getElementById('note_field_body');
          const noteTags = document.getElementById('note_field_tags');

          if (noteTitle) noteTitle.innerText = story.sns.note.title || '';
          
          let noteBody = story.sns.note.body || '';
          if (bestYtUrl) {{
            noteBody = noteBody.replace(/https:\\/\\/youtu\\.be\\/[^\\s)\\]]+/g, bestYtUrl);
          }}
          if (noteBodyEl) noteBodyEl.innerText = noteBody;
          if (noteTags) noteTags.innerText = story.sns.note.tags || '';

          // Update note eyecatch image preview and download
          const imgPath = story.referenceImage || 'sns_brand_assets/channel_banner.jpg';
          const noteImgPreview = document.getElementById('note_image_preview');
          const noteImgDownloadBtn = document.getElementById('note_image_download_btn');
          const noteImgPathText = document.getElementById('note_img_path_text');

          if (noteImgPreview) noteImgPreview.src = imgPath;
          if (noteImgDownloadBtn) {{
            noteImgDownloadBtn.href = imgPath;
            noteImgDownloadBtn.download = `note_eyecatch_chapter${{chStr}}.png`;
          }}
          if (noteImgPathText) noteImgPathText.innerText = imgPath;
        }}

        // X with 3-Pattern support & dynamic YouTube URL
        if (story.sns && story.sns.x) {{
          const t1El = document.getElementById('x_field_t1');
          const t2El = document.getElementById('x_field_t2');
          const t3El = document.getElementById('x_field_t3');
          const tweetBtn = document.getElementById('xDirectTweetBtn');

          let pObj = null;
          if (story.sns.x.patterns && story.sns.x.patterns[currentXPattern]) {{
            pObj = story.sns.x.patterns[currentXPattern];
          }}

          const rawT1 = pObj ? pObj.tweet1 : (story.sns.x.tweet1 || '');
          const rawT2 = pObj ? pObj.tweet2 : (story.sns.x.tweet2 || '');
          let rawT3 = pObj ? pObj.tweet3 : (story.sns.x.tweet3 || '');

          if (bestYtUrl) {{
            rawT3 = rawT3.replace(/https:\\/\\/youtu\\.be\\/[^\\s)\\]]+/g, bestYtUrl);
          }}

          if (t1El) t1El.innerText = rawT1;
          if (t2El) t2El.innerText = rawT2;
          if (t3El) t3El.innerText = rawT3;
          if (tweetBtn) tweetBtn.href = `https://twitter.com/intent/tweet?text=${{encodeURIComponent(rawT1)}}`;
        }}

        // Instagram
        if (story.sns && story.sns.instagram) {{
          const igEl = document.getElementById('ig_field_caption');
          if (igEl) igEl.innerText = story.sns.instagram.caption || '';
        }}
      }} catch (e) {{ console.error("SNS render error:", e); }}

      try {{
        lucide.createIcons();
      }} catch (e) {{ console.error("Lucide icon error:", e); }}
    }}

    function renderMarkdownTable(mdText) {{
      const lines = mdText.split('\\n').filter(l => l.trim().startsWith('|'));
      if (lines.length < 2) return '<p>単語表の読み込み中...</p>';
      
      let html = '<table>';
      lines.forEach((line, idx) => {{
        if (line.includes('---')) return;
        const cells = line.split('|').slice(1, -1).map(c => c.trim());
        if (idx === 0) {{
          html += '<thead><tr>' + cells.map(c => `<th>${{c}}</th>`).join('') + '</tr></thead><tbody>';
        }} else {{
          html += '<tr>' + cells.map(c => `<td>${{c}}</td>`).join('') + '</tr>';
        }}
      }});
      html += '</tbody></table>';
      return html;
    }}

    function toggleRedSheet() {{
      isRedSheetActive = !isRedSheetActive;
      const container = document.getElementById('vocabContainer');
      const btn = document.getElementById('redSheetToggleBtn');
      
      if (isRedSheetActive) {{
        container.classList.add('red-sheet-active');
        btn.classList.add('active');
        btn.innerHTML = '<i data-lucide="eye"></i> 🔴 赤シートを外す (ON中)';
        showToast('赤シートをかぶせました！赤をホバーすると答えが見えます');
      }} else {{
        container.classList.remove('red-sheet-active');
        btn.classList.remove('active');
        btn.innerHTML = '<i data-lucide="eye-off"></i> 🔴 赤シートをかぶせる (OFF)';
        showToast('赤シートを外しました');
      }}
      lucide.createIcons();
    }}

    function switchTab(tabId) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
      
      const targetTab = document.getElementById('tab-' + tabId);
      if (targetTab) targetTab.classList.add('active');

      const navItems = document.querySelectorAll('.nav-item');
      if (tabId === 'veo3' && navItems[0]) navItems[0].classList.add('active');
      if (tabId === 'player' && navItems[1]) navItems[1].classList.add('active');
      if (tabId === 'vocab' && navItems[2]) navItems[2].classList.add('active');
      if (tabId === 'social' && navItems[3]) navItems[3].classList.add('active');
      if (tabId === 'kindle' && navItems[4]) navItems[4].classList.add('active');
      if (tabId === 'brand' && navItems[5]) navItems[5].classList.add('active');

      const titles = {{
        veo3: {{ t: '1. Veo 3 プロンプトステーション (コピペ投入)', s: '各クリップの指示文をコピーしてGeminiに画像添付して送信してください' }},
        player: {{ t: '2. 完成動画プレイヤー & 聴き比べ', s: '共通のVeo 3映像（3カット）をベースに、4級〜準1級＋クラシック原文まで全6バリエーション完成！' }},
        vocab: {{ t: '3. 赤シート対応 単語・熟語チェック表', s: '赤シートをかざすと日本語訳が消えて自力テスト・暗記学習ができます' }},
        social: {{ t: '4. SNSマルチ発信ハブ (再生回数最大化)', s: 'ワンクリックで各SNS向けの投稿テキストをコピー＆投稿画面へ直行できます' }},
        kindle: {{ t: '5. Kindle原稿同期モニター', s: 'Kindle電子書籍内の動画リンク挿入状態プレビュー' }},
        brand: {{ t: '6. ブランド公式画像 ＆ SNSプロフィール設定', s: '全プラットフォーム共通の高品質アイコン・ヘッダーバナーと設定用テキスト' }}
      }};

      if (titles[tabId]) {{
        document.getElementById('pageTitleText').innerText = titles[tabId].t;
        document.getElementById('pageSubtitleText').innerText = titles[tabId].s;
      }}

      // Ensure content is fresh
      renderStory(currentStoryIndex);
      lucide.createIcons();
    }}

    function switchSocialSubTab(platform) {{
      document.querySelectorAll('.social-sub-content').forEach(el => el.style.display = 'none');
      document.querySelectorAll('#tab-social .grade-tab-btn').forEach(btn => btn.classList.remove('active'));
      
      const targetContent = document.getElementById('social-content-' + platform);
      if (targetContent) targetContent.style.display = 'block';

      const btnMap = {{ note: 'btn-sub-note', youtube: 'btn-sub-yt', x: 'btn-sub-x', instagram: 'btn-sub-ig' }};
      if (btnMap[platform]) {{
        const btn = document.getElementById(btnMap[platform]);
        if (btn) btn.classList.add('active');
      }}

      // Ensure current story content is rendered
      renderStory(currentStoryIndex);
      lucide.createIcons();
    }}

    function switchGradeVideo(gradeKey, label, duration, desc, btn) {{
      document.querySelectorAll('#tab-player .grade-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      const player = document.getElementById('mainVideoPlayer');
      const source = document.getElementById('videoSource');
      const story = ALL_STORIES[currentStoryIndex];
      const chStr = story.chapter < 10 ? '0' + story.chapter : story.chapter;
      
      const newSrc = `video_output/chapter${{chStr}}_${{story.key}}/chapter${{chStr}}_${{gradeKey}}.mp4`;
      source.src = newSrc;
      player.load();
      player.play();

      document.getElementById('currentGradeTitle').innerText = `🎬 Chapter ${{chStr}}: ${{story.titleJa}} (${{story.titleEn}}) 【${{label}} 版】`;
      document.getElementById('currentGradeBadge').innerText = `${{label}} レベル`;
      document.getElementById('currentDurationBadge').innerText = `尺: ${{duration}}`;
      document.getElementById('currentGradeDesc').innerHTML = `<b>【レベル特徴】</b> ${{desc}}`;

      showToast(`【${{label}}】の動画に切り替えました`);
    }}

    const YT_GRADES_CONFIG = [
      {{ key: 'Grade_4', label: '英検4級', icon: '🥉' }},
      {{ key: 'Grade_3', label: '英検3級', icon: '🥈' }},
      {{ key: 'Grade_Pre2', label: '英検準2級', icon: '🥇' }},
      {{ key: 'Grade_2', label: '英検2級', icon: '🏆' }},
      {{ key: 'Grade_Pre1', label: '英検準1級', icon: '👑' }},
      {{ key: 'Classic_Original', label: 'クラシック原文', icon: '🏛️' }},
      {{ key: 'Shorts', label: '縦型Shorts', icon: '📱' }}
    ];

    function getStoredGradeYoutubeUrl(chNum, gradeKey) {{
      const storageKey = `mdo3_yt_${{chNum < 10 ? '0' + chNum : chNum}}_${{gradeKey}}`;
      const local = localStorage.getItem(storageKey);
      if (local && local.trim().length > 0) return local.trim();
      const story = ALL_STORIES.find(s => s.chapter === chNum);
      if (story && story.youtubeUrls && story.youtubeUrls[gradeKey]) {{
        return story.youtubeUrls[gradeKey];
      }}
      return '';
    }}

    function getBestYoutubeUrl(chNum) {{
      for (let g of YT_GRADES_CONFIG) {{
        const url = getStoredGradeYoutubeUrl(chNum, g.key);
        if (url) return url;
      }}
      return '';
    }}

    function renderYoutubeSlotsGrid(chNum) {{
      const grid = document.getElementById('yt_all_grade_slots_grid');
      if (!grid) return;
      grid.innerHTML = '';

      YT_GRADES_CONFIG.forEach(g => {{
        const url = getStoredGradeYoutubeUrl(chNum, g.key);
        const isSelected = (currentSelectedYtGrade === g.key);
        const isRegistered = (url && url.length > 0);

        const card = document.createElement('div');
        card.style = `background:${{isSelected ? 'rgba(56,189,248,0.15)' : 'rgba(0,0,0,0.3)'}}; border:1px solid ${{isSelected ? 'var(--accent-primary)' : 'var(--card-border)'}}; border-radius:var(--radius-sm); padding:8px 10px; display:flex; justify-content:space-between; align-items:center;`;
        
        card.innerHTML = `
          <div>
            <div style="font-weight:700; color:${{isSelected ? 'var(--accent-primary)' : '#f8fafc'}}; display:flex; align-items:center; gap:4px;">
              <span>${{g.icon}} ${{g.label}}</span>
              ${{isSelected ? '<span style="font-size:0.68rem; background:var(--accent-primary); color:#000; padding:1px 4px; border-radius:3px; font-weight:800;">編集中</span>' : ''}}
            </div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.72rem; color:${{isRegistered ? 'var(--accent-green)' : 'var(--text-muted)'}}; margin-top:2px; max-width:200px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
              ${{isRegistered ? url : '未登録 (空)'}}
            </div>
          </div>
          <div style="display:flex; gap:4px;">
            ${{isRegistered ? `<a href="${{url}}" target="_blank" class="btn" style="padding:3px 6px; font-size:0.7rem; background:rgba(255,255,255,0.1);"><i data-lucide="external-link"></i></a>` : ''}}
            <button class="btn btn-secondary" style="padding:3px 8px; font-size:0.7rem;" onclick="selectGradeSlotDirectly('${{g.key}}', '${{g.label}}')">
              ${{isSelected ? '入力中' : '選択'}}
            </button>
          </div>
        `;
        grid.appendChild(card);
      }});
      lucide.createIcons();
    }}

    function selectGradeSlotDirectly(gradeKey, label) {{
      const btn = document.getElementById('yt-btn-' + gradeKey);
      if (btn) btn.click();
    }}

    function applyAndSaveYoutubeUrl() {{
      const input = document.getElementById('yt_live_url_input');
      const url = input.value.trim();
      const story = ALL_STORIES[currentStoryIndex];
      const chNum = story.chapter;
      const storageKey = `mdo3_yt_${{chNum < 10 ? '0' + chNum : chNum}}_${{currentSelectedYtGrade}}`;
      
      localStorage.setItem(storageKey, url);
      
      if (!story.youtubeUrls) story.youtubeUrls = {{}};
      story.youtubeUrls[currentSelectedYtGrade] = url;

      renderStory(currentStoryIndex);
      showToast(`🎉【${{currentSelectedYtGrade}}】のYouTube URLを保存＆各SNSに反映しました！`);
    }}

    function switchYtGrade(gradeKey, label, subLabel) {{
      currentSelectedYtGrade = gradeKey;
      document.querySelectorAll('#social-content-youtube .grade-tab-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById('yt-btn-' + gradeKey);
      if (activeBtn) activeBtn.classList.add('active');

      const story = ALL_STORIES[currentStoryIndex];
      if (!story) return;

      // Update Active Slot Input Box
      const slotTitle = document.getElementById('yt_slot_active_title');
      if (slotTitle) slotTitle.innerText = `【${{label}} 版】アップロードした YouTube 動画のURLを登録`;
      
      const slotBadge = document.getElementById('yt_slot_active_badge');
      if (slotBadge) slotBadge.innerText = `現在選択中: ${{label}}`;

      const input = document.getElementById('yt_live_url_input');
      if (input) {{
        input.placeholder = `https://youtu.be/... (${{label}}のURL)`;
        input.value = getStoredGradeYoutubeUrl(story.chapter, gradeKey);
      }}

      renderYoutubeSlotsGrid(story.chapter);

      if (gradeKey === 'Shorts') {{
        document.getElementById('yt_field_title').innerText = `【1分英語】${{story.titleJa}} (${{story.titleEn}})｜ネイティブ朗読×カラオケ字幕 #Shorts #英語学習 #英検`;
        document.getElementById('yt_field_desc').innerText = `イソップ寓話の名作「${{story.titleJa}}」を1分でシャドーイング！\n\nフル動画本編・解説はチャンネル動画一覧からご覧いただけます✨\n\n#Shorts #英語多読 #英検 #英語リスニング #MDO3出版`;
        document.getElementById('yt_field_tags').innerText = `Shorts,英語学習,英検,イソップ寓話,${{story.titleJa}},リスニング,シャドーイング,MDO3出版`;
      }} else if (gradeKey === 'Classic_Original') {{
        document.getElementById('yt_field_title').innerText = `【イギリス英語古典朗読】${{story.titleJa}} (${{story.titleEn}})｜Townsend版 クラシック原文×光るカラオケ字幕`;
        document.getElementById('yt_field_desc').innerText = `格調高いイギリス英語の古典原文（Townsend版）で味わう「${{story.titleJa}}」です。\nネイティブ朗読の発音に合わせて単語が光るリアルタイム字幕でシャドーイングできます。\n\n📚 Kindle電子書籍シリーズも完全無料読み放題で配信中！\n👉 https://www.amazon.co.jp/\n\n#英語学習 #イギリス英語 #イソップ寓話 #クラシック英語 #英語多読 #MDO3出版`;
        document.getElementById('yt_field_tags').innerText = `イギリス英語,クラシック英語,英語多読,イソップ寓話,${{story.titleJa}},${{story.titleEn}},リスニング,シャドーイング,MDO3出版`;
      }} else {{
        document.getElementById('yt_field_title').innerText = `【小中高〜大人の英検多読】${{story.titleJa}} (${{story.titleEn}})｜ネイティブ朗読×光るカラオケ字幕で英語がスラスラ聴こえる！【${{label}}・${{subLabel}}】`;
        document.getElementById('yt_field_desc').innerText = `小中高校生の英検・受験対策から大人の学び直しまで！英語多読チャンネル「MDO3出版」へようこそ！✨\n今回はイソップ寓話の名作「${{story.titleJa}}」の【${{label}} 版】をお届けします。\n\n🌟 【この動画の使い方】\n発音のリズムに合わせて単語が光る【リアルタイム英語カラオケ字幕】です。\n耳で聴きながら、光る単語に合わせて一緒に声に出して読む（シャドーイング）ことで、リスニング力とスピーキング力が劇的にアップします！小中学生の英語の授業や英検対策、親子での英語学習にもぴったりです。\n\n📚 【Kindle完全無料・電子書籍（全60話）】\n小中高生の英語学習を応援！Kindle Unlimited会員なら全巻無料読み放題！\n👉 https://www.amazon.co.jp/\n\n🐦 𝕏 (Twitter): @mdo3_english\n📝 note: https://note.com/mdo3_english\n📸 Instagram: @mdo3_english\n\n👍 いいね・チャンネル登録・コメントで応援していただけると励みになります！\n#英語学習 #${{label.replace(' ', '')}} #イソップ寓話 #${{story.titleJa.replace(' ', '')}} #英語多読 #リスニング #シャドーイング #カラオケ字幕 #MDO3出版`;
        document.getElementById('yt_field_tags').innerText = `英語学習,${{label}},小中学生英語,中学英語,高校英語,イソップ寓話,${{story.titleJa}},${{story.titleEn}},英語多読,リスニング,シャドーイング,カラオケ字幕,英語聞き流し,大人の学び直し英語,MDO3出版`;
      }}

      showToast(`YouTubeメタデータを【${{label}}】に切り替えました`);
    }}

    function switchXPattern(patternKey) {{
      currentXPattern = patternKey;
      document.querySelectorAll('#social-content-x .grade-tab-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById('x-pattern-btn-' + patternKey);
      if (activeBtn) activeBtn.classList.add('active');

      renderStory(currentStoryIndex);
      const names = {{ a: 'パターンA (王道・教育)', b: 'パターンB (文法・対比)', c: 'パターンC (教訓・大人)' }};
      showToast(`𝕏投稿を【${{names[patternKey] || patternKey}}】に切り替えました`);
    }}

    function copyPrompt(elementId, btn) {{
      const text = document.getElementById(elementId).innerText;
      navigator.clipboard.writeText(text).then(() => {{
        showToast('クリップボードにコピーしました！');
        btn.innerHTML = '<i data-lucide="check"></i> コピー完了';
        lucide.createIcons();
        setTimeout(() => {{
          btn.innerHTML = '<i data-lucide="copy"></i> コピーする';
          lucide.createIcons();
        }}, 2000);
      }});
    }}

    function reloadVideo() {{
      const player = document.getElementById('mainVideoPlayer');
      player.load();
      player.play();
      showToast('動画を再読み込みしました');
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      document.getElementById('toastMsg').innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {{ toast.classList.remove('show'); }}, 2500);
    }}

    window.onload = initPortal;
  </script>
</body>
</html>
"""

with open(PORTAL_FILE, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"🎉 Integrated Master Portal Generated Successfully: {PORTAL_FILE}")

import json
import os
import re
import glob
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
OUTPUT_HTML = os.path.join(BASE_DIR, "study_portal_for_son.html")
MASTER_JSON = os.path.join(BASE_DIR, "veo3_production", "veo3_prompts_master.json")

def load_master_stories():
    if os.path.exists(MASTER_JSON):
        with open(MASTER_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("stories", [])
    return []

def get_chapter_full_data(chapter_num):
    ch_str = f"{chapter_num:02d}"
    group_idx = (chapter_num - 1) // 10

    def find_file(tier_num):
        if tier_num == 1:
            candidates = [f"chapter{ch_str}_*.md", f"vol1_chapter{ch_str}_*.md", f"vol{group_idx * 4 + 1}_chapter{ch_str}_*.md"]
        else:
            candidates = [f"vol{tier_num}_chapter{ch_str}_*.md", f"vol{group_idx * 4 + tier_num}_chapter{ch_str}_*.md"]

        for pat in candidates:
            m = glob.glob(os.path.join(BASE_DIR, pat))
            if m:
                return m[0]
        return ""

    v1_file = find_file(1)
    v2_file = find_file(2)
    v3_file = find_file(3)
    v4_file = find_file(4)

    def read_f(fp):
        if fp and os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    v1_c = read_f(v1_file)
    v2_c = read_f(v2_file)
    v3_c = read_f(v3_file)
    v4_c = read_f(v4_file)

    def ext(pattern, content):
        m = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return m.group(1).strip() if m else ""

    g4_text = ext(r"## 1\. Benchmark Level: Eiken (?:Grade )?4[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v1_c)
    g3_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?3[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v1_c)
    gpre2_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?Pre-?2[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v2_c)
    g2_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?2[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v3_c)
    gpre1_text = ext(r"## 2\. Target Level: Eiken (?:Grade )?Pre-?1[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v4_c)
    classic_text = ext(r"## 3\. Classic Original English Text[^\n]*\n\*[^*]+\*\n\n(.*?)(?=\n---|\n<div|\n##)", v1_c)

    vocab_text = ext(r"## 4\. (?:Vocabulary|重要単語・熟語チェック表|Key Vocabulary)[^\n]*\n(.*?)(?=\n---|\n<div|\n##|$)", v1_c)
    if not vocab_text:
        vocab_text = ext(r"(\| Vocabulary \|.*?\n(?:\|.*?\|\n)+)", v1_c)

    moral_text = ext(r"## (?:5|4)\. (?:Moral & Educational Insight|教訓と解説)[^\n]*\n(.*?)(?=\n---|\n<div|\n##|$)", v1_c)

    return {
        "Grade_4": g4_text,
        "Grade_3": g3_text,
        "Grade_Pre2": gpre2_text,
        "Grade_2": g2_text,
        "Grade_Pre1": gpre1_text,
        "Classic_Original": classic_text,
        "vocab": vocab_text,
        "moral": moral_text
    }

def generate_portal_html():
    raw_stories = load_master_stories()
    stories_data = []

    for s in raw_stories:
        ch = s["chapter"]
        full_content = get_chapter_full_data(ch)
        s_obj = {
            "chapter": ch,
            "key": s["key"],
            "titleEn": s["titleEn"],
            "titleJa": s["titleJa"],
            "referenceImage": s.get("referenceImage", f"images/vol1_chapter{ch:02d}.png"),
            "texts": full_content
        }
        stories_data.append(s_obj)

    stories_json = json.dumps(stories_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>DAILY HERO & EIKEN STUDIO｜長男専用 学習＆日課ポータル</title>
  
  <!-- PWA & Mobile Web App Meta Tags -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="DailyHero">
  <meta name="theme-color" content="#070b14">
  <link rel="apple-touch-icon" href="sns_brand_assets/profile_icon.jpg">
  
  <!-- Google Fonts & Lucide Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <script src="Version.js"></script>

  <style>
    :root {{
      --bg-dark: #070b14;
      --bg-card: rgba(18, 25, 43, 0.85);
      --bg-card-hover: rgba(28, 38, 64, 0.95);
      --card-border: rgba(255, 255, 255, 0.08);
      
      --accent-cyan: #38bdf8;
      --accent-green: #10b981;
      --accent-gold: #fbbf24;
      --accent-purple: #c084fc;
      --accent-rose: #f43f5e;
      --accent-red: #ef4444;
      --accent-gradient: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
      --gold-gradient: linear-gradient(135deg, #fbbf24 0%, #f59e0b 50%, #d97706 100%);
      --green-gradient: linear-gradient(135deg, #10b981 0%, #059669 100%);
      --penalty-gradient: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%);
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --red-sheet: #d90429;
      
      --radius-xl: 20px;
      --radius-lg: 14px;
      --radius-md: 10px;
      --radius-sm: 6px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }}
    
    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.15) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(192, 132, 252, 0.15) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(16, 185, 129, 0.05) 0px, transparent 60%);
      background-attachment: fixed;
      padding-bottom: 90px;
    }}

    /* App Header */
    .app-header {{
      background: rgba(11, 17, 32, 0.94);
      backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--card-border);
      padding: 16px 20px;
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .app-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .app-logo {{
      width: 42px;
      height: 42px;
      border-radius: var(--radius-md);
      background: var(--accent-gradient);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #000;
      box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }}

    .app-title h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 900;
      letter-spacing: 0.5px;
      background: var(--accent-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .app-title span {{
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .header-pwa-badge {{
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 6px 12px;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}

    /* Navigation Tabs */
    .nav-tabs-wrapper {{
      padding: 12px 20px;
      background: rgba(7, 11, 20, 0.85);
      border-bottom: 1px solid var(--card-border);
      position: sticky;
      top: 74px;
      z-index: 90;
      backdrop-filter: blur(16px);
      overflow-x: auto;
      white-space: nowrap;
    }}

    .nav-tabs {{
      display: flex;
      gap: 8px;
      max-width: 960px;
      margin: 0 auto;
    }}

    .nav-tab-btn {{
      padding: 9px 16px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      font-weight: 700;
      font-size: 0.82rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}

    .nav-tab-btn:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-main);
    }}

    .nav-tab-btn.active {{
      background: var(--accent-gradient);
      border-color: transparent;
      color: #070b14;
      box-shadow: 0 4px 16px rgba(56, 189, 248, 0.35);
      font-weight: 800;
    }}

    /* Main Container */
    .container {{
      max-width: 960px;
      width: 100%;
      margin: 0 auto;
      padding: 20px;
      flex-grow: 1;
    }}

    .tab-pane {{
      display: none;
    }}
    .tab-pane.active {{
      display: block;
      animation: fadeIn 0.25s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Card Box */
    .hero-card {{
      background: var(--bg-card);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-xl);
      padding: 22px;
      margin-bottom: 20px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
      position: relative;
      overflow: hidden;
    }}

    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--card-border);
    }}

    .card-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.12rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    /* Penalty & Multiplier Banner */
    .penalty-banner {{
      background: rgba(18, 25, 43, 0.95);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      margin-bottom: 20px;
      border: 2px solid rgba(255, 255, 255, 0.1);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}

    .penalty-banner.normal {{
      border-color: var(--accent-green);
      background: rgba(16, 185, 129, 0.1);
    }}

    .penalty-banner.warn1 {{
      border-color: var(--accent-gold);
      background: rgba(251, 191, 36, 0.12);
    }}

    .penalty-banner.warn2 {{
      border-color: #f97316;
      background: rgba(249, 115, 22, 0.15);
    }}

    .penalty-banner.danger {{
      border-color: var(--accent-red);
      background: rgba(239, 68, 68, 0.2);
      animation: pulseAlert 2s infinite;
    }}

    @keyframes pulseAlert {{
      0%, 100% {{ box-shadow: 0 0 15px rgba(239, 68, 68, 0.3); }}
      50% {{ box-shadow: 0 0 30px rgba(239, 68, 68, 0.7); }}
    }}

    /* Task Item Checkboxes & AI Test Trigger */
    .task-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .task-item {{
      background: rgba(11, 17, 32, 0.6);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: all 0.25s;
    }}

    .task-item.passed {{
      background: rgba(16, 185, 129, 0.12);
      border-color: rgba(16, 185, 129, 0.45);
    }}

    .task-main-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}

    .task-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-grow: 1;
    }}

    .status-badge-chip {{
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 800;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
    }}

    .status-badge-chip.pass {{
      background: var(--accent-green);
      color: #070b14;
    }}

    .status-badge-chip.pending {{
      background: rgba(251, 191, 36, 0.2);
      color: var(--accent-gold);
      border: 1px solid rgba(251, 191, 36, 0.4);
    }}

    /* Gemini AI Test Modal / Box */
    .ai-test-box {{
      background: rgba(7, 11, 20, 0.75);
      border: 1px dashed rgba(56, 189, 248, 0.35);
      border-radius: var(--radius-md);
      padding: 14px;
      margin-top: 8px;
    }}

    .drive-upload-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 10px;
    }}

    .btn-drive {{
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: var(--accent-cyan);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      cursor: pointer;
    }}

    .btn-ai-test {{
      background: var(--accent-gradient);
      color: #070b14;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
    }}

    /* Quiz Modal / Question Box */
    .quiz-container {{
      background: rgba(18, 25, 43, 0.98);
      border: 1px solid var(--accent-cyan);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin-top: 14px;
      display: none;
    }}

    .quiz-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 10px;
    }}

    .quiz-q-text {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 12px;
      line-height: 1.5;
    }}

    .quiz-options-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      margin-bottom: 16px;
    }}

    .quiz-opt-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      padding: 10px 14px;
      color: var(--text-main);
      font-size: 0.85rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .quiz-opt-btn:hover {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--accent-cyan);
    }}

    .quiz-opt-btn.selected-correct {{
      background: rgba(16, 185, 129, 0.25);
      border-color: var(--accent-green);
      color: var(--accent-green);
      font-weight: 800;
    }}

    .quiz-opt-btn.selected-wrong {{
      background: rgba(239, 68, 68, 0.25);
      border-color: var(--accent-red);
      color: var(--accent-red);
    }}

    /* Split Allocation Cards (50% Suica/Rakuten Cash + 50% Investment Trust) */
    .allocation-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-top: 16px;
    }}

    .alloc-card {{
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .alloc-card.cash {{
      border-color: rgba(56, 189, 248, 0.4);
    }}

    .alloc-card.invest {{
      border-color: rgba(251, 191, 36, 0.4);
    }}

    .alloc-title {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .alloc-value {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.5rem;
      font-weight: 900;
      color: #fff;
    }}

    /* Audio Player in Reader */
    .audio-player-card {{
      background: rgba(11, 17, 32, 0.8);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
    }}

    .audio-controls-group {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .btn-audio-play {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--accent-cyan);
      color: #070b14;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(56, 189, 248, 0.4);
    }}

    /* Big Submit Buttons */
    .btn-line-submit {{
      background: #06c755;
      color: #fff;
      font-family: 'Outfit', sans-serif;
      font-weight: 900;
      font-size: 1.05rem;
      padding: 16px 24px;
      border-radius: var(--radius-lg);
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      width: 100%;
      text-decoration: none;
      box-shadow: 0 8px 24px rgba(6, 199, 85, 0.4);
      transition: all 0.25s;
    }}

    .btn-line-submit:hover {{
      background: #05b34c;
      transform: translateY(-2px);
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 10px 16px;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.82rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
    }}

    /* Custom Input & Select */
    .custom-select {{
      background: rgba(11, 17, 32, 0.9);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 10px 14px;
      border-radius: var(--radius-md);
      font-size: 0.88rem;
      font-weight: 700;
      outline: none;
    }}

    .task-input-field {{
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-sm);
      color: #fff;
      padding: 6px 10px;
      font-size: 0.82rem;
      width: 180px;
      outline: none;
    }}

    /* Reader & Red Sheet Styles */
    .reader-box {{
      background: #ffffff;
      color: #1e293b;
      border-radius: var(--radius-xl);
      padding: 26px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
      position: relative;
      margin-bottom: 24px;
    }}

    .btn-red-sheet {{
      background: #1e293b;
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: var(--accent-cyan);
      font-weight: 800;
      font-size: 0.82rem;
      padding: 8px 14px;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-red-sheet.active {{
      background: #0284c7;
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
    }}

    .reader-text-body {{
      font-size: 1.02rem;
      line-height: 1.85;
      color: #1e293b;
      white-space: pre-wrap;
    }}

    /* Blackout / Mask Mode on Vocab & Text */
    .vocab-table-container table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
    }}

    .vocab-table-container th, .vocab-table-container td {{
      padding: 10px 12px;
      border: 1px solid #e2e8f0;
      font-size: 0.88rem;
    }}

    .vocab-table-container th {{
      background: #f8fafc;
      color: #334155;
      font-weight: 700;
    }}

    .red-mask-active .vocab-red, .red-mask-active td:nth-child(2) {{
      background: #0f172a !important;
      color: #0f172a !important;
      user-select: none;
      border-radius: 4px;
      cursor: pointer;
      position: relative;
      transition: all 0.15s ease;
    }}

    .red-mask-active .vocab-red::after, .red-mask-active td:nth-child(2)::after {{
      content: '⬛ 隠し中 (タップで表示)';
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 0.72rem;
      font-weight: 700;
      color: #64748b;
      pointer-events: none;
      white-space: nowrap;
    }}

    .red-mask-active .vocab-red.revealed, .red-mask-active td:nth-child(2).revealed {{
      background: rgba(56, 189, 248, 0.12) !important;
      color: #0f172a !important;
      font-weight: 800;
    }}

    .red-mask-active .vocab-red.revealed::after, .red-mask-active td:nth-child(2).revealed::after {{
      display: none;
    }}

    /* Toast */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--accent-green);
      color: #070b14;
      font-weight: 800;
      padding: 12px 20px;
      border-radius: var(--radius-md);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 1000;
    }}
    .toast.show {{ transform: translateY(0); opacity: 1; }}

    @media (max-width: 600px) {{
      .container {{ padding: 12px; }}
      .hero-card {{ padding: 16px; }}
      .allocation-grid {{ grid-template-columns: 1fr; }}
      .task-main-row {{ flex-wrap: wrap; }}
      .app-title h1 {{ font-size: 1rem; }}
    }}
  </style>
</head>
<body>

  <!-- App Header -->
  <header class="app-header">
    <div class="app-brand">
      <div class="app-logo">
        <i data-lucide="zap"></i>
      </div>
      <div class="app-title">
        <h1>DAILY HERO & EIKEN STUDIO <span id="appVerBadge" style="font-size:0.65rem; background:rgba(56,189,248,0.2); color:var(--accent-cyan); padding:2px 6px; border-radius:4px; vertical-align:middle; margin-left:6px;">v1.0.0</span></h1>
        <span>長男専用 毎日の学習＆日課ポータル</span>
      </div>
    </div>
    <div class="header-pwa-badge" onclick="showPwaGuide()">
      <i data-lucide="smartphone"></i> ホーム画面に追加
    </div>
  </header>

  <!-- Nav Tabs -->
  <div class="nav-tabs-wrapper">
    <div class="nav-tabs">
      <button class="nav-tab-btn active" onclick="switchMainTab('quest')">
        <i data-lucide="check-circle-2"></i> 1. 日課＆AIテスト
      </button>
      <button class="nav-tab-btn" onclick="switchMainTab('video')">
        <i data-lucide="play-circle"></i> 2. 英語動画プレイヤー
      </button>
      <button class="nav-tab-btn" onclick="switchMainTab('reader')">
        <i data-lucide="book-open"></i> 3. 英語リーダー (赤シート＆音声)
      </button>
      <button class="nav-tab-btn" onclick="switchMainTab('asset')">
        <i data-lucide="pie-chart"></i> 4. お小遣い＆投資配分
      </button>
    </div>
  </div>

  <main class="container">

    <!-- ============================================================ -->
    <!-- TAB 1: 日課＆AIテスト＆お小遣い (Daily Quest & AI Test) -->
    <!-- ============================================================ -->
    <div id="tab-quest" class="tab-pane active">
      
      <!-- Penalty & Streak Banner -->
      <div class="penalty-banner normal" id="penaltyStatusBanner">
        <div>
          <div style="font-size:0.78rem; font-weight:700; color:var(--text-muted); text-transform:uppercase;">
            ⚡ サボりペナルティ判定ステータス
          </div>
          <div style="font-size:1.15rem; font-weight:900; color:#fff; margin-top:2px;" id="penaltyMultiplierText">
            通常受取: 100% (満額)
          </div>
          <div style="font-size:0.75rem; color:var(--text-muted); margin-top:2px;" id="penaltyDescText">
            連続達成中！サボりなしで翌朝報告すれば全額GET！
          </div>
        </div>
        <div style="text-align:right;">
          <span style="font-size:0.72rem; color:var(--text-muted);">連続サボり日数:</span>
          <select id="slackingDaysSelect" class="custom-select" style="padding:4px 8px; font-size:0.8rem; margin-top:4px;" onchange="updatePenaltyMultiplier(this.value)">
            <option value="0">0日 (通常 100%)</option>
            <option value="1">1日サボり (50% 減額 / 1/2)</option>
            <option value="2">2日サボり (25% 減額 / 1/4)</option>
            <option value="3">3日サボり (12.5% 減額 / 1/8)</option>
            <option value="4">4日サボり (6.25% 減額 / 1/16 ⚡雷⚡)</option>
          </select>
        </div>
      </div>

      <!-- 1. 基本義務ミッション -->
      <div class="hero-card">
        <div class="card-header">
          <div class="card-title">
            <span style="color:var(--accent-gold);"><i data-lucide="shield-check"></i></span>
            <span>【基本義務ミッション】 4項目すべて合格で ￥350</span>
          </div>
          <span class="status-badge-chip" id="baseMissionProgressBadge">未達成 (0/4)</span>
        </div>

        <div class="task-list">
          <!-- 1. 朝5時起床 -->
          <div class="task-item" id="task_wake">
            <div class="task-main-row">
              <div class="task-left">
                <input type="checkbox" id="chk_wake" style="width:20px; height:20px; cursor:pointer;" onchange="toggleTaskManual('wake', this.checked)">
                <div>
                  <h4 style="font-size:0.95rem; font-weight:700;">⏰ 朝5時起床</h4>
                  <p style="font-size:0.78rem; color:var(--text-muted);">父が先に起きているため嘘はつけません（自己申告）</p>
                </div>
              </div>
              <span class="status-badge-chip" id="badge_wake">未達</span>
            </div>
          </div>

          <!-- 2. 素振り100回以上 -->
          <div class="task-item" id="task_swing">
            <div class="task-main-row">
              <div class="task-left">
                <input type="checkbox" id="chk_swing" style="width:20px; height:20px; cursor:pointer;" onchange="toggleTaskManual('swing', this.checked)">
                <div>
                  <h4 style="font-size:0.95rem; font-weight:700;">⚾ 素振り100回以上</h4>
                  <p style="font-size:0.78rem; color:var(--text-muted);">スイング練習（自己申告）</p>
                </div>
              </div>
              <input type="text" id="swing_count_input" class="task-input-field" placeholder="回数 (例: 100回)" value="100回" onchange="calculateDailyReward()">
            </div>
          </div>

          <!-- 3. 漢字検定 (見開き2ページ・計4P ＋ Gemini 10問テスト) -->
          <div class="task-item" id="task_kanji">
            <div class="task-main-row">
              <div class="task-left">
                <span style="color:var(--accent-cyan);"><i data-lucide="brain-circuit"></i></span>
                <div>
                  <h4 style="font-size:0.95rem; font-weight:700;">✍️ 漢字検定 (準2級) 見開き2ページ (計4P)</h4>
                  <p style="font-size:0.78rem; color:var(--text-muted);">やったページのスクショをDriveに保存 ＆ 10問テストに合格でクリア</p>
                </div>
              </div>
              <span class="status-badge-chip pending" id="badge_kanji">テスト未合格</span>
            </div>

            <div class="ai-test-box">
              <div class="drive-upload-bar">
                <a href="https://drive.google.com" target="_blank" class="btn-drive">
                  <i data-lucide="upload-cloud"></i> ① Google DriveにスクショUP
                </a>
                <button class="btn-ai-test" onclick="startAiQuiz('kanji')">
                  <i data-lucide="sparkles"></i> ② Gemini 10問テストを開始
                </button>
              </div>
              <div class="quiz-container" id="quiz_box_kanji">
                <div class="quiz-header">
                  <span style="font-weight:800; font-size:0.85rem; color:var(--accent-cyan);" id="quiz_progress_kanji">漢検 準2級 10問テスト (問 1/10)</span>
                  <span style="font-size:0.75rem; color:var(--accent-gold);">合格基準: 8問以上正解</span>
                </div>
                <div class="quiz-q-text" id="quiz_q_kanji">問題文を読み込み中...</div>
                <div class="quiz-options-grid" id="quiz_opts_kanji"></div>
              </div>
            </div>
          </div>

          <!-- 4. 英語検定 (単語帳見開き2ページ ＋ Gemini 10問テスト) -->
          <div class="task-item" id="task_english">
            <div class="task-main-row">
              <div class="task-left">
                <span style="color:var(--accent-cyan);"><i data-lucide="brain-circuit"></i></span>
                <div>
                  <h4 style="font-size:0.95rem; font-weight:700;">🎧 英語検定 (準2級) 単語帳 見開き2ページ</h4>
                  <p style="font-size:0.78rem; color:var(--text-muted);">単語帳スクショをDrive保存 ＆ 英検準2級 10問テストに合格でクリア</p>
                </div>
              </div>
              <span class="status-badge-chip pending" id="badge_english">テスト未合格</span>
            </div>

            <div class="ai-test-box">
              <div class="drive-upload-bar">
                <a href="https://drive.google.com" target="_blank" class="btn-drive">
                  <i data-lucide="upload-cloud"></i> ① Google DriveにスクショUP
                </a>
                <button class="btn-ai-test" onclick="startAiQuiz('english')">
                  <i data-lucide="sparkles"></i> ② Gemini 10問テストを開始
                </button>
              </div>
              <div class="quiz-container" id="quiz_box_english">
                <div class="quiz-header">
                  <span style="font-weight:800; font-size:0.85rem; color:var(--accent-cyan);" id="quiz_progress_english">英検準2級 10問テスト (問 1/10)</span>
                  <span style="font-size:0.75rem; color:var(--accent-gold);">合格基準: 8問以上正解</span>
                </div>
                <div class="quiz-q-text" id="quiz_q_english">問題文を読み込み中...</div>
                <div class="quiz-options-grid" id="quiz_opts_english"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. 追加2教科学習ボーナス (スタサプ / 進研ゼミ / スマイルゼミ + 各￥100) -->
      <div class="hero-card">
        <div class="card-header">
          <div class="card-title">
            <span style="color:var(--accent-cyan);"><i data-lucide="plus-circle"></i></span>
            <span>【追加2教科ボーナス】 スタサプ/進研/スマイルゼミ (各 +￥100)</span>
          </div>
          <span style="font-size:0.8rem; color:var(--text-muted);">最大 +￥200</span>
        </div>

        <div class="task-list">
          <!-- 追加教科① -->
          <div class="task-item" id="task_extra1">
            <div class="task-main-row">
              <div class="task-left">
                <span style="color:var(--accent-purple);"><i data-lucide="smartphone"></i></span>
                <div>
                  <h4 style="font-size:0.95rem; font-weight:700;">➕ 追加教科 ① (スタサプ/進研/スマイル)</h4>
                  <p style="font-size:0.78rem; color:var(--text-muted);">学習完了画面のスクショをUP ＆ 10問テスト合格で+￥100</p>
                </div>
              </div>
              <span class="status-badge-chip pending" id="badge_extra1">テスト未合格</span>
            </div>
            <div class="ai-test-box">
              <div class="drive-upload-bar">
                <input type="text" id="extra1_subject_name" class="task-input-field" placeholder="教科名 (例: 数学・一次関数)" value="数学">
                <button class="btn-ai-test" onclick="startAiQuiz('extra1')"><i data-lucide="sparkles"></i> 10問テスト開始</button>
              </div>
              <div class="quiz-container" id="quiz_box_extra1">
                <div class="quiz-header">
                  <span style="font-weight:800; font-size:0.85rem; color:var(--accent-cyan);" id="quiz_progress_extra1">追加教科① 10問テスト</span>
                </div>
                <div class="quiz-q-text" id="quiz_q_extra1"></div>
                <div class="quiz-options-grid" id="quiz_opts_extra1"></div>
              </div>
            </div>
          </div>

          <!-- 追加教科② -->
          <div class="task-item" id="task_extra2">
            <div class="task-main-row">
              <div class="task-left">
                <span style="color:var(--accent-purple);"><i data-lucide="smartphone"></i></span>
                <div>
                  <h4 style="font-size:0.95rem; font-weight:700;">➕ 追加教科 ② (スタサプ/進研/スマイル)</h4>
                  <p style="font-size:0.78rem; color:var(--text-muted);">学習完了画面のスクショをUP ＆ 10問テスト合格で+￥100</p>
                </div>
              </div>
              <span class="status-badge-chip pending" id="badge_extra2">テスト未合格</span>
            </div>
            <div class="ai-test-box">
              <div class="drive-upload-bar">
                <input type="text" id="extra2_subject_name" class="task-input-field" placeholder="教科名 (例: 理科・電流)" value="理科">
                <button class="btn-ai-test" onclick="startAiQuiz('extra2')"><i data-lucide="sparkles"></i> 10問テスト開始</button>
              </div>
              <div class="quiz-container" id="quiz_box_extra2">
                <div class="quiz-header">
                  <span style="font-weight:800; font-size:0.85rem; color:var(--accent-cyan);" id="quiz_progress_extra2">追加教科② 10問テスト</span>
                </div>
                <div class="quiz-q-text" id="quiz_q_extra2"></div>
                <div class="quiz-options-grid" id="quiz_opts_extra2"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. 特別自己申告ボーナス -->
      <div class="hero-card">
        <div class="card-header">
          <div class="card-title">
            <span style="color:var(--accent-purple);"><i data-lucide="award"></i></span>
            <span>【特別自己申告ボーナス】 テスト上位・がんばり申告</span>
          </div>
        </div>
        <div style="display:grid; grid-template-columns: 2fr 1fr; gap:12px;">
          <input type="text" id="special_reason_input" class="custom-select" placeholder="理由 (例: 数学小テストでクラス1位！)" oninput="calculateDailyReward()">
          <input type="number" id="special_amount_input" class="custom-select" placeholder="金額 (￥)" min="0" step="50" oninput="calculateDailyReward()">
        </div>
      </div>

      <!-- 今日の計算結果 ＆ LINE送信 -->
      <div class="hero-card" style="border-color:rgba(56,189,248,0.4); background:linear-gradient(135deg, rgba(7,11,20,0.9) 0%, rgba(18,25,43,0.95) 100%);">
        <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap:14px; margin-bottom:16px;">
          <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:var(--radius-lg); text-align:center;">
            <div style="font-size:0.75rem; color:var(--text-muted); font-weight:700;">額面合計 (満額時)</div>
            <div style="font-family:'Outfit',sans-serif; font-size:1.6rem; font-weight:900; color:#fff;" id="rawTotalDisplay">￥0</div>
          </div>
          <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:var(--radius-lg); text-align:center; border:1px solid var(--accent-green);">
            <div style="font-size:0.75rem; color:var(--accent-green); font-weight:700;">実受取額 (サボり減額適用後)</div>
            <div style="font-family:'Outfit',sans-serif; font-size:1.8rem; font-weight:900; color:var(--accent-green);" id="finalTotalDisplay">￥0</div>
          </div>
        </div>

        <!-- 50% Suica/Rakuten + 50% Investment Trust -->
        <div class="allocation-grid" style="margin-bottom:20px;">
          <div class="alloc-card cash">
            <div class="alloc-title"><i data-lucide="credit-card" style="color:var(--accent-cyan);"></i> 📱 Suica / 楽天キャッシュ (50%)</div>
            <div class="alloc-value">￥<span id="allocCashDisplay">0</span></div>
            <span style="font-size:0.7rem; color:var(--text-muted);">自由にお小遣いとして使用可能</span>
          </div>
          <div class="alloc-card invest">
            <div class="alloc-title"><i data-lucide="trending-up" style="color:var(--accent-gold);"></i> 📈 投資信託 積立 (50%)</div>
            <div class="alloc-value">￥<span id="allocInvestDisplay">0</span></div>
            <span style="font-size:0.7rem; color:var(--text-muted);">将来の資産形成へ自動投資</span>
          </div>
        </div>

        <!-- LINE送信ボタン -->
        <a id="lineSubmitBtn" href="#" target="_blank" class="btn-line-submit" onclick="submitToLine()">
          <i data-lucide="send"></i> 🟢 LINEでお父さんに完了報告する
        </a>
      </div>

    </div>

    <!-- ============================================================ -->
    <!-- TAB 2: 英語動画プレイヤー (再生回数カウンター付き) -->
    <!-- ============================================================ -->
    <div id="tab-video" class="tab-pane">
      <div class="hero-card">
        <div class="card-header">
          <div class="card-title">
            <span>🎬 イソップ寓話 全6級動画プレイヤー</span>
          </div>
          <span class="status-badge-chip pass" id="videoPlayCountBadge">再生回数: 0回</span>
        </div>

        <div style="display:flex; gap:12px; align-items:center; margin-bottom:14px; flex-wrap:wrap;">
          <label style="font-size:0.85rem; font-weight:700; color:var(--text-muted);">📖 お話を選択:</label>
          <select id="videoStorySelect" class="custom-select" style="flex-grow:1;" onchange="changeStory(this.value)"></select>
        </div>

        <div class="grade-tabs-bar" id="videoGradeTabsBar" style="display:flex; gap:8px; margin-bottom:14px; overflow-x:auto;">
          <button class="grade-chip" onclick="switchVideoGrade('Grade_4', this)">🥉 4級</button>
          <button class="grade-chip" onclick="switchVideoGrade('Grade_3', this)">🥈 3級</button>
          <button class="grade-chip active" onclick="switchVideoGrade('Grade_Pre2', this)">🥇 準2級 (目標)</button>
          <button class="grade-chip" onclick="switchVideoGrade('Grade_2', this)">🏆 2級</button>
          <button class="grade-chip" onclick="switchVideoGrade('Grade_Pre1', this)">👑 準1級</button>
          <button class="grade-chip" onclick="switchVideoGrade('Classic_Original', this)">🏛️ 原文</button>
        </div>

        <div style="width:100%; aspect-ratio:16/9; background:#000; border-radius:var(--radius-lg); overflow:hidden; margin-bottom:14px; border:1px solid var(--card-border);">
          <video id="sonVideoPlayer" controls playsinline poster="video_output/preview_v2.jpg" style="width:100%; height:100%; object-fit:contain;">
            <source id="sonVideoSource" src="video_output/chapter01_tortoise_and_hare/chapter01_Grade_Pre2.mp4" type="video/mp4">
          </video>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <div>
            <h3 id="currentPlayingTitle" style="font-size:1.05rem; font-weight:800;">Chapter 01: ウサギとカメ 【英検準2級】</h3>
            <p id="currentPlayingDesc" style="font-size:0.8rem; color:var(--text-muted); margin-top:2px;">高校初級・分詞構文・フォーマル構文 × 光るカラオケ字幕</p>
          </div>
          <a id="shortsLinkBtn" href="video_output/shorts_reels/chapter01_shorts_Grade4_9x16.mp4" target="_blank" class="btn-secondary" style="font-size:0.78rem; padding:6px 12px; color:var(--accent-rose); border-color:rgba(244,63,94,0.4);">
            <i data-lucide="smartphone"></i> 1分ショート (9:16)
          </a>
        </div>
      </div>
    </div>

    <!-- ============================================================ -->
    <!-- TAB 3: 英語ブックリーダー (赤シート＆朗読音声ON/OFF) -->
    <!-- ============================================================ -->
    <div id="tab-reader" class="tab-pane">
      
      <!-- Audio Reading Player Box -->
      <div class="audio-player-card">
        <div class="audio-controls-group">
          <button class="btn-audio-play" id="audioPlayPauseBtn" onclick="toggleAudioNarration()">
            <i data-lucide="play" id="audioIcon"></i>
          </button>
          <div>
            <div style="font-size:0.85rem; font-weight:800; color:#fff;" id="audioTrackTitle">朗読音声: Chapter 01 (英検準2級)</div>
            <div style="font-size:0.72rem; color:var(--text-muted);">本を見ながらネイティブの朗読音声を聴く（シャドーイング）</div>
          </div>
        </div>
        <audio id="readerAudioElement" src="video_output/chapter01_tortoise_and_hare/narration_Grade_Pre2.mp3"></audio>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
        <div class="grade-tabs-bar" id="readerGradeTabsBar" style="display:flex; gap:8px; overflow-x:auto;">
          <button class="grade-chip" onclick="switchReaderGrade('Grade_4', this)">🥉 4級</button>
          <button class="grade-chip" onclick="switchReaderGrade('Grade_3', this)">🥈 3級</button>
          <button class="grade-chip active" onclick="switchReaderGrade('Grade_Pre2', this)">🥇 準2級本文</button>
          <button class="grade-chip" onclick="switchReaderGrade('Grade_2', this)">🏆 2級</button>
          <button class="grade-chip" onclick="switchReaderGrade('Grade_Pre1', this)">👑 準1級</button>
          <button class="grade-chip" onclick="switchReaderGrade('Classic_Original', this)">🏛️ 原文</button>
          <button class="grade-chip" onclick="switchReaderGrade('vocab', this)" style="background:rgba(217,4,41,0.15); color:#ff4d6d; border-color:rgba(217,4,41,0.4);">
            📝 単語・熟語・フレーズ集
          </button>
        </div>
        <button class="btn-red-sheet" id="redSheetButton" onclick="toggleRedSheetMode()">
          <i data-lucide="eye-off"></i> 🕶️ 暗記マスク (黒塗り)
        </button>
      </div>

      <div class="reader-box" id="readerContainer">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #e2e8f0; padding-bottom:12px; margin-bottom:16px;">
          <div>
            <h3 class="reader-story-title" id="readerTitleText" style="font-size:1.2rem; font-weight:800; color:#0f172a;">Chapter 01: The Tortoise and the Hare</h3>
            <span style="font-size:0.8rem; color:#64748b;" id="readerGradeBadge">英検準2級 レベル</span>
          </div>
          <span style="font-size:0.75rem; color:var(--accent-cyan); font-weight:700;">※暗記マスクON時は各単語をタップで答えを表示/非表示できます</span>
        </div>

        <div class="reader-text-body" id="readerTextContent"></div>
      </div>
    </div>

    <!-- ============================================================ -->
    <!-- TAB 4: お小遣い＆資産配分台帳 (Asset & Reward Ledger) -->
    <!-- ============================================================ -->
    <div id="tab-asset" class="tab-pane">
      <div class="hero-card">
        <div class="card-header">
          <div class="card-title">
            <span style="color:var(--accent-gold);"><i data-lucide="wallet"></i></span>
            <span>生涯お小遣い ＆ 投資信託 積立シミュレーション</span>
          </div>
        </div>

        <div class="allocation-grid" style="margin-bottom:24px;">
          <div class="alloc-card cash" style="padding:20px;">
            <div class="alloc-title"><i data-lucide="smartphone"></i> 今月の電子マネー受取予定額 (Suica/楽天Cash)</div>
            <div class="alloc-value" style="color:var(--accent-cyan);">￥<span id="ledgerMonthlyCash">0</span></div>
            <p style="font-size:0.75rem; color:var(--text-muted); margin-top:4px;">コンビニ・文房具・自分の楽しみに自由に利用</p>
          </div>
          <div class="alloc-card invest" style="padding:20px;">
            <div class="alloc-title"><i data-lucide="trending-up"></i> 今月の投資信託 積立投資額 (50%)</div>
            <div class="alloc-value" style="color:var(--accent-gold);">￥<span id="ledgerMonthlyInvest">0</span></div>
            <p style="font-size:0.75rem; color:var(--text-muted); margin-top:4px;">年利5%運用で高校・大学時に大きく成長！</p>
          </div>
        </div>

        <h4 style="font-size:0.95rem; font-weight:800; margin-bottom:12px;">📊 獲得履歴ログ</h4>
        <div id="historyLogList" style="display:flex; flex-direction:column; gap:8px;"></div>
      </div>
    </div>

  </main>

  <div class="toast" id="toastBox">メッセージ</div>

  <script>
    const ALL_STORIES = {stories_json};
    let currentStoryIdx = 0;
    let currentVideoGrade = 'Grade_Pre2';
    let currentReaderGrade = 'Grade_Pre2';
    let isRedSheetOn = false;
    let slackingDays = 0;

    // Task Pass State (All must be true for base mission)
    let taskState = {{
      wake: false,
      swing: false,
      kanji: false,
      english: false,
      extra1: false,
      extra2: false
    }};

    const GRADE_NAMES = {{
      Grade_4: '英検4級',
      Grade_3: '英検3級',
      Grade_Pre2: '英検準2級',
      Grade_2: '英検2級',
      Grade_Pre1: '英検準1級',
      Classic_Original: 'クラシック原文'
    }};

    /* Mock Gemini 10-Question Test Bank */
    const QUIZ_BANKS = {{
      kanji: [
        {{ q: '1. 「謙虚」の正しい読み方は？', opts: ['けんきょ', 'けんしょ', 'かんきょ', 'けんちょ'], ans: 0 }},
        {{ q: '2. 「責任をテンカする」の正しい漢字は？', opts: ['点火', '転嫁', '添加', '展開'], ans: 1 }},
        {{ q: '3. 「臨機オウヘン」の正しい漢字は？', opts: ['応変', '往変', '応偏', '欧変'], ans: 0 }},
        {{ q: '4. 「執着」の正しい読み方は？', opts: ['しゅうじゃく', 'しつちゃく', 'しゅうちょく', 'しつじゃく'], ans: 0 }},
        {{ q: '5. 「ユウエツ感に浸る」の正しい漢字は？', opts: ['優悦', '優越', '有越', '悠越'], ans: 1 }},
        {{ q: '6. 「矛盾」の対義語として最も適切なものは？', opts: ['整合', '摩擦', '反発', '衝突'], ans: 0 }},
        {{ q: '7. 「示唆する」の意味として正しいものは？', opts: ['それとなく知らせる', '厳しく叱る', '完全に証明する', '拒否する'], ans: 0 }},
        {{ q: '8. 「ショウシン証明」の正しい漢字は？', opts: ['正真正銘', '初心証明', '正身証明', '正真清明'], ans: 0 }},
        {{ q: '9. 「破綻」の正しい読み方は？', opts: ['はたん', 'はてい', 'はちん', 'はてん'], ans: 0 }},
        {{ q: '10. 「コウバイ意欲をそそる」の正しい漢字は？', opts: ['購買', '公売', '交配', '講買'], ans: 0 }}
      ],
      english: [
        {{ q: '1. "persuade" の意味として最も適切なものは？', opts: ['説得する', '延期する', '避ける', '要求する'], ans: 0 }},
        {{ q: '2. "participate in ~" と同じ意味のイディオムは？', opts: ['take part in', 'take care of', 'give up', 'look forward to'], ans: 0 }},
        {{ q: '3. "frequently" の意味は？', opts: ['頻繁に', 'めったに〜ない', 'ゆっくりと', '突然に'], ans: 0 }},
        {{ q: '4. "The weather was terrible; (___), we enjoyed the trip."', opts: ['nevertheless', 'because', 'unless', 'although'], ans: 0 }},
        {{ q: '5. "convenient" の対義語（反対語）は？', opts: ['inconvenient', 'disconvenient', 'unconvenient', 'nonconvenient'], ans: 0 }},
        {{ q: '6. "opportunity" の意味は？', opts: ['機会・チャンス', '困難', '責任', '結果'], ans: 0 }},
        {{ q: '7. "be supposed to do" の意味は？', opts: ['〜することになっている', '〜するのを好む', '〜するふりをする', '〜するのを拒む'], ans: 0 }},
        {{ q: '8. "exhausted" の意味として最も近いものは？', opts: ['extremely tired', 'very happy', 'quite hungry', 'a little angry'], ans: 0 }},
        {{ q: '9. "increase" の反意語は？', opts: ['decrease', 'improve', 'expand', 'remain'], ans: 0 }},
        {{ q: '10. "rely on ~" の同義語は？', opts: ['depend on', 'put off', 'look into', 'run out of'], ans: 0 }}
      ],
      extra1: [
        {{ q: '1. 一次関数 y = 2x + 3 の傾きは？', opts: ['2', '3', '5', '-2'], ans: 0 }},
        {{ q: '2. 一次関数 y = -3x + 6 の切片は？', opts: ['6', '-3', '2', '0'], ans: 0 }},
        {{ q: '3. 点(1, 4)を通り傾きが3の直線式は？', opts: ['y = 3x + 1', 'y = 3x + 4', 'y = 3x - 1', 'y = x + 3'], ans: 0 }},
        {{ q: '4. 2点(0, 2), (2, 6)を通る直線の傾きは？', opts: ['2', '4', '3', '1'], ans: 0 }},
        {{ q: '5. y = -2x + 4 で x = 3 のときの y の値は？', opts: ['-2', '2', '10', '-6'], ans: 0 }},
        {{ q: '6. y = ax + b で平行な2直線の条件は？', opts: ['傾き a が等しい', '切片 b が等しい', 'a と b の和が0', '傾きの積が1'], ans: 0 }},
        {{ q: '7. x軸と交わる点の座標で常に0になるのは？', opts: ['y座標', 'x座標', '傾き', '切片'], ans: 0 }},
        {{ q: '8. 連立方程式の解はグラフ上の何を表す？', opts: ['交点の座標', '切片の差', '傾きの平均', '面積'], ans: 0 }},
        {{ q: '9. yがxに比例するとき、切片bの値は？', opts: ['0', '1', '-1', '定まらない'], ans: 0 }},
        {{ q: '10. xの変域が 1 <= x <= 3 のとき y = 2x + 1 のyの変域は？', opts: ['3 <= y <= 7', '2 <= y <= 6', '1 <= y <= 3', '4 <= y <= 8'], ans: 0 }}
      ],
      extra2: [
        {{ q: '1. 電流の単位はどれ？', opts: ['A (アンペア)', 'V (ボルト)', 'Ω (オーム)', 'W (ワット)'], ans: 0 }},
        {{ q: '2. オームの法則を表す正しい式は？', opts: ['電圧 = 電流 × 抵抗', '電流 = 電圧 × 抵抗', '抵抗 = 電圧 × 電流', '電圧 = 電流 ÷ 抵抗'], ans: 0 }},
        {{ q: '3. 直列回路において、各部分を流れる電流の強さは？', opts: ['どこでも等しい', '抵抗が大きいほど強い', '電源に近いほど強い', '足し算になる'], ans: 0 }},
        {{ q: '4. 並列回路において、各抵抗にかかる電圧は？', opts: ['すべて等しい', '抵抗の比に比例する', '電源電圧の半分', 'ゼロになる'], ans: 0 }},
        {{ q: '5. 10Ωの抵抗に2Aの電流を流すとき、電圧は何V？', opts: ['20V', '5V', '12V', '0.2V'], ans: 0 }},
        {{ q: '6. 100Vで500Wの電気製品に流れる電流は何A？', opts: ['5A', '50A', '0.2A', '2A'], ans: 0 }},
        {{ q: '7. 磁界の向きは、方位磁針のどちらの極が指す向き？', opts: ['N極', 'S極', '東', '西'], ans: 0 }},
        {{ q: '8. コイルの中の磁界を変化させると電流が流れる現象は？', opts: ['電磁誘導', '静電気', '放電', 'ジュール熱'], ans: 0 }},
        {{ q: '9. 右手の法則で親指が表す向きは？', opts: ['電流の向き', '磁界の向き', '力の向き', '電子の向き'], ans: 0 }},
        {{ q: '10. 電流による発熱量(J)を求める式は？', opts: ['電力(W) × 時間(秒)', '電圧(V) × 電流(A)', '抵抗(Ω) × 時間(秒)', '電力(W) ÷ 60'], ans: 0 }}
      ]
    }};

    let quizState = {{
      currentSubject: '',
      currentIdx: 0,
      score: 0
    }};

    function initApp() {{
      // Set Date
      const now = new Date();
      const dStr = `${{now.getFullYear()}}/${{now.getMonth() + 1}}/${{now.getDate()}} (${{['日','月','火','水','木','金','土'][now.getDay()]}})`;
      
      // Populate Story Select
      const vSelect = document.getElementById('videoStorySelect');
      vSelect.innerHTML = '';
      ALL_STORIES.forEach((s, idx) => {{
        const opt = document.createElement('option');
        opt.value = idx;
        opt.innerText = `第${{s.chapter}}話: ${{s.titleJa}} (${{s.titleEn}})`;
        vSelect.appendChild(opt);
      }});

      // Load Saved State
      loadSavedState();

      // Video Event
      const player = document.getElementById('sonVideoPlayer');
      player.onended = () => {{
        incrementPlayCount(currentStoryIdx);
      }};

      updateStoryView();
      calculateDailyReward();
      lucide.createIcons();
    }}

    function switchMainTab(tabId) {{
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab-btn').forEach(el => el.classList.remove('active'));

      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.add('active');

      const btnIdx = ['quest', 'video', 'reader', 'asset'].indexOf(tabId);
      if (btnIdx >= 0) {{
        document.querySelectorAll('.nav-tab-btn')[btnIdx].classList.add('active');
      }}

      if (tabId === 'asset') renderHistoryList();
      lucide.createIcons();
    }}

    /* ============================================================
       Penalty Multiplier Logic (サボり減額ルール)
    ============================================================ */
    function updatePenaltyMultiplier(val) {{
      slackingDays = parseInt(val);
      const banner = document.getElementById('penaltyStatusBanner');
      const text = document.getElementById('penaltyMultiplierText');
      const desc = document.getElementById('penaltyDescText');

      banner.className = 'penalty-banner';
      if (slackingDays === 0) {{
        banner.classList.add('normal');
        text.innerText = '通常受取: 100% (満額)';
        desc.innerText = '連続達成中！サボりなしで翌朝報告すれば全額GET！';
      }} else if (slackingDays === 1) {{
        banner.classList.add('warn1');
        text.innerText = '⚠️ 1日サボり: 50% (1/2 減額)';
        desc.innerText = '翌日クリアで回復します（都合2日分減額）';
      }} else if (slackingDays === 2) {{
        banner.classList.add('warn2');
        text.innerText = '🚨 2日連続サボり: 25% (1/4 減額)';
        desc.innerText = '回復に4日間の連続クリアが必要です';
      }} else if (slackingDays === 3) {{
        banner.classList.add('warn2');
        text.innerText = '💥 3日連続サボり: 12.5% (1/8 減額)';
        desc.innerText = '大幅減額中！早く日課をこなして立て直そう！';
      }} else {{
        banner.classList.add('danger');
        text.innerText = '⚡ 4日以上サボり: 6.25% (1/16 減額 ＋ 親の雷⚡)';
        desc.innerText = '親からの雷が落ちます！直ちに報告してください！';
      }}

      calculateDailyReward();
    }}

    function getMultiplier() {{
      if (slackingDays === 0) return 1.0;
      if (slackingDays === 1) return 0.5;
      if (slackingDays === 2) return 0.25;
      if (slackingDays === 3) return 0.125;
      return 0.0625;
    }}

    /* ============================================================
       Quiz AI Test Logic (Gemini 10問テスト)
    ============================================================ */
    function startAiQuiz(subject) {{
      quizState.currentSubject = subject;
      quizState.currentIdx = 0;
      quizState.score = 0;

      const quizBox = document.getElementById(`quiz_box_${{subject}}`);
      quizBox.style.display = 'block';
      renderQuizQuestion();
    }}

    function renderQuizQuestion() {{
      const sub = quizState.currentSubject;
      const bank = QUIZ_BANKS[sub] || QUIZ_BANKS['kanji'];
      const qObj = bank[quizState.currentIdx];

      const progEl = document.getElementById(`quiz_progress_${{sub}}`);
      const qTextEl = document.getElementById(`quiz_q_${{sub}}`);
      const optsEl = document.getElementById(`quiz_opts_${{sub}}`);

      progEl.innerText = `問 ${{quizState.currentIdx + 1}} / 10 (現在正解: ${{quizState.score}}問)`;
      qTextEl.innerText = qObj.q;
      optsEl.innerHTML = '';

      qObj.opts.forEach((opt, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'quiz-opt-btn';
        btn.innerText = `${{['A', 'B', 'C', 'D'][idx]}}. ${{opt}}`;
        btn.onclick = () => handleQuizAnswer(idx, qObj.ans, btn);
        optsEl.appendChild(btn);
      }});
    }}

    function handleQuizAnswer(selectedIdx, correctIdx, btn) {{
      const sub = quizState.currentSubject;
      const opts = document.querySelectorAll(`#quiz_opts_${{sub}} .quiz-opt-btn`);
      opts.forEach(b => b.disabled = true);

      if (selectedIdx === correctIdx) {{
        btn.classList.add('selected-correct');
        quizState.score++;
        showToast('正解！ ⭕');
      }} else {{
        btn.classList.add('selected-wrong');
        opts[correctIdx].classList.add('selected-correct');
        showToast('不正解... ❌');
      }}

      setTimeout(() => {{
        quizState.currentIdx++;
        const bank = QUIZ_BANKS[sub] || QUIZ_BANKS['kanji'];
        if (quizState.currentIdx < bank.length) {{
          renderQuizQuestion();
        }} else {{
          finishQuiz();
        }}
      }}, 1200);
    }}

    function finishQuiz() {{
      const sub = quizState.currentSubject;
      const quizBox = document.getElementById(`quiz_box_${{sub}}`);
      const badge = document.getElementById(`badge_${{sub}}`);
      const isPassed = (quizState.score >= 8); // 8問以上で合格

      if (isPassed) {{
        taskState[sub] = true;
        badge.className = 'status-badge-chip pass';
        badge.innerText = `合格 ⭕ (${{quizState.score}}/10問)`;
        quizBox.innerHTML = `
          <div style="text-align:center; padding:16px;">
            <div style="font-size:1.4rem; font-weight:900; color:var(--accent-green);">🎉 合格おめでとう！ (${{quizState.score}}/10問正解)</div>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-top:6px;">ミッションクリア条件を達成しました！</p>
          </div>
        `;
        showToast('🎉 10問テスト合格！クリア認定！');
      }} else {{
        taskState[sub] = false;
        badge.className = 'status-badge-chip pending';
        badge.innerText = `不合格 (${{quizState.score}}/10問)`;
        quizBox.innerHTML = `
          <div style="text-align:center; padding:16px;">
            <div style="font-size:1.1rem; font-weight:800; color:var(--accent-red);">❌ 不合格 (${{quizState.score}}/10問 - 合格基準8問)</div>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">もう一度復習して再挑戦しよう！</p>
            <button class="btn-ai-test" style="margin-top:10px;" onclick="startAiQuiz('${{sub}}')">再挑戦する</button>
          </div>
        `;
        showToast('8問未満のため不合格です。再挑戦してください');
      }}

      calculateDailyReward();
      saveCurrentState();
    }}

    function toggleTaskManual(key, isChecked) {{
      taskState[key] = isChecked;
      const badge = document.getElementById(`badge_${{key}}`);
      if (badge) {{
        if (isChecked) {{
          badge.className = 'status-badge-chip pass';
          badge.innerText = '達成 ⭕';
        }} else {{
          badge.className = 'status-badge-chip';
          badge.innerText = '未達';
        }}
      }}
      calculateDailyReward();
      saveCurrentState();
    }}

    /* ============================================================
       Reward Calculation & Split Allocation (50:50)
    ============================================================ */
    function calculateDailyReward() {{
      let rawTotal = 0;

      // Base 4 Tasks
      const isBaseDone = (taskState.wake && taskState.swing && taskState.kanji && taskState.english);
      const baseBadge = document.getElementById('baseMissionProgressBadge');
      
      const doneCount = (taskState.wake ? 1 : 0) + (taskState.swing ? 1 : 0) + (taskState.kanji ? 1 : 0) + (taskState.english ? 1 : 0);
      if (isBaseDone) {{
        rawTotal += 350;
        baseBadge.innerText = '🎉 完全達成 (4/4) ￥350';
        baseBadge.className = 'status-badge-chip pass';
      }} else {{
        baseBadge.innerText = `進行中 (${{doneCount}}/4)`;
        baseBadge.className = 'status-badge-chip pending';
      }}

      // Extra Subjects
      if (taskState.extra1) rawTotal += 100;
      if (taskState.extra2) rawTotal += 100;

      // Special Bonus
      const specialAmt = parseInt(document.getElementById('special_amount_input').value) || 0;
      if (specialAmt > 0) rawTotal += specialAmt;

      // Apply Penalty Multiplier
      const mult = getMultiplier();
      const finalTotal = Math.floor(rawTotal * mult);

      // Split 50% Cash / 50% Investment
      const cashPart = Math.floor(finalTotal / 2);
      const investPart = finalTotal - cashPart;

      document.getElementById('rawTotalDisplay').innerText = `￥${{rawTotal.toLocaleString()}}`;
      document.getElementById('finalTotalDisplay').innerText = `￥${{finalTotal.toLocaleString()}}`;
      document.getElementById('allocCashDisplay').innerText = cashPart.toLocaleString();
      document.getElementById('allocInvestDisplay').innerText = investPart.toLocaleString();

      return {{ raw: rawTotal, final: finalTotal, cash: cashPart, invest: investPart }};
    }}

    function generateLineReportText() {{
      const now = new Date();
      const dStr = `${{now.getFullYear()}}/${{now.getMonth() + 1}}/${{now.getDate()}}`;
      const calc = calculateDailyReward();
      const isBaseDone = (taskState.wake && taskState.swing && taskState.kanji && taskState.english);

      const swingText = document.getElementById('swing_count_input').value || '100回';
      const specialReason = document.getElementById('special_reason_input').value || '';
      const specialAmt = parseInt(document.getElementById('special_amount_input').value) || 0;

      let msg = `【今日の学習＆日課 完了報告】📅 ${{dStr}}\\n\\n`;
      msg += `⚡ サボり判定: ${{slackingDays === 0 ? 'サボりなし (100% 満額)' : `${{slackingDays}}日サボり (${{getMultiplier() * 100}}% 適用)`}}\\n\\n`;
      msg += `👑 義務ミッション: ${{isBaseDone ? '【完全合格】(￥350)' : '【未完了】'}}\\n`;
      msg += `・⏰ 朝5時起床: ${{taskState.wake ? '達成 ⭕' : '未達 ❌'}}\\n`;
      msg += `・⚾ 素振り: ${{taskState.swing ? `${{swingText}} 達成 ⭕` : '未達 ❌'}}\\n`;
      msg += `・✍️ 漢検準2級 (見開き2P): ${{taskState.kanji ? '10問テスト合格 ⭕' : '未合格 ❌'}}\\n`;
      msg += `・🎧 英検準2級 単語帳: ${{taskState.english ? '10問テスト合格 ⭕' : '未合格 ❌'}}\\n\\n`;

      if (taskState.extra1 || taskState.extra2) {{
        msg += `🌟 追加教科ボーナス:\\n`;
        if (taskState.extra1) msg += `・教科①: 10問テスト合格 (+￥100)\\n`;
        if (taskState.extra2) msg += `・教科②: 10問テスト合格 (+￥100)\\n`;
        msg += `\\n`;
      }}

      if (specialAmt > 0 && specialReason) {{
        msg += `✨ 特別自己申告ボーナス (+￥${{specialAmt}}):\\n`;
        msg += `・理由: ${{specialReason}}\\n\\n`;
      }}

      msg += `━━━━━━━━━━━━━━━━\\n`;
      msg += `💰 額面合計: ￥${{calc.raw.toLocaleString()}}\\n`;
      msg += `🔥 本日の実受取額: ￥${{calc.final.toLocaleString()}}\\n`;
      msg += `・📱 Suica/楽天Cash: ￥${{calc.cash.toLocaleString()}} (50%)\\n`;
      msg += `・📈 投資信託積立: ￥${{calc.invest.toLocaleString()}} (50%)\\n`;
      msg += `━━━━━━━━━━━━━━━━\\n`;
      msg += `明日も朝5時起きでがんばります！`;

      return msg;
    }}

    function submitToLine() {{
      const text = generateLineReportText();
      const lineUrl = `https://line.me/R/msg/text/?${{encodeURIComponent(text.replace(/\\\\n/g, '\\n'))}}`;
      
      // Save entry to ledger
      const calc = calculateDailyReward();
      if (calc.final > 0) {{
        const history = JSON.parse(localStorage.getItem('son_reward_history') || '[]');
        const now = new Date();
        history.unshift({{
          date: `${{now.getFullYear()}}/${{now.getMonth() + 1}}/${{now.getDate()}}`,
          amount: calc.final,
          cash: calc.cash,
          invest: calc.invest,
          detail: text.replace(/\\\\n/g, ' / ')
        }});
        localStorage.setItem('son_reward_history', JSON.stringify(history));
      }}

      window.open(lineUrl, '_blank');
      showToast('LINEアプリを起動します！');
    }}

    /* ============================================================
       Video & Audio Reader Logic
    ============================================================ */
    function changeStory(idx) {{
      currentStoryIdx = parseInt(idx);
      updateStoryView();
    }}

    function updateStoryView() {{
      const story = ALL_STORIES[currentStoryIdx];
      const chStr = story.chapter < 10 ? '0' + story.chapter : story.chapter;
      
      // Video
      const videoSrc = `video_output/chapter${{chStr}}_${{story.key}}/chapter${{chStr}}_${{currentVideoGrade}}.mp4`;
      const player = document.getElementById('sonVideoPlayer');
      const source = document.getElementById('sonVideoSource');
      source.src = videoSrc;
      player.load();

      document.getElementById('currentPlayingTitle').innerText = `Chapter ${{chStr}}: ${{story.titleJa}} 【${{GRADE_NAMES[currentVideoGrade] || currentVideoGrade}}】`;
      
      // Play Count
      const count = getPlayCount(currentStoryIdx);
      document.getElementById('videoPlayCountBadge').innerText = `再生回数: ${{count}}回`;

      // Audio in Reader
      const audioEl = document.getElementById('readerAudioElement');
      audioEl.src = `video_output/chapter${{chStr}}_${{story.key}}/narration_${{currentReaderGrade === 'vocab' ? 'Grade_Pre2' : currentReaderGrade}}.mp3`;
      document.getElementById('audioTrackTitle').innerText = `朗読音声: Chapter ${{chStr}} (${{GRADE_NAMES[currentReaderGrade] || '準2級'}})`;

      updateReaderContent();
    }}

    function switchVideoGrade(gradeKey, btn) {{
      currentVideoGrade = gradeKey;
      document.querySelectorAll('#videoGradeTabsBar .grade-chip').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      updateStoryView();
      document.getElementById('sonVideoPlayer').play();
    }}

    function switchReaderGrade(gradeKey, btn) {{
      currentReaderGrade = gradeKey;
      document.querySelectorAll('#readerGradeTabsBar .grade-chip').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      const story = ALL_STORIES[currentStoryIdx];
      const chStr = story.chapter < 10 ? '0' + story.chapter : story.chapter;
      const audioEl = document.getElementById('readerAudioElement');
      audioEl.src = `video_output/chapter${{chStr}}_${{story.key}}/narration_${{gradeKey === 'vocab' ? 'Grade_Pre2' : gradeKey}}.mp3`;
      document.getElementById('audioTrackTitle').innerText = `朗読音声: Chapter ${{chStr}} (${{GRADE_NAMES[gradeKey] || '準2級'}})`;

      updateReaderContent();
    }}

    function updateReaderContent() {{
      const story = ALL_STORIES[currentStoryIdx];
      const chStr = story.chapter < 10 ? '0' + story.chapter : story.chapter;
      
      document.getElementById('readerTitleText').innerText = `Chapter ${{chStr}}: ${{story.titleJa}} (${{story.titleEn}})`;
      document.getElementById('readerGradeBadge').innerText = GRADE_NAMES[currentReaderGrade] || '重要単語・熟語表';

      const contentBox = document.getElementById('readerTextContent');
      if (currentReaderGrade === 'vocab') {{
        const rawVocab = story.texts.vocab || '';
        contentBox.innerHTML = `<div class="vocab-table-container">${{renderMarkdownTable(rawVocab)}}</div>`;
      }} else {{
        contentBox.innerText = story.texts[currentReaderGrade] || '本文データを読み込み中...';
      }}
    }}

    function toggleAudioNarration() {{
      const audioEl = document.getElementById('readerAudioElement');
      const icon = document.getElementById('audioIcon');
      if (audioEl.paused) {{
        audioEl.play();
        icon.setAttribute('data-lucide', 'pause');
        showToast('朗読音声を再生中');
      }} else {{
        audioEl.pause();
        icon.setAttribute('data-lucide', 'play');
        showToast('朗読音声を一時停止');
      }}
      lucide.createIcons();
    }}

    function toggleRedSheetMode() {{
      isRedSheetOn = !isRedSheetOn;
      const btn = document.getElementById('redSheetButton');
      const container = document.getElementById('readerContainer');
      if (isRedSheetOn) {{
        container.classList.add('red-mask-active');
        btn.classList.add('active');
        btn.innerHTML = '<i data-lucide="eye"></i> 🕶️ 暗記マスク ON中';
        showToast('🕶️ 暗記マスクON！タップで個別確認できます');
      }} else {{
        container.classList.remove('red-mask-active');
        btn.classList.remove('active');
        btn.innerHTML = '<i data-lucide="eye-off"></i> 🕶️ 暗記マスク (黒塗り)';
        showToast('暗記マスクを解除しました');
      }}
      lucide.createIcons();
    }}

    function renderMarkdownTable(mdText) {{
      const lines = mdText.split('\\n').filter(l => l.trim().startsWith('|'));
      if (lines.length < 2) return '<p>単語表データは準備中です</p>';
      
      let html = '<table>';
      lines.forEach((line, idx) => {{
        if (line.includes('---')) return;
        const cells = line.split('|').slice(1, -1).map(c => c.trim());
        if (idx === 0) {{
          html += '<thead><tr>' + cells.map(c => `<th>${{c}}</th>`).join('') + '</tr></thead><tbody>';
        }} else {{
          html += '<tr>' + cells.map((c, i) => `<td class="${{i === 1 ? 'vocab-red' : ''}}" onclick="this.classList.toggle('revealed')">${{c}}</td>`).join('') + '</tr>';
        }}
      }});
      html += '</tbody></table>';
      return html;
    }}

    /* Play Counter */
    function getPlayCount(storyIdx) {{
      const counts = JSON.parse(localStorage.getItem('son_play_counts') || '{{}}');
      return counts[storyIdx] || 0;
    }}

    function incrementPlayCount(storyIdx) {{
      const counts = JSON.parse(localStorage.getItem('son_play_counts') || '{{}}');
      counts[storyIdx] = (counts[storyIdx] || 0) + 1;
      localStorage.setItem('son_play_counts', JSON.stringify(counts));
      document.getElementById('videoPlayCountBadge').innerText = `再生回数: ${{counts[storyIdx]}}回`;
    }}

    /* Persistence & PWA Guide */
    function saveCurrentState() {{
      localStorage.setItem('son_task_state_v2', JSON.stringify(taskState));
    }}

    function loadSavedState() {{
      const saved = localStorage.getItem('son_task_state_v2');
      if (saved) {{
        try {{
          taskState = JSON.parse(saved);
          if (taskState.wake) document.getElementById('chk_wake').checked = true;
          if (taskState.swing) document.getElementById('chk_swing').checked = true;
        }} catch(e) {{}}
      }}
    }}

    function renderHistoryList() {{
      const listEl = document.getElementById('historyLogList');
      const history = JSON.parse(localStorage.getItem('son_reward_history') || '[]');
      
      let mCash = 0;
      let mInvest = 0;
      const curM = new Date().getMonth() + 1;

      history.forEach(item => {{
        const m = parseInt(item.date.split('/')[1]);
        if (m === curM) {{
          mCash += (item.cash || Math.floor(item.amount / 2));
          mInvest += (item.invest || Math.ceil(item.amount / 2));
        }}
      }});

      document.getElementById('ledgerMonthlyCash').innerText = mCash.toLocaleString();
      document.getElementById('ledgerMonthlyInvest').innerText = mInvest.toLocaleString();

      if (history.length === 0) {{
        listEl.innerHTML = '<p style="color:var(--text-muted); text-align:center; padding:16px;">まだ獲得履歴はありません</p>';
        return;
      }}
      listEl.innerHTML = '';
      history.slice(0, 15).forEach(item => {{
        const div = document.createElement('div');
        div.style = "background:rgba(11,17,32,0.6); border:1px solid var(--card-border); border-radius:var(--radius-md); padding:10px 14px; display:flex; justify-content:space-between; align-items:center;";
        div.innerHTML = `
          <div>
            <div style="font-weight:700; font-size:0.82rem; color:#fff;">📅 ${{item.date}}</div>
            <div style="font-size:0.72rem; color:var(--text-muted); margin-top:2px;">Suica: ￥${{(item.cash || Math.floor(item.amount/2)).toLocaleString()}} / 投信: ￥${{(item.invest || Math.ceil(item.amount/2)).toLocaleString()}}</div>
          </div>
          <div style="font-family:'Outfit', sans-serif; font-weight:900; font-size:1.1rem; color:var(--accent-gold);">+￥${{item.amount.toLocaleString()}}</div>
        `;
        listEl.appendChild(div);
      }});
    }}

    function showPwaGuide() {{
      alert('【📱 スマホのアプリ化（ショートカット作成方法）】\\n\\n1. iPhoneの場合 (Safari):\\n画面下の「共有ボタン（四角から上矢印）」をタップ ➔「ホーム画面に追加」を選択。\\n\\n2. Androidの場合 (Chrome):\\n画面右上の「︙（メニュー）」をタップ ➔「ホーム画面に追加」または「アプリをインストール」を選択。\\n\\nこれでホーム画面にアイコンが作成され、全画面アプリとして起動できます！');
    }}

    function showToast(msg) {{
      const t = document.getElementById('toastBox');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{ t.classList.remove('show'); }}, 2500);
    }}

    function initApp() {{
      if (typeof APP_VERSION !== 'undefined') {{
        const badge = document.getElementById('appVerBadge');
        if (badge) badge.innerText = `v${{APP_VERSION}}`;
      }}
      loadSavedState();
      calculateDailyReward();
      lucide.createIcons();
    }}

    window.onload = initApp;
  </script>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Also save as index.html for root deployment
    INDEX_HTML = os.path.join(BASE_DIR, "index.html")
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"🎉 Enhanced Son's Custom Learning Portal Generated Successfully:")
    print(f"   - {OUTPUT_HTML}")
    print(f"   - {INDEX_HTML}")

if __name__ == "__main__":
    generate_portal_html()


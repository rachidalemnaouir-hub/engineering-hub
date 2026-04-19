DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-base:        #050811;
    --bg-card:        rgba(255,255,255,0.04);
    --bg-card-hover:  rgba(255,255,255,0.07);
    --bg-input:       rgba(255,255,255,0.05);
    --bg-sidebar:     #060b17;
    --blue:           #4D9FFF;
    --blue-glow:      rgba(77,159,255,0.35);
    --cyan:           #00D4FF;
    --cyan-glow:      rgba(0,212,255,0.3);
    --purple:         #A855F7;
    --green:          #10F5A0;
    --green-glow:     rgba(16,245,160,0.25);
    --orange:         #FF8C42;
    --red:            #FF4D6A;
    --red-glow:       rgba(255,77,106,0.3);
    --text-primary:   #EDF2FF;
    --text-secondary: #8899BB;
    --text-muted:     #3D5070;
    --border:         rgba(255,255,255,0.07);
    --border-hover:   rgba(77,159,255,0.4);
    --border-active:  rgba(77,159,255,0.7);
    --radius-xl: 20px; --radius-lg: 14px; --radius-md: 10px; --radius-sm: 7px;
    --shadow: 0 8px 32px rgba(0,0,0,0.4), 0 1px 0 rgba(255,255,255,0.05) inset;
    --t: all 0.25s cubic-bezier(0.4,0,0.2,1);
}

*, *::before, *::after { font-family: 'Inter', sans-serif !important; box-sizing: border-box; }
code, pre, .stCode { font-family: 'JetBrains Mono', monospace !important; }

.stApp {
    background: var(--bg-base) !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% 10%, rgba(77,159,255,0.06) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(168,85,247,0.05) 0%, transparent 50%) !important;
    color: var(--text-primary) !important;
    min-height: 100vh;
}
.main .block-container { background: transparent !important; padding: 2rem 2.5rem !important; max-width: 1280px !important; }

[data-testid="stSidebar"] { background: var(--bg-sidebar) !important; border-right: 1px solid var(--border) !important; }
[data-testid="stSidebar"] > div { background: transparent !important; }
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }
[data-testid="stSidebar"] p { color: var(--text-muted) !important; }

div[data-testid="stRadio"] > label { color: var(--text-muted) !important; font-size: 0.65rem !important; font-weight: 700 !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; margin-bottom: 0.5rem !important; }
div[data-testid="stRadio"] div[role="radiogroup"] { gap: 0.25rem !important; flex-direction: column !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label { background: transparent !important; border: 1px solid var(--border) !important; border-radius: var(--radius-md) !important; padding: 0.6rem 1rem !important; color: var(--text-secondary) !important; font-size: 0.875rem !important; font-weight: 500 !important; text-transform: none !important; letter-spacing: 0 !important; transition: var(--t) !important; cursor: pointer !important; width: 100% !important; margin-bottom: 0.25rem !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label:hover { background: var(--bg-card-hover) !important; border-color: var(--border-hover) !important; color: var(--text-primary) !important; transform: translateX(4px) !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) { background: linear-gradient(135deg, rgba(77,159,255,0.15), rgba(168,85,247,0.1)) !important; border-color: var(--border-active) !important; color: var(--blue) !important; font-weight: 600 !important; box-shadow: 0 0 20px rgba(77,159,255,0.1) !important; }
div[data-testid="stRadio"] div[role="radiogroup"] input[type="radio"] { display: none !important; }

.stButton > button { background: linear-gradient(135deg, var(--blue), var(--purple)) !important; color: #fff !important; border: none !important; border-radius: var(--radius-md) !important; font-weight: 600 !important; font-size: 0.875rem !important; padding: 0.55rem 1.5rem !important; transition: var(--t) !important; box-shadow: 0 4px 15px var(--blue-glow) !important; position: relative !important; overflow: hidden !important; }
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 25px var(--blue-glow) !important; }
.stButton > button[kind="secondary"] { background: var(--bg-card) !important; border: 1px solid var(--border) !important; color: var(--text-secondary) !important; box-shadow: none !important; }
.stButton > button[kind="secondary"]:hover { border-color: var(--red) !important; color: var(--red) !important; box-shadow: 0 0 15px var(--red-glow) !important; background: rgba(255,77,106,0.05) !important; transform: none !important; }

.stTextInput > div > div > input,
.stTextArea > div > div > textarea { background: var(--bg-input) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-md) !important; color: var(--text-primary) !important; font-size: 0.9rem !important; transition: var(--t) !important; padding: 0.6rem 0.9rem !important; }
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus { border-color: var(--blue) !important; box-shadow: 0 0 0 3px var(--blue-glow), 0 0 20px rgba(77,159,255,0.1) !important; background: rgba(77,159,255,0.04) !important; outline: none !important; }
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder { color: var(--text-muted) !important; }

label[data-testid="stWidgetLabel"] p { color: var(--text-muted) !important; font-size: 0.7rem !important; font-weight: 700 !important; letter-spacing: 0.12em !important; text-transform: uppercase !important; }

div[data-testid="stSelectbox"] > div > div { background: var(--bg-input) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-md) !important; color: var(--text-primary) !important; transition: var(--t) !important; }
div[data-testid="stSelectbox"] > div > div:hover { border-color: var(--border-hover) !important; }
div[data-testid="stSelectbox"] > div > div > div { color: var(--text-primary) !important; background: transparent !important; }

div[data-testid="stTabs"] { border-bottom: 1px solid var(--border) !important; margin-bottom: 1.5rem !important; }
div[data-testid="stTabs"] button { background: transparent !important; color: var(--text-muted) !important; border: none !important; border-bottom: 2px solid transparent !important; font-weight: 600 !important; font-size: 0.875rem !important; padding: 0.6rem 1.2rem !important; transition: var(--t) !important; }
div[data-testid="stTabs"] button:hover { color: var(--text-secondary) !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color: var(--blue) !important; border-bottom-color: var(--blue) !important; }

details { background: var(--bg-card) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-lg) !important; margin-bottom: 0.75rem !important; transition: var(--t) !important; backdrop-filter: blur(10px) !important; box-shadow: var(--shadow) !important; }
details:hover { border-color: var(--border-hover) !important; }
details[open] { border-color: rgba(77,159,255,0.3) !important; }
details summary { color: var(--text-primary) !important; font-weight: 600 !important; font-size: 0.9rem !important; padding: 1rem 1.2rem !important; cursor: pointer !important; list-style: none !important; }
details > div { padding: 0 1.2rem 1.2rem !important; }

div[data-testid="stDateInput"] input { background: var(--bg-input) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-md) !important; color: var(--text-primary) !important; }

div[data-testid="metric-container"] { background: var(--bg-card) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-lg) !important; padding: 1.25rem !important; backdrop-filter: blur(10px) !important; box-shadow: var(--shadow) !important; transition: var(--t) !important; }
div[data-testid="metric-container"]:hover { border-color: var(--border-hover) !important; transform: translateY(-2px) !important; }
div[data-testid="metric-container"] [data-testid="stMetricLabel"] { color: var(--text-muted) !important; font-size: 0.7rem !important; font-weight: 700 !important; letter-spacing: 0.1em !important; text-transform: uppercase !important; }
div[data-testid="metric-container"] [data-testid="stMetricValue"] { color: var(--text-primary) !important; font-size: 1.8rem !important; font-weight: 800 !important; }

div[data-testid="stProgressBar"] > div { background: rgba(255,255,255,0.06) !important; border-radius: 99px !important; height: 6px !important; }
div[data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg, var(--blue), var(--cyan)) !important; border-radius: 99px !important; box-shadow: 0 0 10px var(--cyan-glow) !important; }

div[data-testid="stForm"] .stButton > button { width: 100% !important; padding: 0.75rem !important; font-size: 0.9rem !important; font-weight: 700 !important; }

::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(77,159,255,0.2); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--blue); }
hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 1.5rem 0 !important; }

/* ── CUSTOM CLASSES ── */
.page-icon { font-size: 2.5rem; margin-bottom: 0.5rem; filter: drop-shadow(0 0 20px rgba(77,159,255,0.4)); }
.page-title { font-size: 2.2rem; font-weight: 900; background: linear-gradient(135deg, #fff 0%, var(--blue) 50%, var(--cyan) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1.1; margin: 0 0 0.4rem 0; letter-spacing: -0.02em; }
.page-subtitle { color: var(--text-muted); font-size: 0.875rem; margin-bottom: 2rem; }

.section-label { font-size: 0.65rem; font-weight: 800; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-muted); display: flex; align-items: center; gap: 0.6rem; margin: 2rem 0 1rem 0; padding-bottom: 0.6rem; border-bottom: 1px solid var(--border); }
.section-label::before { content: ''; width: 16px; height: 2px; background: linear-gradient(90deg, var(--blue), var(--cyan)); border-radius: 99px; flex-shrink: 0; }

.brand-wrap { padding: 1.5rem 1.2rem 1rem; border-bottom: 1px solid var(--border); margin-bottom: 1rem; }
.brand-logo { font-size: 1.4rem; font-weight: 900; background: linear-gradient(135deg, var(--blue), var(--cyan)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: -0.02em; }
.brand-sub { font-size: 0.65rem !important; font-weight: 600 !important; letter-spacing: 0.15em !important; color: var(--text-muted) !important; text-transform: uppercase !important; margin-top: 0.3rem !important; }

.badge { display: inline-flex; align-items: center; padding: 0.2rem 0.65rem; border-radius: 99px; font-size: 0.68rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.badge-blue   { background: rgba(77,159,255,0.12);  color: #4D9FFF; border: 1px solid rgba(77,159,255,0.25); }
.badge-cyan   { background: rgba(0,212,255,0.1);    color: #00D4FF; border: 1px solid rgba(0,212,255,0.25); }
.badge-green  { background: rgba(16,245,160,0.1);   color: #10F5A0; border: 1px solid rgba(16,245,160,0.25); }
.badge-orange { background: rgba(255,140,66,0.12);  color: #FF8C42; border: 1px solid rgba(255,140,66,0.25); }
.badge-purple { background: rgba(168,85,247,0.12);  color: #A855F7; border: 1px solid rgba(168,85,247,0.25); }
.badge-red    { background: rgba(255,77,106,0.1);   color: #FF4D6A; border: 1px solid rgba(255,77,106,0.25); }

.kanban-col { background: rgba(255,255,255,0.02); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1rem; min-height: 180px; }
.col-todo { border-top: 2px solid #FF8C42; }
.col-doing { border-top: 2px solid #4D9FFF; }
.col-done { border-top: 2px solid #10F5A0; }
.kanban-col-header { font-size: 0.65rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; padding-bottom: 0.75rem; margin-bottom: 0.75rem; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 0.4rem; }
.col-todo .kanban-col-header { color: #FF8C42; }
.col-doing .kanban-col-header { color: #4D9FFF; }
.col-done .kanban-col-header { color: #10F5A0; }
.kanban-item { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 0.6rem 0.8rem; margin-bottom: 0.5rem; font-size: 0.82rem; font-weight: 500; color: var(--text-primary); transition: var(--t); }
.kanban-item:hover { border-color: var(--border-hover); transform: translateX(3px); box-shadow: -3px 0 0 #4D9FFF; }
.kanban-empty { color: var(--text-muted); font-size: 0.78rem; text-align: center; padding: 1.5rem 0; font-style: italic; }

.stat-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.25rem 1rem; text-align: center; backdrop-filter: blur(10px); box-shadow: var(--shadow); transition: var(--t); position: relative; overflow: hidden; }
.stat-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent); }
.stat-card:hover { transform: translateY(-3px); border-color: var(--border-hover); }
.stat-num { font-size: 2rem; font-weight: 900; line-height: 1; letter-spacing: -0.03em; }
.stat-lbl { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-muted); margin-top: 0.3rem; }

.tech-bar-item { margin-bottom: 0.8rem; }
.tech-bar-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem; }
.tech-bar-name { font-size: 0.82rem; font-weight: 600; color: var(--text-secondary); }
.tech-bar-count { font-size: 0.72rem; font-weight: 600; color: var(--text-muted); }
.tech-bar-track { height: 5px; background: rgba(255,255,255,0.05); border-radius: 99px; overflow: hidden; }
.tech-bar-fill { height: 100%; border-radius: 99px; background: linear-gradient(90deg, var(--blue), var(--cyan)); box-shadow: 0 0 8px var(--cyan-glow); }

.insight-box { background: linear-gradient(135deg, rgba(77,159,255,0.08), rgba(168,85,247,0.06)); border: 1px solid rgba(77,159,255,0.2); border-radius: var(--radius-lg); padding: 1rem 1.2rem; margin-bottom: 1rem; font-size: 0.88rem; color: var(--text-secondary); line-height: 1.6; }
.insight-box strong { color: var(--blue); }

.code-view { background: #03060f; border: 1px solid rgba(0,212,255,0.15); border-radius: var(--radius-md); padding: 1rem; font-family: 'JetBrains Mono', monospace !important; font-size: 0.78rem; color: var(--cyan); max-height: 220px; overflow: auto; white-space: pre; line-height: 1.7; }

.empty-state { text-align: center; padding: 3rem 1rem; color: var(--text-muted); }
.empty-icon { font-size: 3rem; margin-bottom: 1rem; opacity: 0.4; }
.empty-text { font-size: 0.88rem; font-weight: 500; }

.count-pill { display: inline-flex; align-items: center; background: rgba(77,159,255,0.1); border: 1px solid rgba(77,159,255,0.2); border-radius: 99px; padding: 0.15rem 0.6rem; font-size: 0.7rem; font-weight: 700; color: var(--blue); margin-left: 0.5rem; }
.card-title { font-size: 0.95rem; font-weight: 700; color: var(--text-primary); }
.card-desc { font-size: 0.83rem; color: var(--text-secondary); line-height: 1.6; margin: 0.5rem 0; }
.card-link { font-size: 0.78rem; color: var(--cyan); font-weight: 600; }
.progress-pct { font-size: 3rem; font-weight: 900; background: linear-gradient(135deg, var(--blue), var(--cyan)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: -0.04em; line-height: 1; }
.progress-ring-wrap { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-xl); padding: 1.5rem; backdrop-filter: blur(10px); box-shadow: var(--shadow); }
.mode-btn button { background: rgba(255,255,255,0.04) !important; border: 1px solid var(--border) !important; color: var(--text-secondary) !important; box-shadow: none !important; font-size: 0.82rem !important; font-weight: 600 !important; }
.mode-btn button:hover { border-color: var(--border-hover) !important; color: var(--text-primary) !important; transform: none !important; box-shadow: none !important; }
</style>
"""

LIGHT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-base: #F0F4FF; --bg-card: rgba(255,255,255,0.9); --bg-card-hover: #fff;
    --bg-input: rgba(255,255,255,0.95); --bg-sidebar: #FFFFFF;
    --blue: #2563EB; --blue-glow: rgba(37,99,235,0.2);
    --cyan: #0891B2; --cyan-glow: rgba(8,145,178,0.2);
    --purple: #7C3AED; --green: #059669; --green-glow: rgba(5,150,105,0.15);
    --orange: #EA580C; --red: #DC2626; --red-glow: rgba(220,38,38,0.15);
    --text-primary: #0F172A; --text-secondary: #475569; --text-muted: #94A3B8;
    --border: rgba(0,0,0,0.08); --border-hover: rgba(37,99,235,0.35); --border-active: rgba(37,99,235,0.6);
    --radius-xl: 20px; --radius-lg: 14px; --radius-md: 10px; --radius-sm: 7px;
    --shadow: 0 4px 20px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.08);
    --t: all 0.25s cubic-bezier(0.4,0,0.2,1);
}
*, *::before, *::after { font-family: 'Inter', sans-serif !important; }
code, pre { font-family: 'JetBrains Mono', monospace !important; }
.stApp { background: var(--bg-base) !important; background-image: radial-gradient(ellipse 80% 50% at 20% 10%, rgba(37,99,235,0.04) 0%, transparent 60%), radial-gradient(ellipse 60% 40% at 80% 80%, rgba(124,58,237,0.03) 0%, transparent 50%) !important; color: var(--text-primary) !important; }
.main .block-container { background: transparent !important; padding: 2rem 2.5rem !important; max-width: 1280px !important; }
[data-testid="stSidebar"] { background: var(--bg-sidebar) !important; border-right: 1px solid var(--border) !important; box-shadow: 2px 0 20px rgba(0,0,0,0.05) !important; }
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }
[data-testid="stSidebar"] p { color: var(--text-muted) !important; }
div[data-testid="stRadio"] > label { color: var(--text-muted) !important; font-size: 0.65rem !important; font-weight: 700 !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label { background: rgba(0,0,0,0.02) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-md) !important; padding: 0.6rem 1rem !important; color: var(--text-secondary) !important; font-size: 0.875rem !important; font-weight: 500 !important; text-transform: none !important; letter-spacing: 0 !important; transition: var(--t) !important; cursor: pointer !important; width: 100% !important; margin-bottom: 0.25rem !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label:hover { background: rgba(37,99,235,0.04) !important; border-color: var(--border-hover) !important; color: var(--text-primary) !important; transform: translateX(4px) !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) { background: linear-gradient(135deg, rgba(37,99,235,0.08), rgba(124,58,237,0.05)) !important; border-color: var(--border-active) !important; color: var(--blue) !important; font-weight: 600 !important; box-shadow: 0 2px 8px rgba(37,99,235,0.1) !important; }
div[data-testid="stRadio"] div[role="radiogroup"] input[type="radio"] { display: none !important; }
.stButton > button { background: linear-gradient(135deg, var(--blue), var(--purple)) !important; color: #fff !important; border: none !important; border-radius: var(--radius-md) !important; font-weight: 600 !important; font-size: 0.875rem !important; padding: 0.55rem 1.5rem !important; transition: var(--t) !important; box-shadow: 0 4px 12px var(--blue-glow) !important; }
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 6px 20px var(--blue-glow) !important; }
.stButton > button[kind="secondary"] { background: rgba(0,0,0,0.03) !important; border: 1px solid var(--border) !important; color: var(--text-secondary) !important; box-shadow: none !important; }
.stButton > button[kind="secondary"]:hover { border-color: var(--red) !important; color: var(--red) !important; background: rgba(220,38,38,0.04) !important; transform: none !important; }
.stTextInput > div > div > input, .stTextArea > div > div > textarea { background: var(--bg-input) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-md) !important; color: var(--text-primary) !important; }
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus { border-color: var(--blue) !important; box-shadow: 0 0 0 3px var(--blue-glow) !important; }
label[data-testid="stWidgetLabel"] p { color: var(--text-muted) !important; font-size: 0.7rem !important; font-weight: 700 !important; letter-spacing: 0.12em !important; text-transform: uppercase !important; }
div[data-testid="stSelectbox"] > div > div { background: var(--bg-input) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-md) !important; color: var(--text-primary) !important; }
div[data-testid="stSelectbox"] > div > div > div { color: var(--text-primary) !important; background: transparent !important; }
div[data-testid="stTabs"] button { background: transparent !important; color: var(--text-muted) !important; border: none !important; border-bottom: 2px solid transparent !important; font-weight: 600 !important; transition: var(--t) !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color: var(--blue) !important; border-bottom-color: var(--blue) !important; }
details { background: var(--bg-card) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-lg) !important; margin-bottom: 0.75rem !important; box-shadow: var(--shadow) !important; }
details summary { color: var(--text-primary) !important; font-weight: 600 !important; font-size: 0.9rem !important; padding: 1rem 1.2rem !important; cursor: pointer !important; }
details > div { padding: 0 1.2rem 1.2rem !important; }
div[data-testid="metric-container"] { background: var(--bg-card) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-lg) !important; box-shadow: var(--shadow) !important; }
div[data-testid="stProgressBar"] > div { background: rgba(0,0,0,0.06) !important; border-radius: 99px !important; }
div[data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg, var(--blue), var(--cyan)) !important; border-radius: 99px !important; }
div[data-testid="stForm"] .stButton > button { width: 100% !important; padding: 0.75rem !important; font-weight: 700 !important; }
hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 1.5rem 0 !important; }
::-webkit-scrollbar { width: 4px; } ::-webkit-scrollbar-track { background: transparent; } ::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.1); border-radius: 99px; }

.page-icon { font-size: 2.5rem; margin-bottom: 0.5rem; }
.page-title { font-size: 2.2rem; font-weight: 900; background: linear-gradient(135deg, #0F172A 0%, var(--blue) 60%, var(--cyan) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1.1; margin: 0 0 0.4rem 0; letter-spacing: -0.02em; }
.page-subtitle { color: var(--text-muted); font-size: 0.875rem; margin-bottom: 2rem; }
.section-label { font-size: 0.65rem; font-weight: 800; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-muted); display: flex; align-items: center; gap: 0.6rem; margin: 2rem 0 1rem 0; padding-bottom: 0.6rem; border-bottom: 1px solid var(--border); }
.section-label::before { content: ''; width: 16px; height: 2px; background: linear-gradient(90deg, var(--blue), var(--cyan)); border-radius: 99px; flex-shrink: 0; }
.brand-wrap { padding: 1.5rem 1.2rem 1rem; border-bottom: 1px solid var(--border); margin-bottom: 1rem; }
.brand-logo { font-size: 1.4rem; font-weight: 900; background: linear-gradient(135deg, var(--blue), var(--cyan)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.brand-sub { font-size: 0.65rem !important; font-weight: 600 !important; letter-spacing: 0.15em !important; color: var(--text-muted) !important; text-transform: uppercase !important; margin-top: 0.3rem !important; }
.badge { display: inline-flex; align-items: center; padding: 0.2rem 0.65rem; border-radius: 99px; font-size: 0.68rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.badge-blue   { background: rgba(37,99,235,0.08);  color: #2563EB; border: 1px solid rgba(37,99,235,0.2); }
.badge-cyan   { background: rgba(8,145,178,0.08);  color: #0891B2; border: 1px solid rgba(8,145,178,0.2); }
.badge-green  { background: rgba(5,150,105,0.08);  color: #059669; border: 1px solid rgba(5,150,105,0.2); }
.badge-orange { background: rgba(234,88,12,0.08);  color: #EA580C; border: 1px solid rgba(234,88,12,0.2); }
.badge-purple { background: rgba(124,58,237,0.08); color: #7C3AED; border: 1px solid rgba(124,58,237,0.2); }
.badge-red    { background: rgba(220,38,38,0.08);  color: #DC2626; border: 1px solid rgba(220,38,38,0.2); }
.kanban-col { background: rgba(0,0,0,0.02); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1rem; min-height: 180px; }
.col-todo { border-top: 2px solid #EA580C; } .col-doing { border-top: 2px solid #2563EB; } .col-done { border-top: 2px solid #059669; }
.kanban-col-header { font-size: 0.65rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; padding-bottom: 0.75rem; margin-bottom: 0.75rem; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 0.4rem; }
.col-todo .kanban-col-header { color: #EA580C; } .col-doing .kanban-col-header { color: #2563EB; } .col-done .kanban-col-header { color: #059669; }
.kanban-item { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 0.6rem 0.8rem; margin-bottom: 0.5rem; font-size: 0.82rem; font-weight: 500; color: var(--text-primary); transition: var(--t); }
.kanban-item:hover { border-color: var(--border-hover); transform: translateX(3px); box-shadow: -3px 0 0 #2563EB; }
.kanban-empty { color: var(--text-muted); font-size: 0.78rem; text-align: center; padding: 1.5rem 0; font-style: italic; }
.stat-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.25rem 1rem; text-align: center; box-shadow: var(--shadow); transition: var(--t); }
.stat-card:hover { transform: translateY(-3px); border-color: var(--border-hover); }
.stat-num { font-size: 2rem; font-weight: 900; line-height: 1; letter-spacing: -0.03em; }
.stat-lbl { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-muted); margin-top: 0.3rem; }
.tech-bar-item { margin-bottom: 0.8rem; }
.tech-bar-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem; }
.tech-bar-name { font-size: 0.82rem; font-weight: 600; color: var(--text-secondary); }
.tech-bar-count { font-size: 0.72rem; font-weight: 600; color: var(--text-muted); }
.tech-bar-track { height: 5px; background: rgba(0,0,0,0.06); border-radius: 99px; overflow: hidden; }
.tech-bar-fill { height: 100%; border-radius: 99px; background: linear-gradient(90deg, var(--blue), var(--cyan)); }
.insight-box { background: linear-gradient(135deg, rgba(37,99,235,0.06), rgba(124,58,237,0.04)); border: 1px solid rgba(37,99,235,0.15); border-radius: var(--radius-lg); padding: 1rem 1.2rem; margin-bottom: 1rem; font-size: 0.88rem; color: var(--text-secondary); line-height: 1.6; }
.insight-box strong { color: var(--blue); }
.code-view { background: #F8FAFF; border: 1px solid rgba(8,145,178,0.15); border-radius: var(--radius-md); padding: 1rem; font-family: 'JetBrains Mono', monospace !important; font-size: 0.78rem; color: var(--purple); max-height: 220px; overflow: auto; white-space: pre; line-height: 1.7; }
.empty-state { text-align: center; padding: 3rem 1rem; color: var(--text-muted); }
.empty-icon { font-size: 3rem; margin-bottom: 1rem; opacity: 0.4; }
.empty-text { font-size: 0.88rem; font-weight: 500; }
.count-pill { display: inline-flex; align-items: center; background: rgba(37,99,235,0.08); border: 1px solid rgba(37,99,235,0.15); border-radius: 99px; padding: 0.15rem 0.6rem; font-size: 0.7rem; font-weight: 700; color: var(--blue); margin-left: 0.5rem; }
.card-title { font-size: 0.95rem; font-weight: 700; color: var(--text-primary); }
.card-desc { font-size: 0.83rem; color: var(--text-secondary); line-height: 1.6; margin: 0.5rem 0; }
.card-link { font-size: 0.78rem; color: var(--cyan); font-weight: 600; }
.progress-pct { font-size: 3rem; font-weight: 900; background: linear-gradient(135deg, var(--blue), var(--cyan)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: -0.04em; line-height: 1; }
.progress-ring-wrap { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-xl); padding: 1.5rem; box-shadow: var(--shadow); }
.mode-btn button { background: rgba(0,0,0,0.03) !important; border: 1px solid var(--border) !important; color: var(--text-secondary) !important; box-shadow: none !important; font-size: 0.82rem !important; font-weight: 600 !important; }
</style>
"""

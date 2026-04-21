"""
components.py — Engineering Hub UI Components
All text in English. Clean, modular, production-ready.
"""
import streamlit as st

PREVIEW_LINES = 8   # lines shown before "Show more"

# ══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ══════════════════════════════════════════════════════════════════════════════

def inject_css():
    st.markdown("""<style>
/* ── Hub card ── */
.hub-card{background:var(--bg-card,rgba(255,255,255,0.04));border:1px solid var(--border,rgba(255,255,255,0.08));border-radius:14px;padding:1rem 1.2rem;margin-bottom:.65rem;transition:border-color .2s,box-shadow .2s}
.hub-card:hover{border-color:var(--blue,#4D9FFF);box-shadow:0 4px 24px rgba(77,159,255,.1)}
.pcb-header{display:flex;justify-content:space-between;align-items:flex-start;gap:.8rem;margin-bottom:.5rem;flex-wrap:wrap}
.pcb-title{font-size:.95rem;font-weight:700;color:var(--text-primary,#EDF2FF);line-height:1.4}
.pcb-badges{display:flex;gap:.35rem;flex-wrap:wrap;align-items:center;flex-shrink:0}
.pcb-tags{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:.5rem}
.card-divider{height:1px;background:var(--border,rgba(255,255,255,0.06));margin:.5rem 0 1rem}
.card-desc{font-size:.81rem;color:var(--text-secondary,#8899BB);line-height:1.6;margin:.3rem 0 .5rem}
.card-link{font-size:.77rem;color:var(--cyan,#00D4FF);text-decoration:none;font-weight:600}
.card-link:hover{text-decoration:underline}

/* ── Empty state ── */
.empty-box{text-align:center;padding:2.5rem 1.5rem;border:1.5px dashed var(--border,rgba(255,255,255,0.08));border-radius:14px;margin:.5rem 0}
.empty-box-icon{font-size:2.2rem;margin-bottom:.6rem;opacity:.6}
.empty-box-text{font-size:.85rem;color:var(--text-muted,#3D5070);line-height:1.6}

/* ── Code preview header ── */
.code-hdr{display:flex;justify-content:space-between;align-items:center;padding:.35rem .8rem;background:rgba(0,0,0,.25);border:1px solid var(--border);border-radius:8px 8px 0 0;margin-bottom:-2px}
.code-lang{font-size:.66rem;font-weight:700;color:var(--cyan,#00D4FF);text-transform:uppercase;letter-spacing:.1em;font-family:'JetBrains Mono',monospace}
.code-meta{font-size:.64rem;color:var(--text-muted,#3D5070)}

/* ── File Manager ── */
.fm-row{display:flex;align-items:center;gap:.65rem;background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.65rem .9rem;margin-bottom:.4rem;transition:all .18s}
.fm-row:hover{border-color:var(--blue,#4D9FFF)}
.fm-row-folder:hover{border-color:#F59E0B}
.fm-icon{font-size:1.15rem;flex-shrink:0}
.fm-name{font-size:.86rem;font-weight:600;color:var(--text-primary,#EDF2FF);flex:1;word-break:break-all}
.fm-meta{font-size:.67rem;color:var(--text-muted,#3D5070);white-space:nowrap;flex-shrink:0}
.fm-bc{display:flex;align-items:center;gap:.4rem;font-size:.78rem;margin-bottom:.9rem;flex-wrap:wrap}
.fm-bc a{color:var(--blue,#4D9FFF);font-weight:600;text-decoration:none;cursor:pointer}
.fm-bc-sep{color:var(--text-muted,#3D5070)}
.fm-bc-cur{color:var(--text-primary,#EDF2FF);font-weight:700}

/* ── Stats mini ── */
.stat-mini{text-align:center;padding:.9rem .5rem;background:var(--bg-card);border:1px solid var(--border);border-radius:12px}
.stat-mini-num{font-size:1.55rem;font-weight:900;line-height:1}
.stat-mini-lbl{font-size:.62rem;font-weight:700;color:var(--text-muted,#3D5070);text-transform:uppercase;letter-spacing:.08em;margin-top:.2rem}

/* ── Game container ── */
.game-wrap{border:1px solid var(--border);border-radius:14px;overflow:hidden;margin-top:.5rem}

/* Button consistency */
div[data-testid="stHorizontalBlock"] .stButton>button{font-size:.78rem!important;border-radius:8px!important}
</style>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# BADGE HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def _badge_status(s):
    return '<span class="badge badge-green">✓ Completed</span>' if s == "Completed" else '<span class="badge badge-orange">⟳ In Progress</span>'

def _badge_kanban(k):
    m = {"To-do":"badge-orange","Doing":"badge-blue","Done":"badge-green"}
    return f'<span class="badge {m.get(k,"badge-orange")}">{k}</span>'

def _badge_priority(p):
    m = {"High":("badge-red","🔴"),"Medium":("badge-orange","🟡"),"Low":("badge-cyan","🔵")}
    c,i = m.get(p,("badge-orange","🟡"))
    return f'<span class="badge {c}">{i} {p}</span>'

def _tech_tags(stack):
    if not stack: return ""
    colors = ["badge-blue","badge-purple","badge-cyan","badge-green","badge-orange"]
    return " ".join(f'<span class="badge {colors[i%len(colors)]}">{t.strip()}</span>'
                    for i,t in enumerate([x.strip() for x in stack.split(",") if x.strip()]))

def _ext_icon(ext):
    return {".py":"🐍",".js":"🟨",".ts":"🔷",".html":"🌐",".css":"🎨",
            ".json":"📋",".txt":"📄",".sql":"🗄️",".sh":"⚙️",".md":"📝",
            ".yaml":"⚙️",".yml":"⚙️",".java":"☕",".go":"🐹",".rs":"🦀"}.get(ext.lower(),"📄")

EXT_LANG = {".py":"python",".js":"javascript",".ts":"typescript",".html":"html",
            ".css":"css",".json":"json",".sql":"sql",".sh":"bash",".md":"markdown",
            ".yaml":"yaml",".yml":"yaml",".java":"java",".go":"go",".rs":"rust",".txt":"text"}

ALLOWED = ["py","js","ts","html","css","json","txt","sql","sh","md","yaml","yml","java","go","rs"]


# ══════════════════════════════════════════════════════════════════════════════
# LAYOUT HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def page_header(icon, title, subtitle):
    st.markdown(f"""<div style="padding-bottom:1.5rem">
        <div class="page-icon">{icon}</div>
        <div class="page-title">{title}</div>
        <div class="page-subtitle">{subtitle}</div>
    </div>""", unsafe_allow_html=True)

def section_label(text):
    st.markdown(f'<div class="section-label">{text}</div>', unsafe_allow_html=True)

def empty_state(icon="📭", title="No data yet", sub=""):
    st.markdown(f"""<div class="empty-box">
        <div class="empty-box-icon">{icon}</div>
        <div class="empty-box-text"><strong>{title}</strong>{"<br><span style='font-size:.8rem'>"+sub+"</span>" if sub else ""}</div>
    </div>""", unsafe_allow_html=True)

def divider():
    st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CODE PREVIEW — Show more / Show less  (session_state toggle, no flicker)
# ══════════════════════════════════════════════════════════════════════════════

def code_preview(snippet: str, lang: str, key: str):
    """Preview first N lines; toggle button expands/collapses. Uses st.code()."""
    if not snippet or not snippet.strip():
        st.markdown('<p style="font-size:.74rem;color:var(--text-muted,#3D5070);margin:.3rem 0">No code available</p>', unsafe_allow_html=True)
        return

    lines  = snippet.splitlines()
    total  = len(lines)
    ekey   = f"__ce_{key}"
    if ekey not in st.session_state:
        st.session_state[ekey] = False

    expanded = st.session_state[ekey]
    needs    = total > PREVIEW_LINES

    # Header row
    h1, h2, h3 = st.columns([2, 3, 2])
    with h1:
        st.markdown(f'<div class="code-lang">💾 {lang.upper()}</div>', unsafe_allow_html=True)
    with h2:
        st.markdown(f'<div class="code-meta" style="padding:.45rem 0">{total} lines</div>', unsafe_allow_html=True)
    with h3:
        if needs:
            if st.button("🔼 Show less" if expanded else "🔽 Show more",
                         key=f"__ctog_{key}", use_container_width=True):
                st.session_state[ekey] = not expanded
                st.rerun()

    code_out = snippet if (expanded or not needs) else (
        "\n".join(lines[:PREVIEW_LINES]) + f"\n# ··· {total - PREVIEW_LINES} more lines hidden"
    )
    st.code(code_out, language=lang if lang != "other" else "text")


# ══════════════════════════════════════════════════════════════════════════════
# KANBAN BOARD
# ══════════════════════════════════════════════════════════════════════════════

def kanban_board(items, title_key="title"):
    cols = {"To-do":[],"Doing":[],"Done":[]}
    for i in items:
        cols.get(i.get("kanban_status","To-do"),[]).append(i)
    c1,c2,c3 = st.columns(3)
    def _col(col, css, hdr, data):
        with col:
            st.markdown(f'<div class="kanban-col {css}"><div class="kanban-col-header">{hdr}</div>', unsafe_allow_html=True)
            if not data:
                st.markdown('<div class="kanban-empty">Empty</div>', unsafe_allow_html=True)
            else:
                for i in data:
                    n = i.get(title_key, i.get("goal","—"))
                    st.markdown(f'<div class="kanban-item">{n}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    _col(c1,"col-todo","📋 To-do",cols["To-do"])
    _col(c2,"col-doing","⚡ Doing",cols["Doing"])
    _col(c3,"col-done","✅ Done",cols["Done"])


# ══════════════════════════════════════════════════════════════════════════════
# PROJECT CARD
# ══════════════════════════════════════════════════════════════════════════════

def project_card(p, table_id, update_fn, delete_fn):
    pid, title, tech    = p["id"], p.get("title","Untitled"), p.get("tech_stack","")
    desc, github        = p.get("description",""), p.get("github_link","")
    status, kanban      = p.get("status","In Progress"), p.get("kanban_status","To-do")
    th = _tech_tags(tech)

    st.markdown(f"""<div class="hub-card">
        <div class="pcb-header">
            <span class="pcb-title">{title}</span>
            <span class="pcb-badges">{_badge_status(status)}&nbsp;{_badge_kanban(kanban)}</span>
        </div>
        {('<div class="pcb-tags">'+th+'</div>') if th else ''}
        {('<p class="card-desc">'+desc+'</p>') if desc else ''}
        {('<a href="'+github+'" target="_blank" class="card-link">🔗 GitHub →</a>') if github else ''}
    </div>""", unsafe_allow_html=True)

    b1, b2 = st.columns([3,1])
    with b1:
        opts = ["To-do","Doing","Done"]
        nk = st.selectbox("Status", opts, index=opts.index(kanban) if kanban in opts else 0,
                          key=f"kb_{table_id}_{pid}", label_visibility="collapsed")
        if nk != kanban: update_fn(pid, nk); st.rerun()
    with b2:
        if st.button("🗑 Delete", key=f"del_{table_id}_{pid}", use_container_width=True):
            delete_fn(pid); st.rerun()
    divider()


# ══════════════════════════════════════════════════════════════════════════════
# ADD PROJECT FORM  — ✅ Add  (no reset button — removed as requested)
# ══════════════════════════════════════════════════════════════════════════════

def add_project_form(fkey, save_fn):
    """No reset button — form clears automatically after successful save."""
    rv = f"__pf_{fkey}"
    if rv not in st.session_state: st.session_state[rv] = 0
    v = st.session_state[rv]

    c1,c2 = st.columns(2)
    with c1:
        title  = st.text_input("📌 Project Title *",  placeholder="e.g. ETL Pipeline",       key=f"{fkey}_t{v}")
        tech   = st.text_input("🛠 Tech Stack",        placeholder="Python, Spark, Airflow",   key=f"{fkey}_sk{v}")
        github = st.text_input("🔗 GitHub Link",       placeholder="https://github.com/…",     key=f"{fkey}_gh{v}")
    with c2:
        status = st.selectbox("📊 Status", ["In Progress","Completed"],                        key=f"{fkey}_st{v}")
        desc   = st.text_area("📝 Description", placeholder="What is this project about?",
                               height=130,                                                      key=f"{fkey}_d{v}")

    st.markdown("<br>", unsafe_allow_html=True)
    bc, _ = st.columns([2,7])
    with bc:
        if st.button("✅ Add Project", key=f"{fkey}_add{v}", use_container_width=True):
            if not title.strip():
                st.error("⚠️ Title is required.")
            else:
                ok = save_fn(title.strip(), tech.strip(), desc.strip(), github.strip(), status)
                if ok:
                    st.success(f"✅ **{title.strip()}** added successfully!")
                    st.session_state[rv] += 1
                    st.rerun()
                else:
                    st.error("❌ Failed to save.")


# ══════════════════════════════════════════════════════════════════════════════
# GOAL CARD
# ══════════════════════════════════════════════════════════════════════════════

def goal_card(g, update_fn, delete_fn):
    gid, goal    = g["id"], g.get("goal","")
    kanban, pri  = g.get("kanban_status","To-do"), g.get("priority","Medium")
    deadline     = g.get("deadline","")

    st.markdown(f"""<div class="hub-card">
        <div class="pcb-header">
            <span class="pcb-title">🎯 {goal}</span>
            <span class="pcb-badges">{_badge_priority(pri)}&nbsp;{_badge_kanban(kanban)}</span>
        </div>
        {'<span style="font-size:.74rem;color:var(--text-muted)">📅 '+deadline+'</span>' if deadline else ''}
    </div>""", unsafe_allow_html=True)

    b1,b2 = st.columns([3,1])
    with b1:
        opts = ["To-do","Doing","Done"]
        nk = st.selectbox("s", opts, index=opts.index(kanban) if kanban in opts else 0,
                          key=f"gkb_{gid}", label_visibility="collapsed")
        if nk != kanban: update_fn(gid, nk); st.rerun()
    with b2:
        if st.button("🗑 Delete", key=f"del_goal_{gid}", use_container_width=True):
            delete_fn(gid); st.rerun()
    divider()


# ══════════════════════════════════════════════════════════════════════════════
# LOG CARD — code preview with Show more / Show less
# ══════════════════════════════════════════════════════════════════════════════

def log_card(log, delete_fn):
    lid      = log["id"]
    log_date = log.get("date","")
    tags_raw = log.get("tags","")
    learning = log.get("daily_learning","")
    snippet  = log.get("code_snippet","")
    lang     = log.get("snippet_language","python")

    tags_html = " ".join(f'<span class="badge badge-cyan">#{t.strip()}</span>'
                         for t in tags_raw.split(",") if t.strip()) if tags_raw else ""

    st.markdown(f"""<div class="hub-card">
        <div class="pcb-header">
            <span class="pcb-title">📅 {log_date}</span>
            <span class="pcb-badges">{tags_html}</span>
        </div>
        {('<p class="card-desc">'+learning+'</p>') if learning else ''}
    </div>""", unsafe_allow_html=True)

    if snippet and snippet.strip():
        section_label(f"Code · {lang.upper()}")
        code_preview(snippet, lang, f"log_{lid}")

    _, dc = st.columns([6,1])
    with dc:
        if st.button("🗑", key=f"del_log_{lid}", use_container_width=True):
            delete_fn(lid); st.rerun()
    divider()


# ══════════════════════════════════════════════════════════════════════════════
# FREELANCE CARD
# ══════════════════════════════════════════════════════════════════════════════

def freelance_card(p, update_fn, delete_fn):
    pid     = p["id"]
    title   = p.get("title","Untitled")
    client  = p.get("client","")
    tech    = p.get("tech_stack","")
    desc    = p.get("description","")
    budget  = p.get("budget","")
    status  = p.get("status","In Progress")
    kanban  = p.get("kanban_status","To-do")
    th = _tech_tags(tech)

    st.markdown(f"""<div class="hub-card">
        <div class="pcb-header">
            <span class="pcb-title">{title}</span>
            <span class="pcb-badges">{_badge_status(status)}&nbsp;{_badge_kanban(kanban)}</span>
        </div>
        <div style="display:flex;gap:.8rem;align-items:center;margin-bottom:.4rem">
            {'<span style="font-size:.79rem;color:var(--text-muted)">👤 '+client+'</span>' if client else ''}
            {'<span class="badge badge-green">💰 '+budget+'</span>' if budget else ''}
        </div>
        {('<div class="pcb-tags">'+th+'</div>') if th else ''}
        {('<p class="card-desc">'+desc+'</p>') if desc else ''}
    </div>""", unsafe_allow_html=True)

    b1,b2 = st.columns([3,1])
    with b1:
        opts = ["To-do","Doing","Done"]
        nk = st.selectbox("m", opts, index=opts.index(kanban) if kanban in opts else 0,
                          key=f"fkb_{pid}", label_visibility="collapsed")
        if nk != kanban: update_fn(pid, nk); st.rerun()
    with b2:
        if st.button("🗑 Delete", key=f"del_free_{pid}", use_container_width=True):
            delete_fn(pid); st.rerun()
    divider()


# ══════════════════════════════════════════════════════════════════════════════
# FILE MANAGER
# ══════════════════════════════════════════════════════════════════════════════

def _breadcrumb(stack):
    """Render navigation breadcrumb. stack = [(id, name), ...]"""
    if stack:
        parts = []
        for i, (fid, fname) in enumerate(stack):
            parts.append('<span class="fm-bc-sep">›</span>')
            if i == len(stack) - 1:
                parts.append(f'<span class="fm-bc-cur">📁 {fname}</span>')
            else:
                parts.append(f'<span style="color:var(--blue,#4D9FFF);font-size:.78rem">📁 {fname}</span>')
        st.markdown(f'<div class="fm-bc">🏠 Root {"".join(parts)}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="fm-bc"><span class="fm-bc-cur">🏠 Root</span></div>', unsafe_allow_html=True)


def _upload_file_widget(db, target_folder_id, widget_key_suffix):
    """
    Reusable upload widget. Supports selecting MULTIPLE files at once
    (Ctrl+A or Ctrl+Click). Saves all files into target_folder_id.
    Returns True if at least one file was saved, "cancel" on cancel, False otherwise.
    """
    uploads = st.file_uploader(
        "Choose one or more files  (Ctrl+A to select all)",
        type=ALLOWED,
        accept_multiple_files=True,
        key=f"fm_up_{widget_key_suffix}",
        label_visibility="collapsed",
    )

    if uploads:
        total_kb = 0
        parsed   = []

        for up in uploads:
            ext = ("." + up.name.rsplit(".", 1)[-1].lower()) if "." in up.name else ".txt"
            raw = up.read()
            try:    file_content = raw.decode("utf-8")
            except: file_content = raw.decode("latin-1", errors="replace")
            size_kb = len(file_content.encode()) / 1024
            lang    = EXT_LANG.get(ext, "text")
            n_lines = len(file_content.splitlines())
            total_kb += size_kb
            parsed.append((up.name, ext, file_content, size_kb, lang, n_lines))

        # Summary bar
        st.markdown(
            f'<div style="display:flex;align-items:center;gap:.8rem;'
            f'padding:.6rem .9rem;background:rgba(77,159,255,.07);'
            f'border:1px solid rgba(77,159,255,.2);border-radius:10px;margin:.4rem 0">'
            f'<span style="font-size:1.1rem">📦</span>'
            f'<span style="font-size:.82rem;font-weight:700;color:var(--blue,#4D9FFF)">'
            f'{len(parsed)} file{"s" if len(parsed)!=1 else ""} selected'
            f'</span>'
            f'<span style="font-size:.75rem;color:var(--text-muted,#64748B);margin-left:auto">'
            f'Total: {total_kb:.1f} KB'
            f'</span></div>',
            unsafe_allow_html=True,
        )

        # File list with individual preview toggle
        for fname, ext, file_content, size_kb, lang, n_lines in parsed:
            pk = f"upw_prev_{widget_key_suffix}_{fname}"
            if pk not in st.session_state:
                st.session_state[pk] = False

            r1, r2 = st.columns([5, 1.5])
            with r1:
                st.markdown(
                    f'<div class="fm-row">'
                    f'<span class="fm-icon">{_ext_icon(ext)}</span>'
                    f'<div style="flex:1;min-width:0">'
                    f'<div class="fm-name">{fname}</div>'
                    f'<div class="fm-meta">{size_kb:.1f} KB · {n_lines} lines</div>'
                    f'</div>'
                    f'<span class="badge badge-cyan">{ext}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            with r2:
                prev_lbl = "🔼 Close" if st.session_state[pk] else "👁 Preview"
                if st.button(prev_lbl, key=f"upw_tog_{widget_key_suffix}_{fname}",
                             use_container_width=True):
                    st.session_state[pk] = not st.session_state[pk]
                    st.rerun()

            if st.session_state[pk]:
                code_preview(file_content, lang, f"upw_{widget_key_suffix}_{fname}")

        # Action buttons
        st.markdown("<br>", unsafe_allow_html=True)
        sb1, sb2, _ = st.columns([3, 2, 4])
        with sb1:
            btn_lbl = f"💾 Save {len(parsed)} File{'s' if len(parsed)!=1 else ''} ({total_kb:.1f} KB)"
            if st.button(btn_lbl, key=f"fm_save_{widget_key_suffix}", use_container_width=True):
                saved = 0
                for fname, ext, file_content, size_kb, lang, n_lines in parsed:
                    if db.save_file(fname, ext, file_content, round(size_kb, 2), target_folder_id):
                        saved += 1
                if saved:
                    st.success(f"✅ {saved} file{'s' if saved!=1 else ''} saved successfully!")
                    return True
                else:
                    st.error("❌ Failed to save files.")
        with sb2:
            if st.button("✖ Cancel", key=f"fm_cancelup_{widget_key_suffix}",
                         use_container_width=True):
                return "cancel"

    return False


def file_manager_page(db):
    """
    File Manager rules:
    • Folders CANNOT be created empty — user must upload ≥1 file at creation time.
    • Files are ALWAYS stored inside a folder (no root-level files).
    • File editing is ONLY available from inside the folder that contains the file.
    • Upload File button is only shown when inside a folder.
    """

    # ── Session state ─────────────────────────────────────────────────────
    defaults = {
        "fm_folder_id":       None,   # current open folder id (None = root)
        "fm_stack":           [],     # [(id, name), ...] navigation trail
        "fm_preview_id":      None,   # file id whose content is shown
        "fm_edit_file_id":    None,   # file id being edited
        "fm_rename_folder_id":None,   # folder id being renamed
        "fm_creating_folder": False,  # True while new-folder wizard is open
        "fm_show_upload":     False,  # True while upload panel is open (inside folder)
        "fm_new_folder_name": "",     # draft folder name
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    cur_id    = st.session_state.fm_folder_id
    cur_stack = st.session_state.fm_stack

    # ── Data ──────────────────────────────────────────────────────────────
    subfolders  = db.get_folders(cur_id)
    files       = db.get_files(cur_id)           # only files in current folder
    all_files   = db.get_all_files()
    all_folders = db.get_all_folders()
    total_kb    = sum(f.get("size_kb", 0) for f in all_files)

    # ── Stats ─────────────────────────────────────────────────────────────
    s1, s2, s3, s4 = st.columns(4)
    s1.markdown(f'<div class="stat-mini"><div class="stat-mini-num" style="color:#F59E0B">{len(all_folders)}</div><div class="stat-mini-lbl">Folders</div></div>', unsafe_allow_html=True)
    s2.markdown(f'<div class="stat-mini"><div class="stat-mini-num" style="color:#4D9FFF">{len(all_files)}</div><div class="stat-mini-lbl">Files</div></div>', unsafe_allow_html=True)
    s3.markdown(f'<div class="stat-mini"><div class="stat-mini-num" style="color:#00D4FF">{total_kb:.1f}</div><div class="stat-mini-lbl">KB Total</div></div>', unsafe_allow_html=True)
    s4.markdown(f'<div class="stat-mini"><div class="stat-mini-num" style="color:#10F5A0">{len(subfolders) + len(files)}</div><div class="stat-mini-lbl">Here</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── Breadcrumb ────────────────────────────────────────────────────────
    _breadcrumb(cur_stack)

    # ══════════════════════════════════════════════════════════════════════
    # ROOT VIEW  (cur_id is None)
    # Only action available at root: Create New Folder (with mandatory file)
    # ══════════════════════════════════════════════════════════════════════
    if cur_id is None:

        # Toolbar — root only has "New Folder"
        tc, _ = st.columns([2, 7])
        with tc:
            if not st.session_state.fm_creating_folder:
                if st.button("📁 New Folder", key="fm_root_new", use_container_width=True):
                    st.session_state.fm_creating_folder = True
                    st.session_state.fm_new_folder_name = ""
                    st.rerun()

        # ── New Folder Wizard ──────────────────────────────────────────────
        if st.session_state.fm_creating_folder:
            st.markdown("""<div class="hub-card" style="border:1px solid var(--blue,#4D9FFF);margin-top:.7rem">
                <div style="font-size:.78rem;font-weight:700;color:var(--blue,#4D9FFF);margin-bottom:.8rem;letter-spacing:.05em">
                    📁 CREATE NEW FOLDER
                </div>""", unsafe_allow_html=True)

            # Step 1 — folder name
            nf1, nf2, nf3 = st.columns([5, 1.5, 1.5])
            with nf1:
                folder_name = st.text_input(
                    "Folder name",
                    value=st.session_state.fm_new_folder_name,
                    placeholder="e.g. Python Projects",
                    key="fm_nf_name",
                    label_visibility="collapsed",
                )
                st.session_state.fm_new_folder_name = folder_name
            with nf3:
                if st.button("✖ Cancel", key="fm_nf_cancel", use_container_width=True):
                    st.session_state.fm_creating_folder  = False
                    st.session_state.fm_new_folder_name  = ""
                    st.rerun()

            st.markdown("""<div style="height:1px;background:var(--border);margin:.7rem 0"></div>
                <div style="font-size:.72rem;color:var(--text-muted);margin-bottom:.5rem">
                    📎 <strong>You must upload at least one file</strong> — folders cannot be empty.
                </div>""", unsafe_allow_html=True)

            # Step 2 — mandatory file upload
            up = st.file_uploader(
                "Upload first file",
                type=ALLOWED,
                key="fm_nf_uploader",
                label_visibility="collapsed",
            )

            if up:
                ext = ("." + up.name.rsplit(".", 1)[-1].lower()) if "." in up.name else ".txt"
                raw = up.read()
                try:    content = raw.decode("utf-8")
                except: content = raw.decode("latin-1", errors="replace")
                size_kb = len(content.encode()) / 1024
                lang    = EXT_LANG.get(ext, "text")
                n_lines = len(content.splitlines())

                st.markdown(
                    f'<div class="fm-row" style="margin:.5rem 0">'
                    f'<span class="fm-icon">{_ext_icon(ext)}</span>'
                    f'<span class="fm-name">{up.name}</span>'
                    f'<span class="fm-meta">{size_kb:.1f} KB · {n_lines} lines</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                section_label("Preview")
                code_preview(content, lang, f"nf_prev_{up.name}")

                st.markdown("<br>", unsafe_allow_html=True)
                cb, _ = st.columns([3, 6])
                with cb:
                    if st.button("✅ Create Folder & Save File", key="fm_nf_confirm", use_container_width=True):
                        if not folder_name.strip():
                            st.error("⚠️ Folder name is required.")
                        else:
                            # Create folder then immediately save the file inside it
                            new_fid = db.create_folder_get_id(folder_name.strip(), parent_id=None)
                            if new_fid:
                                db.save_file(up.name, ext, content, round(size_kb, 2), new_fid)
                                st.session_state.fm_creating_folder  = False
                                st.session_state.fm_new_folder_name  = ""
                                st.success(f"✅ Folder **{folder_name.strip()}** created with **{up.name}**!")
                                st.rerun()
                            else:
                                st.error("❌ Failed to create folder.")
            else:
                # No file chosen yet — show placeholder
                st.markdown("""<div style="text-align:center;padding:1.2rem;border:1.5px dashed var(--border);border-radius:10px;margin:.5rem 0">
                    <div style="font-size:1.5rem;opacity:.5">📎</div>
                    <div style="font-size:.78rem;color:var(--text-muted);margin-top:.3rem">
                        Choose a file to upload — folder will be created once you confirm.
                    </div>
                </div>""", unsafe_allow_html=True)

                # Still allow confirming folder name but block if no file
                cb2, _ = st.columns([3, 6])
                with cb2:
                    if st.button("✅ Create Folder & Save File", key="fm_nf_confirm_empty", use_container_width=True):
                        st.error("⚠️ You must add at least one file. Folders cannot be empty.")

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Folder list (root) ─────────────────────────────────────────────
        if subfolders:
            section_label(f"Folders ({len(subfolders)})")
            for folder in subfolders:
                fid, fname = folder["id"], folder["name"]
                n_items = len(db.get_folders(fid)) + len(db.get_files(fid))
                is_ren  = st.session_state.fm_rename_folder_id == fid

                fr1, fr2, fr3, fr4 = st.columns([5, 1.5, 1.5, 1])
                with fr1:
                    st.markdown(
                        f'<div class="fm-row fm-row-folder">'
                        f'<span class="fm-icon">📁</span>'
                        f'<div><div class="fm-name">{fname}</div>'
                        f'<div class="fm-meta">{n_items} item{"s" if n_items!=1 else ""}</div></div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                with fr2:
                    if st.button("📂 Open", key=f"fm_open_{fid}", use_container_width=True):
                        st.session_state.fm_stack.append((fid, fname))
                        st.session_state.fm_folder_id   = fid
                        st.session_state.fm_preview_id  = None
                        st.session_state.fm_edit_file_id = None
                        st.rerun()
                with fr3:
                    ren_lbl = "✖ Cancel" if is_ren else "✏️ Rename"
                    if st.button(ren_lbl, key=f"fm_ren_{fid}", use_container_width=True):
                        st.session_state.fm_rename_folder_id = None if is_ren else fid
                        st.rerun()
                with fr4:
                    if st.button("🗑️", key=f"fm_delf_{fid}", use_container_width=True):
                        db.delete_folder(fid)
                        st.rerun()

                if is_ren:
                    rn1, rn2, _ = st.columns([4, 1.5, 4])
                    with rn1:
                        new_n = st.text_input("New name", value=fname,
                                              key=f"fm_ren_inp_{fid}",
                                              label_visibility="collapsed")
                    with rn2:
                        if st.button("✅ Save", key=f"fm_ren_ok_{fid}", use_container_width=True):
                            if new_n.strip():
                                db.rename_folder(fid, new_n.strip())
                                st.session_state.fm_rename_folder_id = None
                                st.rerun()
        else:
            if not st.session_state.fm_creating_folder:
                empty_state("📁", "No folders yet",
                            "Click 'New Folder' to create your first folder.")

    # ══════════════════════════════════════════════════════════════════════
    # FOLDER VIEW  (cur_id is not None — user is inside a folder)
    # Actions: Back · New Sub-Folder · Upload File · file list with Edit
    # ══════════════════════════════════════════════════════════════════════
    else:
        folder_name_cur = cur_stack[-1][1] if cur_stack else "Folder"

        # Toolbar
        t1, t2, t3, _ = st.columns([2, 2, 2, 3])
        with t1:
            if st.button("⬅ Back", key="fm_back", use_container_width=True):
                cur_stack.pop()
                st.session_state.fm_stack        = cur_stack
                st.session_state.fm_folder_id    = cur_stack[-1][0] if cur_stack else None
                st.session_state.fm_preview_id   = None
                st.session_state.fm_edit_file_id = None
                st.session_state.fm_show_upload  = False
                st.rerun()
        with t2:
            if not st.session_state.fm_creating_folder:
                if st.button("📁 New Sub-Folder", key="fm_sub_new", use_container_width=True):
                    st.session_state.fm_creating_folder = True
                    st.session_state.fm_new_folder_name = ""
                    st.session_state.fm_show_upload     = False
                    st.rerun()
        with t3:
            if not st.session_state.fm_show_upload:
                if st.button("📤 Upload File", key="fm_up_btn", use_container_width=True):
                    st.session_state.fm_show_upload     = True
                    st.session_state.fm_creating_folder = False
                    st.rerun()

        # ── Upload panel (inside folder) ───────────────────────────────────
        if st.session_state.fm_show_upload:
            st.markdown(
                f'<div class="hub-card" style="margin-top:.6rem;border-color:var(--cyan,#00D4FF)">'
                f'<div style="font-size:.75rem;color:var(--text-muted);margin-bottom:.6rem">'
                f'📁 Uploading into: <strong style="color:var(--cyan,#00D4FF)">{folder_name_cur}</strong>'
                f'</div>',
                unsafe_allow_html=True,
            )
            result = _upload_file_widget(db, cur_id, f"inside_{cur_id}")
            if result is True:
                st.session_state.fm_show_upload = False
                st.rerun()
            elif result == "cancel":
                st.session_state.fm_show_upload = False
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        # ── Sub-folder creation wizard (inside folder) ─────────────────────
        if st.session_state.fm_creating_folder:
            st.markdown("""<div class="hub-card" style="border:1px solid var(--blue,#4D9FFF);margin-top:.7rem">
                <div style="font-size:.78rem;font-weight:700;color:var(--blue,#4D9FFF);margin-bottom:.8rem">
                    📁 CREATE SUB-FOLDER
                </div>""", unsafe_allow_html=True)

            sf1, sf2 = st.columns([5, 1.5])
            with sf1:
                sub_name = st.text_input("Sub-folder name", placeholder="e.g. Utils",
                                         key="fm_sub_name", label_visibility="collapsed")
                st.session_state.fm_new_folder_name = sub_name
            with sf2:
                if st.button("✖ Cancel", key="fm_sub_cancel", use_container_width=True):
                    st.session_state.fm_creating_folder = False
                    st.rerun()

            st.markdown('<div style="font-size:.72rem;color:var(--text-muted);margin:.5rem 0">📎 Upload at least one file — sub-folders cannot be empty.</div>', unsafe_allow_html=True)

            up2 = st.file_uploader("Upload first file", type=ALLOWED,
                                   key="fm_sub_uploader", label_visibility="collapsed")
            if up2:
                ext2 = ("." + up2.name.rsplit(".", 1)[-1].lower()) if "." in up2.name else ".txt"
                raw2 = up2.read()
                try:    c2 = raw2.decode("utf-8")
                except: c2 = raw2.decode("latin-1", errors="replace")
                kb2 = len(c2.encode()) / 1024
                lang2 = EXT_LANG.get(ext2, "text")
                st.markdown(f'<div class="fm-row"><span class="fm-icon">{_ext_icon(ext2)}</span><span class="fm-name">{up2.name}</span><span class="fm-meta">{kb2:.1f} KB</span></div>', unsafe_allow_html=True)
                code_preview(c2, lang2, f"sub_prev_{up2.name}")
                st.markdown("<br>", unsafe_allow_html=True)
                scb, _ = st.columns([3, 6])
                with scb:
                    if st.button("✅ Create Sub-Folder & Save File", key="fm_sub_confirm", use_container_width=True):
                        if not sub_name.strip():
                            st.error("⚠️ Sub-folder name is required.")
                        else:
                            new_sfid = db.create_folder_get_id(sub_name.strip(), parent_id=cur_id)
                            if new_sfid:
                                db.save_file(up2.name, ext2, c2, round(kb2, 2), new_sfid)
                                st.session_state.fm_creating_folder = False
                                st.success(f"✅ Sub-folder **{sub_name.strip()}** created with **{up2.name}**!")
                                st.rerun()
                            else:
                                st.error("❌ Failed to create sub-folder.")
            else:
                st.markdown('<div style="text-align:center;padding:1rem;border:1.5px dashed var(--border);border-radius:10px;margin:.4rem 0"><div style="font-size:.78rem;color:var(--text-muted)">Choose a file to continue.</div></div>', unsafe_allow_html=True)
                scb2, _ = st.columns([3, 6])
                with scb2:
                    if st.button("✅ Create Sub-Folder & Save File", key="fm_sub_confirm_empty", use_container_width=True):
                        st.error("⚠️ You must add at least one file. Folders cannot be empty.")

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Sub-folders list ───────────────────────────────────────────────
        if subfolders:
            section_label(f"Sub-Folders ({len(subfolders)})")
            for folder in subfolders:
                fid, fname = folder["id"], folder["name"]
                n_items = len(db.get_folders(fid)) + len(db.get_files(fid))
                is_ren  = st.session_state.fm_rename_folder_id == fid

                fr1, fr2, fr3, fr4 = st.columns([5, 1.5, 1.5, 1])
                with fr1:
                    st.markdown(f'<div class="fm-row fm-row-folder"><span class="fm-icon">📁</span><div><div class="fm-name">{fname}</div><div class="fm-meta">{n_items} item{"s" if n_items!=1 else ""}</div></div></div>', unsafe_allow_html=True)
                with fr2:
                    if st.button("📂 Open", key=f"fm_open_{fid}", use_container_width=True):
                        st.session_state.fm_stack.append((fid, fname))
                        st.session_state.fm_folder_id    = fid
                        st.session_state.fm_preview_id   = None
                        st.session_state.fm_edit_file_id = None
                        st.rerun()
                with fr3:
                    ren_lbl = "✖ Cancel" if is_ren else "✏️ Rename"
                    if st.button(ren_lbl, key=f"fm_ren_{fid}", use_container_width=True):
                        st.session_state.fm_rename_folder_id = None if is_ren else fid
                        st.rerun()
                with fr4:
                    if st.button("🗑️", key=f"fm_delf_{fid}", use_container_width=True):
                        db.delete_folder(fid)
                        st.rerun()

                if is_ren:
                    rn1, rn2, _ = st.columns([4, 1.5, 4])
                    with rn1:
                        new_n = st.text_input("New name", value=fname,
                                              key=f"fm_ren_inp_{fid}", label_visibility="collapsed")
                    with rn2:
                        if st.button("✅ Save", key=f"fm_ren_ok_{fid}", use_container_width=True):
                            if new_n.strip():
                                db.rename_folder(fid, new_n.strip())
                                st.session_state.fm_rename_folder_id = None
                                st.rerun()

        # ── Files list (edit only available here, inside the folder) ──────
        if files:
            section_label(f"Files ({len(files)})")
            for f in files:
                fid      = f["id"]
                filename = f.get("filename", "")
                ext      = f.get("extension", ".txt")
                size_kb  = f.get("size_kb", 0)
                content  = f.get("content", "") or ""
                lang     = EXT_LANG.get(ext, "text")
                n_lines  = len(content.splitlines()) if content else 0
                created  = str(f.get("created_at", ""))[:10]
                is_prev  = st.session_state.fm_preview_id  == fid
                is_edit  = st.session_state.fm_edit_file_id == fid

                fi1, fi2, fi3, fi4 = st.columns([5, 1.3, 1.5, 1])
                with fi1:
                    st.markdown(
                        f'<div class="fm-row">'
                        f'<span class="fm-icon">{_ext_icon(ext)}</span>'
                        f'<div style="flex:1;min-width:0">'
                        f'<div class="fm-name">{filename}</div>'
                        f'<div class="fm-meta">{size_kb:.1f} KB · {n_lines} lines · {created}</div>'
                        f'</div>'
                        f'<span class="badge badge-cyan">{ext}</span>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                with fi2:
                    prev_lbl = "🔼 Close" if is_prev else "👁 View"
                    if st.button(prev_lbl, key=f"fm_prev_{fid}", use_container_width=True):
                        st.session_state.fm_preview_id   = None if is_prev else fid
                        st.session_state.fm_edit_file_id = None
                        st.rerun()
                with fi3:
                    # ✅ Edit is ONLY available from inside the folder
                    edit_lbl = "✖ Close" if is_edit else "✏️ Edit"
                    if st.button(edit_lbl, key=f"fm_edit_{fid}", use_container_width=True):
                        st.session_state.fm_edit_file_id = None if is_edit else fid
                        st.session_state.fm_preview_id   = None
                        st.rerun()
                with fi4:
                    if st.button("🗑️", key=f"fm_delfile_{fid}", use_container_width=True):
                        db.delete_file(fid)
                        if st.session_state.fm_preview_id   == fid: st.session_state.fm_preview_id   = None
                        if st.session_state.fm_edit_file_id == fid: st.session_state.fm_edit_file_id = None
                        st.rerun()

                # View preview
                if is_prev:
                    if content.strip():
                        code_preview(content, lang, f"fmp_{fid}")
                    else:
                        st.markdown('<p style="font-size:.75rem;color:var(--text-muted)">Empty file.</p>', unsafe_allow_html=True)

                # Edit — only available inside the folder (cur_id is not None)
                if is_edit:
                    new_content = st.text_area(
                        "Edit file content",
                        value=content,
                        height=300,
                        key=f"fm_edit_content_{fid}",
                        label_visibility="collapsed",
                    )
                    es1, es2, _ = st.columns([2, 2, 5])
                    with es1:
                        if st.button("💾 Save changes", key=f"fm_edsave_{fid}", use_container_width=True):
                            new_kb = len(new_content.encode()) / 1024
                            db.update_file_content(fid, new_content, round(new_kb, 2))
                            st.session_state.fm_edit_file_id = None
                            st.success("✅ File updated!")
                            st.rerun()
                    with es2:
                        if st.button("✖ Discard", key=f"fm_edcancel_{fid}", use_container_width=True):
                            st.session_state.fm_edit_file_id = None
                            st.rerun()

        elif not subfolders and not st.session_state.fm_show_upload and not st.session_state.fm_creating_folder:
            empty_state("📂", "This folder is empty",
                        "Use 'Upload File' to add a file, or create a sub-folder.")


# ══════════════════════════════════════════════════════════════════════════════
# MINI GAME — Snake (runs inside the sidebar footer / bottom of any page)
# ══════════════════════════════════════════════════════════════════════════════

def render_snake_game():
    """Compact Snake game rendered as an HTML widget."""
    st.markdown("""<div class="game-wrap">""", unsafe_allow_html=True)
    st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#050811;display:flex;flex-direction:column;align-items:center;justify-content:center;height:320px;font-family:'Inter',sans-serif}
canvas{border:1px solid rgba(77,159,255,0.25);border-radius:8px;background:#080d1a}
#hud{display:flex;justify-content:space-between;width:280px;margin-bottom:6px}
.hud-val{font-size:.7rem;font-weight:700;color:#4D9FFF;letter-spacing:.1em;text-transform:uppercase}
#msg{font-size:.68rem;color:#3D5070;margin-top:5px;text-align:center}
</style>
</head>
<body>
<div id="hud"><span class="hud-val">Score: <span id="sc">0</span></span><span class="hud-val">Best: <span id="hi">0</span></span></div>
<canvas id="c" width="280" height="250"></canvas>
<div id="msg">Arrow keys / WASD · Space to pause · R to restart</div>
<script>
const C=document.getElementById('c'),ctx=C.getContext('2d');
const W=28,H=25,SZ=10;
let snake,dir,food,score,best=0,paused,over,loop;

function init(){
  snake=[{x:14,y:12},{x:13,y:12},{x:12,y:12}];
  dir={x:1,y:0};food=rndFood();score=0;paused=false;over=false;
  clearInterval(loop);loop=setInterval(tick,130);
}
function rndFood(){
  let p;do{p={x:Math.floor(Math.random()*W),y:Math.floor(Math.random()*H)}}
  while(snake.some(s=>s.x===p.x&&s.y===p.y));return p;
}
function tick(){
  if(paused||over)return;
  const head={x:(snake[0].x+dir.x+W)%W,y:(snake[0].y+dir.y+H)%H};
  if(snake.some(s=>s.x===head.x&&s.y===head.y)){over=true;clearInterval(loop);draw();return;}
  snake.unshift(head);
  if(head.x===food.x&&head.y===food.y){score++;if(score>best)best=score;document.getElementById('sc').textContent=score;document.getElementById('hi').textContent=best;food=rndFood();}
  else snake.pop();
  draw();
}
function draw(){
  ctx.fillStyle='#080d1a';ctx.fillRect(0,0,W*SZ,H*SZ);
  // Food
  const gf=ctx.createRadialGradient(food.x*SZ+5,food.y*SZ+5,1,food.x*SZ+5,food.y*SZ+5,5);
  gf.addColorStop(0,'#fff');gf.addColorStop(1,'#FF4D6A');
  ctx.fillStyle=gf;ctx.beginPath();ctx.arc(food.x*SZ+5,food.y*SZ+5,4,0,Math.PI*2);ctx.fill();
  // Snake
  snake.forEach((s,i)=>{
    const g=ctx.createLinearGradient(s.x*SZ,s.y*SZ,s.x*SZ+SZ,s.y*SZ+SZ);
    g.addColorStop(0,i===0?'#00D4FF':'#4D9FFF');
    g.addColorStop(1,i===0?'#4D9FFF':'#A855F7');
    ctx.fillStyle=g;
    ctx.beginPath();ctx.roundRect(s.x*SZ+1,s.y*SZ+1,SZ-2,SZ-2,2);ctx.fill();
  });
  if(over){
    ctx.fillStyle='rgba(5,8,17,.75)';ctx.fillRect(0,0,W*SZ,H*SZ);
    ctx.fillStyle='#FF4D6A';ctx.font='bold 16px Inter';ctx.textAlign='center';
    ctx.fillText('Game Over',W*SZ/2,H*SZ/2-10);
    ctx.fillStyle='#4D9FFF';ctx.font='11px Inter';
    ctx.fillText('Press R to restart',W*SZ/2,H*SZ/2+12);
  }
  if(paused&&!over){
    ctx.fillStyle='rgba(5,8,17,.6)';ctx.fillRect(0,0,W*SZ,H*SZ);
    ctx.fillStyle='#4D9FFF';ctx.font='bold 14px Inter';ctx.textAlign='center';
    ctx.fillText('⏸ Paused',W*SZ/2,H*SZ/2);
  }
}
document.addEventListener('keydown',e=>{
  const k=e.key.toLowerCase();
  if(['arrowup','w'].includes(k)&&dir.y===0){dir={x:0,y:-1};}
  else if(['arrowdown','s'].includes(k)&&dir.y===0){dir={x:0,y:1};}
  else if(['arrowleft','a'].includes(k)&&dir.x===0){dir={x:-1,y:0};}
  else if(['arrowright','d'].includes(k)&&dir.x===0){dir={x:1,y:0};}
  else if(k===' '){paused=!paused;draw();}
  else if(k==='r'){init();}
  if(['arrowup','arrowdown','arrowleft','arrowright',' '].includes(e.key.toLowerCase()))e.preventDefault();
});
init();
</script>
</body>
</html>
""", height=320)
    st.markdown("</div>", unsafe_allow_html=True)
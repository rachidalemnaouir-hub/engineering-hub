"""
app.py — Engineering Hub
Main Streamlit application. All text in English.
"""
import streamlit as st
from datetime import date
import db_manager as db
import components as comp
from styles import DARK_CSS, LIGHT_CSS

# ══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Engineering Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

db.init_db()   # creates all tables (safe — IF NOT EXISTS)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

st.markdown(DARK_CSS if st.session_state.dark_mode else LIGHT_CSS, unsafe_allow_html=True)
comp.inject_css()


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div class="brand-wrap">
        <div class="brand-logo">⚡ Engineering Hub</div>
        <div class="brand-sub">Data Engineering Student</div>
    </div>
    """, unsafe_allow_html=True)

    mode_lbl = "☀️ Light Mode" if st.session_state.dark_mode else "🌙 Dark Mode"
    if st.button(mode_lbl, use_container_width=True, type="secondary"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    nav = st.radio("NAVIGATION", [
        "🏠 Overview",
        "🎓 Academic Projects",
        "🚀 Personal Projects",
        "📓 Stage Journal",
        "💼 Freelance",
        "📁 File Manager",
        "📊 Insights",
        "🎮 Mini Game",
    ])

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:.68rem;color:var(--text-muted);text-align:center;line-height:1.9">
        Streamlit · SQLite<br>
        <span style="color:var(--blue)">v3.0 — Pro Edition</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if nav == "🏠 Overview":
    comp.page_header("🏠", "Overview", "Your engineering command center")

    data = db.get_analytics()
    af   = db.get_all_files()
    afld = db.get_all_folders()

    # ── Stats row ─────────────────────────────────────────────────────────
    c1,c2,c3,c4,c5,c6 = st.columns(6)
    def _stat(col, num, lbl, color):
        col.markdown(f'<div class="stat-card"><div class="stat-num" style="color:{color}">{num}</div><div class="stat-lbl">{lbl}</div></div>', unsafe_allow_html=True)

    _stat(c1, data["total"],        "Total Projects", "var(--blue)")
    _stat(c2, data["completed"],    "Completed",      "var(--green)")
    _stat(c3, data["in_progress"],  "In Progress",    "var(--orange)")
    _stat(c4, data["logs_count"],   "Journal Logs",   "#A855F7")
    _stat(c5, len(af),              "Files",          "var(--cyan)")
    _stat(c6, f"{data['goals_done']}/{data['goals_total']}", "Goals", "var(--orange)")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Progress bars ─────────────────────────────────────────────────────
    total = data["total"]
    if total > 0:
        l,r = st.columns(2)
        with l:
            comp.section_label("Project Pipeline")
            for lbl,cnt,color in [
                ("To-do",   sum(1 for _ in db.get_academic_projects()+db.get_personal_projects()+db.get_freelance() if _["kanban_status"]=="To-do"),  "#FF8C42"),
                ("Doing",   sum(1 for _ in db.get_academic_projects()+db.get_personal_projects()+db.get_freelance() if _["kanban_status"]=="Doing"),  "#4D9FFF"),
                ("Done",    sum(1 for _ in db.get_academic_projects()+db.get_personal_projects()+db.get_freelance() if _["kanban_status"]=="Done"),   "#10F5A0"),
            ]:
                pct = int(cnt/total*100) if total else 0
                st.markdown(f"""<div style="margin-bottom:.8rem">
                    <div style="display:flex;justify-content:space-between;margin-bottom:.3rem">
                        <span style="font-size:.78rem;color:var(--text-secondary)">{lbl}</span>
                        <span style="font-size:.78rem;font-weight:700;color:{color}">{cnt} ({pct}%)</span>
                    </div>
                    <div style="height:5px;background:rgba(255,255,255,0.05);border-radius:99px">
                        <div style="width:{pct}%;height:100%;background:{color};border-radius:99px"></div>
                    </div>
                </div>""", unsafe_allow_html=True)

        with r:
            comp.section_label("By Category")
            for lbl,cnt,color in [
                ("🎓 Academic",  data["academic_count"],  "var(--blue)"),
                ("🚀 Personal",  data["personal_count"],  "#A855F7"),
                ("💼 Freelance", data["freelance_count"], "var(--green)"),
            ]:
                pct = int(cnt/total*100) if total else 0
                st.markdown(f"""<div style="margin-bottom:.8rem">
                    <div style="display:flex;justify-content:space-between;margin-bottom:.3rem">
                        <span style="font-size:.78rem;color:var(--text-secondary)">{lbl}</span>
                        <span style="font-size:.78rem;font-weight:700;color:{color}">{cnt}</span>
                    </div>
                    <div style="height:5px;background:rgba(255,255,255,0.05);border-radius:99px">
                        <div style="width:{pct}%;height:100%;background:{color};border-radius:99px"></div>
                    </div>
                </div>""", unsafe_allow_html=True)
    else:
        comp.empty_state("📊", "No data yet", "Start adding projects to see your overview.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ACADEMIC PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
elif nav == "🎓 Academic Projects":
    comp.page_header("🎓", "Academic Projects", "University coursework, research & assignments")
    tab1,tab2,tab3 = st.tabs(["📋 All Projects", "🗂 Kanban Board", "➕ Add Project"])

    with tab1:
        s = st.text_input("🔍 Search projects…", placeholder="Title, tech stack, description…", key="s_acad")
        rows = db.get_academic_projects(s.strip())
        if not rows:
            comp.empty_state("🎓", "No academic projects yet", "Go to the Add Project tab to create one.")
        else:
            comp.section_label(f"{len(rows)} project{'s' if len(rows)!=1 else ''} found")
            for p in rows:
                comp.project_card(p, "acad", db.update_academic_kanban, db.delete_academic_project)

    with tab2:
        kb = db.get_academic_projects()
        comp.kanban_board(kb) if kb else comp.empty_state("🗂", "No projects to display on the board.")

    with tab3:
        comp.section_label("New Academic Project")
        comp.add_project_form("acad", db.add_academic_project)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PERSONAL PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
elif nav == "🚀 Personal Projects":
    comp.page_header("🚀", "Personal Projects", "Side projects, experiments & passion builds")
    tab1,tab2,tab3 = st.tabs(["📋 All Projects", "🗂 Kanban Board", "➕ Add Project"])

    with tab1:
        s = st.text_input("🔍 Search projects…", placeholder="Title, tech stack, description…", key="s_pers")
        rows = db.get_personal_projects(s.strip())
        if not rows:
            comp.empty_state("🚀", "No personal projects yet", "Go to the Add Project tab to create one.")
        else:
            comp.section_label(f"{len(rows)} project{'s' if len(rows)!=1 else ''} found")
            for p in rows:
                comp.project_card(p, "pers", db.update_personal_kanban, db.delete_personal_project)

    with tab2:
        kb = db.get_personal_projects()
        comp.kanban_board(kb) if kb else comp.empty_state("🗂", "No projects to display on the board.")

    with tab3:
        comp.section_label("New Personal Project")
        comp.add_project_form("pers", db.add_personal_project)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: STAGE JOURNAL
# ══════════════════════════════════════════════════════════════════════════════
elif nav == "📓 Stage Journal":
    comp.page_header("📓", "Stage Journal", "Daily learnings, code snippets & goals")
    tab1,tab2,tab3 = st.tabs(["📅 Daily Logs", "🎯 Goals Tracker", "➕ Add Entry"])

    # ── Logs ──────────────────────────────────────────────────────────────
    with tab1:
        s = st.text_input("🔍 Search logs…", placeholder="Keywords, tags, code…", key="s_logs")
        logs = db.get_stage_logs(s.strip())
        if not logs:
            comp.empty_state("📓", "No journal entries yet", "Go to Add Entry to log your first day.")
        else:
            comp.section_label(f"{len(logs)} entr{'ies' if len(logs)!=1 else 'y'} found")
            for log in logs:
                comp.log_card(log, db.delete_stage_log)

    # ── Goals ─────────────────────────────────────────────────────────────
    with tab2:
        goals = db.get_stage_goals()
        if goals:
            comp.section_label("Goals Kanban")
            comp.kanban_board(goals, title_key="goal")
            st.markdown("<br>", unsafe_allow_html=True)
            comp.section_label(f"All Goals ({len(goals)})")
            for g in goals:
                comp.goal_card(g, db.update_stage_goal_kanban, db.delete_stage_goal)
        else:
            comp.empty_state("🎯", "No goals yet", "Add your first goal below.")

        st.markdown("<br>", unsafe_allow_html=True)
        comp.section_label("Add New Goal")

        if "gv" not in st.session_state: st.session_state.gv = 0
        gv = st.session_state.gv
        gc1,gc2 = st.columns(2)
        with gc1:
            g_text  = st.text_input("🎯 Goal *", placeholder="e.g. Master Apache Kafka",  key=f"g_t{gv}")
            g_pri   = st.selectbox("Priority", ["High","Medium","Low"],                    key=f"g_p{gv}")
        with gc2:
            g_dl = st.date_input("📅 Deadline (optional)", value=None,                     key=f"g_d{gv}")

        st.markdown("<br>", unsafe_allow_html=True)
        bc,_ = st.columns([2,7])
        with bc:
            if st.button("✅ Add Goal", key=f"g_add{gv}", use_container_width=True):
                if not g_text.strip():
                    st.error("Goal text is required.")
                else:
                    ok = db.add_stage_goal(g_text.strip(), g_pri, str(g_dl) if g_dl else "")
                    if ok:
                        st.success("✅ Goal added!")
                        st.session_state.gv += 1
                        st.rerun()

    # ── Add Entry ─────────────────────────────────────────────────────────
    with tab3:
        comp.section_label("New Journal Entry")
        if "lv" not in st.session_state: st.session_state.lv = 0
        lv = st.session_state.lv
        lc1,lc2 = st.columns(2)
        with lc1:
            l_date = st.date_input("📅 Date", value=date.today(),                            key=f"l_dt{lv}")
            l_tags = st.text_input("🏷 Tags", placeholder="kafka, python, airflow",          key=f"l_tg{lv}")
        with lc2:
            l_lang = st.selectbox("💻 Language",
                ["python","sql","bash","java","scala","javascript","yaml","json","other"],    key=f"l_lg{lv}")

        l_learn   = st.text_area("📖 Daily Learning *",
            placeholder="What did you learn? Problems solved? Insights?",
            height=120,                                                                       key=f"l_ln{lv}")
        l_snippet = st.text_area("💾 Code Snippet (optional)",
            placeholder="Paste your code here…",
            height=110,                                                                       key=f"l_sn{lv}")

        st.markdown("<br>", unsafe_allow_html=True)
        bsa,_ = st.columns([2,7])
        with bsa:
            if st.button("✅ Save Entry", key=f"l_sv{lv}", use_container_width=True):
                if not l_learn.strip():
                    st.error("Daily learning field is required.")
                else:
                    ok = db.add_stage_log(str(l_date), l_learn.strip(),
                                          l_snippet.strip(), l_lang, l_tags.strip())
                    if ok:
                        st.success("✅ Entry saved!")
                        st.session_state.lv += 1
                        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: FREELANCE
# ══════════════════════════════════════════════════════════════════════════════
elif nav == "💼 Freelance":
    comp.page_header("💼", "Freelance", "Client projects, contracts & deliverables")
    tab1,tab2,tab3 = st.tabs(["📋 All Projects", "🗂 Kanban Board", "➕ Add Project"])

    with tab1:
        s = st.text_input("🔍 Search…", placeholder="Client, title, tech stack…", key="s_free")
        rows = db.get_freelance(s.strip())
        if not rows:
            comp.empty_state("💼", "No freelance projects yet", "Go to Add Project to create one.")
        else:
            comp.section_label(f"{len(rows)} project{'s' if len(rows)!=1 else ''} found")
            for p in rows:
                comp.freelance_card(p, db.update_freelance_kanban, db.delete_freelance)

    with tab2:
        kb = db.get_freelance()
        comp.kanban_board(kb) if kb else comp.empty_state("🗂", "No projects to display on the board.")

    with tab3:
        comp.section_label("New Freelance Project")
        if "fv" not in st.session_state: st.session_state.fv = 0
        fv = st.session_state.fv
        fc1,fc2 = st.columns(2)
        with fc1:
            f_title  = st.text_input("📌 Project Title *", placeholder="e.g. E-commerce Dashboard", key=f"fr_t{fv}")
            f_client = st.text_input("👤 Client",           placeholder="e.g. TechCorp Ltd.",        key=f"fr_cl{fv}")
            f_tech   = st.text_input("🛠 Tech Stack",        placeholder="React, FastAPI, Postgres",  key=f"fr_sk{fv}")
        with fc2:
            f_status = st.selectbox("📊 Status", ["In Progress","Completed"],                        key=f"fr_st{fv}")
            f_budget = st.text_input("💰 Budget / Rate",    placeholder="e.g. 500 MAD, 2000 EUR",    key=f"fr_bg{fv}")
            f_desc   = st.text_area("📝 Description",       placeholder="Project scope…",
                                    height=100,                                                       key=f"fr_ds{fv}")

        st.markdown("<br>", unsafe_allow_html=True)
        bfa,_ = st.columns([2,7])
        with bfa:
            if st.button("✅ Add Project", key=f"fr_add{fv}", use_container_width=True):
                if not f_title.strip():
                    st.error("⚠️ Title is required.")
                else:
                    ok = db.add_freelance(f_title.strip(), f_client.strip(), f_tech.strip(),
                                          f_desc.strip(), f_budget.strip(), f_status)
                    if ok:
                        st.success(f"✅ **{f_title.strip()}** added!")
                        st.session_state.fv += 1
                        st.rerun()
                    else:
                        st.error("❌ Failed to save.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: FILE MANAGER
# ══════════════════════════════════════════════════════════════════════════════
elif nav == "📁 File Manager":
    comp.page_header("📁", "File Manager", "Organize your code files in folders")
    comp.file_manager_page(db)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: INSIGHTS
# ══════════════════════════════════════════════════════════════════════════════
elif nav == "📊 Insights":
    comp.page_header("📊", "Insights", "Analytics across all your projects & activities")

    data  = db.get_analytics()
    total = data["total"]

    comp.section_label("Overview")
    c1,c2,c3,c4,c5 = st.columns(5)
    def sc(col,num,lbl,color):
        col.markdown(f'<div class="stat-card"><div class="stat-num" style="color:{color}">{num}</div><div class="stat-lbl">{lbl}</div></div>', unsafe_allow_html=True)
    sc(c1,total,               "Total Projects","var(--blue)")
    sc(c2,data["completed"],   "Completed",     "var(--green)")
    sc(c3,data["in_progress"], "In Progress",   "var(--orange)")
    sc(c4,data["logs_count"],  "Journal Logs",  "#A855F7")
    sc(c5,f"{data['goals_done']}/{data['goals_total']}","Goals Done","var(--cyan)")

    st.markdown("<br>", unsafe_allow_html=True)
    cl,cr = st.columns(2)

    with cl:
        comp.section_label("Completion Rate")
        if total > 0:
            pct = int((data["completed"]/total)*100)
            st.markdown(f"""<div class="progress-ring-wrap">
                <div style="font-size:.7rem;font-weight:700;color:var(--text-muted);letter-spacing:.1em;text-transform:uppercase;margin-bottom:.4rem">Overall</div>
                <div class="progress-pct">{pct}%</div>
                <div style="font-size:.8rem;color:var(--text-secondary);margin:.4rem 0 .9rem">
                    {data['completed']} of {total} projects completed
                </div>
            </div>""", unsafe_allow_html=True)
            st.progress(pct/100)
            st.markdown("<br>", unsafe_allow_html=True)
            b1,b2,b3 = st.columns(3)
            def ms(col,num,lbl,c):
                col.markdown(f'<div style="text-align:center;padding:.8rem;background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:10px"><div style="font-size:1.5rem;font-weight:900;color:{c}">{num}</div><div style="font-size:.63rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em">{lbl}</div></div>', unsafe_allow_html=True)
            ms(b1,data["academic_count"],  "Academic",  "var(--blue)")
            ms(b2,data["personal_count"],  "Personal",  "#A855F7")
            ms(b3,data["freelance_count"], "Freelance", "var(--green)")
        else:
            comp.empty_state("📊","Add projects to see analytics.")

    with cr:
        comp.section_label("Top Technologies")
        top = data["top_tech"]
        if not top:
            comp.empty_state("🔧","Add tech stacks to your projects.")
        else:
            max_c = top[0][1]
            colors = ["linear-gradient(90deg,#4D9FFF,#00D4FF)","linear-gradient(90deg,#A855F7,#4D9FFF)",
                      "linear-gradient(90deg,#00D4FF,#10F5A0)","linear-gradient(90deg,#10F5A0,#00D4FF)",
                      "linear-gradient(90deg,#FF8C42,#A855F7)","linear-gradient(90deg,#FF4D6A,#FF8C42)"]
            for i,(tech,count) in enumerate(top[:8]):
                bp = int((count/max_c)*100)
                st.markdown(f"""<div class="tech-bar-item">
                    <div class="tech-bar-top">
                        <span class="tech-bar-name">{tech}</span>
                        <span class="tech-bar-count">{count} project{'s' if count!=1 else ''}</span>
                    </div>
                    <div class="tech-bar-track">
                        <div class="tech-bar-fill" style="width:{bp}%;background:{colors[i%len(colors)]}"></div>
                    </div>
                </div>""", unsafe_allow_html=True)

    if data["goals_total"] > 0:
        comp.section_label("Goals Progress")
        g_pct = int((data["goals_done"]/data["goals_total"])*100)
        g1,g2 = st.columns([2,1])
        with g1:
            st.markdown(f'<p style="font-size:.82rem;color:var(--text-muted);margin-bottom:.4rem">Completed: {data["goals_done"]} / {data["goals_total"]}</p>', unsafe_allow_html=True)
            st.progress(g_pct/100)
        with g2:
            st.markdown(f'<div class="progress-pct" style="font-size:2rem;margin-top:-.2rem">{g_pct}%</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: MINI GAME
# ══════════════════════════════════════════════════════════════════════════════
elif nav == "🎮 Mini Game":
    comp.page_header("🎮", "Mini Game", "Take a break — play Snake!")
    st.markdown("""
    <div style="font-size:.8rem;color:var(--text-muted);margin-bottom:1rem">
        🕹 <strong>Controls:</strong> Arrow keys or WASD to move &nbsp;·&nbsp;
        Space to pause &nbsp;·&nbsp; R to restart
    </div>
    """, unsafe_allow_html=True)
    comp.render_snake_game()
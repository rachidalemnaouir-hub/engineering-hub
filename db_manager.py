<<<<<<< HEAD
git add db_manager.py requirements.txt
git commit -m "feat: add Supabase PostgreSQL support"
git push
=======
import sqlite3
import os

DB_PATH = "engineering_hub.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS academic_projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        tech_stack TEXT DEFAULT '',
        description TEXT DEFAULT '',
        github_link TEXT DEFAULT '',
        status TEXT DEFAULT 'In Progress',
        kanban_status TEXT DEFAULT 'To-do',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
     
    c.execute('''CREATE TABLE IF NOT EXISTS personal_projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        tech_stack TEXT DEFAULT '',
        description TEXT DEFAULT '',
        github_link TEXT DEFAULT '',
        status TEXT DEFAULT 'In Progress',
        kanban_status TEXT DEFAULT 'To-do',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS stage_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        daily_learning TEXT DEFAULT '',
        code_snippet TEXT DEFAULT '',
        snippet_language TEXT DEFAULT 'python',
        tags TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS stage_goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        goal TEXT NOT NULL,
        kanban_status TEXT DEFAULT 'To-do',
        priority TEXT DEFAULT 'Medium',
        deadline TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS freelance_work (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        client TEXT DEFAULT '',
        tech_stack TEXT DEFAULT '',
        description TEXT DEFAULT '',
        budget TEXT DEFAULT '',
        status TEXT DEFAULT 'In Progress',
        kanban_status TEXT DEFAULT 'To-do',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # ── File Manager tables ──────────────────────────────────────────────────
    c.execute('''CREATE TABLE IF NOT EXISTS fm_folders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        parent_id INTEGER DEFAULT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS fm_files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder_id INTEGER DEFAULT NULL,
        filename TEXT NOT NULL,
        extension TEXT DEFAULT '',
        content TEXT DEFAULT '',
        size_kb REAL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(folder_id) REFERENCES fm_folders(id) ON DELETE CASCADE
    )''')

    conn.commit()
    conn.close()


# ── BACKWARD COMPAT aliases (used in old app.py) ────────────────────────────
def init_files_table():
    init_db()


# ════════════════════════════════════════════════════════════════════════════
# ACADEMIC PROJECTS
# ════════════════════════════════════════════════════════════════════════════

def add_academic_project(title, tech_stack, description, github_link, status):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO academic_projects (title,tech_stack,description,github_link,status,kanban_status) VALUES (?,?,?,?,?,'To-do')",
            (title, tech_stack, description, github_link, status)
        )
        conn.commit(); return True
    except Exception as e:
        print(f"DB Error: {e}"); return False
    finally:
        conn.close()


def get_academic_projects(search=""):
    conn = get_conn()
    q = f"%{search}%"
    if search:
        rows = conn.execute(
            "SELECT * FROM academic_projects WHERE title LIKE ? OR tech_stack LIKE ? OR description LIKE ? ORDER BY created_at DESC",
            (q, q, q)
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM academic_projects ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_academic_kanban(pid, kanban_status):
    conn = get_conn()
    conn.execute("UPDATE academic_projects SET kanban_status=? WHERE id=?", (kanban_status, pid))
    conn.commit(); conn.close()


def delete_academic_project(pid):
    conn = get_conn()
    conn.execute("DELETE FROM academic_projects WHERE id=?", (pid,))
    conn.commit(); conn.close()


# ════════════════════════════════════════════════════════════════════════════
# PERSONAL PROJECTS
# ════════════════════════════════════════════════════════════════════════════

def add_personal_project(title, tech_stack, description, github_link, status):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO personal_projects (title,tech_stack,description,github_link,status,kanban_status) VALUES (?,?,?,?,?,'To-do')",
            (title, tech_stack, description, github_link, status)
        )
        conn.commit(); return True
    except Exception as e:
        print(f"DB Error: {e}"); return False
    finally:
        conn.close()


def get_personal_projects(search=""):
    conn = get_conn()
    q = f"%{search}%"
    if search:
        rows = conn.execute(
            "SELECT * FROM personal_projects WHERE title LIKE ? OR tech_stack LIKE ? OR description LIKE ? ORDER BY created_at DESC",
            (q, q, q)
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM personal_projects ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_personal_kanban(pid, kanban_status):
    conn = get_conn()
    conn.execute("UPDATE personal_projects SET kanban_status=? WHERE id=?", (kanban_status, pid))
    conn.commit(); conn.close()


def delete_personal_project(pid):
    conn = get_conn()
    conn.execute("DELETE FROM personal_projects WHERE id=?", (pid,))
    conn.commit(); conn.close()


# ════════════════════════════════════════════════════════════════════════════
# STAGE LOGS
# ════════════════════════════════════════════════════════════════════════════

def add_stage_log(date, daily_learning, code_snippet, snippet_language, tags):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO stage_logs (date,daily_learning,code_snippet,snippet_language,tags) VALUES (?,?,?,?,?)",
            (date, daily_learning, code_snippet, snippet_language, tags)
        )
        conn.commit(); return True
    except Exception as e:
        print(f"DB Error: {e}"); return False
    finally:
        conn.close()


def get_stage_logs(search=""):
    conn = get_conn()
    q = f"%{search}%"
    if search:
        rows = conn.execute(
            "SELECT * FROM stage_logs WHERE daily_learning LIKE ? OR code_snippet LIKE ? OR tags LIKE ? ORDER BY date DESC",
            (q, q, q)
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM stage_logs ORDER BY date DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_stage_log(lid):
    conn = get_conn()
    conn.execute("DELETE FROM stage_logs WHERE id=?", (lid,))
    conn.commit(); conn.close()


# ════════════════════════════════════════════════════════════════════════════
# STAGE GOALS
# ════════════════════════════════════════════════════════════════════════════

def add_stage_goal(goal, priority, deadline):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO stage_goals (goal,priority,deadline,kanban_status) VALUES (?,?,?,'To-do')",
            (goal, priority, deadline)
        )
        conn.commit(); return True
    except Exception as e:
        print(f"DB Error: {e}"); return False
    finally:
        conn.close()


def get_stage_goals():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM stage_goals ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_stage_goal_kanban(gid, kanban_status):
    conn = get_conn()
    conn.execute("UPDATE stage_goals SET kanban_status=? WHERE id=?", (kanban_status, gid))
    conn.commit(); conn.close()


def delete_stage_goal(gid):
    conn = get_conn()
    conn.execute("DELETE FROM stage_goals WHERE id=?", (gid,))
    conn.commit(); conn.close()


# ════════════════════════════════════════════════════════════════════════════
# FREELANCE
# ════════════════════════════════════════════════════════════════════════════

def add_freelance(title, client, tech_stack, description, budget, status):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO freelance_work (title,client,tech_stack,description,budget,status,kanban_status) VALUES (?,?,?,?,?,?,'To-do')",
            (title, client, tech_stack, description, budget, status)
        )
        conn.commit(); return True
    except Exception as e:
        print(f"DB Error: {e}"); return False
    finally:
        conn.close()


def get_freelance(search=""):
    conn = get_conn()
    q = f"%{search}%"
    if search:
        rows = conn.execute(
            "SELECT * FROM freelance_work WHERE title LIKE ? OR client LIKE ? OR tech_stack LIKE ? ORDER BY created_at DESC",
            (q, q, q)
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM freelance_work ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_freelance_kanban(pid, kanban_status):
    conn = get_conn()
    conn.execute("UPDATE freelance_work SET kanban_status=? WHERE id=?", (kanban_status, pid))
    conn.commit(); conn.close()


def delete_freelance(pid):
    conn = get_conn()
    conn.execute("DELETE FROM freelance_work WHERE id=?", (pid,))
    conn.commit(); conn.close()


# ════════════════════════════════════════════════════════════════════════════
# FILE MANAGER — FOLDERS
# ════════════════════════════════════════════════════════════════════════════

def create_folder(name: str, parent_id=None) -> bool:
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO fm_folders (name, parent_id) VALUES (?,?)",
            (name.strip(), parent_id)
        )
        conn.commit(); return True
    except Exception as e:
        print(f"DB Error: {e}"); return False
    finally:
        conn.close()


def get_folders(parent_id=None) -> list:
    conn = get_conn()
    if parent_id is None:
        rows = conn.execute(
            "SELECT * FROM fm_folders WHERE parent_id IS NULL ORDER BY name"
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM fm_folders WHERE parent_id=? ORDER BY name", (parent_id,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_folders() -> list:
    conn = get_conn()
    rows = conn.execute("SELECT * FROM fm_folders ORDER BY name").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_folder(fid: int):
    conn = get_conn()
    # Delete all files in folder first
    conn.execute("DELETE FROM fm_files WHERE folder_id=?", (fid,))
    conn.execute("DELETE FROM fm_folders WHERE id=?", (fid,))
    conn.commit(); conn.close()


def rename_folder(fid: int, new_name: str):
    conn = get_conn()
    conn.execute("UPDATE fm_folders SET name=? WHERE id=?", (new_name.strip(), fid))
    conn.commit(); conn.close()


# ════════════════════════════════════════════════════════════════════════════
# FILE MANAGER — FILES
# ════════════════════════════════════════════════════════════════════════════

def save_file(filename: str, extension: str, content: str,
              size_kb: float, folder_id=None) -> bool:
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO fm_files (folder_id,filename,extension,content,size_kb) VALUES (?,?,?,?,?)",
            (folder_id, filename, extension, content, size_kb)
        )
        conn.commit(); return True
    except Exception as e:
        print(f"DB Error: {e}"); return False
    finally:
        conn.close()


# Backward compat alias
def save_uploaded_file(filename: str, extension: str, content: str, size_kb: float) -> bool:
    return save_file(filename, extension, content, size_kb, folder_id=None)


def get_files(folder_id=None) -> list:
    conn = get_conn()
    if folder_id is None:
        rows = conn.execute(
            "SELECT * FROM fm_files WHERE folder_id IS NULL ORDER BY filename"
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM fm_files WHERE folder_id=? ORDER BY filename", (folder_id,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_files() -> list:
    conn = get_conn()
    rows = conn.execute("SELECT * FROM fm_files ORDER BY filename").fetchall()
    conn.close()
    return [dict(r) for r in rows]


# Backward compat alias
def get_uploaded_files() -> list:
    return get_all_files()


def delete_file(fid: int):
    conn = get_conn()
    conn.execute("DELETE FROM fm_files WHERE id=?", (fid,))
    conn.commit(); conn.close()


# Backward compat alias
def delete_uploaded_file(fid: int):
    delete_file(fid)


def move_file(fid: int, new_folder_id):
    conn = get_conn()
    conn.execute("UPDATE fm_files SET folder_id=? WHERE id=?", (new_folder_id, fid))
    conn.commit(); conn.close()


def get_file_content(fid: int) -> dict:
    conn = get_conn()
    row = conn.execute("SELECT * FROM fm_files WHERE id=?", (fid,)).fetchone()
    conn.close()
    return dict(row) if row else {}


# ════════════════════════════════════════════════════════════════════════════
# ANALYTICS
# ════════════════════════════════════════════════════════════════════════════

def get_analytics() -> dict:
    conn = get_conn()
    academic  = [dict(r) for r in conn.execute("SELECT status,tech_stack FROM academic_projects").fetchall()]
    personal  = [dict(r) for r in conn.execute("SELECT status,tech_stack FROM personal_projects").fetchall()]
    freelance = [dict(r) for r in conn.execute("SELECT status,tech_stack FROM freelance_work").fetchall()]
    logs_count = conn.execute("SELECT COUNT(*) as c FROM stage_logs").fetchone()["c"]
    goals      = [dict(r) for r in conn.execute("SELECT kanban_status FROM stage_goals").fetchall()]
    conn.close()

    all_p      = academic + personal + freelance
    total      = len(all_p)
    completed  = sum(1 for p in all_p if p["status"] == "Completed")
    in_progress = total - completed

    tech_counter = {}
    for p in all_p:
        if p.get("tech_stack"):
            for t in p["tech_stack"].split(","):
                t = t.strip()
                if t:
                    tech_counter[t] = tech_counter.get(t, 0) + 1

    top_tech   = sorted(tech_counter.items(), key=lambda x: -x[1])
    goals_done = sum(1 for g in goals if g["kanban_status"] == "Done")

    return {
        "total": total, "completed": completed, "in_progress": in_progress,
        "academic_count": len(academic), "personal_count": len(personal),
        "freelance_count": len(freelance), "logs_count": logs_count,
        "goals_done": goals_done, "goals_total": len(goals),
        "top_tech": top_tech, "tech_counter": tech_counter,
    }

def update_file_content(fid: int, new_content: str, new_size_kb: float):
    conn = get_conn()
    conn.execute("UPDATE fm_files SET content=?, size_kb=? WHERE id=?",
                 (new_content, new_size_kb, fid))
    conn.commit(); conn.close()

def create_folder_get_id(name: str, parent_id=None):
    """Create a folder and return its new id (or None on failure)."""
    conn = get_conn()
    try:
        cur = conn.execute(
            "INSERT INTO fm_folders (name, parent_id) VALUES (?,?)",
            (name.strip(), parent_id)
        )
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print(f"DB Error: {e}"); return None
    finally:
        conn.close()
>>>>>>> 719645f782b793a84316f5c384c5b5896efbc312

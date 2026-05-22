import sqlite3

# =========================================

conn = sqlite3.connect(
    "database/jarvis.db",
    check_same_thread=False
)

cursor = conn.cursor()

# =========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")

conn.commit()

# =========================================

def save_message(role, message):

    cursor.execute(
        "INSERT INTO chat_history(role, message) VALUES(?, ?)",
        (role, message)
    )

    conn.commit()
import sqlite3

def init_db():
    conn = sqlite3.connect("alerts.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS alerts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emotion TEXT,
            time TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_alert(emotion, time):
    conn = sqlite3.connect("alerts.db")
    c = conn.cursor()
    c.execute("INSERT INTO alerts (emotion,time) VALUES (?,?)", (emotion,time))
    conn.commit()
    conn.close()

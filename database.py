import sqlite3
import os

DB_PATH = "logs/usb_logs.db"

def init_db():
    os.makedirs("logs", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usb_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_name TEXT,
        event_type TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def log_event(device_name, event_type):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usb_logs(device_name, event_type)
    VALUES (?, ?)
    """, (device_name, event_type))

    conn.commit()
    conn.close()

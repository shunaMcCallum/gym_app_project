import sqlite3
import os

def get_db():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, "gym_db.db")
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys = 1")
    conn.row_factory = sqlite3.Row
    return conn

def run_sql(sql, values = []):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sql, values)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results
import sqlite3

DB_NAME = "campus_event.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # hasil bisa diakses seperti dict
    return conn

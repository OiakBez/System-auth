import sqlite3
from werkzeug.security import generate_password_hash

def get_db_connection():
    connection = sqlite3.connect("system_auth.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email_verified INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

def add_user(name, email, password):

    conn = get_db_connection()

    password_hash = generate_password_hash(password)

    cursor = conn.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        (name, email, password_hash)
    )

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return user_id
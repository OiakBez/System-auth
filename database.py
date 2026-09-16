import sqlite3
import secrets
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
            email_verified INTEGER DEFAULT 0,
            verification_token TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_user(name, email, password):

    conn = get_db_connection()

    password_hash = generate_password_hash(password)

    verification_token = secrets.token_urlsafe(32)

    cursor = conn.execute(
        """
        INSERT INTO users (name, email, password, verification_token)
        VALUES (?, ?, ?, ?)
        """,
        (name, email, password_hash, verification_token)
    )

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return user_id, verification_token

def get_user_by_verification_token(token):
    conn = get_db_connection()

    user = conn.execute(
        """
        SELECT * FROM users WHERE verification_token = ?
        """,
        (token,)
    ).fetchone()

    conn.close()

    return user

def verify_user(user_id):
    conn = get_db_connection()

    conn.execute(
        """
        UPDATE users SET email_verified = 1,
        verification_token = NULL WHERE id = ?
        """,
        (user_id,)
    )

    conn.commit()
    conn.close()
import sqlite3
from config import config


def init_db():
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            predicted_intent TEXT,
            actual_intent TEXT,
            response TEXT
        )
    ''')
    conn.commit()
    conn.close()


def log_interaction(user_input, predicted_intent, actual_intent, response):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO interactions (user_input, predicted_intent, actual_intent, response)
        VALUES (?, ?, ?, ?)
    ''', (user_input, predicted_intent, actual_intent, response))
    conn.commit()
    conn.close()


def log_feedback(data):
    user_input = data.get("user_input")
    bot_response = data.get("bot_response")
    is_helpful = data.get("is_helpful")
    actual_intent = None if is_helpful else "unknown"

    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE interactions
        SET actual_intent = ?
        WHERE user_input = ? AND response = ?
    ''', (actual_intent, user_input, bot_response))
    conn.commit()
    conn.close()
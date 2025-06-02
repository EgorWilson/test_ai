import sqlite3
from datetime import datetime
import os

# Подключение к БД
from pathlib import Path

def get_db_connection():
    # Создаём папку data, если её нет
    Path("data").mkdir(exist_ok=True)

    # Указываем полный путь к файлу БД
    db_path = os.path.join("data", "database.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Инициализация БД
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        tg_id INTEGER PRIMARY KEY,
        registration_date TEXT NOT NULL,
        is_premium BOOLEAN DEFAULT FALSE,
        email TEXT DEFAULT NULL
    )
    ''')

    conn.commit()
    conn.close()


# Добавление нового пользователя
def add_user(tg_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Проверяем, есть ли пользователь уже в БД
    cursor.execute('SELECT tg_id FROM users WHERE tg_id = ?', (tg_id,))
    if not cursor.fetchone():
        registration_date = datetime.now().isoformat(' ')
        cursor.execute(
            'INSERT INTO users (tg_id, registration_date) VALUES (?, ?)',
            (tg_id, registration_date)
        )

    conn.commit()
    conn.close()


# Обновление статуса подписки
def set_premium(tg_id: int, is_premium: bool = True):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE users SET is_premium = ? WHERE tg_id = ?',
        (is_premium, tg_id)
    )

    conn.commit()
    conn.close()


# Получение информации о пользователе
def get_user(tg_id: int) -> dict:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE tg_id = ?', (tg_id,))
    user = cursor.fetchone()
    conn.close()

    return dict(user) if user else None
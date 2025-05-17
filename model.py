import hashlib
import sqlite3
class User:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
        username TEXT NOT NULL
        password TEXT NOT NULL
        )''')
        self.connection.commit()
    def get_users(self):
        self.cursor.execute('''SELECT * FROM Users''')
        return self.cursor.fetchone()
    def user_registration(self, username, password):
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('''INSERT INTO Users(username, password) VALUES (?, ?)''', (username, hash_password))
        self.connection.commit()
        return "Вы успешно зарегистрированы"
    def sign_in(self, username, password):
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('''SELECT * FROM Users WHERE username = ? AND password = ?''', (username, hash_password))
        if self.cursor.fetchone() is None:
            return "Неверный логин или пароль"
        return "Вы успешно вошли"
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

data_dir = r'C:\Users\student\AppData\Local\Google\Chrome\User Data'
options = Options()
options.add_argument(f'--user-data-dir={data_dir}')
options.add_argument('--profile-directory=Profile 2')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
print(options.arguments)
driver = webdriver.Chrome(options=options)
driver.get("https://github.com/")

from view import *
from model import *
class Controller:
    def __init__(self, root):
        self.user = User()
        self.passwords = PasswordGetter()
        self.view = View(root)
        self._setup_handlers()

    def _setup_handlers(self):
        self.view.set_handlers(
            self.handle_register,
            self.handle_login,
            self.handle_logout,
            self.handle_delete
        )

    def handle_register(self):
        username, password = self.view.get_credentials()
        if not username or not password:
            self.view.show_message("Все поля должны быть заполнены!", "red")
            return

        if self.user.user_registration(username, password):
            self.view.show_success_page(f"Пароли:\n {self.passwords.get_passwords()}")
        else:
            self.view.show_message("Пользователь уже существует!", "red")

    def handle_login(self):
        username, password = self.view.get_credentials()
        if not username or not password:
            self.view.show_message("Все поля должны быть заполнены!", "red")
            return

        if self.user.sign_in(username, password):
            self.view.show_success_page(f"Пароли:\n {self.passwords.get_passwords()}")
        else:
            self.view.show_message("Неверные учетные данные!", "red")

    def handle_logout(self):
        self.view.show_login_page()
    def handle_delete(self):
        self.passwords.delete_passwords()
        self.view.show_success_page(f"Пароли:\n {self.passwords.get_passwords()}")

import tkinter as tk


class View:
    def __init__(self, master):
        self.master = master
        master.title("Регистрация/Вход")
        master.geometry("500x500")

        # Создаем контейнеры для разных страниц
        self.login_frame = tk.Frame(master)
        self.success_frame = tk.Frame(master)

        # Инициализация страниц
        self._setup_login_page()
        self._setup_success_page()

        # Показываем стартовую страницу
        self.show_login_page()

    def _setup_login_page(self):
        # Элементы для страницы входа/регистрации
        self.username_label = tk.Label(self.login_frame, text="Имя пользователя:")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.login_frame, text="Пароль:")
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        self.btn_frame = tk.Frame(self.login_frame)
        self.btn_frame.pack(pady=10)

        self.register_btn = tk.Button(self.btn_frame, text="Зарегистрироваться", width=15)
        self.register_btn.pack(side=tk.LEFT, padx=5)

        self.login_btn = tk.Button(self.btn_frame, text="Войти", width=15)
        self.login_btn.pack(side=tk.RIGHT, padx=5)

        self.message_label = tk.Label(self.login_frame, text="", fg="black")
        self.message_label.pack(pady=5)

    def _setup_success_page(self):
        # Элементы для страницы успешного входа
        self.success_label = tk.Label(self.success_frame, text="", font=('Arial', 14))
        self.success_label.pack(pady=20)

        self.logout_btn = tk.Button(self.success_frame, text="Выйти", width=15)
        self.logout_btn.pack(pady=10)

    def set_handlers(self, register_handler, login_handler, logout_handler):
        self.register_btn.config(command=register_handler)
        self.login_btn.config(command=login_handler)
        self.logout_btn.config(command=logout_handler)

    def show_login_page(self):
        self.success_frame.pack_forget()
        self.login_frame.pack()
        self.clear_entries()
        self.message_label.config(text="")

    def show_success_page(self, message):
        self.login_frame.pack_forget()
        self.success_label.config(text=message)
        self.success_frame.pack()

    def get_credentials(self):
        return (self.username_entry.get().strip(),
                self.password_entry.get().strip())

    def show_message(self, message, color="black"):
        self.message_label.config(text=message, fg=color)
        self.clear_entries()

    def clear_entries(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

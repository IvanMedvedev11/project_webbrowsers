from tkinter import *
import time
root = Tk()
root.geometry("500x400")
class Windows:
    def login_window(self):
        for widget in root.winfo_children():
            widget.destroy()
        help1 = Label(root, text="Имя пользователя:")
        help1.place(x=200, y=100)
        username = Entry(root, width=13)
        username.place(x=200, y=125)
        help2 = Label(root, text="Пароль:")
        help2.place(x=200, y=150)
        password = Entry(root, width=13)
        password.place(x=200, y=175)
        button = Button(root, text="Войти", bg="red", fg="white", width=10)
        button.place(x=200, y=200)
    def register_window(self):
        for widget in root.winfo_children():
            widget.destroy()
        help1 = Label(root, text="Имя пользователя:")
        help1.place(x=200, y=100)
        username = Entry(root, width=13)
        username.place(x=200, y=125)
        help2 = Label(root, text="Пароль:")
        help2.place(x=200, y=150)
        password = Entry(root, width=13)
        password.place(x=200, y=175)
        button = Button(root, text="Регистрация", bg="red", fg="white", width=10)
        button.place(x=200, y=200)
root.mainloop()

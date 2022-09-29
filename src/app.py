from functools import partial
from tkinter import Tk, Toplevel, ttk

from auth import Auth


def new_window(master):
    new_window = Toplevel(master)
    new_window.title("New Window")
    new_window.geometry("200x200")
    ttk.Label(new_window, text="This is a new window").pack()
    ttk.Button(new_window, text="Quit", command=new_window.destroy).pack()


class App:
    def show_login_window(self):
        root = Tk()

        style = ttk.Style(root)
        style.theme_use("clam")

        frm = ttk.Frame(root, padding=10)
        frm.pack()

        username_entry = ttk.Entry(frm, width=15)
        username_entry.grid(column=0, row=0)
        password_entry = ttk.Entry(frm, show="*", width=15)
        password_entry.grid(column=0, row=1)
        ttk.Label(frm, text="").grid(column=0, row=2)

        def login():
            if Auth().login(username_entry.get(), password_entry.get()):
                root.destroy()
                self.show_main_window()

        ttk.Button(
            frm,
            text="Login",
            command=login,
        ).grid(column=0, row=2)

        root.mainloop()

    def show_main_window(self):
        root = Tk()

        style = ttk.Style(root)
        style.theme_use("clam")

        frm = ttk.Frame(root, padding=10)
        frm.pack()

        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

        ttk.Button(frm, text="New", command=partial(new_window, root)).grid(
            column=1, row=2
        )

        root.mainloop()

    def start(self):
        auth = Auth()

        if auth.has_valid_token():
            self.show_main_window()
        else:
            self.show_login_window()


if __name__ == "__main__":
    App().start()

from functools import partial
from tkinter import BOTH, Tk, Toplevel, ttk

from services.auth import Auth
from services.checklists import Checklists


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
        self.root = Tk()
        self.root.title("Mono Project")

        style = ttk.Style(self.root)
        style.theme_use("clam")

        frm = ttk.Frame(self.root, padding=10)
        frm.pack()

        ttk.Label(frm, text="Mono Project").grid(column=0, row=0)
        ttk.Button(frm, text="Checklists", command=self.show_checklists_window).grid(
            column=0, row=2
        )

        self.root.mainloop()

    def show_checklists_window(self):
        self.hide()
        checlists_window = Toplevel(self.root)
        checlists_window.title("Checklists")

        checklists = Checklists().list()

        frm = ttk.Frame(checlists_window, padding=10)
        frm.pack(fill=BOTH, expand=True)

        ttk.Label(frm, text="Checklists").pack()

        def destroy(*args, **kwargs):
            self.show()
            checlists_window.destroy()

        checlists_window.bind("<Destroy>", destroy)

        for i, checklist in enumerate(checklists):
            ttk.Button(
                frm, text=checklist.name, command=partial(new_window, checlists_window)
            ).pack()

        checlists_window.mainloop()

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.deiconify()

    def start(self):
        auth = Auth()

        if auth.has_valid_token():
            self.show_main_window()
        else:
            self.show_login_window()


if __name__ == "__main__":
    App().start()

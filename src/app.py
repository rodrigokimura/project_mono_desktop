from functools import partial
from tkinter import Tk, Toplevel, ttk

from auth import login


def new_window(master):
    new_window = Toplevel(master)
    new_window.title("New Window")
    new_window.geometry("200x200")
    ttk.Label(new_window, text="This is a new window").pack()
    ttk.Button(new_window, text="Quit", command=new_window.destroy).pack()


root = Tk()

style = ttk.Style(root)
style.theme_use("clam")


frm = ttk.Frame(root, padding=10)
frm.pack()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


ttk.Button(frm, text="New", command=partial(new_window, root)).grid(column=1, row=2)

username_entry = ttk.Entry(frm, width=15)
username_entry.grid(column=0, row=1)
password_entry = ttk.Entry(frm, show="*", width=15)
password_entry.grid(column=0, row=2)

ttk.Button(
    frm, text="Login", command=lambda: login(username_entry.get(), password_entry.get())
).grid(column=1, row=1)

root.mainloop()

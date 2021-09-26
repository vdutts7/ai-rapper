import tkinter as tk

class CTkEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Roboto", 10), fg="blue", bg="white")

class CTkButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Roboto", 10), fg="blue", bg="white")

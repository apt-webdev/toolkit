from model import Model
from view import View
import tkinter as tk
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join('icon', 'tool.png')


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self.model)

    def run(self):
        self.root.geometry('400x400')
        self.root.title("toolkit")
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file=icon))
        self.root.deiconify()
        self.root.mainloop()

    # TODO: Event handlers

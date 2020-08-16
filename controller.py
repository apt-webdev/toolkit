from model import Model
from view import View, BOTTOM
import tkinter as tk
import os
from tkinter import filedialog
from shutil import copyfile
from container import Container

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join('icon', 'tool.png')


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()

        self.view = View(self.root, self.model, self)

    def run(self):
        self.root.geometry('400x400')
        self.root.title("toolkit")
        self.root.tk.call('wm', 'iconphoto', self.root.w, tk.PhotoImage(file=icon))
        self.root.deiconify()
        self.root.mainloop()

    def openFile(self):
        filename = self.model.get_file_path(self.root)
        if self.model.verify_extension(self,filename, ".bin"):
            self.view.path["text"] = filename
            self.view.path.pack(side=BOTTOM)
            copyfile(filename, "db/" + filename.split('/')[-1])
            print(filename)

    # TODO: Event handlers




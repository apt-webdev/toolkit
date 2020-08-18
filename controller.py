from model import Model
from view import View
import tkinter as tk
from tkinter import *
import os
from shutil import copyfile
from container import Container

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join('icon', 'tool.png')


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.var_set = StringVar()
        self.view = View(self.root, self.model, self)

    def run(self):
        self.root.geometry('400x400')
        self.root.title("toolkit")
        self.root.tk.call('wm', 'iconphoto', self.root.w, tk.PhotoImage(file=icon))
        self.root.deiconify()
        self.root.mainloop()

    def openfile(self):
        filename = self.model.get_file_path(self.root)
        if self.model.verify_extension(self, filename, ".bin"):
            self.view.path["text"] = filename
            self.view.path.pack(side=BOTTOM)
            copyfile(filename, "db/" + filename.split('/')[-1])
            print(filename)

    def selectdb(self, root):
        files = self.model.db_files
        print(files)
        lab = Container.create_label(root, "Choose a db file to import:", "Calibri", "10")
        Container.container_pack(lab, None)
        # self.var_set = Container.var_radiobutton("srt", files[0])
        # self.var_set = StringVar()
        self.var_set.set(self.model.split_path_name(files[0], "\\", 1))
        print(files[0], self.var_set.get())
        set_radio = []
        for item in files:
            item = self.model.split_path_name(item, "\\", 1)
            radio_butt = Container.create_radiobutton(root, item, self.var_set, item)
            set_radio.append(radio_butt)
            Container.container_pack(radio_butt, None)
        self.submit_radiobutton(root, set_radio, lab)

    def submit_radiobutton(self, root, set_radio, lab):
        selected = Container.create_button(root, "Submit", None, None)
        Container.container_pack(selected, None)
        selected["command"] = lambda: self.submit_radio_file(root, set_radio, lab, selected)

    def submit_radio_file(self, root, set_radio, lab, selected):
        self.model.update_imported_file(self.var_set.get())
        label = Container.create_label(root, self.model.import_db_file, "calibri", "10")
        Container.container_pack(label, None)
        for item in set_radio:
            Container.container_pack_forget(lab)
            Container.container_pack_forget(item)
            Container.container_pack_forget(selected)

        print(self.model.import_db_file)

# TODO: Event handlers

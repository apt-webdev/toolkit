import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from model import Model
from view import View
from container import Container
from shutil import copyfile

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join('icon', 'tool.png')


class Controller:
    def __init__(self):
        self.root = tk.Tk()  # create board
        self.model = Model()
        self.var_set = StringVar()
        self.view = View(self.root, self.model, self)


    def run(self):
        self.root.geometry('500x500')
        self.root.title(" toolkit")
        # self.root.tk.call('wm', 'iconphoto', self.root.w, tk.PhotoImage(file=icon))
        self.root.deiconify()
        self.root.mainloop()

    # Import dirname = file or baseline
    def open_file(self, dir_name):
        file_name = self.model.get_file(self.root) # open standard file - raw_data
        if file_name != '':
            if dir_name == 'db_users':  # for users files .bin
                extension = '.bin'
            else:  # for baseline .txt
                extension = '.txt'
            if self.model.verify_extension(self, file_name, extension) and file_name!='':
                copyfile(file_name, dir_name + "/" + file_name.split('/')[-1])
                print(dir_name, file_name)
                self.clear_status(1)
            else:
                self.message_box("error", "Error extension file.")

    def clear_status(self, flag):
        if flag == 1: self.view.btn3["state"] = "active"
        else: self.view.btn3["state"] = "disabled"

    # Process raw data
    def process_raw(self, root):
        files, baselines = self.model.get_folders() # get lists with the files
        print("Files:", files)
        print("Baseline:", baselines)

        if len(files)==0:
            self.message_box("warning", "No file found in:\n" + THIS_FOLDER +" \db_users")
        elif len(baselines)==0:
            self.message_box("warning", "No file found in:\n" + THIS_FOLDER + "\\baseline")
        else:
            # Take off welcome label
            # Container.ctn_grid_forget(self.view.wel)
            # Container.ctn_grid(self.view.btn4, 10, 0 , 10, 60)
            self.clear_status(0)
            #lb_array = []
            row = 5  #lina do system grid onde posso começar a escrever
            for item in files: # mostra os files a ser processados
                lb_item = Container.create_label(root, item, "Calibri", "10")
                Container.ctn_grid(lb_item, row, 0, 10, 0)
                row = row + 2
                #.append(lb_item)
            self.model.get_baseline_id()
            self.model.get_tables()

    @staticmethod
    def message_box(type, message):
        if type == "error":
            messagebox.showerror("Error Message", message)
        if type == "warning":
            messagebox.showwarning("Warning Message", message)
        if type == "info":
            messagebox.showinfo("Information", message)
        else:
            pass



# TODO: Event handlers

from functools import partial
from tkinter import *
from tkinter import filedialog
from shutil import copyfile
from container import Container


class View:
    def __init__(self, root, model, controller):
        # menu = Container.create_menu(root, 0)

        # self.file = Container.create_menu(menu, 0)
        # menu.add_cascade(label="File", menu=self.file)
        # file.add_command(label="Open File", command=partial(self.openFile, root))
        # self.file.add_command(label="Open File", command=controller.openfile)
        # self.file.add_command(label="Import User File", command=partial(controller.selectdb, root))
        # self.file.add_command(label="Import Baseline File", command=partial(self.openFile, root))

        # edit_menu = Menu(menu, tearoff=0)
        # menu.add_cascade(label="Edit", menu=edit_menu)
        # edit_menu.add_command(label="Plot Data", command=self.cmdo)
        # edit_menu.add_command(label="Show Data", command=self.cmdo)

        # menu.add_command(label="Quit", command=root.destroy)
        # root.config(menu=menu)

        self.wel = Container.create_label(root, "Welcome to toolkit!", "Calibri", "10")
        Container.ctn_grid(self.wel, 0, 0, 200, 10)
        # self.wel.grid(row=0, column=0, padx=200, pady=10)
        # self.bey = Container.create_label(root, "Bey!", "Calibri", "10")
        # self.bey.pack_forget()
        # self.path = Container.create_label(root, text="Loading...", font="Calibri", size="10")
        # self.path["state"] = "disabled"
        # self.path = Container.container_pack_forget(self.path)

        # radio selection
        # v = StringVar(root, "1")
        # values = {"RadioButton 1": "1",
        #          "RadioButton 2": "2",
        #          "RadioButton 3": "3",
        #          "RadioButton 4": "4",
        #          "RadioButton 5": "5"}
        # for (text, value) in values.items():
        #    Radiobutton(root, text=text, variable=v,value=value).pack()

        self.btn1 = Container.create_button(root, "Import Files", "Calibri")
        self.btn1.grid(row=1, column=0, padx=200, pady=10)
        self.btn1["command"] = partial(controller.open_file, "db_users")

        self.btn2 = Container.create_button(root, "Import Baseline", "Calibri")
        self.btn2.grid(row=2, column=0, padx=10, pady=10)
        self.btn2["command"] = partial(controller.open_file, "baseline")

        self.btn3 = Container.create_button(root, "Process Data", "Calibri")
        self.btn3.grid(row=3, column=0, padx=10, pady=10)
        self.btn3["command"] = partial(controller.process_raw, root)

        self.btn4 = Container.create_button(root, "Quit", "Calibri")
        self.btn4.grid(row=15, column=0, padx=10, pady=100)
        self.btn4["command"] = root.destroy




        #self.lb_status = Container.create_label(root, "Status: ", "Calibri", "10")
        #Container.ctn_grid_forget(self.lb_status)


        # Container.ctn_grid_forget(self.lb_status)

        # file_menu.add_command(label="Import Files", command=partial(self.importFile, root))

        #self.myLabel1 = Label(root, text="Welcome to toolkit!").pack()  # .grid(row = 1 ,column = 1)
        #self.myLabel2 = Label(root, text="Bey!").pack()  # .grid(row=2, column=1)

        # self.close_Button(root)
        # if model.verify_import(self, 'db_users/x.bin'):
        #    Label(root, text="File path verified!").pack()

    @staticmethod
    def cmdo(root):
        Label(root, text="Path: ").pack()

    @staticmethod
    def close_button(root):
        Button(root, text="Quit", command=root.destroy).pack()

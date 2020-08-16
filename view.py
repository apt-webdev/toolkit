from functools import partial
from tkinter import *
from tkinter import filedialog
from shutil import copyfile
from container import Container


class View:
    def __init__(self, root, model, controller):
        menu = Container.create_menu(root, 0)

        file = Container.create_menu(menu, 0)
        menu.add_cascade(label="File", menu=file)
        # file.add_command(label="Open File", command=partial(self.openFile, root))
        file.add_command(label="Open File", command=controller.openFile)

        edit_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Plot Data", command=self.cmdo)
        edit_menu.add_command(label="Show Data", command=self.cmdo)

        menu.add_command(label="Quit", command=root.destroy)
        root.config(menu=menu)

        self.wel = Container.create_label(root, "Welcome to toolkit!", "Calibri", "10").pack()
        self.bey = Container.create_label(root, "Bey!", "Calibri", "10").pack()

        self.path = Container.create_label(root, text="Loading...", font="Calibri", size="10")
        self.path["state"]="disabled"
        self.path.pack_forget()

        # self.btn = Container.create_button(root, "Click me!", "Calibri", "10" ).pack()
        # file_menu.add_command(label="Import Files", command=partial(self.importFile, root))

        # self.myLabel1 = Label(root, text="Welcome to toolkit!").pack()  # .grid(row = 1 ,column = 1)
        # self.myLabel2 = Label(root, text="Bey!").pack()  # .grid(row=2, column=1)

        # self.btn = Button(root, text="Open file", command=partial(self.openFile, root)).pack()

        self.closeButton(root)
        if model.verify_import(self, 'db/x.bin'):
            Label(root, text="File path verified!").pack()

    @staticmethod
    def cmdo(root):
        Label(root, text="Path: ").pack()

    @staticmethod
    def openFile(root):
        root.filename = filedialog.askopenfilename(initialdir="C:/Users/patricia/Downloads", title="Choose a file",
                                                   filetypes=(("bin files", "*.bin"), ("all files", "*.*")))
        Label(root, text="Path: " + root.filename).pack()
        print(root.filename)
        copyfile(root.filename, "db/" + root.filename.split('/')[-1])

    # @staticmethod
    # def importFile(root):
    #     Label(root, text="Files imported!").pack()

    @staticmethod
    def closeButton(root):
        Button(root, text="Quit", command=root.destroy).pack()

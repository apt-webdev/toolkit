from functools import partial
from tkinter import *
from tkinter import filedialog
from shutil import copyfile


class View:
    def __init__(self, root, model):
        my_menu = Menu(root)
        root.config(menu=my_menu)

        # create a menu item
        file_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File", command=partial(self.openFile, root))
        # file_menu.add_command(label="Import Files", command=partial(self.importFile, root))

        edit_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Plot Data", command=self.cmdo)
        edit_menu.add_command(label="Show Data", command=self.cmdo)

        my_menu.add_command(label="Exit", command=root.destroy)

        self.myLabel1 = Label(root, text="Hello w!").pack()  # .grid(row = 1 ,column = 1)
        self.myLabel2 = Label(root, text="Bey!").pack()  # .grid(row=2, column=1)

        self.btn = Button(root, text="Open file", command=partial(self.openFile, root)).pack()

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

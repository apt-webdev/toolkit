from tkinter import *


# from tkinter import filedialog


class Container:
    @staticmethod
    def create_menu(root, tearoff):
        menu = Menu(root)
        menu["tearoff"] = tearoff
        return menu

    @staticmethod
    def create_label(root, text, font, size):
        label = Label(root, text=text)
        label["font"] = (font, size)
        return label

    @staticmethod
    def create_button(root, text,font):
        btn = Button(root, text=text)
        btn["font"] = font
        #btn["width"] = width
        return btn

    @staticmethod
    def create_radiobutton(root, text, var, value):
        return Radiobutton(root, text=text, variable=var, value=value)

    @staticmethod
    def var_radiobutton(typevar, setvalue):
        if typevar == "str":
            var = StringVar()
            var.set(setvalue)
        if typevar == "int":
            var = IntVar()
            var.set(setvalue)


    @staticmethod
    def ctn_grid(container, row, column, padx, pady):
        container.grid(row = row, column= column, padx=padx, pady= pady)

    @staticmethod
    def ctn_grid_forget(container):
        container.grid_forget()

    #@staticmethod
    #def container_pack(container, side):
    #    container.pack(side=side)

    #@staticmethod
    #def container_pack_forget(container):
    #    container.pack_forget()



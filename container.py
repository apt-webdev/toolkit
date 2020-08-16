from tkinter import *
# from tkinter import filedialog


class Container:
    @staticmethod
    def create_menu(container,tearoff):
        menu = Menu(container)
        menu["tearoff"] = tearoff
        return menu

    @staticmethod
    def create_label(container, text, font, size):
        label = Label(container, text=text)
        label["font"] = (font, size)
        return label

    @staticmethod
    def create_button(container, text, font, width):
        btn = Button(container, text=text)
        btn["font"] = font
        btn["width"] = width
        return btn




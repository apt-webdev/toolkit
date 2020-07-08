import os
import tkinter as tk
from os import system
from tkinter import filedialog


class View(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.parent.title('toolkit')
        self.parent.geometry('500x500+300+100')  # width x height
        self.text = tk.StringVar()
        self.text.set("Choose a file")
        self.label = tk.Label(self.parent, textvariable=self.text).pack()
        self.button = tk.Button(self.parent,
                                text='Open',
                                command=self.upload_action).pack()

        self.parent.mainloop()

    @staticmethod
    def upload_action():
        filename = filedialog.askopenfilename()
        print('Selected:', filename)


if __name__ == '__main__':
    root = tk.Tk()
    View(root).pack(side="top", fill="both", expand="True")
    root.mainloop()

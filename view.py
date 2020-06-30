import tkinter as tk

from tkinter import filedialog


class View:
    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set("uploading file...")
        self.label = tk.Label(self.root, textvariable=self.text)
        self.button = tk.Button(self.root,
                                text='Open',
                                command=self.upload_action)

        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    @staticmethod
    def upload_action():
        filename = filedialog.askopenfilename()
        print('Selected:', filename)


View()

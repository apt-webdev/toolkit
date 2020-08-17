import os.path
# import sqlite3
# import numpy as np
from tkinter import filedialog
import glob
from typing import List, Any, Union

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join('db', 'evaluation.bin')


class Model:
    def __init__(self):
        self.name = 'Model'
        self.db_files: List[Union[Union[bytes, str], Any]] = glob.glob("db/*.bin")
        self.import_db_file = ""
        print(my_file)
        for item in self.db_files:
            print("-->" + item)

    @staticmethod
    def verify_import(self, filename):
        return print(filename, os.path.isfile(filename))

    # TODO : verify if filename exits, before start db connect import os.path os.path.isfile(filename)

    @staticmethod
    def verify_extension(self, filename, extension):
        print("." + filename.split('.')[-1], extension, "." + filename.split('.')[-1] == extension)
        return "." + filename.split('.')[-1] == extension

    @staticmethod
    def get_file_path(root):
        root.filename = filedialog.askopenfilename(initialdir="C:/Users/patricia/Downloads", title="Choose a file",
                                                   filetypes=(("bin files", "*.bin"), ("all files", "*.*")))
        return root.filename

    @staticmethod
    def split_path_name(filename, char_split, index):
        return filename.split(char_split)[index]

    def update_imported_file(self, filename):
        self.import_db_file = filename
    # Open connection
    # conn = sqlite3.connect(my_file)
    # cursor = conn.cursor()

    # Show table from DB
    # table = 'Tag'
    # show_table(cursor, table)

    # Process the general data from DB - python data_processor.py > ..\files\activity.txt
    # run_table(cursor)
    # path_tasks = activity_loader.run_table(cursor)

    # Process records + tab table in a array records
    # records = records_table(cursor)

    # Process baselines tasks
    # baseline_tasks, _ = tasks.set_tasks()

    # join_activity_records.get_user_means(path_tasks)

    # Relate records table and activity table
    #
    # get_task_records(path_tasks, records)

    # Close connection
    # cursor.close()
    # conn.close()


if __name__ == "__main__":
    Model()

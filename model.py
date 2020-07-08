import os
import sqlite3
from scripts import *

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join('db', 'evaluation.bin')


def show_table(cursor, table_name):
    cursor.execute("select * from " + table_name)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


class Model:
    # Open connection
    conn = sqlite3.connect(my_file)
    cursor = conn.cursor()

    # Show table from DB
    # table = 'Tag'
    # show_table(cursor, table)

    # Process the general data from DB - python data_processor.py > ..\files\activity.txt
    # run_table(cursor)
    #path_tasks = activity_loader.run_table(cursor)

    # Process records + tab table in a array records
    # records = records_table(cursor)

    # Process baselines tasks
    baseline_tasks, _ = tasks.set_tasks()

    join_activity_records.get_user_means(path_tasks)

    # Relate records table and activity table
    #
    # get_task_records(path_tasks, records)

    # Close connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    Model()

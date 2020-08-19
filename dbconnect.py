import sqlite3
import re
import datetime
from typing import List, Any
from path_task import PathTask
from path_graph import PathGraph

# Declare all constant variables
ENTER = 'ENTER'
EXIT = 'EXIT'
ICON = '-->'
HOME = 'Home'
EXIT_ACT_HOME = 'EXIT ACTIVITY:Home'
NONE = 'NONE'
SECONDS = 'none'


# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join('db', 'evaluation.bin')


class DBConnect:

    @staticmethod
    def open_connection(filename):
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def get_data_db(cursor):
        return

    @staticmethod
    def load_data(cursor, graph):



    @staticmethod
    def close_connection(conn, cursor):
        conn.close()
        cursor.close()

    @classmethod
    def create_path(cls, path_tasks):
        p = {}
        aux = ""
        for item in path_tasks:
            if aux:
                if aux != item:  # to ignore the loop in the same vertex
                    if aux in p:
                        p[aux].append(item) # print(True, p.get(aux, "xpto"), item)
                    else:
                        p[aux] = [item]
            aux = item
        path = PathGraph(p) # print(path)
        return path

    @classmethod
    def get_info_table(cls, num_id, data):
        for line in data:
            if line[0] == num_id:
                return line[2]

    @classmethod
    def get_date_diff(cls, exit_home, entry_home, table_nodes):
        # regExr - matches any word character (alphanumeric & underscore).
        exit_date: List[Any] = re.findall(r"[\w']+", exit_home[2])
        entry_date: List[Any] = re.findall(r"[\w']+", entry_home[2])  # regExr
        exit_date = [int(str_num) for str_num in exit_date]  # srt --> int
        entry_date = [int(str_num) for str_num in entry_date]  # str --> int

        exit_date_diff = datetime.datetime(
            exit_date[0], exit_date[1], exit_date[2], exit_date[3], exit_date[4], exit_date[5])

        entry_date_diff = datetime.datetime(
            entry_date[0], entry_date[1], entry_date[2], entry_date[3], entry_date[4], entry_date[5])

        date_diff = entry_date_diff - exit_date_diff
        date_diff_minutes = divmod(date_diff.seconds, 60)  # --> result in minutes

        if date_diff_minutes[0] > 5:
            # print('-------------------USER_EXIT_APP------------------')
            table_nodes.append('-------------------USER_EXIT_APP------------------')
            return date_diff.seconds
        elif date_diff_minutes[0] > 0:
            return date_diff.seconds
        else:
            #    return NONE
            return date_diff.seconds

    @classmethod
    def create_pathgraph(cls, cursor):

        table_nodes = []
        path_tasks = []
        last_activity_id = 0
        cursor.execute("select * from Activity_Log")
        index = 0
        rows = cursor.fetchall()
        last_line = rows[0]
        g1 = []
        for row in rows:
            activity = row[3]
            if activity[:5] == ENTER:
                activity = activity[activity.find(':') + 1:len(activity)]
                if activity == HOME:
                    date_diff = cls.get_date_diff(last_line, row, table_nodes)
                    init_time = cls.get_info_table(last_activity_id, rows)
                    # print(index, last_activity_id, row[0], row[0] - last_activity_id, date_diff, init_time, row[2],
                    # path_tasks)
                    table_nodes.append(
                        (index, last_activity_id, row[0], row[0] - last_activity_id, date_diff, init_time,
                         row[2], path_tasks))
                    g1.append(PathTask(index, None, len(cls.create_path(path_tasks).edges()), date_diff, init_time, row[2],
                                       cls.create_path(path_tasks)))
                    index += 1
                    path_tasks = []
                path_tasks.append(activity)

            elif activity[:4] == EXIT:
                activity = activity[activity.find(':') + 1:len(activity)]
                if activity == HOME:
                    last_activity_id = row[0]  # id
                    last_line = row  # line

            # all activities that do not start with 'ENTER' or 'EXIT'
            else:
                activity = ICON + activity
                path_tasks.append(activity)
        print(g1[4])

        return g1

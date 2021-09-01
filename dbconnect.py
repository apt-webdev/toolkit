import sqlite3
import re
import sys
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
# my_file = os.path.join('db_users', 'evaluation.bin')


class DBConnect:

    @staticmethod
    def open_connection(filename):
        try:
            conn = sqlite3.connect(filename)
            cursor = conn.cursor()
            print("SUCCESS: open database file")
        except Exception as e:
            print("ERROR:", e)
        else:
            return conn, cursor

    @classmethod
    def create_task(self):
        sql = """ CREATE TABLE IF NOT EXISTS Tasks (
            id_task integer,
            id_user integer, 
            tag text, 
            name text,
            count integer,
            date_diff integer,
            init_date text, 
            end_date text,
            path text
        ); """

        return sql

    def create_activity(self):
        sql = """ CREATE TABLE IF NOT EXISTS activities (
            id integer PRIMARY KEY,
            activity text NOT NULL,
            task_id integer NOT NULL
            FOREIGN KEY (task_id) REFERENCES tasks (id)
        );"""
        return sql

    @classmethod
    def insert_task(cls, cursor, graph):
        #id_task, id_user, tag, name, count, date_diff, init_date, end_date, path(actividade)
        sql = """INSERT INTO Tasks(id_task, id_user, tag, name, count, date_diff, init_date, end_date, path)
                      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) """
        for item in graph:
            cursor.execute(sql, item)

    @classmethod
    def load_data(cls, conn, graph):
        try:
            cursor = conn.cursor()
            cursor.execute(cls.create_task())
            cls.insert_task(cursor, graph)
            conn.commit()
            print("SUCCESS: open database file")
        except Exception as e:
            print("ERROR:", e)



    @staticmethod
    def close_connection(conn):
        conn.close()

    @classmethod
    def create_path(cls, path_tasks):
        p = {}
        aux = ""
        for item in path_tasks:
            if aux:
                if aux != item:  # to ignore the loop in the same vertex
                    if aux in p:
                        p[aux].append(item)  # print(True, p.get(aux, "xpto"), item)
                    else:
                        p[aux] = [item]
            aux = item
        path = PathGraph(p)  # print(path)
        return path

    @classmethod
    def get_info_table(cls, num_id, data):
        for line in data:
            if line[0] == num_id:
                return line[2]

    @classmethod
    def get_date_diff(cls, exit_home, entry_home):
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

        return date_diff.seconds

    '''@classmethod
    def create_pathgraph(cls, id_user, cursor):
        # g1 = []
        table_nodes = []
        path_tasks = []
        last_activity_id = 0
        cursor.execute("select * from Activity_Log")
        index = 0
        rows = cursor.fetchall()
        last_line = rows[0]
        init_time = 0
        exit_time = 0
        date_diff = 0
        exit_date = 0
        for row in rows:
            activity = row[3]

            if activity[:5] == ENTER:
                activity = activity[activity.find(':') + 1:len(activity)]
                if activity == HOME:
                    date_diff = cls.get_date_diff(last_line, row)
                    init_time = cls.get_info_table(last_activity_id, rows)

                    # if date_diff > 300:
                    #    continue
                    # print(index, last_activity_id, row[0], row[0] - last_activity_id, date_diff, init_time, row[2],
                    # path_tasks)
                    # table_nodes.append(
                    #    (index, last_activity_id, row[0], row[0] - last_activity_id, date_diff, init_time,
                    #    row[2], path_tasks))

                    # ____________________id_task, id_user, tag, name, count, date_diff, init_date, end_date, path
                    table_nodes.append(
                        (None, id_user, "Noise", None, len(path_tasks), date_diff, init_time, row[2], str(path_tasks)))
                    print(index, last_activity_id, row[0], row[0] - last_activity_id, date_diff, init_time,
                          row[2], str(path_tasks))
                    # print(None, id_user, None, len(path_tasks), date_diff, row[2], path_tasks)
                    # g1.append(
                    # PathTask(index, None, len(cls.create_path(path_tasks).edges()), date_diff, init_time, row[2],
                    # cls.create_path(path_tasks)))
                    index += 1
                    path_tasks = []
                path_tasks.append(activity)
                # print(activity)
            elif activity[:4] == EXIT:
                activity = activity[activity.find(':') + 1:len(activity)]
                if activity == HOME:
                    last_activity_id = row[0]  # id
                    last_line = row  # line
                # print(activity)
            # all activities that do not start with 'ENTER' or 'EXIT'
            else:
                activity = ICON + activity
                path_tasks.append(activity)
                # print(activity)
            # init_time = row[2]
            # print(path_tasks, len(path_tasks))
        # print(table_nodes)
        return table_nodes'''

    @classmethod
    def create_tasks(cls, id_user, cursor):
        cursor.execute("select * from Activity_Log")
        rows = cursor.fetchall()
        new_array = rows
        index = 1
        table_tasks = []  # append all the information about this user
        path = []  # save info for the new activity
        diff = 0 # diff from activity new to the current
        raw_data = []
        for row in rows:
            activity = row[3]
            timestamp = row[2]
            # id_task, id_user, tag, name, count, date_diff, init_date, end_date, path(actividade, )
            if row[3][:4] == 'EXIT':
                if row[3] == 'EXIT ACTIVITY:Home':
                    path.append((diff, activity, timestamp))
                    time_diff = cls.get_date_diff(path[0],row)
                    table_tasks.append((None, id_user, "Noise", None, len(path), time_diff, path[0][2],timestamp, str(path)))
                    #print(None, id_user, "Noise", None, len(path), time_diff, path[0][2],timestamp, str(path))
                    path = []
            else:
                path.append((diff, activity, timestamp))
                if index < len(new_array):
                    diff = cls.get_date_diff( row, new_array[index])
            index += 1

        raw_data = list.copy(table_tasks)
        noise =[]

        original_stdout  = sys.stdout
        with open('./results/data-raw-tasks.txt', 'w') as f:
            sys.stdout = f
            for data in table_tasks:
                if data[4] < 4 or  data[5] >= 200 or data[5] <= 10: #experimentar 7sec
                    noise.append(data)
                    print(data)
                    table_tasks.remove(data)
            sys.stdout = original_stdout



        #print(table_tasks)
        #print(noise)
        return raw_data, noise, table_tasks

    @classmethod
    def create_records(cls, id_user, cursor):
        rec_in = []
        rec_carbs = []
        rec_gli = []
        rec_exercise = []
        rec_photo = []
        rec_note = []
        cursor.execute("select * from Reg_Insulin")
        rows = cursor.fetchall()
        for row in rows:
            #rint(row)
            rec_in.append(('in', row[4]))

        cursor.execute("select * from Reg_CarboHydrate")
        rows = cursor.fetchall()
        for row in rows:
            #print(row)
            rec_carbs.append(('carbs', row[5]))

        cursor.execute("select * from Reg_BloodGlucose")
        rows = cursor.fetchall()
        for row in rows:
            #print(row)
            rec_gli.append(('gli', row[3]))

        cursor.execute("select * from Reg_Exercise")
        rows = cursor.fetchall()
        for row in rows:
            #print(row)
            rec_exercise.append(('exercise', row[3]))

        '''
            # carbs , insulin, glcose, Note
            if row[4] != -1 and row[5] != -1 and row[6] != -1 and row[7] == -1:
                records.append(('in+gli+carbs', row[2]))
                #print(row)
            elif row[6] != -1 and row[7] != -1:
                #print(row)
                records.append(('gli+note', row[2]))
            elif row[4] == -1 and row[5] != -1 and row[6] != -1 and row[7] == -1:
                records.append(('in+gli', row[2]))
                #print(row)
            elif row[4] == -1 and row[5] == -1 and row[6] != -1 and row[7] == -1:
                records.append(('gli', row[2]))
                print(row)
            elif row[4] != -1 and row[5] == -1 and row[6] == -1 and row[7] == -1:
                records.append(('carbs', row[2]))
                #print(row)
            '''

        return rec_in, rec_carbs, rec_gli, rec_exercise





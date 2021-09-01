import os
import math
import sys
import os.path
from typing import TextIO

import numpy as np
from tkinter import filedialog

from bar_plot_count import BarPlotCount
from dbconnect import DBConnect
import statistics

from pie_plot_baseline import Pie_Plot_Base
from task_plot import TaskPlot
from bar_polt import BarPlot
from pie_plot_noise import Pie_Plot_Noise


# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join('db_users', 'evaluation.bin')

def update_tasks(line, id_task):
    lts = list(line)
    lts[2] = 'identified'
    lts[3] = id_task
    # line = tuple(lts)
    return line


class Model:
    def __init__(self):
        self.name = 'Model'
        self.imported_files = []  # List[Union[Union[bytes, str], Any]] = glob.glob("db_users/*.bin")
        self.imported_baseline = []  # List[Union[Union[bytes, str], Any]] = glob.glob("baseline/*.txt")
        # self.import_db_file = ""
        self.created_db = "mix_data\\"
        self.processed_data = None
        self.baseline_id = []  # id_task
        self.baseline_time = []
        self.baseline_name = []
        self.baseline_count = []

        self.raw_tasks = []  # o que vem do orimeiro metodo
        self.noise = []
        self.identified_tasks = []  # pre prcesssamente , sem tarefas demasiado pequenas sem utilidade
        self.to_complete_tasks = []
        self.completed_taks = []
        self.records = []

    # TODO : verify if filename exits, before start db_users connect import os.path os.path.isfile(filename)

    # verify the extension of the imported file with the type of file in the folder
    @staticmethod
    def verify_extension(self, filename, extension):
        return "." + filename.split('.')[-1] == extension

    # get file to open from OS
    @staticmethod
    def get_file(root):
        root.file_name = filedialog.askopenfilename(initialdir="raw_data", title="Choose a file",
                                                    filetypes=(("bin files", "*.bin"), ("txt files", "*.txt")))
        return root.file_name

    # Take of name of the file from directory name
    @staticmethod
    def split_path_name(filename, char_split, index):
        return filename.split(char_split)[index]

    # Get files from folders
    def get_folders(self):
        self.imported_files = []
        self.imported_baseline = []
        for file in os.listdir('db_users/'):
            if file.endswith('.bin'):
                self.imported_files.append(file)
        for file in os.listdir('baseline/'):
            if file.endswith('.txt'):
                self.imported_baseline.append(file)
        return self.imported_files, self.imported_baseline

    '''def identify_baseline(self, line):
        flag = 0
        verify_baseline = []
        for baseline in self.baseline_id:
            #print(baseline)
            for item in baseline:
                #print(item, line[8])
                if item in line[8]:
                    verify_baseline.append(item)
                    flag +=1
            if flag == len(baseline):
                #print(3, item, line[8])
                print(baseline, verify_baseline)'''

    def task_plot(self, graph):
        # id_task, id_user, tag, name, count, date_diff, init_date, end_date, path(actividade)
        flag = 0  #
        noise = 0
        for line in graph:
            line = list(line)
            #print(line)
            if line[2] == 'Noise' and line[5] < 200 and line[5] > 10:
                if 'NewHomeRegistry:Carbs' in line[8] and 'NewHomeRegistry:Glycaemia' in line[
                    8] and 'NewHomeRegistry:Insulin' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'in+gli+carbs'
                    self.identified_tasks.append(line)
                elif 'NewHomeRegistry:Glycaemia' in line[8]:
                    if 'NewHomeRegistry:Insulin' in line[8] and 'NewHomeRegistry:carbs' not in line[8]:
                        flag = flag + 1
                        line[2] = 'Identified'
                        line[3] = 'in+gli'
                        self.identified_tasks.append(line)
                    elif 'NewHomeRegistry:Notes' in line[8]:
                        flag = flag + 1
                        line[2] = 'Identified'
                        line[3] = 'gli+note'
                        self.identified_tasks.append(line)
                    elif 'NewHomeRegistry:Carbs' not in line[8] and 'NewHomeRegistry:Insulin' not in line[8] :
                        flag = flag + 1
                        line[2] = 'Identified'
                        line[3] = 'gli'
                        self.identified_tasks.append(line)
                elif 'SuccessOpenCamera' in line[8] and 'NewHomeRegistry:Carbs' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'carbs+photo'
                    self.identified_tasks.append(line)
                elif 'NewHomeRegistry:Carbs' in line[8]:  # nunca conseguir ver a camera
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'carbs'
                    self.identified_tasks.append(line)
                elif 'LogbookChartList' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'logbook'

                    self.identified_tasks.append(line)
                elif 'SettingsGlycemia' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'sett+gli'
                    #print(line)
                    self.identified_tasks.append(line)
                elif 'Badges' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'badges'
                    self.identified_tasks.append(line)
                elif 'MyData' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'mydata'
                    self.identified_tasks.append(line)
                elif 'Exercise' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'exercise'
                    self.identified_tasks.append(line)
                    # print(line)
                elif 'SettingsInsulins' in line[8]:
                    flag = flag + 1
                    line[2] = 'Identified'
                    line[3] = 'sett+in'

                    self.identified_tasks.append(line)
                else:
                    noise += 1
                    # new_all.append(line)
                    # print(line[8])
                #print(line)

    def gather_data(self, id_user, file):
        filename = "db_users\\" + file
        conn, cursor = DBConnect.open_connection(filename)
        self.raw_tasks, self.noise, self.created_tasks = DBConnect.create_tasks(id_user, cursor)
        DBConnect.load_data(conn, self.created_tasks)
        # self.records = DBConnect.create_records(id_user, cursor)
        DBConnect.close_connection(conn)


    # verify only taks that are in Records = to_complpete_tasks
    def find_completed_tasks(self):
        for task in self.identified_tasks:
            if task[3] != 'logbook' and task[3] != 'sett+gli' and task[3] != 'badges' and task[3] != 'mydata' and task[
                3] != 'sett+in':
                self.to_complete_tasks.append(task)  # + tag  = concluida

    # Get id_task
    def get_baseline_id(self):
        # In case that import more then one, its gonna choose always the first
        baseline_file = self.imported_baseline[0]
        try:
            baseline_file = open("baseline\\" + baseline_file, 'r')
            print("SUCCESS: open baseline file")
        except Exception as e:
            print("ERROR:", e)
        for line in baseline_file:
            baseline_line = line.split(', ')
            self.baseline_name.append(baseline_line[1])
            self.baseline_count.append(baseline_line[2])
            self.baseline_time.append(baseline_line[3])
            self.baseline_id.append(baseline_line[4].split(' '))

    def print_tasks(self, id_user):
        print(":::::STATUS:::::","\nID_user: ", id_user, '\nraw_tasks: ', len(self.raw_tasks), '\nnoise_tasks: ', len(self.noise), '\ncreated_tasks: ',
              len(self.created_tasks), '\nidentified_tasks: ', len(self.identified_tasks))
        # print('to_complete_tasks: ', len(self.to_complete_tasks), '\nCompleted_tasks: ', len(self.completed_taks))

    def print_table(self, total_tasks, t1, t2, t3, t4):
        print("Tarefas_ \t user1 \t user2 \t user3 \t user 4 \t total")
        print("noise___ \t" + str(t1[1]) + "\t" + str(t2[1]) + "\t" + str(t3[1]) + "\t" + str(t4[1]) + "\t" + str(total_tasks[1]))
        print("id. cria \t" + str(t1[2]) + "\t" + str(t2[2]) + "\t" + str(t3[2]) + "\t" + str(t4[2]) + "\t" +  str(total_tasks[2]))
        print("id. base \t" + str(t1[3]) + "\t" + str(t2[3]) + "\t" + str(t3[3]) + "\t" + str(t4[3]) + "\t" +  str(total_tasks[3]))
        print("total/raw\t" + str(t1[0]) + "\t" + str(t2[0]) + "\t" + str(t3[0]) + "\t" + str(t4[0]) + "\t" +  str( total_tasks[0]))

        print("------------------------------------------------------------------------------------\nTarefas_ \t user1 \t user2 \t user3 \t user 4 ")
        print("task iden. \t" + str(t1[3]/t1[2]* 100) +'%' + "\t" + str(t2[3]/t2[2]*100)+'%' + "\t" + str(t3[3]/t3[2]*100)+'%'+ "\t" + str(t4[3]/t4[2]*100)+'%' + "\t" )
        print("Taxas nrº \t" + str(t1[2]) + "\t" + str(t2[2]) + "\t" + str(t3[2]) + "\t" + str(t4[2]) + "\t")



    def get_task_plot(self):
        users_tasks = []
        user_baseline_count = []
        index = 0
        for item in self.baseline_name:
            for task in self.identified_tasks:
                if item == task[3]:
                    users_tasks.append((task[1], item, task[5], self.baseline_time[index]))
                    user_baseline_count.append((task[1], item, task[4], self.baseline_count[index]))
                    #print(task[1], item, task[5], self.baseline_time[index])
            index +=1
            #print(user_baseline_count)
        return users_tasks, user_baseline_count


    def get_bar_plot(self, tasks):
        values = []
        value = []
        for task in tasks:
            for val in task:
                if val:
                    for x in val:
                        value.append(x)
            value.sort()
            values.append(np.median(value))
            value=[]
        return values



    def get_tables(self):
        id_user = 0
        files, _ = self.get_folders()
        users_tasks = []
        users_tasks2 = []
        users_count2 =[]
        total_tasks = [0, 0 ,0, 0]
        total_u1 = [0, 0 ,0, 0]
        total_u2 = [0, 0 ,0, 0]
        total_3 = [0, 0 ,0, 0]
        total_4 = [0, 0, 0, 0]
        for file in files:
            self.gather_data(id_user, file)
            self.task_plot(self.created_tasks)
            #self.find_completed_tasks()  # to_complete_task + records  = competed
            #self.print_tasks(id_user)
            users_tasks, user_baseline_count = self.get_task_plot()
            users_tasks2.append(users_tasks)
            users_count2.append(user_baseline_count)

            total_tasks[0] += len(self.raw_tasks)
            total_tasks[1] += len(self.noise)
            total_tasks[2] += len(self.created_tasks)
            total_tasks[3] += len(self.identified_tasks)

            if id_user == 0:
                total_u1[0] = len(self.raw_tasks)
                total_u1[1] = len(self.noise)
                total_u1[2] = len(self.created_tasks)
                total_u1[3] = len(self.identified_tasks)

            elif id_user ==1:
                total_u2[0] = len(self.raw_tasks)
                total_u2[1] = len(self.noise)
                total_u2[2] = len(self.created_tasks)
                total_u2[3] = len(self.identified_tasks)

            elif id_user == 2:
                total_3[0] = len(self.raw_tasks)
                total_3[1] = len(self.noise)
                total_3[2] = len(self.created_tasks)
                total_3[3] = len(self.identified_tasks)

            elif id_user == 3:
                total_4[0] = len(self.raw_tasks)
                total_4[1] = len(self.noise)
                total_4[2] = len(self.created_tasks)
                total_4[3] = len(self.identified_tasks)

            id_user += 1

            self.raw_tasks = []
            self.noise = []
            self.created_tasks = []
            self.identified_tasks = [] # usar no task plot
            #self.to_complete_tasks = []
            #self.completed_tasks = []



        info_for_task = [[]*4]* 11
        index_task = 0
        for task in self.baseline_name:
            newtask = []
            for user in users_tasks2:
                newuser = []
                index_user = 0
                for it in user:
                    if task == it[1]: #'in+gli+carbs'
                        #print(True,it[1],  it[0],index_user, it[2], index_task, user)
                        newuser.append(it[2])

                newtask.append(newuser)
                index_user += 1
            info_for_task[index_task].append(newtask)
            index_task += 1

        info_for_count = [[] * 4] * 11
        index_task = 0
        for task in self.baseline_name:
            newtask = []
            for user in users_count2:
                newcount = []
                index_user = 0
                for it in user:
                    if task == it[1]:  # 'in+gli+carbs'
                        #print(it, user)
                        # print(True,it[1],  it[0],index_user, it[2], index_task, user)
                        newcount.append(it[2])
                newtask.append(newcount)
                index_user += 1
            info_for_count[index_task].append(newtask)
            index_task += 1


        index_task = 0
        taxas_users = [0, 0, 0, 0]
        sum = 0
        for task in info_for_task[0]:
            #TaskPlot.create_plot(index_task, self.baseline_name, self.baseline_time, task[0], task[1], task[2], task[3])
            index_user = 0
            for x in taxas_users:
                if len(task[index_user])!=0:
                    sum +=1
                    taxas_users[index_user] += 1
                index_user += 1
                sum = 0
            index_task +=1
            #print(task)
        #print(taxas_users, [(x/11*100) for x in taxas_users])


        median_count =  self.get_bar_plot(info_for_count[0])
        median = self.get_bar_plot(info_for_task[0])
        self.baseline_time = [int(x) for x in self.baseline_time]
        self.baseline_count = [int(x) for x in self.baseline_count]
        #BarPlot.create_bar_plot(self.baseline_time, median)
        #BarPlotCount.create_bar_plot(self.baseline_count, median_count)

        #Pie_Plot_Noise.create_plot(total_tasks[1], total_tasks[2])
        #Pie_Plot_Base.create_plot(total_tasks[2], total_tasks[3])

        #self.print_table(total_tasks, total_u1, total_u2, total_3, total_4)

        original_stdout: TextIO = sys.stdout
        with open('./results/data-status.txt', 'w') as f:
            sys.stdout = f
            self.print_table(total_tasks, total_u1, total_u2, total_3, total_4)
            sys.stdout = original_stdout


















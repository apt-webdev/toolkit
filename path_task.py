from path_graph import PathGraph


class PathTask(PathGraph):
    def __init__(self, id_num, name, count, diff_time, init_time, final_time, path):
        self.id_num = id_num
        self.name = name
        self.count = count
        self.diff_time = diff_time
        self.init_time = init_time
        self.final_time = final_time
        self.path = path

    def time_diff(self):
        print(int(self.final_time) - int(self.init_time))

    def __str__(self):
        res = "result: "
        res += (str(self.id_num) + " ")
        res += (str(self.name) + " ")
        res += (str(self.count) + " ")
        res += (str(self.diff_time) + " ")
        res += (self.path.__str__())

        return res

# listPath = []
# listPath.append(PathTask("Tara home", "home, drawer, settings", "23", "30"))

# print("Show first line:")
# print(listPath[0].path)

# listPath[0].time_diff()


# if __name__ == "__main__":
#    listPath = []
#    listPath.append(node_task.Node('ENTRY: Insert new food', 'insert info', 2))
#    listPath.append(node_task.Node('EXIT: Insert new food', 'insert info', 4))
#    print(listPath[1].getNode())
#    new_path = PathTask(1, "get HC", 2, 8, 2, 6, listPath)
#    print(new_path.path[1].activity_name)

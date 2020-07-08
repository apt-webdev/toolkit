class Node:
    def __init__(self, activity_name, goal, level):
        self.activity_name = activity_name
        self.goal = goal
        self.level = level

    def getName(self):
        return self.activity_name

    def detGoal(self):
        return self.goal

    def getLevel(self):
        return self.level

    def getNode(self):
        return self.activity_name, self.goal, self.level

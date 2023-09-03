# how to use class

class Student:
    def __init__(self, name, math, englsh):
        self.name = name
        self.math = math
        self.englsh = englsh
    def avg(self):
        print(self.name + "の数学の平均点は70点です")

a001 = Student("sato", 70, 80)
a001.avg("sato")
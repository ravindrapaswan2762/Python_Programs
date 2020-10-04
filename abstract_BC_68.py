#from abc import ABCMeta, abstractclassmethod
from abc import ABC, abstractclassmethod
class Shap(ABC):
    def printarea(self):
        return 0
#########################################

class rectangle():
    type = "rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breath = 7

    def printarea(self):
        return self.length * self.breath

rect1 = rectangle()
print(rect1.printarea())

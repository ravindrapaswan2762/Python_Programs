class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        pass
        return f"the name is {self.name} salary is {self.salary} and role is {self.role}"


    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_str(cls, string):
       return cls(*string.split("-"))

    @classmethod
    def printgood(cls, string):
        print("this is good " + string)
        return


class player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"the name is {self.name} game is {self.game} "

    ### multiple inheritense use  ###
class coolprogrammer(Employee, player):
    pass


shubham = player("shubham", ["cricket"])
karan = coolprogrammer("karan", 456, "coolprogrammer")

print(shubham.printdetails())

det = karan.printdetails()
print(det)







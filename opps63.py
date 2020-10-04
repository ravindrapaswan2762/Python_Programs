# public- as it is.. - any where use
#protected- with single under score- use under same class
# privet- with double under score- use only under a class

class Employee:
    no_of_leaves = 8
    public = 15
    _protected = 20
    __privet = 25



    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"the name is {self.name} salary is {self.salary} and role is {self.role}"


    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves
emp = Employee("harry", 456, "programmer")
print(emp._protected)
print(emp._Employee__privet)      ## we can't direct print of privet###


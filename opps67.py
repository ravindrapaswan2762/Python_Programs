class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"the name is {self.name} salary is {self.salary} and role is {self.role}"


    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return f"Employee( {self.name}, {self.salary}, {self.role} )"
    def __str__(self):
        return f"the name is {self.name} salary is {self.salary} and role is {self.role}"

emp1 = Employee("harry", 564, "programmer")
emp2 = Employee("rohan", 123, "cleaner")

print(emp1 + emp2)
print(emp1.printdetails())
print(emp2.__repr__())
print(emp2.__str__())
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

    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])
     ## OR  ##
       # return cls(*string.split("-"))

harry = Employee("harry", "2556", "instrutor")
rohan = Employee("rohan", 556, "student")
karan = Employee.from_dash("karan-480-student")

#rohan.change_leaves(34)
#print(rohan.no_of_leaves)
print(karan.salary)
print(karan.__dict__)
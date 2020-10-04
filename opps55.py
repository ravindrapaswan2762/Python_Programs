"""class employee:
    pass


    def printdetails(self):

        return f"name is {self.name} salary is {self.salary} and role is {self.role}"

harry = employee()
rohan = employee()

harry.name = "harry"
harry.salary = 455
harry.role = "instructor"

rohan.name = "rohan"
rohan.salary = 889
rohan.role = "student"

print(harry.printdetails())"""

######################################################   or  ###################
class employee:
     no_of_leaves = 8

     def __init__(self, name, salary, role):
         self.name = name
         self.salary = salary
         self.role = role


     
rohan = employee("rohan", "2556", "student")
print(rohan.__dict__)
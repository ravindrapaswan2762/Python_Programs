class Employee:
    pass
class student:
    no_of_leaves = 8
    pass
harry = student()
larry = student()
sohan = student()
rohan = Employee()


larry.name = "larry"
larry.std = "8th"
larry.section = "C"

harry.name = "harry"
harry.std = "12th"
harry.section = "A"


rohan.name = "rohan"
rohan.work = "cyber_security"
rohan.place = "delhi"

sohan.name = "sohan"
sohan.std = "11"
sohan.section = "A"

#student.no_of_leaves = 9
print(student.no_of_leaves)

print(rohan.__dict__)


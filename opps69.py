class Employee:
     def __init__(self, fname, lname):
         self.fname = fname
         self.lname = lname
         #self.email = f"{fname}.{lname}@gmail.com"

     def explain(self):
         return f"this Employee is {self.fname} {self.lname}, "

     @property   ### as a functiion print karne ki jarurat nai
     def email(self):
         if self.fname==None or self.fname==None:
             return "Email is not set plz set the email"
         return f"{self.fname}{self.lname}@gmail.com"

     @email.setter  ## for direct- rohan.email = "pappu.singh566@gmail.com"
     def email(self, string):
         print("setting now....")
         names = string.split("@")[0]
         self.fname = names.split(".")[0]
         self.lname = names.split(".")[1]\

     @email.deleter
     def email(self):
         self.fname = None
         self.lname = None



mohan = Employee("mohan", "das",)
rohan = Employee("rohan", "das")
lallu = Employee("lallu", "ram")

print(mohan.email)
mohan.fname = "karan"
print(mohan.email)

rohan.email = "pappu.singh566@gmail.com"
print(rohan.email)

print(lallu.email)
del lallu.email
print(lallu.email)
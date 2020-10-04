class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"this Employee is {self.fname} {self.lname}, "

    @property  ### as a functiion print karne ki jarurat nai
    def email(self):
        if self.fname == None or self.fname == None:
            return "Email is not set plz set the email"
        return f"{self.fname}{self.lname}@gmail.com"

    @email.setter  ## for direct- rohan.email = "pappu.singh566@gmail.com"
    def email(self, string):
        print("setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @ email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skill", "F")
print(skillf.email)
print(type("this is a string"))
print(id("this is a string"))

o = "this is a string"   ### iske saath aur kya-kya kar sakte hai##
print(dir(skillf))

import inspect      ### isse saare attribute pata chal jaata hai jo-jo use kar sakte hai ###
print(inspect.getmembers(skillf))


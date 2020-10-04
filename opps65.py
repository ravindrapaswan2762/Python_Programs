class A:
    classvar1 = "i am a class variable in class A"
    def __init__(self):
        self.var1 = "i am inside class A's constructor "
        self.classvar1 = "instance var in class A"
        self.special = "special"

class B(A):
    classvar2 = "i am in class B-2 "
    classvar3 = "i am in class B-3"

a = A()
b = B()
print(b.classvar1)     ### firstly found instant variable in B THEN A, then secondly found class variable in B then A

###############################################################################################

class A:
    classvar1 = "i am a class variable in class A"
    def __init__(self):
        self.var1 = "i am inside class A's constructor "
        self.classvar1 = "instance var in class A"
        self.special = "special"

class B(A):
    classvar2 = "i am in class B-2 "
    classvar3 = "i am in class B-3"

    def __init__(self):

        self.var1 = "i am inside class B's constructor "
        self.classvar1 = "instance var in class B"
        super().__init__()
                                    ## if def function is over writted then doesn't work first function


a = A()
b = B()
print(b.special, b.var1, b.classvar1)
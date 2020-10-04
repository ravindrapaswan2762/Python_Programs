"""def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a = funcret(1)
print(a)
a = funcret(0)
print(a)"""
#############################

"""def executer(func):
    func("this")
executer(print)"""
############################
def dec1(func1):

    def nowexec():
        print("executting now...... ")
        func1()
        print("executed")
    return nowexec

##
"""def who_is_harry():
    print("harry is a programmer")

who_is_harry = dec1(who_is_harry)
who_is_harry()"""

###### OR ######
@dec1
def who_is_harry():
    print("harry is a programmer")
who_is_harry()

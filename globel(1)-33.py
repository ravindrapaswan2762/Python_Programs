"""g = 15          #>>> GLOBAL VARIABLE[UNDER FUNCTION]
def function1(n):
    l = 5       #>>>LOCAL VARIABLE
    m = 10
    global g     #>>> for edit global value
    print(l+45, m)
    print(n, "i have printed")
function1("this is me")"""

x = 89
def ravindra():
    x = 20
    m = 2
    def rohan():
        global x            ##>> its renove x=88 outside of both function(like global)
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", m)

ravindra()     #>>> for run function
print(x)
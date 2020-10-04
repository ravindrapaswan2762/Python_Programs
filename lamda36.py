# lamda function or anonymous function#

def add(a, b):
    return a+b
print(add(9, 4))

   #  OR  #

substract = lambda a, b : a-b
print(substract(9, 4))

    

def a_first(a):
    return a[1]
a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=a_first)
print(a)


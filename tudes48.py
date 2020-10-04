"""numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))

numbers[2] = numbers[2]+1
print(numbers[2])"""


"""def sq(a):
    return a*a
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
square = list(map(sq, num))
print(square)"""

#########  OR #######################################

"""num = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
square = list(map(lambda a:a*a*a, num))
print(square)"""




"""def square(a):
    return a*a
def cube(a):
    return a*a*a

func = [square, cube]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)"""



"""def is_greater_5(num):
    return num>5
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
is_greater_5 = list(filter(lambda x:x>5, list1))
print(is_greater_5)

from functools import reduce
list = [1, 2, 3, 4, ]
num = 0
for i in list1:
    num = reduce(lambda x,y:x+y, list)
print(num)"""



### own logic first time ##
"""def sq(a):
    return a*a
input = int(input("enter the numbers : "))
print(sq(input))"""



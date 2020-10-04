def printjoke(*args, **kwargs):
    for item in args:
        print(item)

list = [1, 2, 3, 4, 5]
printjoke(list)
a = 7
print(a)

list2 = [6, 7, 8, 9, 10]
printjoke(list2)
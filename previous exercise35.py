n = int(input("enter the nimber : "))
boolean = int(input("enter 1 for true and 0 for false : "))
if boolean == 1:
    for i in range(0, n):
        for j in range(i+1):
            print("*", end="")
        print("\n", end="")
if boolean == 0:
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print("\n", end="")


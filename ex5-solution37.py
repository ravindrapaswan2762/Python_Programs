# HEALTH MANAGEMENT SYSTEM #

import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if(k==1):
        c = int(input("enter 1 for exercises and 2 for food : "))
        if(c==1):
            value = input("type here\n")
            with open("harry_ex.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("harry_food.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")



    elif(k==2):
        c = int(input("enter 1 for exercises and 2 for food : "))
        if (c == 1):
            value = input("type here\n")
            with open("rohan_ex.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")

        elif(c == 2):
            value = input("type here\n")
            with open("rohan_food.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")


    elif(k==3):
        c = int(input("enter 1 for exercises and 2 for food : "))
        if (c == 1):
            value = input("type here\n")
            with open("ravindra_ex.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")

        elif(c == 2):
            value = input("type here\n")
            with open("ravindra_food.txt", "a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")

    else:
            print("please enter valid no. 1(harry), 2(rohan), 3(ravindra) : ")


def retrieve(k):
    if(k==1):
        c = int(input("enter 1 for exercise and 2 for food : "))
        if(c==1):
            with open("harry_ex.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif(c==2):
            with open("harry_food.txt")as op:
                for i in op:
                    print(i, end=" ")

    elif(k==2):
        c = int(input("enter 1 for exercise and 2 for food : "))
        if (c == 1):
            with open("rohan_ex.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("rohan_food.txt")as op:
                for i in op:
                    print(i, end=" ")


    elif(k==3):
        c = int(input("enter 1 for exercise and 2 for food : "))
        if (c == 1):
            with open("ravindra_ex.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("ravindra_food.txt")as op:
                for i in op:
                    print(i, end=" ")


    else:
        print("please enter valid input (harry, rohan, ravindra) : ")


a = int(input("press 1 for log the value and 2 for retrieve : "))
if(a==1):
    b = int(input("press 1 for harry 2 for rohan and 3 for ravindra : "))
    take(b)

else:
    b = int(input("press 1 for harry 2 for rohan and 3 for ravindra : "))
    retrieve(b)

















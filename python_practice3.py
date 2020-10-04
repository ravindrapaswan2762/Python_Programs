"""UTHOR : RAVINDRA PASWAN
DATE : 1 SEPTEMBER 2020
PURPOSE : PRACTICE FOR PROBLEM SOLUTION"""

"""QUESTION - You visit a restourant called 24_hours-restourant and food items and food items in ths restaurant are stored
based on their amount of calories.you have to reverse  this list of food items and their calories


You have to following three methods to reverse a list
1 inbuilt method of python
2 listname[::-1] slicing trick
3 swapping first element with last one and second element with second last one and so on....

INPU - take a list as a list from the user
ex:- [1, 2, 3, 4]

OUTPUT -
ex:- [4, 3, 2, 1]
ex:- [4, 3, 2, 1]
ex:- [4, 3, 2, 1]
"""
print("Enter the numbers of the list one by one")
size = int(input("Enter the size : \n"))
mylist = []
for i in range(size):
    mylist.append(int(input("Enter the value of list : ")))
print(f"Your list is {mylist}")

reverse1 = mylist[:]
reverse1.reverse()
print(f"Your first reverse list is {reverse1}")

reverse2 = mylist[::-1]
print(f"Your second reverse list is {reverse2}")

reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    # print(f"the reversed list at i={i} is {reverse3}")
print(f"Your Third reversed list is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result")
###########################################################################
############# some awapping method##########
"""pos1, pos2 = 0, 3
pos3, pos4 = 1, 2
mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]
mylist[pos3], mylist[pos4] = mylist[pos4], mylist[pos3]
print(f"Your third reverse list is {mylist}")"""








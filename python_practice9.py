#### FUNNU NAMES ########
"""
The task you have to perform is “Jumbled Funny Names”.

Problem Statement:-
Its result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.

Input :-
Enter number of friends:

3

Enter the name of your 3 friends:

Rohan Das

Shubham Agarwal

Ritesh Arora

OUTPUT :-
Ritesh Das

Shubham Arora

Rohan Agarwal
"""

import random
def change_sirname(first_name,last_name,size):
    for i in range(0, size):
        # Changing the last name
        joumbled_name = first_name[i] + " " + last_name[random.randint(0, size - 1)]
        name_list.append(joumbled_name)


if __name__ == '__main__':

    size = int(input("How many people add you want ? : "))
    list = []
    first_name = []
    last_name = []
    name_list = []
    for i in range(0,size):
        list.append(input("Enter the full name here : "))
    #print(list)

    # Spliting the elements of the name list
    for ele in list:
        split_name = ele.split(" ")

        first_name.append(split_name[0])
        last_name.append(split_name[1])
    change_sirname(first_name,last_name,size)
    print(name_list)
##############################################################################################################

#### L - 118 ####
"""import random
def wrong_table(number):
    wrong = random.randint(0,9)
    table1 = [i*number for  i in range(1,11)]
    table1[wrong] = table1[wrong] + random.randint(0,10)
    return table1

def cheak_table(number, ):
    table2 = [i*number for  i in range(1,11)]
    return table2


if __name__ == '__main__':
    num1 = int(input("Enter the no. to print table : "))

    if wrong_table(num1) == cheak_table(num1):
        print("wrong_table() is working well !")
        print(f"This table is correct : {cheak_table(num1)}")

    else:
        print("wrong_table() is a froud !")
        print(f"It's creating a wrong table : {wrong_table(num1)}")

        """
##########################################################################################################
############################################ OR ##########################################################
##########################################################################################################
import random
def wrong_table(number):
    wrong = random.randint(0,5)
    table = [i*number for  i in range(1,11)]
    table[wrong] = table[wrong] + random.randint(0,10)
    return table

def is_correct(table,number):
    for i in range(1, 10):
        if table[i-1] != i*number:
            return i-1
    return None

if __name__ == '__main__':
    number = int(input("Enter the no. to print table : "))
    mytable = wrong_table(number)
    print(mytable)

    print("Index is starting from the zero !")
    wrong_index = is_correct(mytable, number)
    print(f"The table is wrong at the index of {wrong_index}")





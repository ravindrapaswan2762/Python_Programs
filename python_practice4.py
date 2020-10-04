# THE NEXT PALINDROME  #######
"""
UTHOR : RAVINDRA PASWAN
DATE : 1 SEPTEMBER 2020
PURPOSE : PRACTICE FOR PROBLEM SOLUTION
"""

"""QUESTION - A palindrome is a string which when reversed is equal to itself:
examples of palindrome includes 616, mom, 676, 1000001
you have to take a number as an input from the user. you have to find next palindrome
corresponding to that numbers. your first input should be 'number of test cases' and
then take all the cases as input from the user

 INPUT- size(like 1 or 2 or 3...), 451, 10, 213, 2133....
 OUTPUT- Next palindrome for 451 is 454
         next palindrome for 10 is 11
         next palindrome for 213 is 222
         next palindrome for 2133 is 2222
         ..............."""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

if __name__ == "__main__":
    print("Enter the number for palindrome one by one\n")
    size = int(input("Enter the size : \n"))
    list = []
    for i in range(size):
        list.append(int(input("Enter the value for palindronme : \n")))
    print(f"Your entered value is {list}\n")

    for i in range(size):
        print(f"Your next palindrome for {list[i]} is {next_palindrome(list[i])}")









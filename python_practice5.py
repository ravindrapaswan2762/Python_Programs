"""
UTHOR : RAVINDRA PASWAN
DATE : 2 SEPTEMBER 2020
PURPOSE : PRACTICE FOR PROBLEM SOLUTION
"""

"""QUESTION - You have given a list which contain some numbers. You have to print a list of next palindromes only
 if the number is greater than 10 otherwise you will print that number

 INPUT- [1, 6, 87, 43]
 OUTPUT- [1, 6, 88,43]"""

##cheack the intered value for palindrome##
def is_palindrome(n):
    return str(n) == str(n)[::-1]

##creat next palindrome##
def next_palindrome(n):

    # if intered value is palindrome then print as it is or single value also a palindrome in itself
    if is_palindrome(n)==n:
        print(n)

    # when intered value is not palindrome then print next palindrome
    while not is_palindrome(n):
        n = n + 1
    return n



if __name__ == '__main__':
    size = int(input("Enter the size of list : \n"))
    list1 = []
    list2 = []
    for i in range(size):
        list1.append(int(input("Enter the value of list : ")))
    print(f"Your entered vaiue is {list1}")
    for i in range(size):

        ## insert palindrome value in list2 from list1 ##
        list2.append(next_palindrome(list1[i]))
    print(f"Your palindrome value is {list2}")













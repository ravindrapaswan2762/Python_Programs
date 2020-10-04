# PYTHON - PRACTICE - 2
"""UTHOR : RAVINDRA PASWAN
DATE : 1 SEPTEMBER 2020
PURPOSE : PRACTICE FOR PROBLEM SOLUTION"""

"""QUESTION - Harry potter has got n numbers of apples. harry has some student among whome, he wants to distribute
the apples. these n numbers of apples are provided to harry by his friends and he can request for few more or
few less apples.

INPUT- take input n, mn, mx from the user

OUTPUT- print whether the numbers between mn and mx are divisor of n or not. if mn = mx, show that 
this is not a range and mn is equal to mx. show the result for that number 
"""
n = int(input("Enter the numbers of apples : "))
mn = int(input("Enter the minimun numbers of children : "))
mx = int(input("Enter the miximun numbers of children : "))
for i in range(mn+1, mn):
    if n%i == 0:
        print(i)
        print(f"{n} number is divisible by {i}")

    else:
        print(f"{n} number is not divisible by {i}")


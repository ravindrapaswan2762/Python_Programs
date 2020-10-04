# python - practice - 1
# L - 103
#### AGE CALCULATOR #######
"""UTHOR : RAVINDRA PASWAN
DATE : 1 SEPTEMBER 2020
PURPOSE : PRACTICE FOR PROBLEM SOLUTION"""

num1 = int(input("Enter your birth year ex: (1995, 1996, 2000, 2005) : "))
num2 = 2020
age = num2 - num1
num3 = 100 - age


if num1 > 2020:
    print("You are not born yet ! ")
elif num1 < 1920:
    print("You are no longer alive ! ")

else:
    def take(num1):
        return age


    print(age)
    print(f"After {num3} years you reached 100 year old, IN {num2+num3}")















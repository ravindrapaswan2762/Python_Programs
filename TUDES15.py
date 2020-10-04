# QUESTION :- WRITE A PROGRAM TO MAKE A FAULTY CALCULATOR WHICH CALCULATE CORRECTLY EXCEPT
               # 45*3 = 555,  56+9 = 77,  56/6 = 4

#list = {"45*3":"555", "56+9":"77", "56/6":"4"}

print("Enter the first number : ")
num1 = int(input())
print("Enter the second number : ")
num2 = int(input())
print("so what you want?"+'+,-,*,/,**,%')
num3 = input()

if num1 == 45 and num2 == 3 and num3 == '*':
    print("The multiplication value is : ", "555")

elif num1 == 56 and num2 == 9 and num3 == '+':
    print("The additional value is : ", "77")

elif num1 == 56 and num2 == 6 and num3 == '/':
    print("The divisional value is : ", "4")

elif num3 == "+":
    a = int(num1 + num2)
    print("The additional vailue is : ", a)

    
elif num3 == "*":
    b = int(num1 * num2)
    print("The multiplicational vailue is : ", b)


elif num3 == "/":
    print("The divisional value is : ", int(num1) / int(num2))


elif num3 == "-":
   # d = int(num1 - num2 )
    print("The substractional value is : ", int(num1) - int(num2))

elif num3 == "**":
    print("The square value is : ", int(num1) ** int(num2))


elif num3 == "%":
    print("The modulas value is : ", int(num1) % int(num2))

else:
    print("not defined!!!!")



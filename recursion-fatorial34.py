
# def factorial_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
# number = int(input("enter the number : "))
# print("factorial using iterative methode :-", factorial_iterative(number))

  ##  OR ###


# number = int(input("enter the number : "))
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return  n * factorial_recursive(n-1)
#
# print("factorial using recursive methode :-", factorial_recursive(number))
""""



0,1,1,2,3,5,8,13,21,34  >>>fibonacci series"""
number = int(input("enter the number : "))
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fabonacci using recursive methode :-", fibonacci(number))

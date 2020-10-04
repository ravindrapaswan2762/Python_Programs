##### operators in python:-
#(1)assignment opperators
#(2)comparision opperators
#(3)logical opperators
#(4)identity opperators
#(5)bitwise opperators
#(6)arithmatic opperators
#(7)membership opperators

#[ARITHMATIC OPPERATORS]:-
print("ARITHMATIC OPPERATORS :-")
print("5 + 2 is = ", 5+2)
print("5 - 2 is = ", 5-2)
print("5 * 2 is = ", 5*2)
print("5 ** 5 2 is = ", 5**2)
print("5 % 5 2 is = ", 5%2)
print("5 / 2 is = ", 5/2)
print("5 // 2 is = ", 5//2)

#[ASSIGNMENT OPPERATORS]:-
print("ASSIGNMENT OPPERATORS :-")
x = 10
x -= 7
x += 3
x /= 2
x += 12
x *= 2
x //= 4  # give only integers value through division
x **= 2
x %= 8   # give only float valu through division
print(x)

# COMPARISION OPPERATORS:-
print("COMPARISION OPPERATORS :-")
i = 10
#print(i == 5)    # >>>false
#print(i == 10)   #>>>true
#print(i > 5)     #>>>true
#print(i < 5)      #>>>false
print(i >= 5)

#LOGICAL OPPERATORS(AND, OR, NOT):-
print("LOGICAL OPPERATORS :-")
a = True
b = False
print(a and b)    #>>> false
print(a or b)      #>>>true

# IDENTITY OPPERATORS( is, is not) :-
print("IDENTITY OPPERATORS :-")
n = 5
m = 10
print(a is b)   #>>> false
print(a is not b)

# MEMBERSHIP OPPERATORS(in, not in) :-
print("MEMBERSHIP OPPERATORS :-")
list = [4, 5, 88, 6, 7, 24, 62]
print(4 in list)     #>>> true
print(56 in list)    #>>>false

# BITWISE OPPERATORS(&, |>>(or)) :-
print("BITWISE OPPERATORS :-")
#0 - 00
#1 - 01
#2 - 10
#3 - 11
print(0 & 1)          #>>>   0*1=0 and  00*01=00, >> 00==0
print(0 | 1)          # ==1
print(0 | 3)          # ==3






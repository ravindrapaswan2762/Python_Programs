## QUESTION :-
print("NUMBER GUISSING GAME")
n = 30
b = 0
while(b<=7):
    b = b+1
    if b>7:
        print("YOU ARE LOOSER....!!")
        print(" GAME OVER!!! ")
        break

    else:
        num1 = int(input("so you can try guise the hidden number : "))
        if num1<n:
            print("you printed number is too lesser ",)
            print("your guesses left is ", 7 - b)
            num1 = input("you can try again : ")
            continue


        elif num1>n:
            print("you printed number is too greater")
            print("your guesses left is ", 7 - b)
            num1 = input("you can try again : ")
            continue
        else:
            print("YOU WON THE MATCH")














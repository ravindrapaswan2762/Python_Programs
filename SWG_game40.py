# snake water gun game :-
import random
list = ["s", "w", "g"]
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" Snake, Water, GUN Game\n")
print("s for snake \nw for water\ng for gun\n")
while no_of_chance<chance:
    no_of_chance = no_of_chance +1

    a = str(input("Snake, Water, GUN : "))
    b = (random.choice(list))

    if a == b:
        print("Tie both 0 point to each other\n")

    elif a == "s" and b == "g":            ####WWWWWWWWWWWWWWWWWWWWWW
        computer_point = computer_point + 1
        print(f"your guiess is {a} and computer guess is {b} \n")
        print("computer win 1 point")
        print(f"computer_point is {computer_point} your point is {human_point}\n")
        print(f"{chance - (no_of_chance)} is left out of {chance}\n")

    elif a == "s" and b == "w":                     ####WWWWWWWWWWWWW
        human_point = human_point + 1
        print(f"your guiess is {a} and computer guess is {b}\n")
        print("you win 1 point")
        print(f"computer_point is {computer_point} your point is {human_point}\n")
        print(f"{chance - (no_of_chance)} is left out of {chance}\n")


    elif a == "w" and b == "s":                  ####WWWWWWWWWWW
        computer_point = computer_point + 1
        print(f"your guiess is {a} and computer guess is {b}\n")
        print("computer win 1 point")
        print(f"computer_point is {computer_point} your point is {human_point}\n")
        print(f"{chance - (no_of_chance)} is left out of {chance}\n")


    elif a == "w" and b == "g":                   #wwwwwwWWWWWWWWWWWW
        computer_point = computer_point + 1
        print(f"your guiess is {a} and computer guess is {b}\n")
        print("computer win 1 point")
        print(f"computer_point is {computer_point} your point is {human_point}\n")
        print(f"{chance - (no_of_chance)} is left out of {chance}\n")


    elif a == "g" and b == "s":                 ###wwwwwwwwwwwwwwwwwww
        human_point = human_point + 1
        print(f"your guiess is {a} and computer guess is {b}\n")
        print("you win 1 point")
        print(f"computer_point is {computer_point} your point is {human_point}\n")
        print(f"{chance - (no_of_chance)} is left out of {chance}\n")


    elif a == "g" and b == "w":                     ###WWWWWWWWWWWWWW
        computer_point = computer_point + 1
        print(f"your guiess is {a} and computer guess is {b} \n")
        print("computer win 1 point")
        print(f"computer_point is {computer_point} your point is {human_point}\n")
        print(f"{chance - (no_of_chance)} is left out of {chance}\n")

    else:
        print("you entered wrong value\n")
        print(f"{chance - (no_of_chance)} is left out of {chance}\n")
print("Game Over")

if computer_point==human_point:
    print("TIE")
elif computer_point>human_point:
     print("you lose and computer win")

elif computer_point<human_point:
     print("you win and computer lose")

     print("your point is {human_point} and computer point is {computer_point}")
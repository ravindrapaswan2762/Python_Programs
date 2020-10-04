##### NUMBER GUESSING GAME ######
"""
UTHOR : RAVINDRA PASWAN
DATE : 2 SEPTEMBER 2020
PURPOSE : PRACTICE FOR PROBLEM SOLUTION
"""

"""
Python Problem 6 |
The task you have to perform is “Guess The number”.

 Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b.
a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep
choosing the number and your program must tell whether the number is greater than the actual number or
less than the actual number. Log the number of trials it took your friend to arrive at the number.
You play the same game and then the person with minimum number of trials wins! Randomly generate a number
after taking a and b as input and don’t show that to the user.

Input:
Enter the value of a

4

Enter the value of b

13

Output:
Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8

"""
"""
In METHOD ONE - if any player guessed the number first, then A special POWER will come near him, with the
help of he can change the two value of a and b, and then next player will be able to find the value"""

#####################################################################################################################
##################################################  METHOD ONE    ###################################################
#####################################################################################################################
import random
total_chance = 5
player_1_chance = 0
player_2_chance = 0
player_1_point = 0
player_2_point = 0

while(True):

    a = int(input("Enter the value of a : "))

    b = int(input("Enter the value of b : "))
    for i in range(a, b):
        random_number = random.randint(a, b)
    print(random_number)

    for i in range(total_chance):

        print("PLAYER 1")

        player_1 = int(input(f"Please guess the numbers between {a} and {b} : "))
        if player_1 == random_number:
            print("Congrates you guessed the number !")


            if player_1 == random_number:
                player_1_point = player_1_point + 1
                print(f"Player_1 have points are {player_1_point}")

            player_1_chance = player_1_chance + 1
            print(f"Your guesess left are {total_chance -player_1_chance} out of {total_chance}")

            a = int(input("Enter the value of a : "))

            b = int(input("Enter the value of b : "))
            for i in range(a, b):
                random_number = random.randint(a, b)
            print(random_number)


        elif player_1 > random_number:
            print("Wrong, guess a lower number again !")

            """if player_1 == random_number:
                player_1_point = player_1_point + 1
                print(f"Player_1 have points are {player_1_point}")"""

            player_1_chance = player_1_chance + 1
            print(f"Your guesess left are {total_chance - player_1_chance} out of {total_chance} ")

        elif player_1 < random_number:
            print("Wrong, guess a greater number again !")

            """if player_1 == random_number:
                player_1_point = player_1_point + 1
                print(f"Player_1 have points are {player_1_point}")"""

            player_1_chance = player_1_chance + 1
            print(f"Your guesess left are {total_chance - player_1_chance} out of {total_chance} ")
        else:
            print("You entered wrong value !")


##################################### FOR NEXT PLAYER #####################################

        print("PLAYER 2")

        player_2 = int(input(f"Pleas guess the numbers between {a} and {b} : "))
        if player_2 == random_number:
            print("Congrates you guessed the number !")


            if player_2 == random_number:
                player_2_point = player_2_point + 1
                print(f"Player_2 have points are {player_2_point}")

            player_2_chance = player_2_chance + 1
            print(f"Your guesess left are {total_chance - player_2_chance} out of {total_chance}")

            a = int(input("Enter the value of a : "))

            b = int(input("Enter the value of b : "))
            for i in range(a, b):
                random_number = random.randint(a, b)
            print(random_number)

        elif player_2 > random_number:
            print("Wrong, guess a lower number again !")

            """if player_2 == random_number:
                player_2_point = player_2_point + 1
                print(f"Player_2 have points are {player_2_point}")"""

            player_2_chance = player_2_chance + 1
            print(f"Your guesess left are {total_chance - player_2_chance} out of {total_chance} ")

        elif player_2 < random_number:
            print("Wrong, guess a greater number again !")

            """if player_2 == random_number:
                player_2_point = player_2_point + 1
                print(f"Player_2 have points are {player_2_point}")"""

            player_2_chance = player_2_chance + 1
            print(f"Your guesess left are {total_chance - player_2_chance} out of {total_chance} ")
        else:
            print("You entered wrong value !")



    break
print(f"plyer_1 have {player_1_point} points and player_2 have {player_2_point} points !")
if player_1_point > player_2_point:
    print(f"Player_1 win the match with {player_1_point-player_2_point} points !")

elif player_1_point < player_2_point:
    print(f"Player_2 win the match with {player_2_point-player_1_point} points !")
else:
    print("Tie the match with ! ")

#############################################################################################################
######################################### next method ################################################################
#############################################################################################################

"""import random
def guessgame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b} : "))
    nguess = 1

    while guess != actual:
        if guess<actual:
            guess = int(input(f"Enter a bigger number : "))
            nguess = nguess + 1
        else:
            guess = int(input(f"Enter a smaller number : "))
            nguess = nguess + 1
    print(f"You guessed the number in {nguess} guesses")
    return nguess

if __name__ == "__main__":
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    actual = random.randint(a, b)
    print(actual)
    print("Player_1's turn ! ")
    g1 = guessgame(a, b, actual)
    print("Player_2's turn ! ")
    g2 = guessgame(a, b, actual)

    if g1 < g2:
        print("Player_1 won the match !")
    elif g1 > g2:
        print("Player_2 won the match !")
    else:
        print("Tie the match !")"""

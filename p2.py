

import os
import random

while True:
    os.system("cls")
    x = random.randint(0, 10)
    a = 0

    print("i have a number between 0 and 10, try and guess it")

    while True:
        user = int(input("your guess: "))

        a += 1

        if user == x:
            print("you've guessed my number!")
            print(f"it took you {a} guesses")
            break

        elif user > x+2:
            print("too high, try again.")

        elif user < x-2:
            print("too low, try again.")

        elif user > x:
            print("a bit high, try again.")

        elif user < x:
            print("a bit low, try again.")


    again = input("do you want to play again?(y/n): ")


    if again == "y" :
        os.system("cls")
        break

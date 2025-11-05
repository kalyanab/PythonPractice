import sys
import random
from enum   import Enum

def Play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

        PlayerChoice = input("Enter.....\n1 Rock,\n2 paper,\n3 scissors:\n\n")
        if PlayerChoice not in ["1","2","3"]:
           print("Please enter the value 1 or 2 or 3")
           return Play_rps()

        Player = int(PlayerChoice)

        Computerchoice = random.choice("123")
        Computer = int(Computerchoice)

        print("You chose " + PlayerChoice)
        print("Python chose " + Computerchoice)

        if Player == 1 and Computer ==3:
            print("🥳🥳 You won...")
        elif Player == 2 and Computer ==1:
            print("🥳🥳 You won...")
        elif Player == 3 and Computer ==2:
            print("🥳🥳 You won...")
        elif Player == Computer:
            print("🪢 Game is tie")
        else:
            print("😁 Python Won")

        playagin_input = input("Do you want to play again? \n yes \n no \n")
        if playagin_input.lower() == "yes":
            continue
        else:
            playagin = False
            print("Thanks for playing...")
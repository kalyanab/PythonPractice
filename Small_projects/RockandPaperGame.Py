import sys
import random

PlayerChoice = input("Enter.....\n1 Rock,\n2 paper,\n3 scissors:\n\n")
Player = int(PlayerChoice)

if  Player < 1 or Player > 3:
    sys.exit("Please enter the value 1 or 2 or 3")

Computerchoice = random.choice("123")
Computer = int(Computerchoice)

print("You chose " + PlayerChoice)
print("Python chose " + Computerchoice)

if Player == 1 and Computer ==3:
    print("You won...")
elif Player == 2 and Computer ==1:
    print("You won...")
elif Player == 3 and Computer ==2:
    print("You won...")
elif Player == Computer:
else:
    print("Python Won")
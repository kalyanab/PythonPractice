import sys
import random

playagin = True
while playagin:
    PlayerChoice = input("Enter.....\n1 Rock,\n2 paper,\n3 scissors:\n\n")
    Player = int(PlayerChoice)

    if  Player < 1 or Player > 3:
        sys.exit("Please enter the value 1 or 2 or 3")

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

playagin = input("Do you want to play again? (yes/no): ")
# if playagin.lower() != "yes":
#     print("thank you for playing...")
#     playagin = False
#     print("Thanks for playing...")
# else:
#     playagin = True
if playagin.lower() == "yes":
    playagin = True
else:
    playagin.lower() == "no"
    playagin = False
    print("Thanks for playing...")
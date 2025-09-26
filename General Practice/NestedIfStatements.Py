Weather = input("Enter Weather type :")
Time_Of_the_Day = input("Enter time of the day :")

if Weather == "Sunny":
    if Time_Of_the_Day == "Day":
        print("We can go out")
    else:
       print("Stay at home")
elif Weather == "Rainy":
    print("Its raining better dont go out")
elif Weather == "Snowy":
    if Time_Of_the_Day == "Night":
        print("Drink a cup of tea")
    else:
        print("Drink a cup of Coffee")
    
else:
    print("Just relax")

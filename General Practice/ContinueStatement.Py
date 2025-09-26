Candies = 10

for i in range(Candies):
    print("Distributing")

    if  Candies - i == 6:
        print("Only five left")
        continue
print("Giving candies to friend")
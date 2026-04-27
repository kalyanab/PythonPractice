# def add_one(num):
#     if (num >= 9):
#         return num + 1
    
#     total = num + 1
#     print(total)

#     return add_one(total)
# add_one(0)

# mynewtotal = add_one(0)
# print(mynewtotal)


n = int(input("Enter a number: "))
b = 1

for i in range(1, n + 1):
    for j in range (1,i+1):
      print(b)
      b +=1
      print()
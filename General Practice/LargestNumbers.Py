a = input()

x,y,z = a.split(",")
num1 = int (x)
num2 = int (y)
num3 = int (z)

greater = 0
if  num1>num2 and num1>num3:
    greater = num1
elif num2>num3:
    greater = num2
else:
    greater = num3
print("The greatest values is: ",greater)




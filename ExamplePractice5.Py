# Finding Factorial 

n = int(input("Give the value of n:"))
Factorial = 1

while n>0:
    Factorial = Factorial * n
    n-=1
print(Factorial)
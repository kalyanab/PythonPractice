#Quadratic roots

a = int(input("Give a :"))
b = int(input("Give b :"))
c = int(input("Give c :"))

root1 = 0
root2 = 0
d = (b**2)-4*a*c
root1 = (-b + (d**(0.05)))/2*a
root2 = (-b - (d**(0.05)))/2*a
print(f"Roots: ({root1},{root2})")


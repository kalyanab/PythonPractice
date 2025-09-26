#Finding the area of a circle

radius = int(input("Give the radius :"))
#Method1
#print("Area of the circle is:",3.14*radius*radius)

#Method2
print(f"Area of the circle is:{3.14*radius*radius}")

#Method3
# Instead of printing formula every time we can store the formula in variable
#a = 3.14*radius*radius

#Method4
#Instead of using radius twice we can write as:
a = 3.14*(radius**2)
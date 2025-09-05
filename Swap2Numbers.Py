#swapping the values of two variable without using a temporary variable.

#Method1: Using temporary variable
'''
a = int(input("Give the value of a :"))
b = int(input("Give the value of b :"))

temp = a
a = b
b = temp

print(f"The value of a is :{a}")
print(f"The value of b is :{b}") 
'''

#Method2: Without using temporary variable

a = int(input("Give a value :"))
b = int(input("Give b value :"))
b = b + a
a = b - a
b = b - a
print(f"The value of a is :{a}")
print(f"The value of b is :{b}")
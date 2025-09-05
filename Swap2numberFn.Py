def swap(a,b):
    b = b + a
    a = b - a
    b = b - a
    print(f"The value of a is :{a}")
    print(f"The value of b is :{b}")
swap(10,5)
swap(15,20)
swap(10,20)
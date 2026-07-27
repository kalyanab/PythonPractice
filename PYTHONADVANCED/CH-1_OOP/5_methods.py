class MyClass:


    my_var = 100
    #Dunder method or Magic method
    def __init__(self):
        print("This is a constructor method")
    
    #Dunder method for string
    def __str__(self):
        return "string representation of the object"

    @classmethod
    def _change_value(cls,new_value):
        cls.my_var = new_value
    def dummy(self):
        return "This is a dummy method"
obj1 = MyClass()
print(obj1.my_var)
obj1._change_value(200)
print(obj1.my_var)
obj2 = MyClass()
print(obj2.my_var)
obj3 = MyClass()
print(obj3.dummy())
obj4 = MyClass()
print(obj4.__str__())
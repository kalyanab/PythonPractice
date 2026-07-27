class MyClass:
   var1 = "kalyan"
   var2 = "abhi"
   def __init__(self,dy1,dy2,dy3):
    self.dy1 = dy1
    self.dy2 = dy2
    self.dy3 = dy3
   def func1(self):
    print(f"Hello world{self.dy1}")
   def func2(self):
    print(f"Hello Globe{self.dy2}")
   def func3(self):
    print(f"Hello universe{self.dy3}")

obj = MyClass(" Ram"," krish"," kumar")
obj.func2() 

obj_new = MyClass("abc"," xyz"," pqr")
obj.var2 = "Changed"
print(obj.var2)
class MyClass:
   var1 = "kalyan"
   var2 = "abhi"
   def __init__(self,dy1,dy2,dy3):
    self.dy1 = dy1 #public variable
    self.__dy2 = dy2 #Private variable
    self._dy3 = dy3 #Protected variable
   def func1(self):
    print(f"Hello world{self.dy1}")
   def func2(self):
    print(f"Hello Globe{self.__dy2}")
   def func3(self):
    print(f"Hello universe{self._dy3}")
obj = MyClass(" Ram"," krish"," kumar")
obj.dy1 = "kiran"
print(obj.dy1)

#obj._dy3 = "kumar"
print(obj._dy3)
import numpy as np
# # 0 dimensional array
# c = np.array([0])
# print(c)

# # 1 dimensional array
# a = np.array([1,2,3,4,5])
# print(a)

# # 2 dimensional array
# b = np.array([[30,40,50],[60,70,80]])
# print(b[1][0])

# # 3 dimensional array
# d = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
# print(d[0][1][0])

# Method -2 asarray() with nditer()
# a = ([[10,20],[40,50]])
# b = np.asarray(a,dtype = int,order = 'C')
# for i in np.nditer(b):
#     print(i)

#Method  - 3 Frombuffer method()
# a = b"Welcome to Python"
# b = np.frombuffer(a,dtype = 'S1',count = 2,offset = 9)
# print(b)

#Method - 4 fromiter() method
# a = [10,20,30,40]
# b =np.fromiter(a,dtype = int,count = 3)
# print(b)

#Inialising arrays
# 1.Zeros Method 1:
# a = np.zeros(3)
# print(a)

# #Zeroes Method 2:
# a = np.zeros([2,3,3])
# print(a)

#2.Full
# a = np.full([2,3],10)
# print(a)

# #3.Random
# a = np.random.rand(2,3)
# print(a)

#4 One 
# a = np.ones([2,3])
# print(a)

# Eye
# a = np.eye(3)
# print(a)

#6.Numerical Ranges
#Arange
# a = np.arange(0,100,20,dtype=float)
# print(a)

# 7.Line Space
# a = np.linspace(10,100,10,endpoint=False,retstep=True,dtype=int)
# print(a)

#8.Logspace
# a = np.logspace(1,10,10,base=2)
# print(a)

#Append method
# a = np.array([10,20,30])
# b = np.array([40,50,60])
# c = np.append(b,a).reshape(3,2)
# print(c)

#Insert method
# a = [10,20,30,40]
# np.insert(a,3,[35,45])
# print(a)

#Split
a = np.arange(10,110,10)
b = np.split(a,5)
print(b)

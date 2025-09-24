# input : [1,2,3,2,1,4,2,5]
# input2 : 2

# Method 1:
# l = [int(item) for item in input("Give the input : ").split(",")]
# n = int(input())
# c = l.count(n)
# print(c)

 
#Method 2 : something wrong not able to execute

l = [int(item) for item in input("Give the input : ").split(",")]
n = int(input())

count = 0

for i in l:
    if i == n:
        count+=1
print(count)
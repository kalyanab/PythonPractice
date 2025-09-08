# Input : 10,20,30,20,10,50

# Method 1 :
inp = input().split(',')
l = [int(a) for a in inp]
s = set(l)
newL = list(s)
print(newL)




# Method 2 :
# inp = input().split(',')
# l = [int(item) for item in inp]
# newL = []
# for i in l:
#     if i in newL:
#         continue
#     else:
#         newL.append(i)
#     print(newL)
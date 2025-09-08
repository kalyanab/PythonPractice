# Input : 10,20,30,20,10,50
inp = input().split(',')
l = [int(item) for item in inp]
newL = []
for i in l:
    if i in newL:
        continue
    else:
        newL.append(i)
    print(newL)
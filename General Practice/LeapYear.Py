year = int(input())

Leap = False

if year%4 == 0 and (year%100 !=0 or year%400 ==0):
    Leap = True
else:
    Leap == False    
print(Leap)


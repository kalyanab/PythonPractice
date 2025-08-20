year = int(input())

Leap = False

if year%100 == 0 and year%400 !=0:
    Leap = False
elif year%4 ==0:
    Leap == True
else:
    Leap == False    
print(Leap)
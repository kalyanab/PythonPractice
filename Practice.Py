m = int(input("Enter the Maths marks:"))
s = int(input("Enter the Science marks:"))
e = int(input("Enter the English marks:"))

Total = m + s + e
Average  = Total/3
percentage = (Total/300)*100

if percentage > 90:
    grade = 'A'
elif percentage > 80 and percentage <= 90:
    grade = 'B'
elif percentage > 70 and percentage <= 80:
    grade = 'C'
else    :
    grade = 'P'

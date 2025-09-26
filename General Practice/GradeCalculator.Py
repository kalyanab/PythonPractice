m = int(input("Marks in Maths: "))
s = int(input("Marks in Science: "))
e = int(input("Marks in English: "))

Total = m + s + e
Average = Total / 3

percentage  = (Total / 300) * 100

if percentage >= 90:
    grade = 'A'
elif percentage > 80 and percentage < 90:
    grade = 'B'
elif percentage > 70 and percentage <= 80:
    grade = 'C'
else:
    grade = 'p'

print(f"Total Marks:{Total} \n average Marks:{Average} \n Percentage:{percentage}% \n Grade:{grade}")


name = input()

level = 1
counter = 0
sum_grades = 0
while level <= 12:
    grades = float(input())
    if grades >= 4:
        level += 1
        sum_grades += grades

print(f"{name} graduated. Average grade: {(sum_grades / 12):.2f}")

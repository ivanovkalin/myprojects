import math

income = float(input())
grade = float(input())
min_salary = float(input())

social_scholarship = 0
excellent_scholarship = 0

if income < min_salary and grade > 4.50:
    social_scholarship = min_salary * 0.35
if grade >= 5.50:
    excellent_scholarship = grade * 25

excellent_scholarship = int(excellent_scholarship)
social_scholarship = int(social_scholarship)

if (income >= min_salary and grade < 5.50) or (income < min_salary and grade < 4.5):
    print("You cannot get a scholarship!")
elif social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif excellent_scholarship > social_scholarship:
    print(f"You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN")


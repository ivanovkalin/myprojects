flower_type = input()
number_of_flowers = int(input())
budget = int(input())
price = 0

if flower_type == "Roses":
    price = 5
    if number_of_flowers >= 80:
        price *= 0.90
elif flower_type == "Dahlias":
    price = 3.80
    if number_of_flowers >= 90:
        price *= 0.85
elif flower_type == "Tulips":
    price = 2.80
    if number_of_flowers >= 80:
        price *= 0.85
elif flower_type == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        price *= 1.15
elif flower_type == "Gladiolus":
    price = 3
    if number_of_flowers < 80:
        price *= 1.20

money_total = price * number_of_flowers

if budget >= money_total:
    money_left = budget - money_total
    print(f'Hey, you have a great garden with {number_of_flowers} {flower_type} and {money_left:.2f} leva left.')
else:
    money_needed = money_total - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')
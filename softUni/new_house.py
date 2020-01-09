type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

discount = 0
money = 0
price = 0
not_enough_money = 0
enough_money = 0

if type_of_flower == "Roses":
    price = 5
    if number_of_flowers > 80:
        discount = 0.1
        money = (number_of_flowers * price)
        money -= money * discount
    else:
        money = (number_of_flowers * price)

elif type_of_flower == "Dahlias":
    price = 3.8
    if number_of_flowers > 90:
        discount = 0.15
        money = (number_of_flowers * price)
        money -= money * discount
    else:
        money = (number_of_flowers * price)

elif type_of_flower == "Tulips":
    price = 2.8
    if number_of_flowers > 80:
        discount = 0.15
        money = (number_of_flowers * price)
        money -= money * discount
    else:
        money = (number_of_flowers * price)

elif type_of_flower == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        discount = 0.15
        money = (number_of_flowers * price)
        money += money * discount
    else:
        money = (number_of_flowers * price)

elif type_of_flower == "Gladiolus":
    price = 2.5
    if number_of_flowers < 80:
        discount = 0.2
        money = (number_of_flowers * price)
        money += money * discount
    else:
        money = (number_of_flowers * price)


if money > budget:
    not_enough_money = money - budget
    print(f"Not enough money, you need {not_enough_money:.2f} leva more.")
else:
    if money <= budget:
        enough_money = budget - money
        print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {enough_money:.2f} leva left.")

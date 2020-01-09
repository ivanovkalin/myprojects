

budget = int(input())
season = input()
fishermen = int(input())

ship_cost = 0

if season == "Spring":
    ship_cost = 3000

    if fishermen <= 6:
        ship_cost *= 0.9
    elif fishermen <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75

    if fishermen % 2 == 0:
        ship_cost *= 0.95

elif season == "Summer":
    ship_cost = 4200

    if fishermen <= 6:
        ship_cost *= 0.9
    elif fishermen <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75

    if fishermen % 2 == 0:
        ship_cost *= 0.95

elif season == "Autumn":
    ship_cost = 4200

    if fishermen <= 6:
        ship_cost *= 0.9
    elif fishermen <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75

elif season == "Winter":
    ship_cost = 2600

    if fishermen <= 6:
        ship_cost *= 0.9
    elif fishermen <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75

    if fishermen % 2 == 0:
        ship_cost *= 0.95


if budget >= ship_cost:
    money_left = budget - ship_cost
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = ship_cost - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")

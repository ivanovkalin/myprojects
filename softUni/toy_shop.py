
# Toy prices
puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

# Console Input
excursion_price = float(input())
quantity_puzzles = int(input())
quantity_talking_dolls = int(input())
quantity_teddy_bears = int(input())
quantity_minions = int(input())
quantity_trucks = int(input())

puzzle_sum = quantity_puzzles * puzzle
dolls_sum = quantity_talking_dolls * talking_doll
bears_sum = quantity_teddy_bears * teddy_bear
minions_sum = quantity_minions * minion
trucks_sum = quantity_trucks * truck



total_sum = puzzle_sum + dolls_sum + bears_sum + minions_sum + trucks_sum
total_toys_count = quantity_puzzles + quantity_talking_dolls + quantity_teddy_bears + quantity_minions + quantity_trucks

if total_toys_count >= 50:
    total_sum = total_sum - total_sum * 0.25

total_sum -= total_sum * 0.1

money_left = total_sum - excursion_price
if total_sum >= excursion_price:
    print (f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")


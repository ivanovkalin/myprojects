

active_camp_days = int(input())
number_of_bakers = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cake_value = 45
waffles_value = 5.80
pancakes_value = 3.20

cake_price = cakes_count * cake_value
waffles_price = waffles_count * waffles_value
pancakes_price = pancakes_count * pancakes_value

daily_total = (cake_price + waffles_price + pancakes_price) * number_of_bakers

total_days_sum = daily_total * active_camp_days
final_sum = total_days_sum - (1 / 8 * total_days_sum)

print(f'{final_sum:.2f}')




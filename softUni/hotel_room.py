
month = input()
nights = int(input())

Apartment = 0
Studio = 0
discount = 0

result_apartment = 0
result_studio = 0

if month == "May" or month == "October":
    Apartment = 65
    Studio = 50

    if 7 < nights <= 14:
        Studio = Studio * 0.05
    elif nights > 14:
        Studio -= Studio * 0.3
        Apartment -= Apartment * 0.1

elif month == "June" or month == "September":
    Apartment = 68.70
    Studio = 75.20

    if nights > 14:
        Studio -= Studio * 0.2
        Apartment -= Apartment * 0.1

elif month == "July" or month == "August":
    Apartment = 77
    Studio = 76

    if nights > 14:
        Apartment -= Apartment * 0.1
        Studio = 76

result_apartment = Apartment * nights
result_studio = Studio * nights

print(f"Apartment: {result_apartment:.2f} lv.\nStudio: {result_studio:.2f} lv.")

month = input()
days = int(input())

total_price_room = 0
total_price_apart = 0

if month == 'May' or month == 'October':
    total_price_room = days * 50
    total_price_apart = days * 65
    if 7 < days <= 14:
        total_price_room -= total_price_room * 0.05
    elif days > 14:
        total_price_room -= total_price_room * 0.30
elif month == 'June' or month == 'September ':
    total_price_room = days * 75.20
    total_price_apart = days * 68.70
    if days > 14:
        total_price_room -= total_price_room * 0.20
elif month == 'July' or month == 'August':
    total_price_room = days * 76
    total_price_apart = days * 77

if days > 14:
    total_price_apart -= total_price_apart * 0.10

print(f'Apartment: {total_price_apart:.2f} lv.')
print(f'Studio: {total_price_room:.2f} lv.')

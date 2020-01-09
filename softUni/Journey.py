budget = float(input())
season = input()

destination = 0
type_holiday = 0

if budget <= 100:
    destination = "Bulgaria"

    if season == "winter":
        budget = budget * 0.7
        type_holiday = "Hotel"

    elif season == "summer":
        budget = budget * 0.3
        type_holiday = "Camp"

elif budget <= 1000:
    destination = "Balkans"

    if season == "winter":
        budget = budget * 0.8
        type_holiday = "Hotel"

    elif season == "summer":
        budget = budget * 0.4
        type_holiday = "Camp"

elif budget > 1000:
    destination = "Europe"

    if season == " winter" or "Summer":
        budget = budget * 0.9
        type_holiday = "Hotel"

print(f"Somewhere in {destination}")
print (f"{type_holiday} - {budget:.2f}")





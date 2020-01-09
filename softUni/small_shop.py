
product = input()
city = input()
quantity = float(input())

coffee = 0
water = 0
beer = 0
sweets = 0
peanuts = 0

if product == "coffee":
    if city == "Sofia":
        coffee = 0.50
        print(coffee * quantity)
    elif city == "Plovdiv":
        coffee = 0.40
        print(coffee * quantity)
    elif city == "Varna":
        coffee = 0.45
        print(coffee * quantity)

if product == "peanuts":
    if city == "Sofia":
        peanuts = 1.60
        print(peanuts * quantity)
    elif city == "Plovdiv":
        peanuts = 1.50
        print(peanuts * quantity)
    elif city == "Varna":
        peanuts = 1.55
        print(peanuts * quantity)

if product == "water":
    if city == "Sofia":
        water = 0.80
        print(water * quantity)
    elif city == "Plovdiv":
        water = 0.70
        print(water * quantity)
    elif city == "Varna":
        water = 0.70
        print(water * quantity)

if product == "beer":
    if city == "Sofia":
        beer = 1.20
        print(beer * quantity)
    elif city == "Plovdiv":
        beer = 1.15
        print(beer * quantity)
    elif city == "Varna":
        beer = 1.10
        print(beer * quantity)

if product == "sweets":
    if city == "Sofia":
        sweets = 1.45
        print(sweets * quantity)
    elif city == "Plovdiv":
        sweets = 1.30
        print(sweets * quantity)
    elif city == "Varna":
        sweets = 1.35
        print(sweets * quantity)




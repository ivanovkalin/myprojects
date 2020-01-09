installments_count = int(input())

installments_made_counter = 0
balance = 0

while installments_made_counter < installments_count:
    money = float(input())
    if money < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {money:.2f}")
    balance += money
    installments_made_counter += 1

print(f"Total: {balance:.2f}")



square_meters = float(input())
price_for_square_meter = 7.61
price = square_meters * price_for_square_meter
discount = 0.18
total_discount_percentage = discount * price
total_discount = price - total_discount_percentage

print (f"The final price is: {total_discount:.2f} lv.")
print(f"The discount is: {total_discount_percentage:.2f} lv.")


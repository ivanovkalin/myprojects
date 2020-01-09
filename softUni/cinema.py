
screening_type = input()
row_numbers = int(input())
column_numbers = int(input())

price = 0
total = 0

if screening_type == "Premiere":
    price = 12
    total = (row_numbers * column_numbers) * 12
elif screening_type == "Normal":
    price = 7.5
    total = (row_numbers * column_numbers) * 7.5
elif screening_type == "Discount":
    price = 5.0
    total = (row_numbers * column_numbers) * 5

print(f"{total:.2f}")
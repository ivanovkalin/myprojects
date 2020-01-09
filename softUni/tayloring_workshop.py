
usd_exchange_rate = 1.85

number_of_rectangle_tables = int(input())
length_of_rectangle_tables_in_m = float(input())
width_of_rectangle_tables_in_m = float(input())

total_size_of_table_covers = number_of_rectangle_tables * (length_of_rectangle_tables_in_m  + 2 * 0.30) * (width_of_rectangle_tables_in_m + 2 * 0.30)
total_area_of_table_mini_cover = number_of_rectangle_tables * (length_of_rectangle_tables_in_m / 2) * (length_of_rectangle_tables_in_m / 2)


price_in_usd = total_size_of_table_covers * 7 + total_area_of_table_mini_cover * 9
price_in_bgn =  price_in_usd * usd_exchange_rate

print(f"{price_in_usd:.2f} USD")
print(f"{price_in_bgn:.2f} BGN")
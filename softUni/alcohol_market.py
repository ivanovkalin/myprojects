
wiskey_lv = float(input())

beer_liters = float(input())
wine_liters = float(input())
rakia_liters = float(input())
wiskey_liters = float(input())

rakia_price = wiskey_lv / 2

wine_price = rakia_price - (0.4 * rakia_price)
beer_price = rakia_price - (0.8 * rakia_price)

rakia_total_price = rakia_liters * rakia_price
wine_total_price = wine_price * wine_liters
beer_total_price = beer_price * beer_liters
wiskey_total_price = wiskey_liters * wiskey_lv

grand_total = rakia_total_price + wine_total_price + beer_total_price + wiskey_total_price

print(f"{grand_total:.2f}")

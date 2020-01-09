import math

l_in_length_m = float(input())
w_in_width_m = float(input())
a_side_of_wardrobe = float(input())
wardrobe_size_in_cm = a_side_of_wardrobe * 100

size_hall = (l_in_length_m * 100) * (w_in_width_m * 100)

size_wardrobe = wardrobe_size_in_cm * wardrobe_size_in_cm

bench_size = size_hall / 10

free_space = size_hall - size_wardrobe - bench_size

number_of_dancers = free_space / (40 + 7000)

print(math.floor(number_of_dancers))
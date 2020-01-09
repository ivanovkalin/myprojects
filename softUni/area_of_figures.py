from math import pi

figure_type = input()
area = 0

if figure_type == "square":

    a = float(input())
    area = a * a

elif figure_type == "rectangle":

    a = float(input())
    b = float(input())
    area = a * b

elif figure_type == "circle":

    radius = float(input())
    area =  pi * radius * radius

elif figure_type == "triangle":

    side = float(input())
    height = float(input())
    area = (side * height) / 2

print(f"{area:.3f}")



x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs(x1 - x2)
width = abs(y1 - y2)

area = length * width
perimeter = length * 2 + width * 2

print(f'{area:.2f}')
print(f'{perimeter:.2f}')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

first_condition = (y1 == y or y == y2) and (x >= x1 and x<= x2)
second_condition =(x1 == x or x == x2) and (y >= y1 and y<= y2)

if first_condition or second_condition:
    print("Border")
else:
    print("Inside / Outside")

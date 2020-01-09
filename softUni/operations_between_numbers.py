n1 = int(input())
n2 = int(input())
operate = input()

sum = 0

if operate == '+':
    sum = n1 + n2
elif operate == '-':
    sum = n1 - n2
elif operate == '*':
    sum = n1 * n2

if operate != '/' and operate != "%":
    if sum % 2 == 0:
        print(f'{n1} {operate} {n2} = {sum} - even')
    else:
        print(f'{n1} {operate} {n2} = {sum} - odd')

if n2 != 0:
    if operate == '/':
        sum = n1 / n2
        print(f'{n1} {operate} {n2} = {sum:.2f}')
    elif operate == '%':
        sum = n1 % n2
        print(f'{n1} {operate} {n2} = {sum}')
else:
    print(f"Cannot divide {n1} by zero")

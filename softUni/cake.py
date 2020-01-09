
length = int(input())
width = int(input())

cake_size = length * width
is_cake_over = False

count = input()

while not count == "STOP":
    count = int(count)

    cake_size -= count

    if cake_size <= 0:
        is_cake_over = True
        print(f"No more cake left! You need {abs(cake_size)} pieces more.")
        break

    count = input()

if not is_cake_over:
    print(f"{cake_size} pieces are left.")

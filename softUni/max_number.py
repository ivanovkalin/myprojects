import sys

number_count = int(input())

counter = 0
biggest_n = -sys.maxsize

while counter < number_count:
    current_n = int(input())
    counter += 1
    if current_n > biggest_n:
        biggest_n = current_n

print(f"{biggest_n}")




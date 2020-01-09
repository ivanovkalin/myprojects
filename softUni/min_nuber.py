import sys

number_count = int(input())

counter = 0
smallest_n = sys.maxsize

while counter < number_count:
    current_n = int(input())
    counter += 1
    if current_n < smallest_n:
        smallest_n = current_n

print(smallest_n)




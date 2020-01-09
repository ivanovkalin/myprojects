first_place = int(input())
second_place = int(input())
third_place = int(input())

sum = first_place + second_place + third_place

minutes = sum // 60
seconds = sum % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")

else:
    print(f"{minutes}:{seconds}")
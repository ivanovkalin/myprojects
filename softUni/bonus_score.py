inputted_points = int(input())
bonus_points = 0

if inputted_points > 1000:
    added_points = inputted_points * 0.1
    bonus_points += added_points

elif inputted_points > 100:
    added_points = inputted_points * 0.2
    bonus_points += added_points

else:
    bonus_points += 5


if inputted_points % 2 == 0:
    bonus_points += 1

elif inputted_points % 10 == 5:
    bonus_points += 2

print(bonus_points)

sum = inputted_points + bonus_points
print(sum)

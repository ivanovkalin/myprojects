lenght_in_cm = int(input())
width_in_cm = int(input())
heihgt_in_cm = int(input())
taken_percents = float(input()) / 100

volume = (lenght_in_cm * width_in_cm * heihgt_in_cm) / 1000
volume -= volume * taken_percents

print(f"{volume:.3f}")
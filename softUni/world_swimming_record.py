
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_1m = float(input())

distance_to_swim = distance_in_meters * time_in_seconds_for_one_1m

added_time_per_15m = (distance_in_meters // 15) * 12.5

total_time = distance_to_swim + added_time_per_15m

if record_in_seconds > total_time :
    print(f" Yes, he succeeded! The new world record is {(total_time):.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time - record_in_seconds):.2f} seconds slower.")
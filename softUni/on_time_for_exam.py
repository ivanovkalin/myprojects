
exam_hours = int(input())
exam_minutes = int(input())

arrival_hours = int(input())
arrival_minutes = int(input())

late = "Late"
on_time = "On Time"
early = "Early"

exam_time = (exam_hours * 60) + exam_minutes
arrival_time = (arrival_hours * 60) * arrival_minutes

total_minutes_difference = arrival_time - exam_time





student_arrival = late
if total_minutes_difference < -30:
    student_arrival = early
elif total_minutes_difference <= 0:
    student_arrival = on_time

result = ""
if total_minutes_difference != 0:
    




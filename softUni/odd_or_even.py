
number_input = int(input("Please choose a number: "))
check_number = number_input % 2

if check_number > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
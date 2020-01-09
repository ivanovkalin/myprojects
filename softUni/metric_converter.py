
number_to_be_converted = float(input())
what_is_being_converted = input()
to_what_should_be_converted = input()

if what_is_being_converted == "cm" and to_what_should_be_converted == "m":
    ans = float(number_to_be_converted) * 0.01
    print(f"{ans:.3f}")
elif what_is_being_converted == "mm" and to_what_should_be_converted == "cm":
    ans = float(number_to_be_converted) * 0.1
    print(f"{ans:.3f}")
elif what_is_being_converted == "m" and to_what_should_be_converted == "cm":
    ans = float(number_to_be_converted) * 100
    print(f"{ans:.3f}")
elif what_is_being_converted == "cm" and to_what_should_be_converted == "mm":
    ans = float(number_to_be_converted) * 10
    print(f"{ans:.3f}")
elif what_is_being_converted == "mm" and to_what_should_be_converted == "m":
    ans = float(number_to_be_converted) * 0.001
    print(f"{ans:.3f}")
elif what_is_being_converted == "m" and to_what_should_be_converted == "mm":
    ans = float(number_to_be_converted) * 1000
    print(f"{ans:.3f}")

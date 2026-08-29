def number_checker(number): 
    if number > 10:
        return "big number"
    else:
        return "not a big number"

print(number_checker(11))
print(number_checker(5))


def two_number(first_num, second_num):
    if first_num > 10 and second_num > 10:
        return "big numbers"
    elif first_num > 10 or second_num > 10:
        return "mixed"
    else:
        return "small numbers"

print(two_number(5, 6))
print(two_number(11, 6))
print(two_number(11, 11))


last_guess = 0 
while last_guess != 3 and last_guess != 7:
    last_guess = int(input("please enter a number between 1 and 10: "))
print("You have guessed the number")


def add_numbers():
    total = 0 
    number = 1

    while number <= 10:
        total += number 
        number += 1

    return total 

print(add_numbers())
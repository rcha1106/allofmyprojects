#1
def count_to_ten():
    number = 1

    while number <= 10:
        print(number)
        number += 1

count_to_ten()

#2
def goup_by_two():
    number = 2 

    while number <= 10:
        print(number)
        number += 2

goup_by_two()

#3
def arg_add(max_value):
    number = 1

    while number <= max_value:
        print(number)
        number += 1

arg_add(6)

#4
def add_input():
    max_value = int(input("Please enter a max value: "))
    number = 1

    while number <= max_value:
        print(number)
        number += 1 

add_input()

#5
def doubling_sequence():
    value = 1

    while value < 1000:
        print(value)
        value = value * 2

doubling_sequence()

#6 
def doubling_sequence_arg(max_number):
    value = 1

    while value < max_number:
        print(value)
        value = value * 2 

doubling_sequence_arg(30)

#7
def add_input():
    max_value = int(input("Please enter a max value: "))
    number = 1
    total = 0 

    while number <= max_value:
        print(number)
        total = total + number 
        number += 1

    return total  

print(add_input())

#8
def doubling_sequence():
    value = 1
    total = 0

    while value < 1000:
        print(value)
        total = total + value
        value = value * 2

    return total

print(doubling_sequence())

#9 
def doubling_sequence_arg(max_number):
    value = 1
    total = 0

    while value < max_number:
        print(value)
        total = total + value
        value = value * 2 

    return total 

print(doubling_sequence_arg(30))
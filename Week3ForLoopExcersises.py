#1
def class_love_n_times(times_to_print):
    for i in range(times_to_print):
        print("I love CPDM-120")

class_love_n_times(6)

#2
def print_string_five_times(txt):
    for i in range(5):
        print(txt)

print_string_five_times("My name is Raj")

#3 
def print_string_n_times(txt, number):
    for i in range(number):
        print(txt)

print_string_n_times("I am Raj", 3)

#4
def two_to_twenty():
    for i in range(2, 20, 2):
        print(i)

two_to_twenty()

#5
def twelve_to_twenty():
    for i in range(12, 20, 2):
        print(i)

twelve_to_twenty()

#6
def five_to_zero_while():
    number = 5
    while number > 0:
        print(number)
        number = number - 1
    print("Blastoff!")

five_to_zero_while()

#7
def five_to_zero():
    for i in range(5, 0, -1):
        print(i)
    print("Blastoff!")

five_to_zero()

#8
def num_to_zero(num):
    for i in range(num, -1):
        print(num)
        num = num - 1
    print("Blastoff!")

num_to_zero(6)

#9
def num_to_zero(num):
    for i in range(num, -1):
        print(num)
        num = num - 1
    print("Blastoff!")

num_to_zero(2)

#10
def num_in_between(num1, num2):
    for i in range(num1, num2 + 1):
        print(i)

num_in_between(1, 10)

#11
def even_in_between(num1, num2):
    for i in range(num1, num2):
        if i % 2 == 0:
            print(i)

even_in_between(1, 10)
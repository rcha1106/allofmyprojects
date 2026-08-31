#Part 1
#1 
def is_positive(number): 
    if number > 0:
        print("True")
    else: 
        print("False")

is_positive(1)
is_positive(0)
is_positive(-1)


#2 
def print_even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    elif number % 2 == 1:
        print("odd")

print_even_or_odd(2)
print_even_or_odd(3)


#3
def larger_number(number1, number2):
    if number1 > number2:
        print("Number 1 is larger than number 2")
    elif number1 < number2:
        print("Number 1 is less than number 2")
    else: 
        print("Number 1 is equal to number 2")

larger_number(2, 1)
larger_number(1, 2)
larger_number(2, 2)


#4
def temperature_warning(temperature):
    if temperature < 32:
        print("Freezing!")
    elif temperature > 32:
        print("Not freezing")
    else:
        print("Exactly 32")

temperature_warning(23)
temperature_warning(67)
temperature_warning(32)


#5 
def calculate_discount(price):
    if price >= 100:
        price = price * 0.80
    else:
        price = price * 0.90

    return price 

print("Your price is", calculate_discount(120))
print("Your price is", calculate_discount(100))
print("Your price is", calculate_discount(90))


#6
def grade_message(score):
    if score >= 70:
        print("Passing")
    else:
        print("Not passing")

grade_message(92)
grade_message(63)
grade_message(70)


#7
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(6))
print(is_even(3))


# 8
def is_divisible_by_17(number):
    if number % 17 == 0:
        return True
    else:
        return False

print(is_divisible_by_17(34))
print(is_divisible_by_17(35))


# 9
def is_divisible_by(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False

print(is_divisible_by(27, 3))
print(is_divisible_by(14, 3))


# Part 2
# 1
def count_up(number):
    count = 1

    while count <= number:
        print(count)
        count = count + 1

count_up(5)


# 2
def count_down(number):
    count = number

    while count >= 1:
        print(count)
        count = count - 1

count_down(5)


# 3
def sum_to(number):
    count = 1
    total = 0

    while count <= number:
        total = total + count
        count = count + 1

    return total

answer = sum_to(5)
print(answer)


# 4
def double_until_large(number):

    while number < 100:
        number = number * 2
        print(number)

    return number

answer = double_until_large(10)
print("Final:", answer)


# 5
def count_evens(number):
    count = 1
    total = 0

    while count <= number:
        if count % 2 == 0:
            total = total + 1

        count = count + 1

    return total

answer = count_evens(10)
print(answer)


# 6
def keep_adding(number):
    total = 0

    while total < 100:
        total = total + number
        print(total)

    return total

answer = keep_adding(30)
print("Final:", answer)
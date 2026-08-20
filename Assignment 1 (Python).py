#Part 1

def find_area():
    circradi = float(input("What is the radius of the circle: "))
    pi = 3.14
    result = pi * circradi ** 2
    return result

print(find_area())

#Part 2

def three_nums():
    first_num = float(input("What do you want your first number to be: "))
    second_num = float(input("What do you want you second number to be: "))
    third_num = float(input("What do you want your third number to be: "))
    sum = first_num + second_num
    product = first_num * third_num
    quotient = second_num / third_num
    remainder = third_num % second_num
    add_mul = (first_num + second_num) * 5
    add_div = (first_num + third_num) / second_num + third_num
    div_rema = third_num % (first_num + second_num)
    result = (first_num ** 3 + second_num ** 3 + third_num ** 3) / first_num
    cubed = (first_num + third_num) ** 3 / (first_num + second_num) ** 2
    print(sum)
    print(product)
    print(quotient)
    print(remainder)
    print(add_mul)
    print(add_div)
    print(div_rema)
    print(result)
    print(cubed)

three_nums()
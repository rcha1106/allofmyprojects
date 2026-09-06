#1
def calculate_rect_area(length, height):
    area = length * height
    return area 

print(calculate_rect_area(5, 7))

#2 
def calculate_triangle_area(length, height):
    area = length * height 
    return area

print(calculate_triangle_area(3, 5))

#3
def calculate_shape_area(length, height, shape):
    if shape == "rectangle":
        return calculate_rect_area(length, height)
    elif shape == "triangle":
        return calculate_triangle_area(length, height)
    else:
        return 

print(calculate_shape_area(5, 6, "rectangle"))
print(calculate_shape_area(7, 2, "triangle"))

#4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(5))
print(is_even(6))

#5
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(5))
print(is_odd(6))

#6
def multiplication_table(number):
    for i in range(1, 11):
        print(number * i)

multiplication_table(3)

#7
def calculate_total_cost(price, tax_rate = 0.07):
    print(price + (price * tax_rate))

calculate_total_cost(52)
calculate_total_cost(52, 0.08)
#1
def display_instructions():
    '''
    This function just prints 3 lines
    '''
    print("This program will demonstrate how to make and use functions in Python.")
    print("In addition it will demonstrate how to pass values and variables into")
    print("a procedure as parameters")

display_instructions()


#2
def display_message(print_count):
    '''
    This prints "I love CPDM120" as many times as the argument print_count is
    '''
    for i in range(print_count):
        print("I love CPDM120")

display_message(3)


#3
def get_larger_value(value1, value2):
    '''
    This function comapres value1 to value2 and seeing which is larger or equal by taking arguments
    '''
    if value1 > value2:
        print("Value 1 is larger than value 2")
    elif value2 > value1:
        print("Value 2 is larger than value 1")
    else:
        print("Value 1 and value 2 are equal")

get_larger_value(2, 1)
get_larger_value(1, 2)
get_larger_value(1, 1)


#4
def get_larger_value(value1, value2, value3, value4, value5, value6, value7):
    '''
    This function finds out the maximum value from the 7 values. In this case we can't use the max() function so we used this if/elif logic
    '''

    if value1 > value2 and value1 > value3 and value1 > value4 and value1 > value5 and value1 > value6 and value1 > value7:
        return value1


    if value2 > value1 and value2 > value3 and value2 > value4 and value2 > value5 and value2 > value6 and value2 > value7:
        return value2


    if value3 > value1 and value3 > value2 and value3 > value4 and value3 > value5 and value3 > value6 and value3 > value7:
        return value3


    if value4 > value1 and value4 > value2 and value4 > value3 and value4 > value5 and value4 > value6 and value4 > value7:
        return value4


    if value5 > value1 and value5 > value2 and value5 > value3 and value5 > value4 and value5 > value6 and value5 > value7:
        return value5


    if value6 > value1 and value6 > value2 and value6 > value3 and value6 > value4 and value6 > value5 and value6 > value7:
        return value6


    if value7 > value1 and value7 > value2 and value7 > value3 and value7 > value4 and value7 > value5 and value7 > value6:
        return value7

print(get_larger_value(1, 2, 3, 4, 5, 6, 7))
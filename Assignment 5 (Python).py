# Function using a while loop
def calc_wage_while(starting_wage, raise_percent):
    wage = starting_wage
    year = 1

    while year <= 10:
        yearly_pay = wage * 40 * 52
        print("Year ", year, " - ", yearly_pay)
        wage = wage + (wage * raise_percent / 100)
        year = year + 1


# Function using a for loop
def calc_wage_for(starting_wage, raise_percent):
    wage = starting_wage

    for year in range(1, 11):
        yearly_pay = wage * 40 * 52
        print("Year ", year, " - ", yearly_pay)
        wage = wage + (wage * raise_percent / 100)


# Call both functions
calc_wage_while(20, 5)
calc_wage_for(20, 5)

# I think the for loop version is better because it is easier to read
# and it works well when you know exactly how many times you want to repeat something.
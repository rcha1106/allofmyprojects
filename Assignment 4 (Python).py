def rental_cost():
    season = int(input("What season are you planning to come? Type 1 for OFF SEASON, Type 2 for PEAK SEASON, Type 3 for STANDARD SEASON: "))
    amt_of_days = int(input("How many days are you planning to stay?: "))
    membership = input("Are you a member of the AAA or the AARP? If you ARE, type: YES  If NOT, type: NO : ")
    florida_resident = int(input("Are you from the State of Florida? Type 1 for YES and Type 2 for NO: "))

    if season == 1:
        subtotal = amt_of_days * 50.00
    elif season == 2:
        subtotal = amt_of_days * 150.00
    elif season == 3:
        subtotal = amt_of_days * 100.00

    final_price = subtotal

    if amt_of_days > 30:
        final_price -= final_price * 10 / 100
    elif amt_of_days > 14:
        final_price -= final_price * 5 / 100

    if membership == "YES":
        final_price -= final_price * 2.5 / 100

    if florida_resident == 1:
        final_price -= final_price * 10 / 100

    print("Your subtotal is: $", subtotal)
    print("Your final price is: $", final_price)

rental_cost()
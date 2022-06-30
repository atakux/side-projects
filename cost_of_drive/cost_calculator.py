"""
Calculation of User's Trip Cost
Based on user's specific mpg, price of gas they pay, and total amount
of miles they plan to drive
"""

# try except just in case user inputs something thats not a number
try:
    # receive user's specific info to prepare for calculations
    mpg = float(input("Enter your miles per gallon: "))
    current_price = float(input("Enter current gas price: "))

    # calculating the cost of 1 mile
    # the ratio to calculate cost of 1 mile
    ratio = 1 / mpg
    cost_of_1mi = ratio * current_price

    # receive user input of how many miles they will be driving
    how_many_miles = float(input("How many miles are you driving ? "))

    # calculate the cost of the trip based on how many
    # miles they plan to drive and the cost of 1 mi
    # and round it
    trip_cost = cost_of_1mi * how_many_miles
    trip_cost = '{:0.2f}'.format(trip_cost)

    # display user's cost
    if int(how_many_miles) == 1:
        print(f"Your {how_many_miles} mile trip will cost ${trip_cost} total. Safe driving :>")
    else:
        print(f"Your {how_many_miles} miles trip will cost ${trip_cost} total. Safe driving :>")
except:
    print("Invalid input detected. Run again.")

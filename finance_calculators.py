"""
Explain "investment" and "bond" option to user.
Ask user to input their option.
If the input from user is not valid, ask user to input again.
Ask user to input elements for calculation.
Calculate the result according to chosen option.
print the calculation result.
"""

import math

print("""
investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan
""")

while True:

    choice = (input("Enter either 'investment' or 'bond' from the menu above to proceed: \n").lower())
    if choice == "investment":
        while True:
            try:
                amount = float(input("Enter the amount of money (in $) that you want to deposit in: \n"))
                interest_rate = float(input("Enter the interest rate (as a percentage) that you expect to earn: \n"))/100
                number_year = int(input("Enter the number of year you plan on investing: \n"))
                interest = (input("Enter either 'simple' or 'compound' interest you are earning: \n").lower())

                while True:
                    if interest == "simple":
                        total_amount = amount * (1 + interest_rate * number_year)
                        break
                    elif interest == "compound":
                        total_amount = amount * math.pow((1 + interest_rate), number_year)
                        break
                    else:
                        print("Sorry you have not enter either one of interest options correctly.  Please enter again: \n")

                total_amount = round(total_amount, 2)
                print(f"The total amount you will receive: ${total_amount}")
                break
            except ValueError:
                print("Invalid input.  Please enter again.")
        break
    elif choice == "bond":
        while True:
            try:
                present_value_house = float(input("Enter the present value of your house (in $): \n"))
                interest_rate_house = float(input("Enter the interest rate (as a percentage) that you pay: \n"))/100/12
                number_month = int(input("Enter the number of months you plan to take to repay the bond: \n"))

                monthly_repayment = (interest_rate_house * present_value_house) / (1 - (1 + interest_rate_house) ** (- number_month))

                monthly_repayment = round(monthly_repayment, 2)
                print(f"The amount that you will have to be repaid on a home loan each month will be: ${monthly_repayment}")
                break
            except ValueError:
                print("Invalid input.  Please enter again.")
        break
    else:
        print("Sorry you have not enter either one of options correctly.  Please enter again: \n")

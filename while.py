"""
Define number, count, average.
Ask user to input a number
Ask user enter again if invalid value is entered
increase count when user input a valid number
calculate total sum of numbers entered
stop loop when user entered "-1"
calculate average
print average
"""

number = 0
count = 0
average = 0
while True:
    try:
        enter_number = float(input("Please enter a number: \n"))
        if enter_number == -1:
            break
        number = number + enter_number
        count += 1
    except ValueError:
        print("Invalid input.  Please enter a number again.")
average = number/count
print(f"The average of numbers you entered is {average:.2f}")

"""
Ask user to input his/her age, and store it as integer variable, and name it as "age"
If the age is over 100, output the message "Sorry, you're dead.")
If the age is 65 or over, output the message "Enjoy your retirement!")
If the age is 40 or over, output the message "You're over the hill")
If the age is 21, output the message "Congrats on your 21st!"
If the age is under 13, output the message "You qualify for the kiddie discount.")
Else, out the message "Age is but a number.")
"""
age = int(input("What is your age? \n"))
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number")

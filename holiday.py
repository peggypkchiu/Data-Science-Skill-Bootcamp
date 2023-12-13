"""
Ask user to input their name
Ask user to input the city they will be flying to
Ask user to input the number of nights they will be staying at hotel
Ask user to input the number of days for which they will be hiring a car
If invalid input, ask user to enter again
Create the function to calculate hotel cost
Create the function to calculate plane cost
Create the function to calculate car rental cost
Create the function to calculate total holiday cost
Print all the details about the holiday, and show total cost.
"""

while True:
    try:
        user_name = input("What is your name:\n").capitalize()
        print("Hi " + user_name)
        user_city_flight = str(input("Please enter the city you will be flying to (Singapore/ Thailand/ France):\n").lower())
        if user_city_flight not in ["singapore", "france", "thailand"]:
            print("Invalid input.  Please enter again.")
        else:
            user_num_nights = int(input("Please enter the number of nights you will be staying at a hotel:\n"))
            user_rental_days = int(input("Please enter the number of days for which you will be hiring a car:\n"))
            break
    except ValueError:
        print("Invalid input.  Please enter again.")


def hotel_cost(num_nights):
    h = num_nights * 90
    return h


def plane_cost(city_flight):
    if city_flight == "singapore":
        city_plane_cost = 1000
    elif city_flight == "thailand":
        city_plane_cost = 800
    else:
        city_plane_cost = 300
    p = city_plane_cost
    return p


def car_rental(rental_days):
    c = rental_days * 50
    return c


def holiday_cost(city_flight, num_nights, rental_days):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total


user_holiday_cost = holiday_cost(user_city_flight, user_num_nights, user_rental_days)
print(f"{user_name}, you will be flying to {user_city_flight.capitalize()} with plane cost of GBP{plane_cost(user_city_flight)}, \n"
      f"and staying at hotel for {user_num_nights} nights with hotel cost of GBP{hotel_cost(user_num_nights)}, \n"
      f"and hiring a car for {user_rental_days} days with rental cost of GBP{car_rental(user_rental_days)}. \n"
      f"Your total holiday cost will be GBP{user_holiday_cost}.")

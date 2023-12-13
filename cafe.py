"""
Create a list called menu, which contains 4 items sold in the cafe.
Create a dictionary called stock, which contains the stock value for each item on the menu.
Create another dictionary called price, which contains the prices for each item on the menu.
Calculate total_stock worth in the cafe by looping through item in the menu list and accessing corresponding value by using item as key.
Print out the result of calculation.
"""
menu = ["coffee", "tea", "cake", "biscuit"]
stock = {"coffee": 10, "tea": 11, "cake": 12, "biscuit": 13}
price = {"coffee": 3.2, "tea": 3.3, "cake": 5.1, "biscuit": 4.2}
total_value = 0
for items in menu:
    stock_items = stock[items]
    price_items = price[items]
    item_value = stock_items * price_items
    total_value = total_value + item_value
print(f"The total_stock worth in the cafe is {total_value:.2f}")

import json
import os

def load_existing_orders(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return {}

def save_order_to_file(order, customer_name, file_name):
    all_orders = load_existing_orders(file_name)
    all_orders[customer_name] = order
    with open(file_name, 'w') as file:
        json.dump(all_orders, file, indent=4)
    print(f"Your order has been saved to {file_name}")

def display_menu(menu):
    print("Menu:")
    for index, (item, price) in enumerate(menu.items(), start=1):
        print(f"{index}. {item}: Rs {price}")
    print("\n")

def take_order(menu):
    order = {}
    menu_items = list(menu.keys())
    while True:
        item_number = input("Enter the serial number of the item you want to order (or '0' to finish): ").lower()
        if item_number == '0':
            break
        elif item_number.isdigit() and 1 <= int(item_number) <= len(menu_items):
            item_index = int(item_number) - 1
            item = menu_items[item_index]
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Sorry, that's not a valid menu item number.")
    return order

def calculate_total(order, menu):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def generate_receipt(order, menu, customer_name):
    print(f"Here's Your Receipt {customer_name}")
    for item, quantity in order.items():
        print(f"{item} x{quantity}: Rs{menu[item] * quantity}")
    total = calculate_total(order, menu)
    print(f"Total: Rs{total}\n")

def add_food_item(menu):
    item = input("Enter the name of the food item to add: ").title()
    price = int(input(f"Enter the price for {item}: "))
    menu[item] = price
    print(f"{item} has been added to the menu.\n")

def remove_food_item(menu):
    item = input("Enter the name of the food item to remove: ").title()
    if item in menu:
        del menu[item]
        print(f"{item} has been removed from the menu.\n")
    else:
        print(f"{item} is not in the menu.\n")

def admin_menu(menu):
    while True:
        print("Admin Menu:")
        print("1. Add Food Item")
        print("2. Remove Food Item")
        print("3. View Menu")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_food_item(menu)
        elif choice == '2':
            remove_food_item(menu)
        elif choice == '3':
            display_menu(menu)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.\n")

def user_menu(menu, orders_file):
    print("Welcome To Sk Alauddin Food App")
    customer_name = input("Please Enter Your Name: ").title()
    display_menu(menu)
    order = take_order(menu)
    total = calculate_total(order, menu)
    generate_receipt(order, menu, customer_name)
    save_order_to_file(order, customer_name, orders_file)
    print(f"Thank You For Your Order! Have a nice day {customer_name}")

menu = {
    "Pizza": 250,
    "Burger": 130,
    "Pasta": 180,
    "Salad": 110,
    "Soda": 20,
    "Water": 20
}
orders_file = "all_orders.json"

while True:
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    role = input("Enter your role: ")
    if role == '1':
        admin_menu(menu)
    elif role == '2':
        user_menu(menu, orders_file)
    elif role == '3':
        break
    else:
        print("Invalid choice. Please try again.\n")
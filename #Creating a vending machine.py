# Friendly greeting for vending machine
print("""
█▀▄▀█ ▄▀█ █▀█ █ █▄█ ▄▀█ █▀▄▀█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
█░▀░█ █▀█ █▀▄ █ ░█░ █▀█ █░▀░█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")

# Creating an Inventory made using nested dictionary
Menu_Inventory = {
    "Snacks": {
        "Takis": {"code": "S01", "price": 1.5, "stock": 10},
        "Cookie": {"code": "S02", "price": 2.0, "stock": 5},
        "Snickers": {"code": "S03", "price": 3.0, "stock": 8},
        "KitKat": {"code": "S04", "price": 3.0, "stock": 7},
    },
    "Drinks": {
        "Water": {"code": "D01", "price": 1.0, "stock": 20},
        "Coca Cola": {"code": "D02", "price": 2.5, "stock": 15},
        "Mango juice": {"code": "D03", "price": 2.0, "stock": 12},
        "Seven up": {"code": "D04", "price": 2.5, "stock": 15},
    },
    "Healthy Options": {
        "Energy Bar": {"code": "H01", "price": 2.0, "stock": 7},
        "Pretzels": {"code": "H02", "price": 2.5, "stock": 5},
        "Fruit Cup": {"code": "H03", "price": 3.0, "stock": 6},
        "Banana": {"code": "H04", "price": 2.0, "stock": 6},
    },
}

# Function for displaying the menu
def display_menu(menu):
    print("Welcome to the Vending Machine!")
    print("We have all you might need!\n")
    for category in menu:  # Loop through each category
        print(f"{category}:")
        for item in menu[category]:  # Loop through each item in the category
            details = menu[category][item]
            print(f"  {details['code']} - {item} (${details['price']}, Stock: {details['stock']})")
        print()  # Blank line after each category

# Function for getting the user input
def get_item_code():
    user_code = input(" Please enter the code of the item you want to purchase: ").strip().upper()
    return user_code

# Function for checking if the input is valid
def check_valid_code(user_code):
    for category, items in Menu_Inventory.items():
        for item, details in items.items():
            if details["code"] == user_code:
                return category, item, details
    return None, None, None

# Function for updating the stock after purchase
def reduce_stock(category, item):
    Menu_Inventory[category][item]["stock"] -= 1

# Function for handling the payment
def pay(price):
    print(f"Price: AED{price:.2f}")
    while True:
        try:
            money = float(input("Insert money: "))
            if money < price:
                print(f"You need AED{price - money:.2f} more.")
            else:
                change = money - price
                if change > 0:
                    print(f"Here is your change: AED{change:.2f}")
                print("Payment successful!")
                return True
        except ValueError:
            print("Invalid input. Enter a number.")

# Asking the user if they want another item
def ask_for_more():
    answer = input("Do you want to purchase another item? (yes/no): ").strip().lower()
    return answer == "yes"

# Main function to run the vending machine
def run_vending_machine():
    while True:
        display_menu(Menu_Inventory)  # Pass the inventory to display the menu
        code = get_item_code()
        category, item, details = check_valid_code(code)
        if not category:
            print("Invalid code. Try again.")
            continue
        if details["stock"] == 0:
            print(f"Sorry, {item} is out of stock. Please choose another item.")
            continue
        if pay(details["price"]):
            reduce_stock(category, item)
            print(f"Enjoy your {item}!")
        if not ask_for_more():
            print("Thank you for using the vending machine. Goodbye!")
            break

# Running the program
run_vending_machine()


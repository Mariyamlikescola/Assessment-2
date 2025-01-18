#Creating a vending machine 
#Friendly greeting for vending machine
print("""

█▀▄▀█ ▄▀█ █▀█ █ █▄█ ▄▀█ █▀▄▀█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
█░▀░█ █▀█ █▀▄ █ ░█░ █▀█ █░▀░█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")
#Creating an Inventory made using nest dictionary
# Vending machine menu
Menu_Inventory = {
    "Snacks": {
        "Takis": {"code": "S01", "price": 1.5, "stock": 10},
        "Cookie": {"code": "S02", "price": 2.0, "stock": 5},
        "Snickers": {"code": "S03", "price": 3.0, "stock": 8},
        "KitKat":{"code": "S04", "price": 3.0, "stock": 7},
    },
    "Drinks": {
        "Water": {"code": "D01", "price": 1.0, "stock": 20},
        "Coca Cola": {"code": "D02", "price": 2.5, "stock": 15},
        "Mango juice": {"code": "D03", "price": 2.0, "stock": 12},
        "Seven up":{"code": "D04", "price": 2.5, "stock": 15},
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

# Calling the function to display the menu
display_menu(Menu_Inventory)

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
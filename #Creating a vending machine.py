#Creating a vending machine 
#Friendly greeting for vending machine
print("""

█▀▄▀█ ▄▀█ █▀█ █ █▄█ ▄▀█ █▀▄▀█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
█░▀░█ █▀█ █▀▄ █ ░█░ █▀█ █░▀░█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")
#Inventory made using nest dictionary
# Vending machine menu
Menu_Inventory = {
    "Snacks": {
        "Takis": {"code": "S01", "price": 1.5, "stock": 10},
        "Cookie": {"code": "S02", "price": 2.0, "stock": 5},
        "Snickers": {"code": "S03", "price": 1.75, "stock": 8},
    },
    "Drinks": {
        "Water": {"code": "D01", "price": 1.0, "stock": 20},
        "Coca Cola": {"code": "D02", "price": 1.25, "stock": 15},
        "Mango juice": {"code": "D03", "price": 1.5, "stock": 12},
    },
    "Healthy Options": {
        "Energy Bar": {"code": "H01", "price": 2.0, "stock": 7},
        "Pretzels": {"code": "H02", "price": 2.5, "stock": 5},
        "Fruit Cup": {"code": "H03", "price": 3.0, "stock": 6},
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
# Friendly greeting for vending machine
print("""
█▀▄▀█ ▄▀█ █▀█ █ █▄█ ▄▀█ █▀▄▀█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
█░▀░█ █▀█ █▀▄ █ ░█░ █▀█ █░▀░█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")

# Creating an Inventory made using nested dictionary
Menu_Inventory = {
    "Snacks": {
        "Takis": {"code": "S01", "price": 2.0, "stock": 10},
        "Cookie": {"code": "S02", "price": 2.0, "stock": 5},
        "Oreo": {"code": "S03", "price": 3.0, "stock": 8},
        "KitKat": {"code": "S04", "price": 3.0, "stock": 7},
        "Biscuit": {"code": "S05", "price": 3.0, "stock": 6},
        "Cheetos": {"code": "S06", "price": 3.0, "stock": 10},

    },
    "Drinks": {
        "Water": {"code": "D01", "price": 1.0, "stock": 20},
        "Coca Cola": {"code": "D02", "price": 2.5, "stock": 15},
        "Mango juice": {"code": "D03", "price": 2.0, "stock": 12},
        "Seven up": {"code": "D04", "price": 2.5, "stock": 15},
        "Cold coffee can": {"code": "D05", "price": 2.0, "stock": 6},
        "Milk": {"code": "D06", "price": 2.0, "stock": 8}
    },
    "Healthy Options": {
        "Energy Bar": {"code": "H01", "price": 2.0, "stock": 7},
        "Pretzels": {"code": "H02", "price": 2.5, "stock": 5},
        "Fruit Cup": {"code": "H03", "price": 3.0, "stock": 6},
        "Banana": {"code": "H04", "price": 2.0, "stock": 6},
        "Almonds": {"code": "H05", "price": 2.5, "stock": 8},
        "Fruit Bowl": {"code": "H06", "price": 3.0, "stock": 8},

    },
}
#Pairing the menu items with their complimentary items.
paring = { 
    "S01" : "D02" , "S02" : "D06","S03" : "D06" ,"S04" : "D06" ,"S05" : "D05" ,"S06" : "D02" ,
    "D01" : "H01" ,"D02" : "S06" ,"D03" : "H03" ,"D04" : "S01" ,"D05" : "H02" ,"D06" : "H02" ,"H01" : "D06" ,
    "H02" : "D06" ,"H03" : "D03" ,"H04" : "H06" ,"H05" : "D06" ,"H06" : "H04" ,
}

# Function for displaying the menu
def display_menu(menu):
    print("Welcome to the Vending Machine!")
    print("We have all you might need!\n")
   # Looping through each category
    for category in menu: 
        print(f"{category}:")
     # Looping through each item in the category
        for item in menu[category]:
            details = menu[category][item]
            print(f"  {details['code']} - {item} (AED{details['price']}, Stock: {details['stock']})")
       #leaving a break
        print()

# Function for getting the user input
def get_item_code():
    global user_code
    #using .upper to return a copy of the string in uppercase
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
   #deducts stock after each purchase
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
               #generating the remaining amount
                change = money - price
                if change > 0:
                    print(f"Here is your change: AED{change:.2f}")
                print("Payment successful!")
                return True 
        except ValueError:
            print("Invalid input. Enter a number.")

#Pairing the menu items with their complimentary items.
paring = { 
    "S01" : "D02" , "S02" : "D06","S03" : "D06" ,"S04" : "D06" ,"S05" : "D05" ,"S06" : "D02" ,
    "D01" : "H01" ,"D02" : "S06" ,"D03" : "H03" ,"D04" : "S01" ,"D05" : "H02" ,"D06" : "H02" ,"H01" : "D06" ,
    "H02" : "D06" ,"H03" : "D03" ,"H04" : "H06" ,"H05" : "D06" ,"H06" : "H04" ,
}

#function for generating a suggested pairing with each item based on the previous code
def ask_for_more(user_code):
    if user_code in paring:
        paired_code = paring[user_code]
        for category, items in Menu_Inventory.items():
            for item, details in items.items():
                if details["code"] == paired_code:
                    print(f"Would you like to add {item} for AED{details['price']}? It will make an amazing combo!")
                    break
    answer = input("Do you want to purchase another item? (yes/no): ").strip().lower()
    return answer == "yes"
# Main function to bring all the functions together to run the vending machine
def run_vending_machine():
    while True:
      # Pass the inventory to display the menu
        display_menu(Menu_Inventory)
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
        if not ask_for_more(code):
            print("Thank you for using the vending machine. Goodbye!")
            break

# Running the program
run_vending_machine()


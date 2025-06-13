# ============================================================
#                WELCOME TO THE COFFEE MACHINE!
# ============================================================
"""COINS OPERATED
PENNY   = 1 CENT   = $0.01
NICKEL  = 5 CENTS  = $0.05
DIME    = 10 CENTS = $0.10
QUARTER = 25 CENTS = $0.25
--------------------------------------------------------------
TYPE 'REPORT' TO CHECK HOW MUCH RESOURCES ARE LEFT
--------------------------------------------------------------
"""

# ===================== MENU & RESOURCES =====================
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profits = 0

# ===================== FUNCTIONS ============================
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"☒ SORRY THERE IS NOT ENOUGH {item.upper()}")
            return False
    return True

def process_coins():
    print("\n💰 PLEASE INSERT THE COINS 💰")
    total = 0
    total += int(input("HOW MANY 'QUARTERS'? : ")) * 0.25
    total += int(input("HOW MANY 'DIMES'?    : ")) * 0.10
    total += int(input("HOW MANY 'NICKELS'?  : ")) * 0.05
    total += int(input("HOW MANY 'PENNIES'?  : ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    global profits
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"✅ HERE IS THE CHANGE: ${change}")
        profits += drink_cost
        return True
    else:
        print("☒ SORRY THAT'S NOT ENOUGH MONEY, MONEY REFUNDED")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕ HERE IS YOUR DRINK: {drink_name.upper()}! ENJOY! ☕\n")

# ===================== MAIN LOOP ============================
is_on = True
while is_on:
    print("-----------------------------------------------------------")
    choice = input("WHAT WOULD YOU LIKE TO HAVE (ESPRESSO / LATTE / CAPPUCCINO)? : ").lower()
    print("-----------------------------------------------------------")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"\n📋 RESOURCE REPORT 📋")
        print(f"Water  : {resources['water']}ml")
        print(f"Milk   : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money  : ${profits}\n")
    else:
        drink = MENU.get(choice)
        if drink and is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
# ============================================================

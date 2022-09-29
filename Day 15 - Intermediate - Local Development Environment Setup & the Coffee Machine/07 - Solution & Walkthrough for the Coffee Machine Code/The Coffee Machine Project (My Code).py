from data import MENU, resources


# Creating a list for report
water_amount = resources["water"]
milk_amount = resources["milk"]
coffee_amount = resources["coffee"]
money = 0
coffee_off = False


# Function for coin transaction
def coins(command):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * .25
    dimes = int(input("how many dimes?: ")) * .10
    nickles = int(input("how many nickles?: ")) * .05
    pennies = int(input("how many pennies?: ")) * .01
    total = quarters + dimes + nickles + pennies
    return round(total - MENU[command]["cost"], 2)



while coffee_off == False:

    command = input("What would you like? (espresso/latte/cappuccino): ").lower()

    report_list = [
        f"Water: {water_amount}ml",
        f"Milk: {milk_amount}ml",
        f"Coffee: {coffee_amount}g",
        f"Money: ${money}"
    ]

    if command == "espresso" or command == "latte" or command == "cappuccino":

        print(f"Here is ${coins(command)} in change.")

        water_amount -= MENU[command]["ingredients"]["water"]
        if command != "espresso":
            milk_amount -= MENU[command]["ingredients"]["milk"]
        coffee_amount -= MENU[command]["ingredients"]["coffee"]
        money += MENU[command]["cost"]

    elif command == "report":
        for n in report_list:
            print(n)
    elif command == "off":
        exit()
    else:
        print("Please pick a valid keyword.")
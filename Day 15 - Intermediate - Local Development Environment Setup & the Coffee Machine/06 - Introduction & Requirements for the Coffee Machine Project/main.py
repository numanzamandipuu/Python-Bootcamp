from data import MENU, resources

# print(MENU[command]["cost"])
# print(MENU["espresso"]["ingredients"]["coffee"])

# Function for coin transaction
def coins(command):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * .25
    dimes = int(input("how many dimes?: ")) * .10
    nickles = int(input("how many nickles?: ")) * .05
    pennies = int(input("how many pennies?: ")) * .01
    total = quarters + dimes + nickles + pennies
    return round(total - MENU[command]["cost"], 2)


command = input("What would you like? (espresso/latte/cappuccino): ").lower()


if command == "espresso" or command == "latte" or command == "cappuccino":
    print(f"Here is ${coins(command)} in change.")
elif command == "report":
    print(resources)
elif command == "off":
    exit()
else:
    print("Please pick a valid keyword.")


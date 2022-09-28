from data import MENU, resources

# print(MENU["espresso"]["ingredients"]["coffee"])

command = input("What would you like? (espresso/latte/cappuccino): ").lower()


if command == "espresso" or command == "latte" or command == "cappuccino":
    print("Please insert coins.")
elif command == "report":
    print(resources)
elif command == "off":
    exit()
else:
    print("Please pick a valid keyword.")


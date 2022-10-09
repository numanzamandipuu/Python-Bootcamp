from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
items = menu.get_items()

while is_on == True:
    choice = input(f"What would you like? ({items}): ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print("")
        is_on = False
    else:
        print("Please pick a valid keyword.")
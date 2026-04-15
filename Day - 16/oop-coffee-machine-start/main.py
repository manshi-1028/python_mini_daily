from os import name
from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
COFFEE_MAKER = CoffeeMaker()
MONEY_MAKER = MoneyMachine()
MENU_MAKER = Menu()
on=True
while on:
    print(MENU_MAKER.get_items())
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        print(COFFEE_MAKER.report())
        print(MONEY_MAKER.report())
    else:
        drink=MENU_MAKER.find_drink(choice)
        if COFFEE_MAKER.is_resource_sufficient(drink) and MONEY_MAKER.make_payment(drink.cost):
            COFFEE_MAKER.make_coffee(drink)






from data import MENU, resources

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

def coin_payment():
    total = float(int(input("How many quarters? ")) * quarter)
    total += float(int(input("How many dimes? ")) * dime)
    total += float(int(input("How many nickles? ")) * nickel)
    total += float(int(input("How many pennies? ")) * penny)
    return total

def show_report(ingredients):
    print("Ingredients:")
    for ingredient in ingredients:
        print(f"{ingredient}: {ingredients[ingredient]}")

def resources_sufficient(drink):

    water_for_drink = MENU[drink]["ingredients"]["water"]
    milk_for_drink = MENU[drink]["ingredients"]["milk"]
    coffee_for_drink = MENU[drink]["ingredients"]["coffee"]

    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]

    missing_ingredients = []

    if water_available < water_for_drink:
        missing_ingredients.append("water")
    if milk_available < milk_for_drink:
        missing_ingredients.append("milk")
    if coffee_available < coffee_for_drink:
        missing_ingredients.append("coffee")

    return missing_ingredients


def main():
    user = True
    while user:
        drink = input("What drink would you like? (espresso/latte/cappuccino): ").lower()
        if drink == "off" or drink == "Off":
            print("Coffee Machine is turning off.")
            user = False
        else:
            if drink in MENU:
                report = input("Would you like to see your drink's ingredient report? (Y/N) ")
                if report == "off" or report == "Off":
                    print("Coffee Machine is turning off.")
                    user = False
                else:
                    if report == "y" or report == "Y":
                        ingredients = MENU[drink]["ingredients"]
                        show_report(ingredients)
                    price = MENU[drink]["cost"]
                    # coffee_price = "{:.2f}".format(price)
                    print(f"Cost: ${float(price):.2f}")
                    total_paid = 0.0
                    while total_paid < float(price):
                        print("Insert your coins.")
                        total_paid += coin_payment()
                        if total_paid > float(price):
                            change = float(total_paid - float(price))
                            print(f"Here is ${change:.2f} in change.")
                        else:
                            print(f"Sorry, that's not enough money. Please enter ${price - total_paid:.2f}.")
                    print(f"Here is your {drink} ☕. Enjoy!")
                    resources["water"] -= MENU[drink]["ingredients"]["water"]
                    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                    user = True
            else:
                print("Sorry, we don't serve that drink.")
main()
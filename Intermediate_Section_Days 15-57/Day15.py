'''
Day 15 Topics:

Project - Virtual Coffee Machine
'''


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
    "money": 0
}

#methods

def prompt():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    return order

def turnOff(order):
    if order == "off":
        powered = False

def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"])+ "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))
def resourceCheck(order):
    if order == "espresso":
        if (resources["water"] >= 50):
            if(resources["coffee"] >= 18):
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False
    elif order == "latte":
        if (resources["water"] >= 200):
            if resources["coffee"] >= 24:
                if resources["milk"] >= 100:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False
    elif order == "cappuccino":
        if (resources["water"] >= 250):
            if resources["coffee"] >= 24:
                if resources["milk"] >= 150:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False


def processCoins():
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    coins = [0, 0, 0, 0]
    total = 0.0

    print("Please insert coins.")
    coins[0] = int(input("How many quarters?: "))
    coins[1] = int(input("How many dimes?: "))
    coins[2] = int(input("How many nickels?: "))
    coins[3] = int(input("How many pennies?: "))
    total = coins[0] * quarter + coins[1] * dime + coins[2] * nickel + coins[3] * penny
    return total

def checkTransaction(coins, order):
    change = 0.0
    price = 0
    if order == "espresso":
        price = 1.50
    elif order == "latte":
        price = 2.50
    else:
        price = 3.00
    if coins >= price:
        change = coins - price
        print("Here is your $" + str(format(change, ".2f")) + " in change.")
        print("Here is your " + order + ". Enjoy!")
        resources["money"] = resources["money"] + price
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False

def makeCoffee(order):
    if order == "espresso":
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
    elif order == "latte":
        resources["water"] = resources["water"] - 200
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 150
    else:
        resources["water"] = resources["water"] - 250
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 100

#coffee machine
powered = True
while powered:
    order = prompt()
    if order == "off":
        powered = False
    elif order == "report":
        report()
    else:
        if(resourceCheck(order)):
            if(checkTransaction(processCoins(), order)):
                makeCoffee(order)

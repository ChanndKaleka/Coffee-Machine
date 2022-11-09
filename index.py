
Menu = {
    "espresso": {
        "ingredients": 
            {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": 
        {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": 
        {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

stock={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}

profit=0
def checkSufficiency(ingredients):
    isEnough=True
    for item in ingredients:
        if ingredients[item]>stock[item]:
            print(f"Sorry there is not enough {item}")
            isEnough= False   
    return True

def processCoins():
    print("Please insert coins ")
    total=int(input("How many quarters? "))*0.25
    total+=int(input("How many dimes? "))*0.1
    total+=int(input("How many nickles? "))*0.05
    total+=int(input("How many pennies? "))*0.05
    return total

def checkTransaction(recieved, cost):
    if recieved>=cost:
        change=round(recieved-cost,2)
        print(f"Your change is {change} $")
        global profit
        profit += cost
        return True
    else:
        print(f"Sorry, that is not enough money!\n It costs {cost} $")
        return False
    
def makeCoffee(drink, recipe):
    for item in recipe:
        stock[item]-=recipe[item]
    print(f"Here is your {drink}")
        
while True:
    userChoice=input("What would you like to order, espresso, latte or a cappuccino? ")
    if userChoice=="off":
        print("You have turned off the machine!")
        break
    elif(userChoice=="report"):
        print(f"Water: {stock['water']}")
        print(f"Milk: {stock['milk']}")
        print(f"Coffee: {stock['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = Menu[userChoice]
        if checkSufficiency(drink["ingredients"]):
            payment= processCoins()
            if checkTransaction(payment, drink["cost"]):
                makeCoffee(userChoice,drink["ingredients"])
from D5_coffee_data import MENU, resources

#python programming for implementing a simple coffee machine

profit = 0 #initial value in machine set to 0
is_on = True   

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):

# TODO 2:Turn off the Coffee Machine by entering “off” to the prompt.

# TODO 3:Print report.
# def report():

# TODO 4:Check resources sufficient?
def is_reource_sufficient(order_ing):
    """
    Take order ingredients from user chosen option of coffee
    Return the compared with resources
    """
    for item in order_ing:
        if order_ing[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.\n")
            return False
    return True



# TODO 5:Process coins
def process_coin():
    #returns the total calculated from the inserted coins
    print("Please insert coins.\n")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# TODO 6:Check transaction successfull
def is_transation_succesful(mr,cost):
    """Returns True when payment is accepted"""
    if mr > cost:
        change = round(mr - cost,2)
        print(f"\nHere is ${change} $ in change.\n")
        global profit
        profit += cost
        return True
    else:
        print("Sorry there is not enough money. Money reunded")


# TODO 7: Make Coffee.
def make_coffee(drink_name, order_ingredients):
    """deduct the required engridients from the list of resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.\n")

if __name__ == "__main__":

 
    while is_on:
        #looping until the user input offs 
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "off":
            is_on = False
        elif user_input == "report":
            for k, v in resources.items():
                print(k, v)
            print(f"Money: ${profit}")
        else: 
           drink = MENU[user_input] 
           if is_reource_sufficient(drink["ingredients"]): #getting hold of the values under the key ingredients under specific coffee option
               payment = process_coin()
               if is_transation_succesful(payment, drink["cost"]):
                   make_coffee(user_input,drink["ingredients"])



    # main()
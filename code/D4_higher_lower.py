#importing art and data module
from D4_higher_lower_art import logo, vs
from D4_higher_lower_data import data 
import random
from replit import clear

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, {account_country}"



#display the art
print(logo)
score = 0
game_cont = True
account_b = random.choice(data)

while game_cont:


#generate a random account from data 
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? type 'A' or 'B': ").lower()

    def check_answer(guess, a_follower, b_follower):
        """
        Takes followers of a and b.
        Compares them
        returns if the user guess is right or not"""
        if a_follower > b_follower:
            return guess == "a"
        else:
            return guess == "b"

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # is_correct = check_answer(guess, a_follower_count, b_follower_count)




    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You are right! current score:{score}.")
    else:
        game_cont = False
        print(f"Sorry, that is wrong. Final score. {score}")
    
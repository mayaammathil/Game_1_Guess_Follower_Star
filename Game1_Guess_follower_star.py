###### Main game Python file  ####

from art import logo, vs, play, won
import random
# generate and display random account
from game_data import data

def account_details(account):
    """PRINTS ACCOUNT DETAILS """
    account_name = account["name"]
    return f"{account_name}, with ------------------------ followers"

def  compare_accounts(account_1, account_2):
    """Compare accounts to find the winner"""
    account_1_follower_count = account_1["follower_count"]
    account_2_follower_count = account_2["follower_count"]
    if  account_1_follower_count > account_2_follower_count:
            return "account_1"
    elif account_2_follower_count > account_1_follower_count:
            return "account_2"
    elif account_2_follower_count ==account_1_follower_count:
            return "tie"

def play_game():
    """Main code to play game"""
    print(play)
    print(logo)
    score = 0
    account_1 = random.choice(data)
    while True:

        account_2 = random.choice(data)
        while account_1 == account_2:
            account_2 = random.choice(data)

        print(f"account1: {account_details(account_1)}")
        print(vs)

        print(f"account2: {account_details(account_2)}")
        # format into printable format
        winner = compare_accounts(account_1, account_2)
        # ask for a guess
        guess = str(input(f"Who has more followers? Type: account_1 or account_2 :  ")).lower()
        while guess != "account_1" and guess != "account_2":
            print("Invalid input. Please enter only account_1 or account_2 ")
            guess = str(input(f"Who has more followers? Type: account_1 or account_2 :  ")).lower()
        if guess == winner:
            score += 1
            print(f"You won!{won}")
        else:
            print("You lost!")

        print(f"Current score: {score}")
        print(f"Account 1 followers: {account_1['follower_count']}")
        print(f"Account 2 followers: {account_2['follower_count']}")
        restart = input("Do you want to play again? If yes, type Y, or type N for No:   ").lower()
        while restart != "y" and restart != "n":
            print("Invalid input. Please enter only Y or N.")
            restart = input("Do you want to play again? Type Y for Yes or N for No: ").lower()

        if restart == "y":
            account_1 = account_2
            continue

        elif restart == "n":
            print(f"Final Score: {score}")
            break
play_game()




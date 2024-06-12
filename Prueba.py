import random

# Global choice options.
options = ("rock", "paper", "scissors")

def computer_choice():
    """Gets a random option for the computer to use."""
    return random.choice(options)

def user_choice():
    """Gets the option the player will use."""
    while True:
        user = input("Select what you want to play this round: Rock, paper, scissors.\n").lower()
        if user in options:
            return user
        else:
            print("Your choice is not valid. Check for typos and try again.")

def run_game():
    """Starts and handles the game from start to finish."""
    rounds = 3
    user_win = 0
    computer_win = 0

    print("*" * 15)
    print("The game will start now.")
    print("*" * 15)

    while rounds > 0:
        computer = computer_choice()
        user = user_choice()
        print(f"{user} vs {computer}, ")

        if user == computer:
            print(f"""
            Tie!
            You have both picked {user}
            {rounds} remaining.
            """)
        elif (user == "scissors" and computer == "paper") or (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock"):
            user_win += 1
            print(f"""
            You have won this round!
            {user} beats {computer}!
            {rounds} remaining.
            """)
        else:
            computer_win += 1
            print(f"""
            You have lost this round.
            {computer} beats {user}!
            {rounds} remaining.
            """)
        rounds -= 1

    if user_win == computer_win:
        print("It's a tie, you ended the game with the same amount of points.")
    elif computer_win > user_win:
        print(f"Match ended. The winner is the computer with {computer_win} points.")
    else:
        print(f"Match ended. You are the winner with {user_win} points!")

if __name__ == "__main__":
    run_game()

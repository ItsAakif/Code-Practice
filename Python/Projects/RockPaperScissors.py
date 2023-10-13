import random
import time

# Function to get the user's choice with input validation
def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\nIt's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "\nYou win!"
    else:
        return "\nComputer wins!"

# Main game loop
def play_game():
    while True:
        print("Let's play Rock, Paper, Scissors!")
        print("****************************************")
        
        # Introduce delays for a more user-friendly experience
        time.sleep(1)

        # Get user and computer choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Display choices and determine the winner
        print(f"\nYou chose {user_choice}.")
        time.sleep(1)
        print(f"Computer chose {computer_choice}.")
        time.sleep(1)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        time.sleep(1)
        
        # Ask the user if they want to play again
        while True:
            play_again = input("\nPlay again? (y/n): ").strip().lower()
            if play_again == 'n':
                return  # Exit the game loop
            elif play_again == 'y':
                break  # Continue to the next game
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == '__main__':
    play_game()

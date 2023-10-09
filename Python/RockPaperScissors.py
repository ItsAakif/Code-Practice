import random

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    flag = 1
    while flag:
        print("Let's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again == 'n':
            flag = 0

if __name__ == '__main__':
    play_game()

import time

# Function to display text with a typewriter effect
def slow_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n")

# Function to handle a player's choice
def make_choice(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice. Please select a valid option.\n")

# Main game loop
def main():
    print("Welcome to the Adventure Game!")
    time.sleep(1)

    # Introduction
    slow_text("You find yourself in a mysterious forest.")
    slow_text("You have two paths in front of you.")

    # First choice
    choice_1 = make_choice("Which path will you take?", ["Follow the left path", "Follow the right path"])

    if choice_1 == 1:
        slow_text("You follow the left path and discover a hidden treasure!")
    else:
        slow_text("You follow the right path and encounter a friendly traveler.")

    # Second choice
    choice_2 = make_choice("What will you do?", ["Take the treasure", "Chat with the traveler"])

    if choice_2 == 1:
        slow_text("You take the treasure and become rich!")
    else:
        slow_text("You have a pleasant conversation with the traveler and gain a new friend.")

    slow_text("Congratulations! You have completed the adventure.")

if __name__ == "__main__":
    main()
# <Game> by Moutasim Qazi
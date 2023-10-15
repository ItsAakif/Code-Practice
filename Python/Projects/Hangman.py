import random
import time

categories = {
    "Animals": ["elephant", "giraffe", "kangaroo", "octopus", "rhinoceros"],
    "Fruits": ["banana", "pineapple", "strawberry", "watermelon", "blueberry"],
    "Countries": ["australia", "canada", "france", "japan", "russia"]
}

def get_random_word(category):
    return random.choice(categories[category])

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    category = input("Choose a category (Animals, Fruits, Countries): ").capitalize()
    word = get_random_word(category)
    guessed_letters = []
    attempts = 6
    score = 0

    print(f"Category: {category}")
    print("\nWelcome to Hangman!")

    while True:
        displayed_word = display_word(word, guessed_letters)
        time.sleep(0.1)  # Pause for 0.1 seconds
        print(displayed_word)
        print(f"Attempts left: {attempts}")

        if displayed_word == word:
            score += 1
            time.sleep(1)  # Pause for 1 second
            print(f"Congratulations! You guessed the word '{word}'")
            time.sleep(1)  # Pause for 1 second
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break
            else:
                word = get_random_word(category)
                guessed_letters = []
                attempts = 6
                print(f"Category: {category}")
                print("New round!")
                time.sleep(1)  # Pause for 1 second

        if attempts == 0:
            time.sleep(1) # Pause for 1 second
            print(f"Game over! The word was '{word}'")
            time.sleep(1)  # Pause for 1 second
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break
            else:
                word = get_random_word(category)
                guessed_letters = []
                attempts = 6
                print(f"Category: {category}")
                print("New round!")
                time.sleep(1)  # Pause for 1 second

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1
        time.sleep(0.5)  # Pause for 0.5 seconds

if __name__ == "__main__":
    hangman()

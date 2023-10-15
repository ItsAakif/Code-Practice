import random

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
    print("Welcome to Hangman!")

    while True:
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)
        print(f"Attempts left: {attempts}")

        if displayed_word == word:
            score += 1
            print(f"Congratulations! You guessed the word '{word}'")
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break
            else:
                word = get_random_word(category)
                guessed_letters = []
                attempts = 6
                print(f"Category: {category}")
                print("New round!")

        if attempts == 0:
            print(f"Game over! The word was '{word}'. Your score: {score}")
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break
            else:
                word = get_random_word(category)
                guessed_letters = []
                attempts = 6
                print(f"Category: {category}")
                print("New round!")

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

if __name__ == "__main__":
    hangman()

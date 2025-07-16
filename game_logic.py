import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # Maximum allowed mistakes before game over

    print("Welcome to Snowman Meltdown!")
    print(f"The word has {len(secret_word)} letters. You can make {max_mistakes} mistakes before the snowman melts!")
    
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You saved the snowman! The word was: {secret_word}")
            return True
            
        # Check lose condition
        if mistakes >= max_mistakes:
            print(f"\nOh no! The snowman melted! The word was: {secret_word}")
            return False
            
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Guess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
        elif guess in secret_word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            mistakes += 1
            print(f"Wrong guess! You have {max_mistakes - mistakes} mistakes left.")

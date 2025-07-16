import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current game state with the snowman and word progress."""
    # Clear screen for better visibility (works in most terminals)
    print("\033[H\033[J", end="")
    
    # Game header
    print("=" * 50)
    print("SNOWMAN MELTDOWN".center(50))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}".center(50))
    print("=" * 50)
    
    # Display the snowman
    print("\n" + STAGES[mistakes])
    
    # Display the word with spaces between letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "_ "
    
    print("\n" + " " * 15 + display_word + "\n")
    print("-" * 50)


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # Maximum allowed mistakes before game over

    print("\n" + "=" * 50)
    print("WELCOME TO SNOWMAN MELTDOWN".center(50))
    print("=" * 50)
    print(f"\nThe word has {len(secret_word)} letters.")
    print(f"You can make {max_mistakes} mistakes before the snowman melts!\n")
    print("-" * 50 + "\n")
    
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Check lose condition
        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"\n☃️  OH NO! The snowman melted! ☃️")
            print(f"The word was: {secret_word.upper()}")
            return False
            
        # Display guessed letters in alphabetical order
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        else:
            print("No letters guessed yet.")
            
        # Get and validate user input
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("\n❌ Please enter a single letter (a-z).")
            input("Press Enter to continue...")
            continue
            
        if guess in guessed_letters:
            print(f"\n❌ You've already guessed '{guess}'. Try a different letter!")
            input("Press Enter to continue...")
            continue
            
        guessed_letters.append(guess)
            
        if guess in secret_word:
            print("\n✅ Good guess!")
            # Check if all letters are guessed
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f"\n🎉 CONGRATULATIONS! You saved the snowman! The word was: {secret_word.upper()}")
                return True
        else:
            mistakes += 1
            remaining = max_mistakes - mistakes
            print(f"\n❌ Wrong guess! {remaining} mistake{'s' if remaining != 1 else ''} left.")
            if remaining > 0:
                input("Press Enter to continue...")
                
        # Only clear the screen if the game is continuing
        if mistakes < max_mistakes and not all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)

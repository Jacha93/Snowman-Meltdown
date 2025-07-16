from game_logic import play_game

def main():
    print("\n" + "=" * 50)
    print("WELCOME TO SNOWMAN MELTDOWN".center(50))
    print("=" * 50)
    
    while True:
        play_game()
        
        # Ask if player wants to play again
        while True:
            play_again = input("\nDid you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'n', 'yes', 'no']:
                break
            print("Please enter 'y' for Yes or 'n' for No.")
            
        if play_again in ['n', 'no']:
            print("\nThank you for playing! Goodbye! 👋")
            break
        
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()
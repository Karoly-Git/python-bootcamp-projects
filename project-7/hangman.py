import random
import art

while True:
    print(art.hangman_logo)

    word_list = ["puzzle", "shadow", "planet", "bridge", "silent", "garden", "rocket", "tiger", "mirror", "castle"]

    random_word = random.choice(word_list)

    displayed_word = "_ " * len(random_word)  # Display underscores for each letter in the word
    print(f"Word to guess: {displayed_word}")

    num_of_lifes = 6
    guessed_letters = []

    while num_of_lifes > 0:
        user_guess = input("\nGuess a letter: ").lower()

        if user_guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please guess a valid letter.")
            continue

        guessed_letters.append(user_guess)

        if user_guess in random_word:
            print(f"\nGood guess! The letter '{user_guess}' is in the word. You have {num_of_lifes} lifes remaining.")

            # Update the displayed word
            displayed_word_list = list(displayed_word.strip())
            for i, char in enumerate(random_word):
                if char == user_guess:
                    displayed_word_list[2 * i] = user_guess  # Update only the letter positions

            displayed_word = "".join(displayed_word_list)
            print(f"Word to guess: {displayed_word}")

            # Check if the word has been fully guessed
            if "_" not in displayed_word:
                print(f"\nCongratulations, you guessed the word {random_word.strip().upper()}!\n")
                break
        else:
            num_of_lifes -= 1
            print(art.lifes[num_of_lifes])
            print(f"Incorrect guess. You have {num_of_lifes} lifes remaining.")
            print(f"Word to guess: {displayed_word}")

        if num_of_lifes == 0:
            print(f"\nSorry, you've run out of lifes. The word was {random_word.strip().upper()}!\n")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye!")
        break  # Exit the game loop

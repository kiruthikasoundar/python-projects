import random

# List of words for the game
word_list = ["python", "programming", "language", "computer", "science"]

# Randomly select a word from the list
word = random.choice(word_list)

# Initialize variables for the game
hidden_word = ["_"] * len(word)
guessed_letters = []
incorrect_guesses = 0

while "_" in hidden_word and incorrect_guesses < 6:
    # Print the current state of the word
    print(" ".join(hidden_word))

    # Get the user's guess
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
    # Check if the letter is in the word
    elif guess in word:
        # Replace the underscores with the correctly guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        # Increase the number of incorrect guesses
        incorrect_guesses += 1
        print("Incorrect. You have", 6 - incorrect_guesses, "guesses left.")

    # Add the letter to the list of guessed letters
    guessed_letters.append(guess)

# Check if the player won or lost
if "_" not in hidden_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you lost. The word was", word + ".")

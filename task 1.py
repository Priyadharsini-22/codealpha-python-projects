import random
 
def play_hangman():
    # Predefined list of 5 words
    words = ["python", "hangman", "internship", "computer", "keyboard"]
    word = random.choice(words)
 
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
 
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
 
    while wrong_guesses < max_wrong_guesses:
        # Display current progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord: " + display_word)
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
 
        # Check win condition
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word: " + word)
            break
 
        guess = input("Guess a letter: ").lower()
 
        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
 
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
 
        guessed_letters.append(guess)
 
        if guess in word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
 
    if wrong_guesses == max_wrong_guesses:
        print("\nGame Over! You've used all your guesses.")
        print("The word was: " + word)
 
 
if __name__ == "__main__":
    play_hangman()
 
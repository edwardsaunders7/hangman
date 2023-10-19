def check_guess(guess):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word!")
    else:
        print(f"Sorry! '{guess}' is not in the word! Try again")

def ask_for_input():
    while True:
        guess = input("Please provide a letter guess: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)  # Call the check_guess function to check if the guess is in the word
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Secret word
secret_word = "apple"

# Call the ask_for_input function to test your code
ask_for_input()

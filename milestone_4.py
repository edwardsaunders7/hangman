import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _pick_random_word(self):
        return random.choice(self.word_list)

    def _update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

    def _display_word(self):
        return " ".join(self.word_guessed)

    def _is_game_over(self):
        return self.num_lives == 0 or self.num_letters == 0

    def play(self):
        print("Welcome to Hangman!")
        while not self._is_game_over():
            self._display_game_state()
            guess = self._ask_for_input()
            self._check_guess(guess)

        if self.num_letters == 0:
            print(f"Congratulations! You've guessed the word: {self.word}")
        else:
            print(f"Game Over! You've run out of lives. The word was: {self.word}")

    def _display_game_state(self):
        print(f"Word: {self._display_word()}")
        print(f"Remaining Lives: {self.num_lives}")

    def _ask_for_input(self):
        while True:
            guess = input("Please provide a letter guess: ").lower()
            if self._is_valid_guess(guess):
                return guess

    def _is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()

    def _check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

# Example usage:
word_list = ["apple", "banana", "cherry", "date"]
hangman_game = Hangman(word_list)
hangman_game.play()

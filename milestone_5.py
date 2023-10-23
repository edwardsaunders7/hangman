import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self._pick_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _pick_random_word(self):
        self.word = random.choice(self.word_list)

    def play(self):
        print("Welcome to Hangman!")
        while self.num_lives > 0 and '_' in self.word_guessed:
            self._display_game_state()
            guess = self._ask_for_input()
            if guess in self.list_of_guesses:
                print(f"You already tried that letter: {guess}")
            else:
                self.list_of_guesses.append(guess)
                self._check_guess(guess)

        if '_' not in self.word_guessed:
            print(f"Congratulations. You won the game! The word was: {self.word}")
        else:
            print("You lost!")

    def _display_game_state(self):
        print(f"Word: {' '.join(self.word_guessed)}")
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

    def _update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

def main():
    word_list = ["apple", "banana", "cherry", "date"]
    game = Hangman(word_list)
    game.play()

if __name__ == "__main__":
    main()

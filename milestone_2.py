import random

word_list = ["Banana", "Apple", "Mango", "Raspberry", "Strawberry"]

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Please provide a letter guess")
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input")



import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.tries = 6

    def display_word(self):
        displayed = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                displayed += letter
            else:
                displayed += "_"
        return displayed

    def guess_letter(self, letter):
        letter = letter.lower()

        if letter in self.guessed_letters:
            print("You already guessed this letter.")
            return

        self.guessed_letters.append(letter)

        if letter in self.secret_word:
            print("Correct guess!", self.display_word())
        else:
            self.tries -= 1
            print("Wrong guess! Tries left:", self.tries)

    def is_won(self):
        return "_" not in self.display_word()

    def is_lost(self):
        return self.tries <= 0


# Game running through an object
words_list = ["python", "computer", "hangman", "programming", "machine", "learning"]
game = Hangman(words_list)

print("Welcome to Hangman!")

while True:
    print("Word:", game.display_word())

    if game.is_won():
        print("You won! The word was:", game.secret_word)
        break

    if game.is_lost():
        print("Game Over! The word was:", game.secret_word)
        break

    guess = input("Guess a letter: ")
    game.guess_letter(guess)

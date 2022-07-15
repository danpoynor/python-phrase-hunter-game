"""Phrase Hunter Guessing Game Class Module."""
import os
import sys
import random

# Using relative import (.) to load phrase module from current package.
# REF: https://docs.python.org/3/tutorial/modules.html#intra-package-references
from .phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.correct = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.active_phrase_words = self.active_phrase.phrase.split()
        self.active_phrase_letters = self.active_phrase.phrase.replace(" ", "")
        self.active_phrase_letters_set = set(self.active_phrase_letters)
        self.active_phrase_spaces = len(self.active_phrase.phrase) - len(self.active_phrase_letters)
        # NOTE: You can't create an empty set by just using empty curly braces.
        # That would be an empty dictionary. Use the set() constructor instead.
        self.guesses = set()
        self.user_guess = None

    @staticmethod
    def welcome():
        print("="*79)
        print("Welcome to Phrase Hunter!".center(79))
        print("Guess the phrase before you run out of turns.".center(79))
        print("5 misses and you loose the game. Good luck!".center(79))
        print("="*79)
        print()

    @staticmethod
    def create_phrases():
        # Create List of five Phrase Objects
        return [
            Phrase("Hello World"),
            Phrase("Shot In The Dark"),
            Phrase("May the force be with you"),
            Phrase("Make it work"),
            Phrase("Easy As Pie")
        ]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    @staticmethod
    def get_guess():
        return input("\nGuess a letter: ").lower()

    @staticmethod
    def is_valid_guess(self, guess):
        if len(guess) > 1:
            print("-"*79)
            print("Please enter a single letter character (a-z).")
            print("-"*79)
            return False
        elif not guess.isalpha():
            print("-"*79)
            print("\nPlease enter a letter (a-z).")
            print("-"*79)
            return False
        elif guess in self.guesses:
            print("-"*79)
            print("\nYou already guessed that letter. Try again.")
            print("-"*79)
            return False
        else:
            return True

    def check_guess_in_phrase(self):
        # Check if the user's guess is in the phrase and update counts.
        if self.active_phrase.check_guess(self.user_guess):
            print("+"*79)
            print(f":) YAY! Correct guess: '{self.user_guess}' :)".center(79))
            print("+"*79)
            self.correct += 1
        else:
            print("-"*79)
            print(f":( BUMMER! Incorrect guess: '{self.user_guess}' :(".center(79))
            print("-"*79)
            self.missed += 1

    def game_over(self):
        # Clear screen each time before showing game over message.
        os.system('cls' if os.name == 'nt' else 'clear')
        self.welcome()

        print("-"*79)
        print("G  A  M  E    O  V  E  R".center(79))
        print("-"*79)
        print()

        if self.active_phrase.check_complete(self.guesses):
            print("===============================================".center(79))
            print()
            print("You guessed the phrase. Congratulations!".center(79))
            print()
            print(f"Secret phrase was: {self.active_phrase.phrase}".center(79))
            print(f"You got it with {len(self.guesses)} guesses.".center(79))
            print()
            print("===============================================".center(79))
        else:
            print("===============================================".center(79))
            print()
            print("You didn't guess the phrase. Better luck next time!".center(79))
            print()
            print(f"Secret phrase was: {self.active_phrase.phrase}".center(79))
            print(f"You missed it with {len(self.guesses)} guesses.".center(79))
            print()
            print("===============================================".center(79))

        # Let user play multiple games.
        if input("\nWant to play again? (y/n) ").lower() == "y":
            self.__init__()
            self.start()
        else:
            # Clear screen before exiting.
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nBye :)")
            sys.exit("Program exited successfully.\n")

    def start(self):
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:
            # Clear screen each time the game starts and after each guess.
            os.system('cls' if os.name == 'nt' else 'clear')
            # Show the welcome header.
            self.welcome()

            # Display active phrase with guesses made so far.
            self.active_phrase.display(self.guesses)

            print(f"The phrase contains: {len(self.active_phrase_words)} words, {len(self.active_phrase_letters_set)} letters (a-z), and {self.active_phrase_spaces} spaces.".center(79))
            print()

            # If guesses have been made, print guesses separated by a comma
            # along with the scoreboard.
            if self.guesses:
                letters_remaining = len(self.active_phrase_letters_set - self.guesses)
                # Get Intersection between guesses and active_phrase_letters Sets.
                letters_correct = self.guesses & self.active_phrase_letters_set
                # Get Difference between guesses and active_phrase_letters Sets.
                letters_incorrect = self.guesses - letters_correct
                print(
                    "=========================== SCOREBOARD ===========================".center(79))
                print(
                    f"{self.correct} correct guesses so far: {', '.join(letters_correct)} - {letters_remaining} remaining.".center(79))
                print(
                    "------------------------------------------------------------".center(79))
                print(
                    f"{self.missed} missed guesses so far: {', '.join(letters_incorrect)} - {5 - self.missed} remaining.".center(79))
                print(
                    "==================================================================".center(79))
                print()

            # Get user's next guess.
            self.user_guess = self.get_guess()

            while not self.is_valid_guess(self, self.user_guess):
                print()
                self.user_guess = self.get_guess()
            else:
                # Add 'self.user_guess' value to the 'self.guesses' set().
                self.guesses.add(self.user_guess)
                self.check_guess_in_phrase()

        self.game_over()

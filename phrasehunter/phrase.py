"""Phrase Hunter Guessing Phrase Class Module."""


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_set = set(self.phrase.replace(" ", ""))

    def display(self, guesses):
        # Loop through the letters in the 'phrase' attribute. If the letter
        # was found in 'self.phrase', print the letter and then a space.
        # Otherwise, print an underscore "_" followed by a space.
        phrase_state = ""
        for letter in self.phrase:
            if letter == " ":
                phrase_state += " "
            elif letter in guesses:
                phrase_state += letter
            else:
                phrase_state += "_"
        print(f"The secret phrase is: {phrase_state}".center(79))
        print()

    def check_guess(self, guess):
        if guess in self.phrase_set:
            return True
        else:
            return False

    def check_complete(self, guesses):
        # Test if self.phrase_set is a subset of guesses.
        if self.phrase_set <= guesses:
            return True
        else:
            return False

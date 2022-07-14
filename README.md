# Python Phrase Hunter Game

Demo console-based game app uses Python and OOP (Object-Oriented Programming) approaches to select a phrase at random, hidden from the player. A player then tries to guess the phrase by inputting individual characters.

Features

- A random phrase is automatically chosen and each letter of the phrase is displayed as an underscore character placeholders, _.
- Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase.
- If the user enters more than one letter, or a non-letter character, the program will display an error message.
- If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.
- A player continues to select letters until they guess the phrase (and wins), or make five incorrect guesses (and loses).
- If the player completes the phrase before they run out of guesses, a winning screen appears.
- If the player guesses incorrectly five times, a losing screen appears.

</details>

---

## Run the app

After cloning the repository to your local hard-drive, `cd` into the 'python-phrase-hunter-game` directory and run the following command in the terminal:

```bash
python3 app.py
```

NOTE: Python 3.10 was used to develop and test this app.

---

## Screen Recording Showing Some Example Game States

<details open>
<summary>Expand/Collapse</summary>

https://user-images.githubusercontent.com/764270/178861802-64b3c9ff-9d68-4638-aa42-efa3b9f4590b.mp4

</details>

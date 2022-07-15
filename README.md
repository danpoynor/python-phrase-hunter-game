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

## Run Unit Tests

Some basic unit tests are included to test the `dm.py` module.

<details>
  <summary>Expand/Collapse</summary>
To run the tests, use something like:


```bash
python3 -m unittest -v tests.test_game
```

and you should see some test result output like this:

```bash
test_active_phrase_display (tests.test_game.GameTestCase) ... ok
test_check_guess_in_phrase (tests.test_game.GameTestCase) ... ok
test_game_over_loser (tests.test_game.GameTestCase) ... skipped "TODO: When there's more time"
test_game_over_winner (tests.test_game.GameTestCase) ... skipped "TODO: When there's more time"
test_get_random_phrase_returns_a_string (tests.test_game.GameTestCase) ... ok
test_is_valid_guess (tests.test_game.GameTestCase) ... ok
test_scoreboard_stats (tests.test_game.GameTestCase) ... skipped "TODO: When there's more time, test this"
test_should_include_at_least_5_phrases (tests.test_game.GameTestCase) ... ok
test_welcome_message (tests.test_game.GameTestCase) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK (skipped=3)
```

Note: If you run the command without the -v flag, such as:

```bash
python3 -m unittest tests.test_game
```

You should see test result output like this:

```bash
..ss..s..
----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK (skipped=3)
```

The `..ss..s..` indicates six tests ran and three were skipped.

</details>

---

## Screen Recording Showing Some Example Game States

<details open>
<summary>Expand/Collapse</summary>

https://user-images.githubusercontent.com/764270/178861802-64b3c9ff-9d68-4638-aa42-efa3b9f4590b.mp4

</details>

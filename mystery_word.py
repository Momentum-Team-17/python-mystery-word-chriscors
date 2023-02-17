import numpy as np


def select_word(word_list: list):
    import random
    return (random.choice(word_list))


def play_game(word: str):
    # Declare vars
    secret_word = list(word)
    current_guess = ["_"] * len(word)

    # Track state
    guesses_remaining = 8

    # First tell user how many letters:
    print(f'''
Welcome to Hangman!
You secret word has {len(word)} letters.

Current guess:
{" ".join(current_guess)}''')

    while guesses_remaining > 0:
        guess = input("Take a guess! ").upper()
        print()

        if guess in secret_word:
            array = np.array(secret_word)
            indexes = list(np.where(array == guess)[0])
            for index in indexes:
                current_guess[index] = guess
            if "_" not in current_guess:
                print(f"YES! The word was {word}")
                print()
                if input("You win! Play again? (y/n):") == y:
                    print()
                    play_game()
                else:
                    break
            elif guess in current_guess:
                print(f'You already guessed {guess}! Try again?')
                print(f'You have {guesses_remaining} guesses left.')
                print()
                print('Current guess:')
                print(" ".join(current_guess))
                print()
            else:
                print(f'Yes! {guess} was in the word {len(indexes)} time(s).')
                print(f'You have {guesses_remaining} guesses left.')
                print()
                print('Current guess:')
                print(" ".join(current_guess))
                print()
        else:
            guesses_remaining -= 1
            print(f'Sorry! {guess} was not in the word.')
            print(f'You have {guesses_remaining} guesses left.')
            print()
            print('Current guess:')
            print(" ".join(current_guess))
            print()
    # If loss
    print(f"Good try! The word was {word}.")
    if input("Play again? (y/n):") == y:
        print()
        play_game()
    else:
        pass


if __name__ == "__main__":
    from pathlib import Path
    file = Path("words.txt")
    with open(file) as opened_file:
        parsed_file = opened_file.read()

    parsed_file = parsed_file.split('\n')

    word = select_word(parsed_file)
    print(word)
    play_game(word.upper())

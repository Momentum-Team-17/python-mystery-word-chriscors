def select_word(word_list: list):
    import random
    return (random.choice(word_list))


def play_game(word: str):
    pass


if __name__ == "__main__":
    from pathlib import Path
    file = Path("test-word.txt")
    with open(file) as opened_file:
        parsed_file = opened_file.read()
    print(type(parsed_file))
    parsed_file = parsed_file.split('\n')

    word = select_word(parsed_file)
    print(word)
    play_game(word)

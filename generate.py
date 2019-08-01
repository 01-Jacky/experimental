import os
import random

# os.system('git add *')
# os.system('git commit -m "added a word"')

NUM_WORDS = 3
OUTPUT_FILE = "hello.txt"


def issue_commands():
    pass


def _read_words(filename: str) -> list:
    """Get words from a new line separated file"""
    words = []
    with open(filename) as file:
        count = 0
        for line in file.readlines():
            count += 1
            words.append(line)
    return words


def _get_random_word(words: list, num: int) -> str:
    """"Return a list of n random elements from specified list"""
    return [random.choice(words) for _ in range(num)]


def _write_word(filename: str, word: str):
    """Append a word to a file"""
    os.system(f'echo {word} > {filename}')


def main():
    words = _read_words('words')
    random_words = _get_random_word(words, NUM_WORDS)
    for word in random_words:
        _write_word(OUTPUT_FILE, word)

    os.system('echo ezz > hello.txt')

if __name__ == "__main__":
    main()
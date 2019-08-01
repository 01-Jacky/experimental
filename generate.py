import os
import random
import copy
# os.system('git add *')
# os.system('git commit -m "added a word"')

OUTPUT_FILE = 'fib.txt'
NUM_TO_GENERATE = 300;


def _fib():
    """ Generateor function """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fib_generator = _fib()

    with open(OUTPUT_FILE, "a") as output_file:
        for i in range(NUM_TO_GENERATE):
            next_fib = next(fib_generator)
            output_file.write(str(next_fib) + '\n')

            # Make commit as of x date





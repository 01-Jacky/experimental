import os
import random
import copy
import datetime

# os.system('git add *')
# os.system('git commit -m "added a word"')

OUTPUT_FILE = 'fib.txt'
NUM_TO_GENERATE = 300;

WEEKDAY_CHANCES = {
    0: 0.95,
    1: 0.95,
    2: 0.75,
    3: 0.85,
    4: 0.35,
    5: 0.51,
    6: 0.51,
}

BLACKOUT_DATES = {
    datetime.date(2018, 8, 21),
    datetime.date(2018, 8, 22),
    datetime.date(2018, 8, 23),
    datetime.date(2018, 8, 24),
    datetime.date(2018, 8, 25),
    datetime.date(2018, 12, 23),
    datetime.date(2018, 12, 24),
    datetime.date(2018, 12, 25),
    datetime.date(2018, 12, 26),
    datetime.date(2019, 3, 30),
    datetime.date(2019, 3, 31),
    datetime.date(2019, 4, 1),
    datetime.date(2019, 4, 2),
    datetime.date(2019, 4, 3),
    datetime.date(2019, 4, 4),
    datetime.date(2019, 4, 5),
    datetime.date(2019, 4, 6),
    datetime.date(2019, 4, 7),
    datetime.date(2019, 4, 8),
    datetime.date(2019, 7, 1),
    datetime.date(2019, 7, 2),
    datetime.date(2019, 7, 3),
    datetime.date(2019, 7, 4),
    datetime.date(2019, 7, 5),
}


def _fib():
    """Generator function for fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def _get_random_dates(num) -> list:
    """ Return a list of x random dates"""
    pass


def main():
    fib_generator = _fib()

    with open(OUTPUT_FILE, "a") as output_file:
        # Get list of dates to commit


        for i in range(NUM_TO_GENERATE):
            next_fib = next(fib_generator)
            output_file.write(str(next_fib) + '\n')

            # Make commit as of x date


if __name__ == "__main__":
    cur_date = datetime.date(2018, 8, 1)

    for i in range(345):
        cur_date += datetime.timedelta(days=1)

        if cur_date in BLACKOUT_DATES:
            print(str(cur_date))
            continue

        if random.random() < WEEKDAY_CHANCES[cur_date.weekday()]:
            print(str(cur_date) + ' 1')
        else:
            print(str(cur_date))

from functools import reduce


numberstrings = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
]


def parse_number(s, i):
    return s[i] \
        if s[i].isdigit() \
        else next((n[1] for n in numberstrings if s.startswith(n[0], i)), None)


def all_numbers_in(s):
    return (n for i in range(0, len(s)) if (n := parse_number(s, i)) is not None)


def first_and_last_number_in(s):
    return reduce(lambda r, n: (r[0] or n, n), all_numbers_in(s), (None, None))


def calibration_value(s: str) -> int:
    return int(''.join(first_and_last_number_in(s)))


if __name__ == '__main__':
    with open('input/day_01.txt') as file:
        print(f'The sum is: {sum(calibration_value(line) for line in file)}')

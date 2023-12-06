import functools
import math


def parse_numbers(line, prefix):
    return [int(n.strip()) for n in line.removeprefix(prefix + ':').strip().split(' ') if len(n)]


def compute_count(b, c):
    discriminant = math.sqrt(b ** 2 - 4 * c)
    return math.ceil((b+discriminant)/2) - math.floor((b - discriminant)/2) - 1


def count_ways(lines):
    pairs = list(zip(parse_numbers(next(lines), 'Time'), parse_numbers(next(lines), 'Distance')))
    return [compute_count(pair[0], pair[1]) for pair in pairs]


def product_of_ways(lines):
    return functools.reduce(lambda x, y: x*y, (w for w in count_ways(lines)), 1)


if __name__ == '__main__':
    with open('input/day_06.txt') as file:
        result = product_of_ways((line.strip('\n').replace(' ', '') for line in file))
        print(f'The result is: {result}')

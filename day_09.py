import itertools


def number_sequence(line):
    return [int(n) for n in line.split(' ')]


def next_values(lines):
    return [compute_new_values(number_sequence(line)) for line in lines]


def differences(row):
    return [b-a for a, b in itertools.pairwise(row)]


def compute_new_values(row):
    if not any(row):
        return (0, 0)
    else:
        d = compute_new_values(differences(row))
        return row[0] - d[0], row[len(row) - 1] + d[1]


def sum_of_next_value(lines):
    values = next_values(lines)
    return sum(begin for begin, end in values), sum(end for begin, end in values)


if __name__ == '__main__':
    with open('input/day_09.txt') as file:
        result = sum_of_next_value((line.strip('\n') for line in file))
        print(f'The result is: {result}')


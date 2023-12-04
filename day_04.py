import re
from dataclasses import dataclass
from typing import List


@dataclass
class Card:
    number: int
    winning_numbers: List[str]
    my_numbers: List[str]

    def count_matching_numbers(self):
        return len(set(self.winning_numbers) & set(self.my_numbers))


def points(line):
    return compute_points(parse_card(line).count_matching_numbers())


def parse_card(line):
    match = re.match(r'Card +(\d+):(.+)\|(.+)', line)
    return Card(int(match.group(1)),
                [n for n in match.group(2).strip().split(' ') if len(n)],
                [n for n in match.group(3).strip().split(' ') if len(n)]) if match else None


def compute_points(nb_matches):
    return 2 ** (nb_matches - 1) if nb_matches else 0


def sum_of_points(file):
    return sum(points(line) for line in file)


def add_copies(copies, card: Card):
    copies_of_card = copies.get(card.number, 0) + 1
    for i in range(1, card.count_matching_numbers()+1):
        copies[card.number+i] = copies.get(card.number+i, 0) + copies_of_card

    return copies_of_card


def sum_of_cards(file):
    copies = dict()
    return sum(add_copies(copies, parse_card(line)) for line in file)


if __name__ == '__main__':
    with open('input/day_04.txt') as file:
        print(f'The sum is: {sum_of_cards(file)}')

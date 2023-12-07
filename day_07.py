import functools
import itertools
from operator import attrgetter


def value_of(card: str):
    if card.isdigit():
        return int(card)
    match card:
        case 'T': return 10
        case 'J': return 1
        case 'Q': return 12
        case 'K': return 13
        case 'A': return 14


class Hand:
    def __init__(self, hand: str, bid: int):
        self.strength = (self.type_strength(hand) * 100 ** 5) + self.card_order_strength(hand)
        self.bid = bid

    def card_order_strength(self, hand):
        return functools.reduce(lambda x, y: x * 100 + value_of(y), hand, 0)

    def type_strength(self, hand):
        withouth_jokers = hand.replace('J', '')
        type = sorted([len(list(values)) for card, values in itertools.groupby(sorted(withouth_jokers))], reverse=True)
        joker_count = (5 - len(withouth_jokers))
        return functools.reduce(lambda x, y: x + type[y] * (10 ** (5 - y)),
                                (i for i in range(0, len(type))), 0) + joker_count * 10 ** 5


def to_hand(line):
    split = line.split(' ')
    return Hand(split[0], int(split[1]))


def total_winnings(lines):
    hands = sorted([to_hand(line) for line in lines if len(line)], key=attrgetter('strength'))
    return sum(hands[i].bid*(i+1) for i in range(0, len(hands)))


if __name__ == '__main__':
    with open('input/day_07.txt') as file:
        result = total_winnings((line.strip('\n') for line in file))
        print(f'The result is: {result}')

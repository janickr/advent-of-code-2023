from dataclasses import dataclass
from typing import List


@dataclass
class Cubes:
    red: int = 0
    green: int = 0
    blue: int = 0

    def fits(self, cubes: 'Cubes'):
        return self.red <= cubes.red and self.green <= cubes.green and self.blue <= cubes.blue

    def max(self, cubes: 'Cubes'):
        return Cubes(
            red=max(self.red, cubes.red),
            green=max(self.green, cubes.green),
            blue=max(self.blue, cubes.blue)
        )

    def power(self):
        return self.red * self.green * self.blue


@dataclass
class Game:
    id: int
    samples: List[Cubes]

    def fewest_possible(self):
        fewest = Cubes(0, 0, 0)
        for cubes in self.samples:
            fewest = fewest.max(cubes)

        return fewest

    def is_possible_with_bag(self, cubes: Cubes):
        return self.fewest_possible().fits(cubes)


def parse_cubes(sample: str) -> Cubes:
    colors = [color.strip(' ').split(' ') for color in sample.strip(' ').split(',')]
    return Cubes(**{color.strip(' '): int(amount.strip(' ')) for amount, color in colors})


def parse_game(s: str) -> Game:
    game, samples = s.strip('\n').split(':')
    game_id = int(game.removeprefix('Game '))
    samples = [parse_cubes(sample) for sample in samples.split(';')]
    return Game(game_id, samples)


if __name__ == '__main__':
    cubes = Cubes(red=12, green=13, blue=14)
    sum_ids = 0
    sum_power = 0
    with open('input/day_02.txt') as file:
        for line in file:
            game = parse_game(line)
            sum_power += game.fewest_possible().power()
            if game.is_possible_with_bag(cubes):
                sum_ids += game.id

        print(f'The sum is: {sum_ids}')
        print(f'The sum of the power is: {sum_power}')

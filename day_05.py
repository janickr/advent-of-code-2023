import itertools
from dataclasses import dataclass
from operator import attrgetter
from typing import List

@dataclass
class Range:
    start: int
    end: int

    def empty(self):
        return self.start is None or self.end is None or self.start > self.end

@dataclass
class Mapping:
    dst_start: int
    src: Range

    def compute(self, seed_number: int):
        return (seed_number + self.dst_start - self.src.start) if self.src.start <= seed_number <= self.src.end else None

    def compute_range(self, results, seed_range):
        results.append(Range(seed_range.start, min(self.src.start-1, seed_range.end)))
        results.append(Range(
            self.compute(max(self.src.start, seed_range.start)),
            self.compute(min(self.src.end, seed_range.end))))
        return Range(max(seed_range.start, self.src.end+1), seed_range.end)


@dataclass
class CategoryMap:
    name: str
    mappings: List[Mapping]

    def __post_init__(self):
        self.mappings.sort(key=attrgetter('src.start'))

    def compute(self, seed_number):
        return next((result for mapping in self.mappings if (result := mapping.compute(seed_number))), seed_number)

    def compute_range(self, seed_range) -> List[Range]:
        mapped = []
        for mapping in self.mappings:
            seed_range = mapping.compute_range(mapped, seed_range)
            if seed_range.empty():
                break

        mapped.append(seed_range)
        return [m for m in mapped if not m.empty()]


def get_map(lines):
    name = next(lines, None)
    while name:
        yield CategoryMap(
            name,
            [to_mapping(mapping) for mapping in itertools.takewhile(lambda l: len(l) > 0, lines)])
        name = next(lines, None)


def to_mapping(mapping):
    numbers = [int(n) for n in mapping.split()]
    return Mapping(numbers[0], Range(numbers[1], numbers[1]+numbers[2]-1))


def get_maps(lines):
    return [category_map for category_map in get_map(lines)]


def min_location_from_almanac_part1(lines):
    seeds = [int(n.strip()) for n in next(lines).removeprefix('seeds: ').split(' ')]
    next(lines)

    for category_map in get_maps(lines):
        seeds = [category_map.compute(s) for s in seeds]

    return min(*seeds)


def to_ranges(numbers) -> List[Range]:
    return [Range(numbers[i], numbers[i]+numbers[i+1]-1) for i in range(0, len(numbers), 2)]


def min_location_from_almanac_part2(lines):
    seeds = to_ranges([int(n.strip()) for n in next(lines).removeprefix('seeds: ').split(' ')])
    next(lines)

    for category_map in get_maps(lines):
        seeds = [m for m in itertools.chain(*(category_map.compute_range(s) for s in seeds))]

    return min(*(s.start for s in seeds))


if __name__ == '__main__':
    with open('input/day_05.txt') as file:
        min_location = min_location_from_almanac_part2((line.strip('\n') for line in file))
        print(f'The minimum is: {min_location}')

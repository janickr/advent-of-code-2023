import re
from dataclasses import dataclass
from typing import List, Iterable


def is_symbol(s: str):
    return not s.isalnum() and not s.isspace() and s.isprintable() and s != '.'


def is_gear(s: str):
    return s == '*'


@dataclass
class PartNumber:
    number: int
    start: int
    end: int

    def near(self, i: int):
        return self.start-2 < i < self.end+2


@dataclass
class Line:
    parts: List[PartNumber]
    symbols: List[int]
    gears: List[int]


@dataclass
class SlidingWindow:
    lines = [
        Line([], [], []),
        Line([], [], []),
        Line([], [], [])
    ]

    def push(self, line: Line):
        self.lines.insert(0, line)
        del self.lines[3]

    def get_part_numbers(self):
        return [p.number for p in self.lines[1].parts if self.near_symbol(p)]
    
    def get_gear_ratios(self):
        return [(r[0] * r[1]) for r in [self.get_ratios(g) for g in self.lines[1].gears] if len(r) == 2]

    def near_symbol(self, p):
        for line in self.lines:
            for i in line.symbols:
                if p.near(i):
                    return True
        return False

    def get_ratios(self, g):
        return [p.number for line in self.lines for p in line.parts if p.near(g)]


def parse_line(s: str) -> Line:
    return Line(
        [PartNumber(int(m[0]), m.start(), m.end()-1) for m in re.finditer(r'[0-9]+', s)],
        [i for i in range(0, len(s)) if is_symbol(s[i])],
        [i for i in range(0, len(s)) if is_gear(s[i])]
    )


def sum_of_part_numbers(file: Iterable):
    window = SlidingWindow()
    sum_part = 0
    sum_ratios = 0
    for line in file:
        window.push(parse_line(line))
        sum_part += sum(window.get_part_numbers())
        sum_ratios += sum(window.get_gear_ratios())
    window.push(Line([], [], []))
    sum_part += sum(window.get_part_numbers())
    sum_ratios += sum(window.get_gear_ratios())
    return sum_part, sum_ratios


if __name__ == '__main__':
    with open('input/day_03.txt') as file:
        sum_parts, sum_ratios = sum_of_part_numbers(file)
        print(f'Sum of part numbers: {sum_parts}')
        print(f'Sum of ratios: {sum_ratios}')

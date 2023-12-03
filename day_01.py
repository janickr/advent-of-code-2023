from dataclasses import dataclass


@dataclass
class NumberString:
    string: str
    value: int


numberstrings = [
    NumberString('one', 1),
    NumberString('two', 2),
    NumberString('three', 3),
    NumberString('four', 4),
    NumberString('five', 5),
    NumberString('six', 6),
    NumberString('seven', 7),
    NumberString('eight', 8),
    NumberString('nine', 9),
]

@dataclass
class Values:
    first: int | None
    last: int | None

    def add_value(self, value: int):
        if self.first is None:
            self.first = value
        self.last = value

    def total(self):
        return self.first * 10 + self.last


def parse_number_string(s, i):
    for n in numberstrings:
        if s.startswith(n.string, i):
            return n.value
    return None


def calibration_value(s: str) -> int:
    values = Values(None, None)

    for i in range(0, len(s)):
        if s[i].isdigit():
            values.add_value(int(s[i]))
        else:
            value = parse_number_string(s, i)
            if value is not None:
                values.add_value(value)

    return values.total()


if __name__ == '__main__':
    with open('input/day_01.txt') as file:
        sum_values = 0
        for line in file:
            sum_values += calibration_value(line)

        print(f'The sum is: {sum_values}')




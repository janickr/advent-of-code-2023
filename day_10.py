import itertools
from dataclasses import dataclass
from operator import attrgetter
from typing import Callable, Sequence, Set


@dataclass
class Tile:
    name: str
    pos: Sequence
    connect: Set[Sequence]

    def move(self, old):
        return next(iter(dst)) if len(dst := self.connect - {old}) == 1 else self.pos

    def is_connected(self, pos):
        return pos in self.connect


@dataclass
class Pos:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def up(self) : return Pos(self.x, self.y-1)
    def down(self) : return Pos(self.x, self.y+1)
    def left(self) : return Pos(self.x-1, self.y)
    def right(self) : return Pos(self.x+1, self.y)

    def neighbors(self):
        return self.up(), self.down(), self.left(), self.right()


def to_tile(pos, t):
    match t:
        case '-': return Tile(t, pos, {pos.left(), pos.right()})
        case '|': return Tile(t, pos, {pos.up(), pos.down()})
        case 'L': return Tile(t, pos, {pos.up(), pos.right()})
        case 'J': return Tile(t, pos, {pos.up(), pos.left()})
        case '7': return Tile(t, pos, {pos.left(), pos.down()})
        case 'F': return Tile(t, pos, {pos.right(), pos.down()})

    return Tile(t, pos, {pos})


def to_tiles(y, line):
    return [to_tile(Pos(x, y), t) for x, t in enumerate(line)]


def find_start(sketch):
    for pos, tile in sketch.items():
        if tile.name == 'S':
            return tile


def traverse(sketch):
    curr_tile = find_start(sketch)
    next_tile = next((sketch[p] for p in curr_tile.pos.neighbors() if sketch[p].is_connected(curr_tile.pos)))
    yield curr_tile
    while not (next_tile == curr_tile):
        pos = next_tile.move(curr_tile.pos)
        curr_tile = next_tile
        next_tile = sketch[pos]
        yield curr_tile


def find_path(lines):
    sketch = {tile.pos: tile for tile in itertools.chain(*(to_tiles(y, line) for y, line in enumerate(lines)))}
    return [t for t in traverse(sketch)]


def distance_farthest_point(lines):
    return (len(find_path(lines)) - 1) / 2


def enclosed_area(lines):
    sorted_path = sorted(find_path(lines), key=attrgetter('pos.x', 'pos.y'))
    by_column = [list(g) for k, g in itertools.groupby(sorted_path, key=attrgetter('pos.x'))]
    return sum(count_enclosed(column) for column in by_column)


def in_or_out(enclosed, last, next):
    if next == '|':
        return enclosed
    if next in '-F7':
        return not enclosed

    match last, next:
        case 'F', 'L': return not enclosed
        case 'F', 'J': return enclosed
        case '7', 'J': return not enclosed
        case '7', 'L': return enclosed


def count_enclosed(path):
    enclosed = False
    relevant = None
    previous = None
    sum = 0
    for tile in sorted(path, key=attrgetter('pos.y')):
        if enclosed:
            sum += tile.pos.y - previous.pos.y - 1

        enclosed = in_or_out(enclosed, relevant, tile.name)
        if not(tile.name == '|'):
            relevant = tile.name
        previous = tile

    return sum


if __name__ == '__main__':
    with open('input/day_10.txt') as file:
        result = enclosed_area((line.strip('\n') for line in file))
        print(f'The result is: {result}')
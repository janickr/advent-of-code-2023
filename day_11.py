import itertools
from dataclasses import dataclass


@dataclass
class Pos:
    x: int
    y: int

    def distance(self, p):
        return abs(self.x - p.x) + abs(self.y - p.y)


def to_galaxies(y, line):
    return [Pos(x, y) for x, g in enumerate(line) if g == '#']


def galaxy_positions(lines):
    return list(itertools.chain(*(to_galaxies(y, line) for y, line in enumerate(lines))))


def shortest_distances(lines, expansion=2):
    galaxies = galaxy_positions(lines)
    expand = compute_expansion(expansion, galaxies)

    expanded_galaxies = [(i+1, expand(g)) for i, g in enumerate(galaxies)]
    galaxy_pairs = itertools.combinations(expanded_galaxies, 2)

    return [(id1, id2, pos1.distance(pos2)) for (id1, pos1), (id2, pos2) in galaxy_pairs]


def compute_expansion(expansion, galaxies):
    ys = [expansion - 1] * (max(*(g.y for g in galaxies))+1)
    xs = [expansion - 1] * (max(*(g.x for g in galaxies))+1)
    for galaxy in galaxies:
        xs[galaxy.x] = 0
        ys[galaxy.y] = 0

    dx = list(itertools.accumulate(xs))
    dy = list(itertools.accumulate(ys))

    return lambda pos: Pos(pos.x+dx[pos.x], pos.y+dy[pos.y])


def sum_shortest_distances(lines, expansion=2):
    return sum(dist for g1, g2, dist in shortest_distances(lines, expansion=expansion))


if __name__ == '__main__':
    with open('input/day_11.txt') as file:
        result = sum_shortest_distances((line.strip('\n') for line in file), expansion=1000000)
        print(f'The result is: {result}')
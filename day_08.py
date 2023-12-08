import functools
import math
import re
from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Node:
    name: str
    L: str
    R: str


def to_node(line):
    m = re.match(r'([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)', line)
    return Node(m.group(1), m.group(2), m.group(3))


def traverse(network, path, current, stop_condition):
    i = 0
    while not stop_condition(current):
        current = attrgetter(path[i])(network[current])
        i = (i+1) % len(path)
        yield current


def path_length(lines, method):
    path = next(lines)
    next(lines)
    network = {node.name: node for node in (to_node(line) for line in lines)}

    return method(network, path)


def normal_path_length_from(network, path, name, stop_condition):
    return functools.reduce(lambda length, n: length + 1, traverse(network, path, name, stop_condition), 0)


def normal_path_length(network, path):
    return normal_path_length_from(network, path, 'AAA', lambda current: current == 'ZZZ')


def ghost_path_length(network, path):
    starting_nodes = [name for name, node in network.items() if name[2] == 'A']
    paths = [normal_path_length_from(network, path, name, lambda current: current[2] == 'Z') for name in starting_nodes]
    return math.lcm(*paths)


if __name__ == '__main__':
    with open('input/day_08.txt') as file:
        result = path_length((line.strip('\n') for line in file), ghost_path_length)
        print(f'The result is: {result}')

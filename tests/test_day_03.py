from day_03 import parse_line, sum_of_part_numbers, Line, PartNumber, SlidingWindow


class TestDay03:

    def test_parse(self):
        assert parse_line('467..114..') == Line([PartNumber(467, 0, 2), PartNumber(114, 5, 7)], [], [])
        assert parse_line('...*......') == Line([], [3], [3])
        assert parse_line('617*......') == Line([PartNumber(617, 0, 2)], [3], [3])


    def test_window(self):
        w = SlidingWindow()
        w.push(parse_line('467..114..'))
        w.push(parse_line('...*......'))
        assert w.get_part_numbers() == [467]

    def test_sum_of_parts(self):
        schematic = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split('\n')
        assert sum_of_part_numbers(schematic) == (4361, 467835)

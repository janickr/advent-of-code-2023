import day_10


class TestDay10:


    def test_example_part1_values(self):
        assert day_10.distance_farthest_point((l for l in ('''.....
.S-7.
.|.|.
.L-J.
.....'''.split('\n')))) == 4

    def test_example_part1(self):
        assert day_10.distance_farthest_point((l for l in ('''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''.split('\n')))) == 8

    def test_example_part2(self):
        assert day_10.enclosed_area((l for l in ('''...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....'''.split('\n')))) == 4

    def test_example_part2_larger(self):
        assert day_10.enclosed_area((l for l in (
'''
OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO'''.split('\n')))) == 8

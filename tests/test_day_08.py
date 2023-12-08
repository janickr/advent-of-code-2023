import day_08


class TestDay08:

    def test_example_part1(self):
        assert day_08.path_length((l for l in ('''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.split('\n'))), day_08.normal_path_length) == 6

    def test_example_part2(self):
        assert day_08.path_length((l for l in ('''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.split('\n'))), day_08.ghost_path_length) == 6


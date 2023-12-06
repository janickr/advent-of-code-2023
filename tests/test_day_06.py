import day_06


class TestDay06:

    def test_example_part1_ways(self):
        assert day_06.count_ways((l for l in ('''Time:      7  15   30
Distance:  9  40  200'''.split('\n')))) == [4, 8, 9]

    def test_example_part1_result(self):
        assert day_06.product_of_ways((l for l in ('''Time:      7  15   30
Distance:  9  40  200'''.split('\n')))) == 288

    def test_example_part2_result(self):
        assert day_06.product_of_ways((l.replace(' ', '') for l in ('''Time:      7  15   30
Distance:  9  40  200'''.split('\n')))) == 71503


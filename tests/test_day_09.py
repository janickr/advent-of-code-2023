import day_09


class TestDay09:

    def test_example_part1_values(self):
        assert day_09.next_values((l for l in ('''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.split('\n')))) == [(-3, 18), (0, 28), (5, 68)]

    def test_example_part1(self):
        assert day_09.sum_of_next_value((l for l in ('''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.split('\n')))) == (2, 114)

import day_07


class TestDay06:

    def test_example_part1(self):
        assert day_07.total_winnings((l for l in ('''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.split('\n')))) == 5905


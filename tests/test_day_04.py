from day_04 import sum_of_points, points, sum_of_cards


class TestDay04:

#    1
#    1 1
#    1 2 1
#    1 2 4 1
#    1   4 8 1
#              1
    def test_parse(self):
        assert points('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53') == 8
        assert points('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19') == 2
        assert points('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1') == 2
        assert points('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83') == 1
        assert points('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36') == 0
        assert points('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11') == 0

    def test_bug(self):
        assert points('Card   1: 42 68 56  3 28 97  1 78 55 48 | 78 54  3 38 94 73 72 57 51 31 86 43  7 81  4 27 26 58 75 69 74 55  5 28 40') == 8


    def test_sum_of_parts(self):
        cards = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')
        assert sum_of_points(cards) == 13

    def test_sum_of_cards(self):
        cards = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')
        assert sum_of_cards(cards) == 30

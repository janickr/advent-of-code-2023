from day_02 import parse_game, Game, Cubes


class TestDay02:

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    def test_parse_game(self):
        assert parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == \
               Game(1, [
                   Cubes(blue=3, red=4),
                   Cubes(red=1, green=2, blue=6),
                   Cubes(green=2)
               ])
        assert parse_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == \
               Game(2, [
                   Cubes(blue=1, green=2),
                   Cubes(green=3, blue=4, red=1),
                   Cubes(green=1, blue=1)
               ])

        assert parse_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') == \
               Game(3, [
                   Cubes(green=8, blue=6, red=20),
                   Cubes(blue=5, red=4, green=13),
                   Cubes(green=5, red=1)
               ])

        assert parse_game('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') == \
               Game(4, [
                   Cubes(green=1, red=3, blue=6),
                   Cubes(green=3, red=6),
                   Cubes(green=3, blue=15, red=14)
               ])

        assert parse_game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') == \
               Game(5, [
                   Cubes(red=6, blue=1, green=3),
                   Cubes(blue=2, red=1, green=2)
               ])

    def test_is_possible(self):
        bag = Cubes(red=12, green=13, blue=14)
        assert Game(1, [
            Cubes(blue=3, red=4),
            Cubes(red=1, green=2, blue=6),
            Cubes(green=2)
        ]).is_possible_with_bag(bag) is True
        assert Game(2, [
            Cubes(blue=1, green=2),
            Cubes(green=3, blue=4, red=1),
            Cubes(green=1, blue=1)
        ]).is_possible_with_bag(bag) is True

        assert Game(3, [
            Cubes(green=8, blue=6, red=20),
            Cubes(blue=5, red=4, green=13),
            Cubes(green=5, red=1)
        ]).is_possible_with_bag(bag) is False

        assert Game(4, [
            Cubes(green=1, red=3, blue=6),
            Cubes(green=3, red=6),
            Cubes(green=3, blue=15, red=14)
        ]).is_possible_with_bag(bag) is False

        assert Game(5, [
            Cubes(red=6, blue=1, green=3),
            Cubes(blue=2, red=1, green=2)
        ]).is_possible_with_bag(bag) is True


    def test_max(self):
        assert Cubes(red=2, green=2).max(Cubes(red=1, blue=1)) == Cubes(red=2, green=2, blue=1)

    def test_power(self):
        assert Cubes(red=2, green=2, blue=1).power() == 4

    def test_power_of_fewest(self):
        assert Game(1, [
            Cubes(blue=3, red=4),
            Cubes(red=1, green=2, blue=6),
            Cubes(green=2)
        ]).fewest_possible().power() == 48
        assert Game(2, [
            Cubes(blue=1, green=2),
            Cubes(green=3, blue=4, red=1),
            Cubes(green=1, blue=1)
        ]).fewest_possible().power() == 12

        assert Game(3, [
            Cubes(green=8, blue=6, red=20),
            Cubes(blue=5, red=4, green=13),
            Cubes(green=5, red=1)
        ]).fewest_possible().power() == 1560

        assert Game(4, [
            Cubes(green=1, red=3, blue=6),
            Cubes(green=3, red=6),
            Cubes(green=3, blue=15, red=14)
        ]).fewest_possible().power() == 630

        assert Game(5, [
            Cubes(red=6, blue=1, green=3),
            Cubes(blue=2, red=1, green=2)
        ]).fewest_possible().power() == 36

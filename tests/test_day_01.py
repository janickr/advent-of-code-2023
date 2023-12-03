from day_01 import calibration_value


class TestDay01:
    def test_digits(self):
        assert calibration_value('1abc2') == 12
        assert calibration_value('pqr3stu8vwx') == 38
        assert calibration_value('a1b2c3d4e5f') == 15
        assert calibration_value('treb7uchet') == 77


    def test_number_strings(self):
        assert calibration_value('two1nine') == 29
        assert calibration_value('eightwothree') == 83
        assert calibration_value('abcone2threexyz') == 13
        assert calibration_value('xtwone3four') == 24
        assert calibration_value('4nineeightseven2') == 42
        assert calibration_value('zoneight234') == 14
        assert calibration_value('7pqrstsixteen') == 76


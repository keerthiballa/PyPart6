import unittest
import temperature_utils
import temperature_utils_v2

class TemperatureUtilsTest(unittest.TestCase):

    def test_convert_to_celsius(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils.convert_to_celsius(temp_in))

    def test_convert_to_fahrenheit(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils.convert_to_fahrenheit(temp_in))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils.temperature_tuple(temps_input, "f")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils.temperature_tuple(temps_input, "c")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils.temperature_tuple(temps_input, "a"))

    def test_convert_kelvin_to_celsius(self):
        test_cases = [
            (0,-273.15),
            (32,-241.15),
            (100,-173.15),
            (273.15,0)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_kelvin_to_celsius(temp_in))

    def test_convert_kelvin_to_fahrenheit(self):
        test_cases = [
            (0,-459.67),
            (32,-402.07),
            (100,-279.67),
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_kelvin_to_fahrenheit(temp_in))

    def test_convert_fahrenheit_to_kelvin(self):
        test_cases = [
            (-459.67,0),
            (-402.07,32),
            (-279.67,100),
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_fahrenheit_to_kelvin(temp_in))

    def test_convert_celsius_to_kelvin(self):
        test_cases = [
            (-273.15,0),
            (-241.15,32),
            (-173.15,100),
            (0,273.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_celsius_to_kelvin(temp_in))

    def test_temperature_tuple_v2(self):
        temps_input = (-273.15, -241.15, -173.15, 0)
        expected = ((-273.15,0),(-241.15,32),(-173.15,100),(0,273.15))
        actual = temperature_utils_v2.temperature_tuple_v2(temps_input, "c","k")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple_v2(self):
        temps_input = (-459.67, -402.07, -279.67)
        expected = ((-459.67,0),(-402.07,32),(-279.67,100))
        actual = temperature_utils_v2.temperature_tuple_v2(temps_input, "f", "k")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple_v2(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils_v2.temperature_tuple_v2(temps_input,"a", "h"))
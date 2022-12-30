import unittest

from cliching import Line

class TestLine(unittest.TestCase):
    def test_cointoss(self):
        result = Line.cointoss()
        self.assertIn(result, [2, 3])

    def test_generate_line(self):
        result = Line.generate_line()
        self.assertIn(result, [6, 7, 8, 9, 10])

    def test_locate_hexagram(self):
        hex_pattern = '123456'
        result = Line.locate_hexagram(hex_pattern)
        self.assertIsInstance(result, dict)
        self.assertEqual(result['pattern'], int(hex_pattern))

    def test_convert_hexagrams(self):
        hexagram = '123456'
        result = Line.convert_hexagrams(hexagram)
        self.assertIsNone(result)

    def test_generate_hexagram(self):
        result = Line.generate_hexagram()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

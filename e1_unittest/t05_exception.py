import unittest


# A simple function to illustrate
def parse_int(s):
    return int(s)


class TestConversion1(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')


class TestConversion2(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A')


class TestConversion3(unittest.TestCase):
    def test_bad_int(self):
        with self.assertRaisesRegex(ValueError, 'invalid literal .*'):
            parse_int('N/A')


if __name__ == '__main__':
    unittest.main(verbosity=2)

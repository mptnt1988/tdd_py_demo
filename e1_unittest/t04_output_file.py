# t04_output_file.py
import sys
import unittest


# code
def some_func():
    return 1


# test
class Problem(unittest.TestCase):
    def setUp(self):
        tc_id = self.id()
        print()
        print('Setting up', tc_id, '...')

    def tearDown(self):
        tc_id = self.id()
        print('Tearing down', tc_id, '...')

    def test_one(self):
        self.assertEqual(some_func(), 1)

    def test_second(self):
        self.assertEqual(some_func(), 1)


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('t04_output_file.out', 'w') as f:
        main(f)

# t02_tc_selected.py
import unittest


# code
def some_func():
    return 1


# test
class Problem(unittest.TestCase):
    def test_one(self):
        self.assertEqual(some_func(), 1)

    def test_second(self):
        self.assertEqual(some_func(), 1)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Problem('test_one'), )
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

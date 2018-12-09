# t01_basic.py
import unittest


# code
def some_func():
    return 1


# test
class Problem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        clz = cls.__name__
        print()
        print(f'Setting up class {clz}...')

    @classmethod
    def tearDownClass(cls):
        clz = cls.__name__
        print(f'Tearing down class {clz}...')

    def setUp(self):
        tc_id = self.id()
        print()
        print(f'Setting up {tc_id}...')

    def tearDown(self):
        tc_id = self.id()
        print(f'Tearing down {tc_id}...')

    def test_one(self):
        self.assertEqual(some_func(), 1)

    def test_second(self):
        self.assertEqual(some_func(), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)

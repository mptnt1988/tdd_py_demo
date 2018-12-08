import errno
import unittest


class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
            f.close()
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')


if __name__ == '__main__':
    unittest.main(verbosity=2)

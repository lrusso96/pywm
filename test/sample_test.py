from pywmit import check
import unittest


class TestSampleMethods(unittest.TestCase):
    def test_simple(self):
        check("Council of Fashion Designers of America")


if __name__ == '__main__':
    unittest.main()

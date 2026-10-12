import unittest
from main import add

class TestAdd(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(sorted(add([2, 7, 11, 15], 9)), [0, 1])

    def test_example_2(self):
        self.assertEqual(sorted(add([3, 2, 4], 6)), [1, 2])

    def test_example_3(self):
        self.assertEqual(sorted(add([3, 3], 6)), [0, 1])

    def test_no_solution(self):
        self.assertEqual(add([1, 2, 3], 100), [])

    def test_negative(self):
        self.assertEqual(sorted(add([-3, 4, 3, 90], 0)), [0, 2])

    def test_zeros(self):
        self.assertEqual(sorted(add([0, 4, 3, 0], 0)), [0, 3])

    def test_at_the_end(self):
        self.assertEqual(sorted(add([1, 2, 100, 5], 105)), [2, 3])



if __name__ == '__main__':
    unittest.main()
import unittest
from Pyfoundation.core.mathematics.algebra import Algebra


class TestAlgebra(unittest.TestCase):

    def test_tool_exists(self):
        pass

    def test_summation(self):
        # Test cases for summation
        self.assertEqual(Algebra.summation([1, 2, 3], [1, 2, 3]), [2, 4, 6])
        self.assertEqual(Algebra.summation([2], [4]), [6])
        self.assertEqual(Algebra.summation(2, 4), 6)

    # Add more test cases as needed
    def test_subtraction(self):
        # Test cases for subtraction
        self.assertEqual(Algebra.subtraction([2, 3, 4], [1, 2, 3]), [1, 1, 1])
        self.assertEqual(Algebra.subtraction([2], [1]), [1])
        self.assertEqual(Algebra.subtraction(2, 1), 1)

    def test_division(self):
        # Test cases for division
        self.assertEqual(Algebra.division([2, 4, 6], [1, 2, 3]), [2, 2, 2])
        self.assertEqual(Algebra.division([2], [1]), [2])
        self.assertEqual(Algebra.division(2, 1), 2)

    def test_multiplication(self):
        # Test cases for multiplication
        self.assertEqual(Algebra.multiplication([2, 3, 4], [1, 2, 3]), [2, 6, 12])
        self.assertEqual(Algebra.multiplication([2], [1]), [2])
        self.assertEqual(Algebra.multiplication(2, 1), 2)

    def test_square_root(self):
        # Test cases for square root
        self.assertEqual(Algebra.square_root([4, 9, 16, 25, 36]), [2, 3, 4, 5, 6])
        self.assertEqual(Algebra.square_root([4]), [2])
        self.assertEqual(Algebra.square_root(4), 2)

    def test_power(self):
        self.assertEqual(Algebra.power(2, 3), 8)
        self.assertEqual(Algebra.power([2, 3, 4, 5], [2, 2, 2, 2]), [4, 9, 16, 25])
        self.assertEqual(Algebra.power([2], [2]), [4])

    def test_sum_natural_numbers(self):
        self.assertEqual(Algebra.sum_natural_numbers(5), 15)

    def test_log10(self):
        self.assertEqual(Algebra.log10(10), 1)
        self.assertEqual(Algebra.log10([10]), [1])
        self.assertEqual(Algebra.log10([10, 100]), [1, 2])


if __name__ == '__main__':
    unittest.main()

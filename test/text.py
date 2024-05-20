import unittest

from mathematics.algebra import (summation, subtraction, division, multiplication, square_root, power,
                                 sum_natural_numbers, log, log10)  # Import your


# functions here


class TestYourTool(unittest.TestCase):

    def test_tool_exists(self):
        pass

    def test_summation(self):
        # Test cases for summation
        self.assertEqual(summation([1, 2, 3], [1, 2, 3]), [2, 4, 6])
        self.assertEqual(summation([2], [4]), [6])
        self.assertEqual(summation(2, 4), 6)

    # Add more test cases as needed
    def test_subtraction(self):
        # Test cases for subtraction
        self.assertEqual(subtraction([2, 3, 4], [1, 2, 3]), [1, 1, 1])
        self.assertEqual(subtraction([2], [1]), [1])
        self.assertEqual(subtraction(2, 1), 1)

    def test_division(self):
        # Test cases for division
        self.assertEqual(division([2, 4, 6], [1, 2, 3]), [2, 2, 2])
        self.assertEqual(division([2], [1]), [2])
        self.assertEqual(division(2, 1), 2)

    def test_multiplication(self):
        # Test cases for multiplication
        self.assertEqual(multiplication([2, 3, 4], [1, 2, 3]), [2, 6, 12])
        self.assertEqual(multiplication([2], [1]), [2])
        self.assertEqual(multiplication(2, 1), 2)

    def test_square_root(self):
        # Test cases for square root
        self.assertEqual(square_root([4, 9, 16, 25, 36]), [2, 3, 4, 5, 6])
        self.assertEqual(square_root([4]), [2])
        self.assertEqual(square_root(4), 2)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power([2, 3, 4, 5], [2, 2, 2, 2]), [4, 9, 16, 25])
        self.assertEqual(power([2], [2]), [4])

    def test_sum_natural_numbers(self):
        self.assertEqual(sum_natural_numbers(5), 15)

    def test_log10(self):
        self.assertEqual(log10(10), 1)
        self.assertEqual(log10([10]), [1])
        self.assertEqual(log10([10, 100]), [1, 2])


if __name__ == '__main__':
    unittest.main()

import cmath
import math


class Algebra:
    @staticmethod
    def summation(*args):
        """summation returns the sum of the given two values"""
        if len(args[0]) != len(args[0]):  # Check if both lists have the same length
            raise ValueError("Both lists must have the same length")
        summed_list = []  # Create a new list to store the sum
        # Iterate through both lists and add corresponding elements
        for i in range(len(args[0])):
            summed_list.append(args[0][i] + args[1][i])
        return summed_list

    def subtraction(self):
        """subtraction returns the subtraction of the given two values"""
        pass

    def multiplication(self):
        """multiplication returns the multiplication of given two values"""
        pass

    def division(self):
        """division returns the division of given two values"""
        pass

    @staticmethod
    def square_root(value):
        """square root returns the square root of given value"""
        return cmath.sqrt(value)

    @staticmethod
    def power(base, base_power=1):
        """power returns the power of the given power with the base"""
        value = 1
        for i in range(1, base_power + 1):
            value = value * base
        return value

    @staticmethod
    def factorial(*args):
        """factorial return the factorial of given value"""
        if not all(isinstance(n, int) and n >= 0 for n in args[0]):
            raise ValueError("All elements in the list must be non-negative integers")
        return [math.factorial(n) for n in args[0]]

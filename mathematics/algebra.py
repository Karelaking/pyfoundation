import cmath
import math


class Algebra:
    @staticmethod
    def summation(*args):
        """summation returns the sum of the given two values"""
        if isinstance(args[0] and args[1], int):
            return args[0] + args[1]
        else:
            if len(args[0]) != len(args[0]):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(args[0])):
                summed_list.append(args[0][i] + args[1][i])
            return summed_list

    def subtraction(*args):
        """subtraction returns the subtraction of the given two values"""
        if isinstance(args[0] and args[1], int):
            return args[0] - args[1]
        else:
            if len(args[0]) != len(args[0]):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(args[0])):
                summed_list.append(args[0][i] - args[1][i])
            return summed_list

    def multiplication(*args):
        """multiplication returns the multiplication of given two values"""
        if isinstance(args[0] and args[1], int):
            return args[0] * args[1]
        else:
            if len(args[0]) != len(args[0]):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(args[0])):
                summed_list.append(args[0][i] * args[1][i])
            return summed_list

    def division(*args):
        """division returns the division of given two values"""
        if isinstance(args[0] and args[1], int):
            return args[0] / args[1]
        else:
            if len(args[0]) != len(args[0]):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(args[0])):
                summed_list.append(args[0][i] / args[1][i])
            return summed_list

    @staticmethod
    def square_root(*args):
        """square root returns the square root of given value"""
        if isinstance(args[0], int):
            return math.sqrt(args[0])
        else:
            if not all(isinstance(n, int) and n >= 0 for n in args[0]):
                raise ValueError("All elements in the list must be non-negative integers")
            return [math.sqrt(n) for n in args[0]]

    @staticmethod
    def power(*args):
        """power returns the power of the given power with the base"""
        if isinstance(args[0] and args[1], int):
            return math.pow(args[0], args[1])
        else:
            if len(args[0]) != len(args[0]):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(args[0])):
                summed_list.append(math.pow(args[0][i], args[1][i]))
            return summed_list

    @staticmethod
    def factorial(*args):
        """factorial return the factorial of given value"""
        if isinstance(args[0], int):
            return math.factorial(args[0])
        else:
            if not all(isinstance(n, int) and n >= 0 for n in args[0]):
                raise ValueError("All elements in the list must be non-negative integers")
            return [math.factorial(n) for n in args[0]]


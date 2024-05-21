import math
from typing import Union, List

dataType = Union[Union[int, float], List[Union[int, float]]]


class Algebra:

    @staticmethod
    def summation(*args: dataType) -> dataType:
        f"""Summation returns the sum of multiple integers or element-wise sum of multiple lists of integers. \n
        :rtype: f"{dataType}"
        """
        if not args:
            return 0
            # raise ValueError("At least one argument is required.")
        # If all arguments are integers
        if all(isinstance(arg, (int, float)) for arg in args):
            return sum(args)
        # If all arguments are lists
        if all(isinstance(arg, list) for arg in args):
            list_length = len(args[0])
            if any(len(arg) != list_length for arg in args):
                raise ValueError("All lists must have the same length.")
            if any(not all(isinstance(item, (int, float)) for item in arg) for arg in args):
                raise TypeError("All lists must contain only integers.")
            return [sum(items) for items in zip(*args)]
        raise TypeError("Inputs must be all integers or all lists of integers of the same length.")

    @staticmethod
    def subtraction(*args: dataType) -> dataType:
        """Subtraction returns the subtraction of multiple numbers (integers or floats) or element-wise subtraction
            of multiple lists of numbers."""
        if not args:
            raise ValueError("At least one argument is required.")
        # If all arguments are numbers (int or float)
        if all(isinstance(arg, (int, float)) for arg in args):
            return args[0] - sum(args[1:])
        # If all arguments are lists
        if all(isinstance(arg, list) for arg in args):
            list_length = len(args[0])
            if any(len(arg) != list_length for arg in args):
                raise ValueError("All lists must have the same length.")
            if any(not all(isinstance(item, (int, float)) for item in arg) for arg in args):
                raise TypeError("All lists must contain only numbers (integers or floats).")
            return [items[0] - sum(items[1:]) for items in zip(*args)]
        raise TypeError("Inputs must be all numbers (integers or floats) or all lists of numbers of the same length.")

    @staticmethod
    def multiplication(*args):
        """Multiplication returns the product of multiple numbers (integers or floats) or element-wise multiplication
            of multiple lists of numbers."""
        if not args:
            raise ValueError("At least one argument is required.")
        # If all arguments are numbers (int or float)
        if all(isinstance(arg, (int, float)) for arg in args):
            result = 1
            for num in args:
                result *= num
            return result
        # If all arguments are lists
        if all(isinstance(arg, list) for arg in args):
            list_length = len(args[0])
            if any(len(arg) != list_length for arg in args):
                raise ValueError("All lists must have the same length.")
            if any(not all(isinstance(item, (int, float)) for item in arg) for arg in args):
                raise TypeError("All lists must contain only numbers (integers or floats).")
            # return [item[0] * item[1] for item in zip(*args)]
            return [item[0] * item[1] for item in zip(*args)]
        raise TypeError("Inputs must be all numbers (integers or floats) or all lists of numbers of the same length.")

    @staticmethod
    def division(*args):
        """Division returns the division of multiple numbers (integers or floats) or element-wise division of multiple
            lists of numbers."""
        if not args:
            raise ValueError("At least one argument is required.")
        # If all arguments are numbers (int or float)
        if all(isinstance(arg, (int, float)) for arg in args):
            result = args[0]
            for num in args[1:]:
                result /= num
            return result
        # If all arguments are lists
        if all(isinstance(arg, list) for arg in args):
            list_length = len(args[0])
            if any(len(arg) != list_length for arg in args):
                raise ValueError("All lists must have the same length.")
            if any(not all(isinstance(item, (int, float)) for item in arg) for arg in args):
                raise TypeError("All lists must contain only numbers (integers or floats).")
            return [item[0] / item[1] for item in zip(*args)]
        raise TypeError("Inputs must be all numbers (integers or floats) or all lists of numbers of the same length.")

    @staticmethod
    def square_root(*args):
        """Square root returns the square root of given values (integers or floats)."""
        if not args:
            raise ValueError("At least one argument is required.")
        # If all arguments are single numbers (int or float)
        if len(args) == 1 and isinstance(args[0], (int, float)):
            if args[0] < 0:
                raise ValueError("Cannot take the square root of a negative number")
            return math.sqrt(args[0])
        # If the argument is a list of numbers
        if len(args) == 1 and isinstance(args[0], list):
            if not all(isinstance(n, (int, float)) and n >= 0 for n in args[0]):
                raise ValueError("All elements in the list must be non-negative integers or floats")
            return [math.sqrt(n) for n in args[0]]
        raise TypeError("Input must be a single non-negative number or a list of non-negative numbers")

    @staticmethod
    def power(*args):
        """Power returns the power of the given base and exponent."""
        if len(args) != 2:
            raise ValueError("Two arguments are required: base(s) and exponent(s).")
        base, exponent = args
        # Single number case
        if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
            return math.pow(base, exponent)
        # Lists case
        if isinstance(base, list) and isinstance(exponent, list):
            if len(base) != len(exponent):
                raise ValueError("Both lists must have the same length.")
            if not all(isinstance(b, (int, float)) for b in base):
                raise TypeError("All elements in the base list must be integers or floats.")
            if not all(isinstance(e, (int, float)) for e in exponent):
                raise TypeError("All elements in the exponent list must be integers or floats.")
            return [math.pow(b, e) for b, e in zip(base, exponent)]
        raise TypeError("Arguments must be either both numbers or both lists of numbers.")

    @staticmethod
    def factorial(*args):
        """Factorial returns the factorial of given values."""
        if len(args) != 1:
            raise ValueError(
                "One argument is required: a single non-negative integer or a list of non-negative integers.")
        value = args[0]
        # Single integer case
        if isinstance(value, int):
            if value < 0:
                raise ValueError("Cannot compute factorial of a negative number.")
            return math.factorial(value)
        # List of integers case
        if isinstance(value, list):
            if not all(isinstance(n, int) and n >= 0 for n in value):
                raise ValueError("All elements in the list must be non-negative integers.")
            return [math.factorial(n) for n in value]
        raise TypeError("Input must be a single non-negative integer or a list of non-negative integers.")

    @staticmethod
    def log(*args):
        """Log returns the natural logarithm of given values."""
        if len(args) != 1:
            raise ValueError(
                "Exactly one argument is required: a non-negative number or a list of non-negative numbers.")
        value = args[0]
        # Single number case
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError("Cannot compute logarithm of a non-positive number.")
            return math.log(value)
        # List of numbers case
        if isinstance(value, list):
            if not all(isinstance(n, (int, float)) and n > 0 for n in value):
                raise ValueError("All elements in the list must be positive numbers.")
            return [math.log(n) for n in value]
        raise TypeError("Input must be a single positive number or a list of positive numbers.")

    @staticmethod
    def log10(*args):
        """Log10 returns the base-10 logarithm of given values."""
        if len(args) != 1:
            raise ValueError("Exactly one argument is required: a positive number or a list of positive numbers.")
        value = args[0]
        # Single number case
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError("Cannot compute logarithm of a non-positive number.")
            return math.log10(value)
        # List of numbers case
        if isinstance(value, list):
            if not all(isinstance(n, (int, float)) and n > 0 for n in value):
                raise ValueError("All elements in the list must be positive numbers.")
            return [math.log10(n) for n in value]
        raise TypeError("Input must be a single positive number or a list of positive numbers.")

    @staticmethod
    def ln(*args):
        pass

    @staticmethod
    def exponential(*args):
        """Exponential returns the exponential (e^x) of given values."""
        if len(args) != 1:
            raise ValueError("Exactly one argument is required: a number or a list of numbers.")
        value = args[0]
        # Single number case
        if isinstance(value, (int, float)):
            return math.exp(value)
        # List of numbers case
        if isinstance(value, list):
            if not all(isinstance(n, (int, float)) for n in value):
                raise ValueError("All elements in the list must be numbers.")
            return [math.exp(n) for n in value]
        raise TypeError("Input must be a single number or a list of numbers.")

    @staticmethod
    def sum_natural_numbers(*args):
        """Sum of natural numbers up to the given values."""
        if len(args) != 1:
            raise ValueError(
                "Exactly one argument is required: a non-negative integer or a list of non-negative integers.")
        value = args[0]

        # Function to calculate the sum of natural numbers up to n
        def sum_up_to(n):
            if n < 0:
                raise ValueError("Input must be a non-negative integer.")
            return n * (n + 1) // 2

        # Single integer case
        if isinstance(value, int):
            return sum_up_to(value)
        # List of integers case
        if isinstance(value, list):
            if not all(isinstance(n, int) and n >= 0 for n in value):
                raise ValueError("All elements in the list must be non-negative integers.")
            return [sum_up_to(n) for n in value]
        raise TypeError("Input must be a single non-negative integer or a list of non-negative integers.")

    @staticmethod
    def sum_squares_natural_numbers(*args):
        """Returns the sum of the squares of all natural numbers in the input."""
        if len(args) != 1:
            raise ValueError("Exactly one argument is required: a natural number or a list of natural numbers.")
        value = args[0]

        def is_natural_number(n):
            return isinstance(n, int) and n > 0

        # Single number case
        if is_natural_number(value):
            return value * (value + 1) * (2 * value + 1) // 6
        # List of numbers case
        if isinstance(value, list):
            if not all(is_natural_number(n) for n in value):
                raise ValueError("All elements in the list must be natural numbers.")
            return sum(n * (n + 1) * (2 * n + 1) // 6 for n in value)
        raise TypeError("Input must be a natural number or a list of natural numbers.")

    @staticmethod
    def sum_cubes_natural_numbers(*args):
        """Returns the sum of the cubes of all natural numbers in the input."""
        if len(args) != 1:
            raise ValueError("Exactly one argument is required: a natural number or a list of natural numbers.")
        value = args[0]

        # Helper function to calculate the cube
        def cube(n):
            if isinstance(n, int) and n > 0:
                return n ** 3
            else:
                raise ValueError("All elements must be natural numbers.")

        # Single number case
        if isinstance(value, int):
            return cube(value)
        # List of numbers case
        if isinstance(value, list):
            if not all(isinstance(n, int) and n > 0 for n in value):
                raise ValueError("All elements in the list must be natural numbers.")
            return sum(cube(n) for n in value)
        raise TypeError("Input must be a single natural number or a list of natural numbers.")

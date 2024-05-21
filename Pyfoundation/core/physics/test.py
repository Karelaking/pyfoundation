from typing import Union, List
import math

Number = Union[int, float]
NumberList = Union[Number, List[Number]]


def displacement(_u: NumberList, t: NumberList, a: NumberList) -> NumberList:
    if isinstance(_u, list):
        return [_u[i] * t[i] + 0.5 * a[i] * t[i] ** 2 for i in range(len(_u))]
    return _u * t + 0.5 * a * t ** 2


def final_velocity(u: NumberList, a: NumberList, t: NumberList) -> NumberList:
    if isinstance(u, list):
        return [u[i] + a[i] * t[i] for i in range(len(u))]
    return u + a * t


def final_velocity_squared(u: NumberList, a: NumberList, s: NumberList) -> NumberList:
    if isinstance(u, list):
        return [u[i] ** 2 + 2 * a[i] * s[i] for i in range(len(u))]
    return u ** 2 + 2 * a * s


def time_from_velocity(u: NumberList, v: NumberList, a: NumberList) -> NumberList:
    if isinstance(u, list):
        return [(v[i] - u[i]) / a[i] for i in range(len(u))]
    return (v - u) / a


def displacement_from_velocity(u: NumberList, v: NumberList, t: NumberList) -> NumberList:
    if isinstance(u, list):
        return [(u[i] + v[i]) / 2 * t[i] for i in range(len(u))]
    return (u + v) / 2 * t


def initial_velocity(v: NumberList, a: NumberList, t: NumberList) -> NumberList:
    if isinstance(v, list):
        return [v[i] - a[i] * t[i] for i in range(len(v))]
    return v - a * t


def acceleration(u: NumberList, v: NumberList, t: NumberList) -> NumberList:
    if isinstance(u, list):
        return [(v[i] - u[i]) / t[i] for i in range(len(u))]
    return (v - u) / t


def time_from_displacement(u: NumberList, s: NumberList, a: NumberList) -> NumberList:
    if isinstance(u, list):
        return [
            max(
                (-u[i] + math.sqrt(u[i] ** 2 - 2 * a[i] * -s[i])) / a[i],
                (-u[i] - math.sqrt(u[i] ** 2 - 2 * a[i] * -s[i])) / a[i]
            ) for i in range(len(u))
        ]
    discriminant = u ** 2 - 2 * a * -s
    if discriminant < 0:
        raise ValueError("No real solution exists")
    t1 = (-u + math.sqrt(discriminant)) / a
    t2 = (-u - math.sqrt(discriminant)) / a
    return max(t1, t2)


def average_velocity(u: NumberList, v: NumberList) -> NumberList:
    if isinstance(u, list):
        return [(u[i] + v[i]) / 2 for i in range(len(u))]
    return (u + v) / 2


def initial_velocity_from_displacement(s: NumberList, t: NumberList, a: NumberList) -> NumberList:
    if isinstance(s, list):
        return [(s[i] - 0.5 * a[i] * t[i] ** 2) / t[i] for i in range(len(s))]
    return (s - 0.5 * a * t ** 2) / t


def time_from_acceleration(v: NumberList, u: NumberList, a: NumberList) -> NumberList:
    if isinstance(v, list):
        return [(v[i] - u[i]) / a[i] for i in range(len(v))]
    return (v - u) / a


def displacement_from_initial_velocity(u: NumberList, v: NumberList, t: NumberList) -> NumberList:
    if isinstance(u, list):
        return [(u[i] + v[i]) / 2 * t[i] for i in range(len(u))]
    return (u + v) / 2 * t


def final_position(_initial_position: NumberList, u: NumberList, a: NumberList, t: NumberList) -> NumberList:
    if isinstance(_initial_position, list):
        return [_initial_position[i] + u[i] * t[i] + 0.5 * a[i] * t[i] ** 2 for i in range(len(_initial_position))]
    return _initial_position + u * t + 0.5 * a * t ** 2


def initial_position(_final_position: NumberList, u: NumberList, a: NumberList, t: NumberList) -> NumberList:
    if isinstance(_final_position, list):
        return [_final_position[i] - (u[i] * t[i] + 0.5 * a[i] * t[i] ** 2) for i in range(len(_final_position))]
    return _final_position - (u * t + 0.5 * a * t ** 2)


value = initial_velocity(v=[2, 3.0, 4], a=[10, 10.5, 10], t=[2, 2.3, 2])
print(value)


Number = Union[int, float]
NumberList = List[Number]


def summation(a: Union[Number, NumberList], b: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Both lists must have the same length")
        return [x + y for x, y in zip(a, b)]
    return a + b


def subtraction(a: Union[Number, NumberList], b: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Both lists must have the same length")
        return [x - y for x, y in zip(a, b)]
    return a - b


def multiplication(a: Union[Number, NumberList], b: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Both lists must have the same length")
        return [x * y for x, y in zip(a, b)]
    return a * b


def division(a: Union[Number, NumberList], b: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Both lists must have the same length")
        return [_x / _y for _x, _y in zip(a, b)]
    return a / b


def power(a: Union[Number, NumberList], b: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Both lists must have the same length")
        return [math.pow(x, y) for x, y in zip(a, b)]
    return math.pow(a, b)


def factorial(n: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(n, list):
        if not all(isinstance(i, int) and i >= 0 for i in n):
            raise ValueError("All elements in the list must be non-negative integers")
        return [math.factorial(i) for i in n]
    if isinstance(n, int) and n >= 0:
        return math.factorial(n)
    raise ValueError("Input must be a non-negative integer")


def square_root(n: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(n, list):
        if not all(isinstance(i, (int, float)) and i >= 0 for i in n):
            raise ValueError("All elements in the list must be non-negative numbers")
        return [math.sqrt(i) for i in n]
    if isinstance(n, (int, float)) and n >= 0:
        return math.sqrt(n)
    raise ValueError("Input must be a non-negative number")


def log(n: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(n, list):
        if not all(isinstance(i, (int, float)) and i > 0 for i in n):
            raise ValueError("All elements in the list must be positive numbers")
        return [math.log(i) for i in n]
    if isinstance(n, (int, float)) and n > 0:
        return math.log(n)
    raise ValueError("Input must be a positive number")


def log10(n: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(n, list):
        if not all(isinstance(i, (int, float)) and i > 0 for i in n):
            raise ValueError("All elements in the list must be positive numbers")
        return [math.log10(i) for i in n]
    if isinstance(n, (int, float)) and n > 0:
        return math.log10(n)
    raise ValueError("Input must be a positive number")


def exponential(n: Union[Number, NumberList]) -> Union[Number, NumberList]:
    if isinstance(n, list):
        if not all(isinstance(i, (int, float)) for i in n):
            raise ValueError("All elements in the list must be numbers")
        return [math.exp(i) for i in n]
    if isinstance(n, (int, float)):
        return math.exp(n)
    raise ValueError("Input must be a number")

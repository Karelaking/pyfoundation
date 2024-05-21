from typing import Union, List

dataType = Union[Union[int, float], List[Union[int, float]]]


class Kinematics:
    def __init__(self):
        super().__init__()

    @staticmethod
    def distance(_speed: dataType, _time: dataType) -> dataType:
        f"""
        Calculate distance given speed and time \n

        This function handles both single values and lists of values. If both inputs 
        are single values (either integers or floats), it returns the distance as a single value. 
        If both inputs are lists of values, it returns a list of distances for each corresponding 
        pair of speed and time values. The lists must be of equal length.\n

        Parameters:\n
        speed (int, float, list of int, or list of float): The speed(s).
        time (int, float, list of int, or list of float): The time(s) taken.\n

        Returns:\n
        float or list of float: The calculated distance(s).\n

        Raises:\n
        TypeError: If the inputs are not both numbers or both lists of equal length.\n

        Examples:\n
        > distance(50, 2)\n
        100.0\n
        > distance([50, 60], [2, 3])\n
        [100.0, 180.0]\n
        """
        if isinstance(_speed, (int, float)) and isinstance(_time, (int, float)):
            return _speed * _time
        if isinstance(_speed, list) and isinstance(_time, list) and len(_speed) == len(_time):
            return [s * t for s, t in zip(_speed, _time)]
        raise TypeError("Inputs must be either both numbers or both lists of equal length")

    @staticmethod
    def speed(_distance: dataType, _time: dataType) -> dataType:
        f"""
        Calculate speed given distance and time.\n

        This function handles both single values and lists of values. If both inputs
        are single values (either integers or floats), it returns the speed as a single value.
        If both inputs are lists of values, it returns a list of speeds for each corresponding
        pair of distance and time values. The lists must be of equal length.\n

        Parameters:\n
        distance (int, float, list of int, or list of float): The distance(s) traveled.
        time (int, float, list of int, or list of float): The time(s) taken.\n

        Returns:\n
        float or list of float: The calculated speed(s).\n

        Raises:\n
        TypeError: If the inputs are not both numbers or both lists of equal length.\n

        Examples:\n
        > speed(100, 2)\n
        50.0\n
        > speed([100, 200], [2, 4])\n
        [50.0, 50.0]\n
        :rtype: f"{dataType}
        """
        if isinstance(_distance, (int, float)) and isinstance(_time, (int, float)):
            return _distance / _time
        if isinstance(_distance, list) and isinstance(_time, list) and len(_distance) == len(_time):
            return [d / t for d, t in zip(_distance, _time)]
        raise TypeError("Inputs must be either both numbers or both lists of equal length")

    @staticmethod
    def time(_distance: dataType, _speed: dataType) -> dataType:
        f"""
        Calculate time given distance and speed.    

        This function handles both single values and lists of values. If both inputs
        are single values (either integers or floats), it returns the time as a single value.
        If both inputs are lists of values, it returns a list of times for each corresponding
        pair of distance and speed values. The lists must be of equal length.

        Parameters:
        distance (int, float, list of int, or list of float): The distance(s) traveled.
        speed (int, float, list of int, or list of float): The speed(s).

        Returns:
        float or list of float: The calculated time(s).

        Raises:
        TypeError: If the inputs are not both numbers or both lists of equal length.

        Examples:
        > time(100, 50)
        2.0
        > time([100, 180], [50, 60])
        [2.0, 3.0]
        """
        if isinstance(_distance, (int, float)) and isinstance(_speed, (int, float)):
            return _distance / _speed
        if isinstance(_distance, list) and isinstance(_speed, list) and len(_distance) == len(_speed):
            return [d / s for d, s in zip(_distance, _speed)]
        raise TypeError("Inputs must be either both numbers or both lists of equal length")

    @staticmethod
    def velocity(_initial_position: dataType, _final_position: dataType, _initial_time: dataType,
                 _final_time: dataType) -> (
            dataType):
        f"""
        Calculate velocity given initial and final positions and times.

        This function handles both single values and lists of values. If all inputs
        are single values (either integers or floats), it returns the velocity as a single value.
        If all inputs are lists of values, it returns a list of velocities for each corresponding
        set of positions and times. The lists must be of equal length.

        Parameters:
        initial_position (int, float, list of int, or list of float): The initial position(s).
        final_position (int, float, list of int, or list of float): The final position(s).
        initial_time (int, float, list of int, or list of float): The initial time(s).
        final_time (int, float, list of int, or list of float): The final time(s).

        Returns:
        float or list of float: The calculated velocity(s).

        Raises:
        ValueError: If the final time equals the initial time for any pair.
        TypeError: If the inputs are not all numbers or all lists of equal length.

        Examples:
        > velocity(0, 100, 0, 2)
        50.0
        > velocity([0, 0], [100, 200], [0, 0], [2, 4])
        [50.0, 50.0]
        """
        if all(isinstance(i, (int, float)) for i in [_initial_position, _final_position, _initial_time, _final_time]):
            if _final_time == _initial_time:
                raise ValueError("Initial and final times cannot be equal")
            return (_final_position - _initial_position) / (_final_time - _initial_time)
        if all(isinstance(i, list) for i in [_initial_position, _final_position, _initial_time, _final_time]):
            if len(_initial_position) != len(_final_position) or len(_initial_time) != len(_final_time) or len(
                    _initial_position) != len(_initial_time):
                raise ValueError("All lists must have the same length")
            if any(ft == it for ft, it in zip(_final_time, _initial_time)):
                raise ValueError("Initial and final times cannot be equal for any pair")
            return [(fp - ip) / (ft - it) for fp, ip, ft, it in
                    zip(_final_position, _initial_position, _final_time, _initial_time)]
        raise TypeError("Inputs must be either all numbers or all lists of equal length")

    @staticmethod
    def displacement(_initial_position: dataType, _final_position: dataType) -> dataType:
        f"""
        Calculate displacement given initial and final positions.

        This function handles both single values and lists of values. If both inputs
        are single values (either integers or floats), it returns the displacement as a single value.
        If both inputs are lists of values, it returns a list of displacements for each corresponding
        pair of initial and final positions. The lists must be of equal length.

        Parameters:
        initial_position (int, float, list of int, or list of float): The initial position(s).
        final_position (int, float, list of int, or list of float): The final position(s).

        Returns:
        float or list of float: The calculated displacement(s).

        Raises:
        TypeError: If the inputs are not both numbers or both lists of equal length.

        Examples:
        > displacement(0, 100)
        100.0
        > displacement([0, 0], [100, 200])
        [100.0, 200.0]
        """
        if isinstance(_initial_position, (int, float)) and isinstance(_final_position, (int, float)):
            return _final_position - _initial_position
        if isinstance(_initial_position, list) and isinstance(_final_position, list) and len(_initial_position) == len(
                _final_position):
            return [fp - ip for fp, ip in zip(_final_position, _initial_position)]
        raise TypeError("Inputs must be either both numbers or both lists of equal length")

    @staticmethod
    def acceleration(_initial_velocity: dataType, _final_velocity: dataType, _initial_time: dataType,
                     _final_time: dataType) -> dataType:
        f"""
        Calculate acceleration given initial and final velocities and times.

        This function handles both single values and lists of values. If all inputs
        are single values (either integers or floats), it returns the acceleration as a single value.
        If all inputs are lists of values, it returns a list of accelerations for each corresponding
        set of velocities and times. The lists must be of equal length.

        Parameters:
        initial_velocity (int, float, list of int, or list of float): The initial velocity(s).
        final_velocity (int, float, list of int, or list of float): The final velocity(s).
        initial_time (int, float, list of int, or list of float): The initial time(s).
        final_time (int, float, list of int, or list of float): The final time(s).

        Returns:
        float or list of float: The calculated acceleration(s).

        Raises:
        ValueError: If the final time equals the initial time for any pair.
        TypeError: If the inputs are not all numbers or all lists of equal length.

        Examples:
        > acceleration(0, 100, 0, 2)
        50.0
        > acceleration([0, 0], [100, 200], [0, 0], [2, 4])
        [50.0, 50.0]
        """
        if all(isinstance(i, (int, float)) for i in [_initial_velocity, _final_velocity, _initial_time, _final_time]):
            if _final_time == _initial_time:
                raise ValueError("Initial and final times cannot be equal")
            return (_final_velocity - _initial_velocity) / (_final_time - _initial_time)
        if all(isinstance(i, list) for i in [_initial_velocity, _final_velocity, _initial_time, _final_time]):
            if len(_initial_velocity) != len(_final_velocity) or len(_initial_time) != len(_final_time) or len(
                    _initial_velocity) != len(_initial_time):
                raise ValueError("All lists must have the same length")
            if any(ft == it for ft, it in zip(_final_time, _initial_time)):
                raise ValueError("Initial and final times cannot be equal for any pair")
            return [(fv - iv) / (ft - it) for fv, iv, ft, it in
                    zip(_final_velocity, _initial_velocity, _final_time, _initial_time)]
        raise TypeError("Inputs must be either all numbers or all lists of equal length")

    @staticmethod
    def first_equation_of_motion(_initial_velocity: dataType, _acceleration: dataType, _time: dataType) -> dataType:
        f"""
        Calculate final velocity using the first equation of motion: v = u + at.

        This function handles both single values and lists of values. If all inputs
        are single values (either integers or floats), it returns the final velocity as a single value.
        If all inputs are lists of values, it returns a list of final velocities for each corresponding
        set of initial velocity, acceleration, and time values. The lists must be of equal length.

        Parameters:
        initial_velocity (int, float, list of int, or list of float): The initial velocity(s) (u).
        acceleration (int, float, list of int, or list of float): The acceleration(s) (a).
        time (int, float, list of int, or list of float): The time(s) (t).

        Returns:
        float or list of float: The calculated final velocity(s) (v).

        Raises:
        TypeError: If the inputs are not all numbers or all lists of equal length.

        Examples:
        > first_equation_of_motion(0, 10, 5)
        50.0
        > first_equation_of_motion([0, 5], [10, 2], [5, 3])
        [50.0, 11.0]
        """
        if all(isinstance(i, (int, float)) for i in [_initial_velocity, _acceleration, _time]):
            return _initial_velocity + _acceleration * _time
        if all(isinstance(i, list) for i in [_initial_velocity, _acceleration, _time]) and len(
                _initial_velocity) == len(
                _acceleration) == len(_time):
            return [u + a * t for u, a, t in zip(_initial_velocity, _acceleration, _time)]
        raise TypeError("Inputs must be either all numbers or all lists of equal length")

    @staticmethod
    def second_equation_of_motion(_initial_velocity: dataType, _acceleration: dataType, _time: dataType) -> dataType:
        f"""
        Calculate displacement using the second equation of motion: s = ut + 0.5at^2.

        This function handles both single values and lists of values. If all inputs
        are single values (either integers or floats), it returns the displacement as a single value.
        If all inputs are lists of values, it returns a list of displacements for each corresponding
        set of initial velocity, acceleration, and time values. The lists must be of equal length.

        Parameters:
        initial_velocity (int, float, list of int, or list of float): The initial velocity(s).
        acceleration (int, float, list of int, or list of float): The acceleration(s).
        time (int, float, list of int, or list of float): The time(s).

        Returns:
        float or list of float: The calculated displacement(s).

        Raises:
        TypeError: If the inputs are not all numbers or all lists of equal length.

        Examples:
        > second_equation_of_motion(0, 10, 5)
        125.0
        > second_equation_of_motion([0, 10], [10, 5], [5, 3])
        [125.0, 67.5]
        """
        if isinstance(_initial_velocity, (int, float)) and isinstance(_acceleration, (int, float)) and isinstance(
                _time, (int, float)):
            return _initial_velocity * _time + 0.5 * _acceleration * _time ** 2
        if isinstance(_initial_velocity, list) and isinstance(_acceleration, list) and isinstance(_time, list) and len(
                _initial_velocity) == len(_acceleration) == len(_time):
            return [u * t + 0.5 * a * t ** 2 for u, a, t in zip(_initial_velocity)]
        raise TypeError("Inputs must be either all numbers or all lists of equal length")

    @staticmethod
    def third_equation_of_motion(_initial_velocity: dataType, _acceleration: dataType,
                                 _displacement: dataType) -> dataType:
        f"""
        Calculate final velocity using the third equation of motion: v^2 = u^2 + 2as.

        This function handles both single values and lists of values. If all inputs 
        are single values (either integers or floats), it returns the final velocity as a single value. 
        If all inputs are lists of values, it returns a list of final velocities for each corresponding 
        set of initial velocities, accelerations, and displacements. The lists must be of equal length.

        Parameters:
        initial_velocity (int, float, list of int, or list of float): The initial velocity(s).
        acceleration (int, float, list of int, or list of float): The acceleration(s).
        displacement (int, float, list of int, or list of float): The displacement(s).

        Returns:
        float or list of float: The calculated final velocity(s).

        Raises:
        TypeError: If the inputs are not all numbers or all lists of equal length.

        Examples:
        > third_equation_of_motion(0, 10, 5)
        10.0
        > third_equation_of_motion([0, 0], [10, 20], [5, 3])
        [10.0, 10.954451150103322]
        """
        if all(isinstance(i, (int, float)) for i in [_initial_velocity, _acceleration, _displacement]):
            return (_initial_velocity ** 2 + 2 * _acceleration * _displacement) ** 0.5
        if all(isinstance(i, list) for i in [_initial_velocity, _acceleration, _displacement]):
            if len(_initial_velocity) != len(_acceleration) or len(_acceleration) != len(_displacement):
                raise TypeError("All lists must have the same length")
            return [(u ** 2 + 2 * a * s) ** 0.5 for u, a, s in zip(_initial_velocity, _acceleration, _displacement)]
        raise TypeError("Inputs must be either all numbers or all lists of equal length")

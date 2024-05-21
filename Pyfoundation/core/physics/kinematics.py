class Kinematics:
    def __init__(self):
        super().__init__()

    @staticmethod
    def speed(_distance, _time):
        """Calculates speed given distance and time. Handles both single values and lists of values."""
        if isinstance(_distance, (int, float)) and isinstance(_time, (int, float)):
            return _distance / _time
        if isinstance(_distance, list) and isinstance(_time, list):
            if len(_distance) != len(_time):
                raise ValueError("Both lists must have the same length")
            if not all(isinstance(d, (int, float)) and isinstance(t, (int, float)) for d, t in zip(_distance, _time)):
                raise ValueError("All elements in both lists must be numbers")
            return [d / t for d, t in zip(_distance, _time)]
        raise TypeError("Inputs must be either both numbers or both lists of numbers")

    @staticmethod
    def distance(_speed, _time):
        """Calculates distance given speed and time. Handles both single values and lists of values."""
        if isinstance(_speed, (int, float)) and isinstance(_time, (int, float)):
            return _speed * _time
        if isinstance(_speed, list) and isinstance(_time, list):
            if len(_speed) != len(_time):
                raise ValueError("Both lists must have the same length")
            if not all(isinstance(s, (int, float)) and isinstance(t, (int, float)) for s, t in zip(_speed, _time)):
                raise ValueError("All elements in both lists must be numbers")
            return [s * t for s, t in zip(_speed, _time)]
        raise TypeError("Inputs must be either both numbers or both lists of numbers")

    @staticmethod
    def time(_distance, _speed):
        """Calculates time given distance and speed. Handles both single values and lists of values."""
        if isinstance(_distance, (int, float)) and isinstance(_speed, (int, float)):
            if _speed == 0:
                raise ValueError("Speed cannot be zero")
            return _distance / _speed
        if isinstance(_distance, list) and isinstance(_speed, list):
            if len(_distance) != len(_speed):
                raise ValueError("Both lists must have the same length")
            if not all(isinstance(d, (int, float)) and isinstance(s, (int, float)) for d, s in zip(_distance, _speed)):
                raise ValueError("All elements in both lists must be numbers")
            if any(s == 0 for s in _speed):
                raise ValueError("Speed cannot be zero")
            return [d / s for d, s in zip(_distance, _speed)]
        raise TypeError("Inputs must be either both numbers or both lists of numbers")

    @staticmethod
    def velocity(_initial_position, _final_position, _initial_time, _final_time):
        """Calculates velocity given initial and final positions and times.
        Handles both single values and lists of values."""
        if isinstance(_initial_position, (int, float)) and isinstance(_final_position, (int, float)) and \
                isinstance(_initial_time, (int, float)) and isinstance(_final_time, (int, float)):
            if _final_time == _initial_time:
                raise ValueError("Initial and final times cannot be equal")
            return (_final_position - _initial_position) / (_final_time - _initial_time)
        if isinstance(_initial_position, list) and isinstance(_final_position, list) and \
                isinstance(_initial_time, list) and isinstance(_final_time, list):
            if len(_initial_position) != len(_final_position) or len(_initial_time) != len(_final_time) or \
                    len(_initial_position) != len(_initial_time):
                raise ValueError("All lists must have the same length")
            if any(f - i == 0 for f, i in zip(_final_time, _initial_time)):
                raise ValueError("Initial and final times cannot be equal for any pair")
            return [(f - i) / (ft - it) for f, i, ft, it in zip(_final_position, _initial_position, _final_time,
                                                                _initial_time)]
        raise TypeError("Inputs must be either both numbers or both lists of numbers")

    @staticmethod
    def displacement():
        pass

    @staticmethod
    def acceleration():
        pass

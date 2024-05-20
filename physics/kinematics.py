class Kinematics:
    @staticmethod
    def speed(distance, time):
        if isinstance(distance and time, int):
            return distance / time
        else:
            if len(distance) != len(time):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(distance)):
                summed_list.append(distance[i] / time[i])
            return summed_list

    @staticmethod
    def distance(speed, time):
        if isinstance(speed and time, int):
            return speed * time
        else:
            if len(speed) != len(time):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(speed)):
                summed_list.append(speed[i] * time[i])
            return summed_list

    @staticmethod
    def time(distance, speed):
        if isinstance(distance and speed, int):
            return distance / speed
        else:
            if len(distance) != len(speed):  # Check if both lists have the same length
                raise ValueError("Both lists must have the same length")
            summed_list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(distance)):
                summed_list.append(distance[i] / speed[i])
            return summed_list

    @staticmethod
    def velocity(initial_position, final_position, initial_time, final_time):
        if isinstance(initial_time and final_time and initial_position and final_position, int):
            return (final_position - initial_position) / (final_time - initial_time)
        else:
            if len(initial_position) != len(final_position) and len(initial_time) != len(final_time) and len(
                    initial_position) != len(initial_time):  # Check if
                # both lists
                # have the same length
                raise ValueError("Both lists must have the same length")
            _list = []  # Create a new list to store the sum
            # Iterate through both lists and add corresponding elements
            for i in range(len(initial_position)):
                _list.append((final_position[i] - initial_position[i]) / (final_time[i] - initial_time[i]))
            return _list

    @staticmethod
    def displacement():
        pass

    @staticmethod
    def acceleration():
        pass

import unittest
from Pyfoundation.core.physics.kinematics import Kinematics


class TestAlgebra(unittest.TestCase):
    def test_speed(self):
        self.assertEqual(Kinematics.speed(4, 2), 2)
        self.assertEqual(Kinematics.speed([4], [2]), [2])
        self.assertEqual(Kinematics.speed([2, 4, 6, 8, 10], [1, 2, 3, 4, 5]), [2, 2, 2, 2, 2])
        self.assertEqual(Kinematics.speed(4.4, 2.2), 2.0)
        self.assertEqual(Kinematics.speed([4.4], [2.2]), [2.0])
        self.assertEqual(Kinematics.speed([2.4, 4.2, 6.4, 8.8, 10.0], [1.2, 2.1, 3.2, 4.4, 5.0]),
                         [2.0, 2.0, 2.0, 2.0, 2.0])


if __name__ == '__main__':
    unittest.main()

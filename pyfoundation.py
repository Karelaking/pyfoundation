from Pyfoundation.core.physics.kinematics import Kinematics
from Pyfoundation.core.mathematics.algebra import Algebra
from Pyfoundation.core.mathematics.trigonometry import Trigonometry


class Pyfoundation(Kinematics, Algebra, Trigonometry):
    def __init__(self):
        super().__init__()

        self.e = 2.718281828459045
        self.pi = 3.141592653589793
        self.tau = 6.283185307179586


value = Pyfoundation
print(value.summation())

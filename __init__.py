"""
This Library Contains Various Types Of Mathematics, Physics And Chemistry Formulas.
"""
from mathematics.calculus import Integration
from mathematics import algebra
from mathematics.trigonometry import Trigonometry
from physics.kinematics import Kinematics

__name__ = "pyfoundation"
__author__ = "White Angel"


class Pyfoundation(Trigonometry, Integration, Kinematics):
    def __init__(self):
        super().__init__()

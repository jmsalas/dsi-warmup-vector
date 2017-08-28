import unittest
from linalg import Vector


class linalg_test(unittest.TestCase):
    # def __init__(self):
    #     self.v1 = Vector([1, 2, 3])
    #     self.v2 = Vector([2, 3, 4])
    # this doesn't work because we already have an init built-in with TestCase

    def setUp(self):
        self.v1 = Vector([1, 2, 3])
        self.v2 = Vector([2, 3, 4])
        self.v3 = Vector([2, 3, 6])
        self.v4 = Vector([1, 1, 4])

    def test_start(self):
        self.assertEqual(1 + 1, 2)

# TODO add equality test

    def test_add(self):
        expected_output = [3, 5, 7]
        self.assertEqual(self.v1.add(self.v2), Vector(expected_output), 'Addition did not give expected value')

    def test_add_magic(self):
        self.assertEqual(self.v1 + self.v2, self.v1.add(self.v2), 'Magic method and other did not give the same answer')

    def test_subtract(self):
        '''
        Subtract v2 from v1
        '''
        expected_output = Vector([1, 1, 1])
        self.assertEqual(self.v2.subtract(self.v1), expected_output, 'Subtract does not work')

    def test_subtract_magic(self):
        self.assertEqual(self.v2 - self.v1, self.v2.subtract(self.v1), 'Subtract magic fails')

    def test_scalar_multiply(self):
        expected_output = Vector([3, 6, 9])
        scalar = 3
        self.assertEqual(self.v1.scalar_multiply(scalar), expected_output, 'Scalar multiplication gave incorrect answer')

    def test_magnitude(self):
        '''
        Use vector3 for convenience of pythagorean quadruple
        '''
        expected_output = 6.855654600401044
        self.assertEqual(self.v3.magnitude(), expected_output, 'magnitude does not work')

    def test_dot(self):
        expected_output = 20
        self.assertEqual(self.v1.dot(self.v2), expected_output, 'Dot product gives invalid answer')

    def test_dot_magic(self):
        self.assertEqual(self.v1.dot(self.v2), self.v2 * self.v1, 'Dot product magic fails')

    def test_scalar_multiply_magic(self):
        expected_output = Vector([3, 6, 9])
        scalar = 3
        self.assertEqual(self.v1 * scalar, expected_output, 'Scalar multiplication gave incorrect answer')

    def test_distance(self):
        '''
        subtract v4 from v3 for convenient integer output
        '''
        expected_output = 3
        self.assertEqual(self.v3.distance(self.v4), expected_output)

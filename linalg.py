from functools import reduce


class Vector():

    values = [0]

    def __init__(self, values):

        if not isinstance(values, list):
            raise('Vector class only supports objects of type "list".')

        self.values = values

    def dimension(self):
        return len(self.values)

    def add(self, other):
        if self.dimension() != other.dimension():
            raise('Both vectors need to have the same dimensions.')

        return Vector([self.values[i] + other.values[i] for i in range(self.dimension())])

    def subtract(self, other):
        if self.dimension() != other.dimension():
            raise('Both vectors need to have the same dimensions.')

        return Vector([self.values[i] - other.values[i] for i in range(self.dimension())])

    def scalar_multiply(self, other):
        return Vector([self.values[i] * other for i in range(self.dimension())])

    def dot(self, other):
        if self.dimension() != other.dimension():
            raise('Both vectors need to have the same dimensions.')

        return sum([self.values[i] * other.values[i] for i in range(self.dimension())])

    def magnitude(self):
        res = reduce(lambda x, y: x+y**2, self.values)
        return res**0.5

    def distance(self, other):
        sub = self - other
        return sub.magnitude()

    def is_equal(self, other):
        return all([x == y for x, y in zip(self.values, other.values)])

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.scalar_multiply(other)

    def __eq__(self, other):
        return self.is_equal(other)

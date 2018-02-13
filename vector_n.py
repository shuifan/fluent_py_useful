from array import array
import math
import numbers
import operator
import functools

class Vector:

    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            raise TypeError('TypeError input is not a number or slice')

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a,b in zip(self, other))

    def __hash__(self):
        return functools.reduce(operator.xor, self._components, 0)


if __name__ == '__main__':
    # v = Vector(range(7))
    # print(list(v))
    v = Vector([i for i in range(5)])
    print(len(v))
import math
from array import array


class Vector2d:
    type_code = 'd'

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __repr__(self):
        cls_name = type(self).__name__
        return '{}({!r}, {!r})'.format(cls_name, *self)

    def __bytes__(self):
        return bytes([ord(self.type_code)]) + bytes(array(self.type_code, self))

    def __format__(self, format_spec=''):
        args = (format(a, format_spec) for a in self)
        return '({}, {})'.format(*args)

    def __abs__(self):
        return math.hypot(self.x, self.y)


if __name__ == '__main__':
    v1 = Vector2d(2, 3)
    # print(v1.x, v1.y)
    # x, y = v1
    # print(x, y)
    # print(v1)
    # print(repr(v1))
    # v1_bytes = bytes(v1)
    # print(v1_bytes)
    # v2 = Vector2d.frombytes(v1_bytes)
    # print(v2)
    print(format(v1))
    print(format(v1, '.2f'))

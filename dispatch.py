import functools
import numbers
from collections import abc


@functools.singledispatch
def htmlize(obj):
    return 'obj -> {obj}'.format(obj = obj)


@htmlize.register(str)
def _(text):
    return 'str -> {text}'.format(text = text)


@htmlize.register(numbers.Integral)
def _(n):
    return 'Integral -> {n} {n:x}'.format(n = n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    return 'Seq -> ' + ','.join(seq)

def some_function(a):
    return a

if __name__ == '__main__':
    print(htmlize(1))
    print(htmlize('1'))
    print(htmlize(['1','2','3']))
    print(htmlize(some_function))
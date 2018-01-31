from clock import clock
import time
import functools
import types
import tkinter
import tensorflow

i = 0


def counter(func):

    def the_counter(*args):
        global i
        i += 1
        return func(*args)

    return the_counter


@clock
def my(seconds):
    time.sleep(seconds)


@functools.lru_cache()
# @clock
# @counter
def febonaqie(n):
    print('n -> %d' % n)
    if n < 2:
        return n
    return febonaqie(n - 2) + febonaqie(n - 1)


if __name__ == '__main__':
    # t0 = time.time()
    # time.sleep(2)
    # t1 = time.time()
    # print(t1 - t0)
    # print(febonaqie(30))
    # print(i)
    # t = type(counter)
    # print(isinstance(counter, types.FunctionType))
    # print(str(t))
    # print('function' in str(t))
    # print(list.__mro__)
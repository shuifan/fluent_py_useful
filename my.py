from clock import clock
import time
import functools

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
@counter
def febonaqie(n):
    if n < 2:
        return n
    return febonaqie(n - 2) + febonaqie(n - 1)

class test():
    def __init__(self, value):
        self.x = value

    def __call__(self, value):
        return self.x * value

if __name__ == '__main__':
    # t0 = time.time()
    # time.sleep(2)
    # t1 = time.time()
    # print(t1 - t0)
    # print(febonaqie(30))
    # print(i)
    a = test(4)
    print(a(4))

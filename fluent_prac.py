# coding: utf-8

if __name__ == '__main__':
    # a = [1,2,3,4]
    # b = ['a']
    # # print(2 * a)
    # print(a[1::2])
    # board = [['_']*3 for i in range(3)]
    # print(board)
    # board[1][2] = 'X'
    # print(board)
    #
    # board = ['_']*3
    # board[2] = 'X'
    # print(board)
    #
    # # 列表中 引用复制3份
    # board = [['_']*3] * 3
    # board[1][2] = 'X'
    # print(board)
    #
    # a = '3'
    # a *= 3
    # print(a)

    # a = (1,2,[3,4])
    # try:
    #     a[2] += [5]
    # except TypeError:
    #     print(a)

    # s = '{0:<2d}{1:>2d}'
    # print(s.format(1,2))

    # HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    # import bisect
    # print(bisect.bisect(HAYSTACK, 2))

    # import bisect
    # import random
    #
    # random.seed(1772)
    # range_size = 7
    # bisect_list = []
    # for i in range(7):
    #     new_item = random.randrange(range_size * 2)
    #     bisect.insort(bisect_list, new_item)
    #     print('{0:<2d} -> {1}'.format(new_item, bisect_list))

    # print(10 ** 2)

    from array import array
    from random import random
    import timeit


    # old_array = array('d', (random() for i in range(10 ** 7)))
    # print(old_array[-1])
    # old_file = open('oldArray.bin', 'wb')
    # old_array.tofile(old_file)
    # new_array = array('d')
    # new_file = open('oldArray.bin', 'rb')
    # new_array.fromfile(new_file, 10 ** 7)
    # print(new_array[-1])
    # def use_array():
    #     array('d', (random() for i in range(10 ** 7)))
    # def use_list():
    #     a = [random() for i in range(10 ** 7)]
    # def read_bin():
    #     new_array = array('d')
    #     new_file = open('oldArray.bin', 'rb')
    #     new_array.fromfile(new_file, 10 ** 7)
    # print(timeit.timeit('use_array()', globals= globals(), number=1))
    # print(timeit.timeit('use_list()', globals= globals(), number=1))
    # print(timeit.timeit('read_bin()', globals= globals(), number=1))
    # mybuf = [1,2,34]
    # mybuf[2:3] = [100]
    # print(mybuf)

    # from collections import ChainMap
    # import builtins
    # pylookup = ChainMap(locals(), globals(), vars(builtins))
    # print(pylookup)

    # a = {1:1, 2:2, 3:3}
    # print(a.items())
    # print(1 in a)
    # from collections import UserDict

    # from dis import dis
    # print(dis('{1}'))
    # print(dis('set([1])'))

    # from unicodedata import name
    # a = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
    # print(a)
    #
    # print(bool(''))
    # print(name(chr(234)))

    # print(hash(1))
    # print(id('a'))
    # print(id('a'))
    # print(id(2))
    # print(hash('b'))

    # from collections import namedtuple
    # import sys
    # A = namedtuple('A', ['a', 'b'])
    # b= A(1,2)
    # c = tuple(b)
    # print(sys.getsizeof(b))
    # print(sys.getsizeof(c))
    # len()
    # chr()
    # print(ord(b'c'))

    # import locale
    # print(locale.getpreferredencoding(do_setlocale=True))

    # from unicodedata import normalize
    # s = 'cafe\u0301'
    # s1 = normalize('NFC', s)
    # print(s)
    # print(s1)

    # def fac():
    #     """this is a doc"""
    #     return 1
    #
    # print(type(fac))
    # print(help(fac))

    # a,b = [1,2]
    # c,d = (3,4)

    # def test_yield():
    #     for i in range(10):
    #         yield i
    #     for j in range(20, 30):
    #         yield j
    # def counter(maximum):
    #     i = 0
    #     while i < maximum:
    #         val = (yield i)
    #         # If value provided, change counter
    #         if val is not None:
    #             i = val
    #         else:
    #             i += 1
    # test = counter(8)
    # for i in range(4):
    #     next(test)
    # # 将 send 的 值 赋予 yield表达式
    # # 会继续执行到 下一次出现yield表达式的地方 返回相应的值
    # # 正常情况下 a = (yield i) a 的值 为 none
    # print(test.send(6))
    # print(next(test))

    # import itertools
    # import os

    # print(itertools.tee(itertools.count(), 3))
    #
    # a =itertools.starmap(os.path.join,
    #                   [('bin', 'python'), ('usr', 'bin', 'java'),
    #                    ('usr', 'bin', 'perl'), ('usr', 'bin', 'ruby')])
    # print(list(a))

    # city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
    #          ('Anchorage', 'AK'), ('Nome', 'AK'),
    #          ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')]
    #
    # def get_type(city_state):
    #     return city_state[1]
    #
    # a = itertools.groupby(city_list, key=get_type)
    # print(list(a))

    # import functools
    #
    # def log(msg, subsystem):
    #     print("%s, %s" % (subsystem, msg))
    #
    # server_log = functools.partial(log, subsystem = 'server')
    #
    # server_log('The network is offline.')\

    # import random
    #
    #
    # class Bingo:
    #
    #     def __init__(self, items):
    #         self._items = list(items)
    #         random.shuffle(self._items)
    #
    #     def pick(self):
    #         try:
    #             return self._items.pop()
    #         except IndexError:
    #             # raise LookupError('the list is empty')
    #             pass
    #
    #     def __call__(self, *args, **kwargs):
    #         return self.pick()
    #
    #
    # bingo = Bingo(range(3))
    # print(bingo.pick())
    # print(bingo())
    # print(bingo())
    # print(bingo())

    # def f(a, *, b):
    #     return a, b
    #
    #
    # print(f(1, b=2))



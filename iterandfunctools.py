import itertools
import operator

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

if __name__ == '__main__':
    print(list(itertools.accumulate(sample)))
    print(list(itertools.accumulate(sample, min)))
    print(list(itertools.accumulate(sample, max)))
    print(list(itertools.accumulate(sample, operator.mul)))
    print(list(itertools.accumulate(range(1,11), operator.mul)))

    print(list(enumerate('albatroz', 1)))
    print(list(map(operator.mul, range(11), range(11))))
    print(list(map(operator.mul, range(11), range(3))))
    print(list(map(lambda a,b : (a,b), range(11), range(3))))
    print(list(itertools.starmap(operator.mul, enumerate('abcdef', 1))))

    # 计算平均值
    print(list(itertools.starmap(lambda a,b:'{:.2f}'.format(b/a), enumerate(itertools.accumulate(sample), 1))))

    print(list(itertools.chain('abc', range(10))))
    print(list(itertools.chain(enumerate('abc'))))
    print(list(enumerate(enumerate('abc'))))
    print(list(itertools.chain.from_iterable(enumerate(enumerate('abc')))))
    print(list(zip('abc', range(10))))
    print(list(zip('abc', range(10), 'def')))
    print(list(itertools.zip_longest('abc', range(10))))
    print(list(itertools.zip_longest('abc', range(10), fillvalue = '*')))

    #计算笛卡儿积
    print(list(itertools.product('abc', range(4))))
    print(list(itertools.product('abc', repeat=3)))

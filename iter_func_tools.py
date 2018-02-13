import itertools
from random import randint


def d6():
    return randint(1,6)



if __name__ == '__main__':
    # ct = itertools.count()
    # print(next(ct))
    # print(list(itertools.islice(ct, 7)))
    # cy = itertools.cycle('abc')
    # print(list(itertools.islice(cy, 7)))
    #
    # print(list(itertools.groupby('aabbnnvvhhh')))
    # for k,v in itertools.groupby('aabbnnvvhhh'):
    #     print(k , '->' , list(v))
    #
    # animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
    # animals.sort(key=len)
    # for k,v in itertools.groupby(animals, key=len):
    #     print(k , '->' , list(v))
    #
    # print(list(reversed(animals)))
    #
    # print(list(itertools.tee('abc', 2)))
    # d6_iter = iter(d6, 1)
    # for roll in d6_iter:
    #     print(roll)
    # with open('a.txt') as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)

    e = enumerate('abc')
    print(e)
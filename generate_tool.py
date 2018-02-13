import itertools


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    ap_gen = itertools.count(begin, step)
    if end is not None:
        return itertools.takewhile(lambda x : x < end, ap_gen)
    return ap_gen

def vowel(c):
    return c.lower() in 'aeiou'

if __name__ == '__main__':
    # print(list(filter(vowel, 'Aaabbc')))
    # print(list(itertools.filterfalse(vowel, 'Aaabbc')))
    print(list(itertools.dropwhile(vowel, 'bardvaark')))
    print(list(itertools.takewhile(vowel, 'Aabardvaark')))
    print('a'.lower() in 'aeiou')

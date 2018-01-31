import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

if __name__ == '__main__':
    s = Sentence('I am sorry. But, I tried my best!')
    print(repr(s))
    print(list(s))
    it = iter(s)
    print(repr(it))

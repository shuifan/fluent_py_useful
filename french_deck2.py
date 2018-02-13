import collections
import random


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(collections.MutableSequence):

    rank = [i for i in range(2,11)] + list('AJQK')
    suit = 'fang mei hei hong'.split()

    def __init__(self):
        self._cards = [Card(i, j) for i in self.rank
                       for j in self.suit]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    cards = FrenchDeck()

    def set_card(self, position, card):
        self._cards[position] = card

    FrenchDeck.__setitem__ = set_card
    random.shuffle(cards)
    print(list(cards))
    


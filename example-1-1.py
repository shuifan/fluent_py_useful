import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'meihua fangkuai heitao hongtao'.split(' ')

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]
suit_rank = dict(meihua = 1, fangkuai = 2, heitao = 3, hongtao = 4)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * 10 + suit_rank.get(card.suit)

if __name__ == '__main__':
    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[3])
    # print(deck[:3])
    # print(deck[12::13])
    # for card in deck:
    #     print(card)
    # print(spades_high(deck[0]))
    # print(FrenchDeck.ranks.index(deck[1].rank))
    # for card in sorted(deck, key = spades_high):
    #     print(card)
    # for card in reversed(sorted(deck, key = spades_high)):
    #     print(card)
    print(str.format('{a}{b}', a = 2, b = 3))
    print(bool(1))


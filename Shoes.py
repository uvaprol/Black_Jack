from random import shuffle, randint


class Shoes:
    CARDS = [[p, w] for w in range(2, 15) for p in '♠♣♥♦']  # range(4)
    deck_count: int
    deck: list

    def __init__(self, n: int = 1) -> None:
        self.deck_count = n
        self.deck = self.CARDS * self.deck_count
        return

    def deck_shuffle(self) -> None:
        shuffle(self.deck)
        return

    def get_card(self) -> list:
        return self.deck.pop()

    def check_shuffler(self):
        return True if (randint(0, 52 * self.deck_count) > (len(self.deck) + 10 * (self.deck_count + 1))) \
                       or (len(self.deck) < 10 * (self.deck_count + 1)) else False


# a = Shoes()
# while not a.check_shuffler():
#     print(a.get_card())
# print(len(a.deck))
# print(a.deck)
# a.deck_shuffle()
# print(a.get_card())
# print(a.deck)
# print(a.get_card())
# print(a.deck)

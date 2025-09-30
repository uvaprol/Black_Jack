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


class Dealer(Shoes):
    dealer_score: int = 0
    dealer_hand: list = []
    player_score: int = 0
    player_hand: list = []
    player_split: list = []
    player_bet: int = 0

    def bet(self, n=100):
        self.player_bet += n
        return

    def play(self):
        if self.player_bet == 0:
            return print('Bet is 0')
        else:
            self.deck_shuffle()
            return self.deal()

    def deal(self):
        for i in range(2):
            self.dealer_take()
            self.take_card()
        print('dealer:', self.dealer_hand[0], ['', ''])

    def take_card(self):
        card = self.get_card()
        self.player_hand.append(card)
        self.player_score += (card[1] if card[1] < 12 else 10)
        print('player:', self.player_hand)
        print('player:', self.player_score)

    def dealer_take(self):
        card = self.get_card()
        self.dealer_hand.append(card)
        self.dealer_score += (card[1] if card[1] < 12 else 10)

    def hold(self):
        while self.dealer_score < self.player_score and self.dealer_score < 16:
            self.dealer_take()
            print('dealer:', self.dealer_hand)
        #TODO прописать винкондишен
        print(self.dealer_score, self.player_score, self.check_shuffler())

    def player_step(self):
        commands = {
            'bet': self.bet,
            'play': self.play,
            'take': self.take_card,
            'hold': self.hold,
            'exit': exit
        }
        while True:
            step = input(': ')
            try:
                commands[step]()
            except:
                pass


a = Dealer()
a.player_step()

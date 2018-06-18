#Blackjack game

import random

class Card(object):
    def __init__(self,suit,val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val,self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def show(self):
        for card in self.cards:
           print(card.show())

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, 1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


deck = Deck()
deck.shuffle()
deck.show()

bob = Player("Bob")
bob.draw(deck).draw(deck)
bob.showHand()
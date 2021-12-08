import random
from card import Card


class Deck:
    def __init__(self):
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        cards = []
        for value in Card.VALUE_NAMES.values():
            for suit in Card.SUIT_SYMBOLS.values():
                card = Card(value, suit)
                cards.append(card)

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal(self, num_cards):
        pass

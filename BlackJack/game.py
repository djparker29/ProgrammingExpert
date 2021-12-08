from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        while True:
            start_game = input(f"You are starting with ${self.player.balance}.  Would you like to play a hand? (y/n)")
            if start_game.lower() not in ['y', 'yes']:
                print("Ending game. Goodbye!")
                break

            bet = self.place_bet()

            self.player.balance += bet
            print(f"The dealer busts.  You win ${bet}!")
            print()

    def place_bet(self):
        while True:
            bet = int(input("Place your bet: $"))

            if bet < 0:
                print(f"The minimum bet is ${Game.MINIMUM_BET}")
            elif bet > self.player.balance:
                print(f"You do not have sufficient funds.")
            else:
                break

        return bet

            
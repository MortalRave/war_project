import random

class Table:

    def __init__(self,deck_of_cards):
        self.deck_of_cards = deck_of_cards

    def shuffle_deck(self):
        random.shuffle(self.deck_of_cards)

    def deal_the_cards(self,player1,player2):
        n = 0
        while n < len(self.deck_of_cards):
            for i in range (len(self.deck_of_cards)):
                if n % 2 != 0:
                    player1.append(self.deck_of_cards[i])
                else:
                    player2.append(self.deck_of_cards[i])
                n+=1
        return player1,player2
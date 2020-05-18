import random

class Deck():

    def __init__(self, n_decks=1):
        self.card_list = [num + suit
            for suit in '\u2665\u2666\u2663\u2660'
            for num in 'A23456789TJQK'
            for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)
    
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card
    
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


dk = Deck(6)
for i in range(5):
    print(dk.deal(), end='  ')

# ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
#     'J', 'Q', 'K', 'A']
# suits = ['clubs', 'diamonds', 'hearts', 'spades']
# my_deck = Deck(52)

# Deal twelve poker hands, so user can compare before
# and after shuffling
# for i in range(12):
#     for i in range(5):
#         d = my_deck.deal()
#         r = d % 13
#         s = d // 13
#         print(ranks[r], 'of', suits[s])
#     print()

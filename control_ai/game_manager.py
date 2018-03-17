import random

import pandas as pd


class GameManager(object):
    def __init__(self):
        self.deck = pd.read_csv('./data/control_deck.csv')

    def get_random_index_of_deck(self):
        return random.randint(0, len(self.deck.query("location == 'deck'").index))

    def draw_five_cards_for_player(self, player='one'):
        self.deck.iloc[self.get_random_index_of_deck(), 3] = 'player_' + str(player)
        self.deck.iloc[self.get_random_index_of_deck(), 3] = 'player_' + str(player)
        self.deck.iloc[self.get_random_index_of_deck(), 3] = 'player_' + str(player)
        self.deck.iloc[self.get_random_index_of_deck(), 3] = 'player_' + str(player)
        self.deck.iloc[self.get_random_index_of_deck(), 3] = 'player_' + str(player)

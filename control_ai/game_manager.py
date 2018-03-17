import random

import pandas as pd
import control_ai.possible_moves

class GameManager(object):
    def __init__(self):
        self.deck = pd.read_csv('./data/control_deck.csv')

    def get_random_index_of_deck(self, max_index):
        return random.randint(0, max_index - 1)

    def draw_starting_hand(self, player='one'):
        for x in range(0, 5):
            self.draw_card_for_player(player)

    def draw_card_for_player(self, player='one'):
        cards_in_deck_location = self.deck.index[self.deck['location'] == 'deck'].tolist()
        card_to_draw_index = self.get_random_index_of_deck(len(cards_in_deck_location))
        self.deck.at[cards_in_deck_location[card_to_draw_index], 'location'] = str(player)

    def card_could_be_drawn(self):
        return len(self.deck.query("location == 'deck'").index) > 0

    def possible_moves_for_player(self, player):
        if self.card_could_be_drawn() == False:
            return []
        return [control_ai.possible_moves.PossibleMoves(player)]
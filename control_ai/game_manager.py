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

    def player_has_max_hand_size(self, player):
        return len(self.deck.query("location == '{}'".format(player)).index) > 6

    def add_right_number_of_draw_moves(self, player):
        if self.card_could_be_drawn() == False or self.player_has_max_hand_size(player):
            return []
        return [control_ai.possible_moves.PossibleMoves(player)]

    def add_install(self, player, card_name, possible_moves_array):
        return possible_moves_array.append(control_ai.possible_moves.PossibleMoves(player, 'install', card_name))

    def possible_moves_for_player(self, player):
        possible_moves_array_to_return = self.add_right_number_of_draw_moves(player)
        cards_player_has = self.deck.query("location == '{}'".format(player))
        for idx, card in cards_player_has.iterrows():
            self.add_install(player, card.loc['name'], possible_moves_array_to_return)
        return possible_moves_array_to_return

    def do_move(self, possible_move):
        if possible_move.game_state.action == 'draw':
            self.draw_card_for_player(possible_move.game_state.player)
        else:
            rows_with_correct_name = self.deck['name'] == possible_move.game_state.card_name
            rows_with_correct_location = self.deck['location'] == possible_move.game_state.player
            matching_rows = rows_with_correct_name & rows_with_correct_location
            self.deck.loc[matching_rows[matching_rows == True].index[0], 'location'] = possible_move.game_state.player + '_install'

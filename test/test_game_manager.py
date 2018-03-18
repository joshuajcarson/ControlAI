import random
import unittest
import unittest.mock

import control_ai.game_manager
import control_ai.possible_moves


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.class_under_test = control_ai.game_manager.GameManager()

    def test_game_manager_deck_is_52_cards(self):
        self.assertEqual(52, len(self.class_under_test.deck.index))

    def test_game_manager_deck_is_all_located_in_deck_on_creation(self):
        self.assertEqual(52, len(self.class_under_test.deck.query("location == 'deck'")))

    def test_game_manager_draw_starting_hand_calls_draw_card_five_times(self):
        player = 'one'
        self.class_under_test.draw_card_for_player = unittest.mock.MagicMock()
        self.class_under_test.draw_starting_hand(player)
        self.assertEqual(5, self.class_under_test.draw_card_for_player.call_count)

    def test_game_manager_draw_starting_hand_calls_draw_card_with_same_arguments(self):
        player = 'two'
        self.class_under_test.draw_card_for_player = unittest.mock.MagicMock()
        self.class_under_test.draw_starting_hand(player)
        self.class_under_test.draw_card_for_player.assert_called_with(player)

    def test_draw_card_for_player_one_draws_a_card_from_deck(self):
        self.class_under_test.get_random_index_of_deck = unittest.mock.MagicMock()
        self.class_under_test.get_random_index_of_deck.return_value = 1
        self.class_under_test.draw_card_for_player('one')
        self.assertEqual(1, len(self.class_under_test.deck.query("location == 'one'")))
        self.assertEqual(51, len(self.class_under_test.deck.query("location == 'deck'")))
        self.assertEqual(1, self.class_under_test.get_random_index_of_deck.call_count)

    def test_card_could_be_drawn_returns_true_if_any_card_still_in_deck(self):
        self.assertEqual(True, self.class_under_test.card_could_be_drawn())

    def test_card_could_be_drawn_returns_false_if_no_card_still_in_deck(self):
        for x in range(0, 52):
            self.class_under_test.draw_card_for_player('one')
        self.assertEqual(False, self.class_under_test.card_could_be_drawn())

    def test_possible_moves_for_player_contain_draw_if_cards_in_deck(self):
        array_of_possible_moves = self.class_under_test.possible_moves_for_player('one')
        contains_draw = False
        for possible_moves in array_of_possible_moves:
            if possible_moves.game_state.action == 'draw' and possible_moves.game_state.player == 'one':
                contains_draw = True
                break
        self.assertEqual(True, contains_draw)

    def test_possible_moves_for_player_contain_draw_for_right_player(self):
        player = 'complicated_and_long_player_id'
        array_of_possible_moves = self.class_under_test.possible_moves_for_player(player)
        contains_draw = False
        for possible_moves in array_of_possible_moves:
            if possible_moves.game_state.action == 'draw' and possible_moves.game_state.player == player:
                contains_draw = True
                break
        self.assertEqual(True, contains_draw)

    def test_possible_moves_for_player_does_not_contain_draw_if_no_cards_in_deck_location(self):
        self.class_under_test.deck.loc[:, 'location'] = 'discard'
        array_of_possible_moves = self.class_under_test.possible_moves_for_player('one')
        contains_draw = False
        for possible_moves in array_of_possible_moves:
            if possible_moves.game_state.action == 'draw':
                contains_draw = True
                break
        self.assertEqual(False, contains_draw)

    def test_possible_moves_for_player_does_not_contain_draw_if_player_has_seven_cards_in_hand(self):
        player = 'one'
        self.class_under_test.deck.loc[0:6, 'location'] = player
        array_of_possible_moves = self.class_under_test.possible_moves_for_player(player)
        contains_draw = False
        for possible_moves in array_of_possible_moves:
            if possible_moves.game_state.action == 'draw':
                contains_draw = True
                break
        self.assertEqual(False, contains_draw)

    def test_do_move_will_take_possible_move_draw_and_add_card_to_player_hand(self):
        player = 'one'
        draw_move = control_ai.possible_moves.PossibleMoves(player)
        draw_move.game_state.action = 'draw'
        location_query = "location == '{}'".format(player)

        self.class_under_test.do_move(draw_move)

        self.assertEqual(1, len(self.class_under_test.deck.query(location_query)))

    def test_do_move_will_take_possible_move_draw_and_remove_card_from_deck(self):
        player = 'one'
        draw_move = control_ai.possible_moves.PossibleMoves(player)
        draw_move.game_state.action = 'draw'
        location_query = "location == '{}'".format('deck')

        self.class_under_test.do_move(draw_move)

        self.assertEqual(51, len(self.class_under_test.deck.query(location_query)))

    def test_possible_moves_for_player_contain_install_if_player_has_any_card_in_hand(self):
        player = 'one'
        self.class_under_test.deck.loc[random.randint(0,51), 'location'] = player
        array_of_possible_moves = self.class_under_test.possible_moves_for_player(player)
        contains_install = False
        for possible_moves in array_of_possible_moves:
            if possible_moves.game_state.action == 'install':
                contains_install = True
                break
        self.assertEqual(True, contains_install)

    def test_possible_moves_for_player_contain_install_for_particular_cards_player_has(self):
        player = 'one'

        first_card = 1
        self.class_under_test.deck.loc[first_card, 'location'] = player
        first_card_name = self.class_under_test.deck.at[first_card, 'name']

        second_card = 10
        self.class_under_test.deck.loc[second_card, 'location'] = player
        second_card_name = self.class_under_test.deck.at[second_card, 'name']

        array_of_possible_moves = self.class_under_test.possible_moves_for_player(player)

        contains_install_for_first_card = False
        for possible_moves in array_of_possible_moves:
            if possible_moves.game_state.action == 'install' and possible_moves.game_state.card_name == first_card_name:
                contains_install_for_first_card = True
                break
        self.assertEqual(True, contains_install_for_first_card)

        contains_install_for_second_card = False
        for possible_moves in array_of_possible_moves:
            if possible_moves.game_state.action == 'install' and possible_moves.game_state.card_name == second_card_name:
                contains_install_for_second_card = True
                break
        self.assertEqual(True, contains_install_for_second_card)

    def test_do_move_for_install_will_put_card_from_player_hand_to_player_install(self):
        player = 'one'
        card_first_index = 8
        self.class_under_test.deck.loc[card_first_index:card_first_index+3, 'location'] = player
        cards_in_hand = self.class_under_test.deck.query("location == '{}'".format(str(player)))
        self.assertEqual(4, len(cards_in_hand.index))
        card_name = self.class_under_test.deck.loc[card_first_index, 'name']
        install_move = control_ai.possible_moves.PossibleMoves(player, 'install', card_name)

        self.class_under_test.do_move(install_move)

        cards_installed = self.class_under_test.deck.query("location == '{}'".format(str(player) + '_install'))
        self.assertEqual(1, len(cards_installed.index))
        cards_in_hand = self.class_under_test.deck.query("location == '{}'".format(str(player)))
        self.assertEqual(3, len(cards_in_hand.index))

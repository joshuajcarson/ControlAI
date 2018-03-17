import unittest
import unittest.mock

import control_ai.game_manager


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
        self.assertEqual(1, len(self.class_under_test.deck.query("location == 'player_one'")))
        self.assertEqual(51, len(self.class_under_test.deck.query("location == 'deck'")))
        self.assertEqual(1, self.class_under_test.get_random_index_of_deck.call_count)

    def test_card_could_be_drawn_returns_true_if_any_card_still_in_deck(self):
        self.assertEqual(True, self.class_under_test.card_could_be_drawn())

    def test_card_could_be_drawn_returns_false_if_no_card_still_in_deck(self):
        for x in range(0, 52):
            self.class_under_test.draw_card_for_player('one')
        self.assertEqual(False, self.class_under_test.card_could_be_drawn())

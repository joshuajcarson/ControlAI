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

    def test_game_manager_deck_has_four_rift_cards(self):
        cards = self.class_under_test.deck.query("name == 'rift'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 1")))
        self.assertEqual(4, len(cards.query("type == 'silver'")))

    def test_game_manager_deck_has_four_exotic_matter_cards(self):
        cards = self.class_under_test.deck.query("name == 'exotic_matter'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 2")))
        self.assertEqual(4, len(cards.query("type == 'silver'")))

    def test_game_manager_deck_has_four_deflector_cards(self):
        cards = self.class_under_test.deck.query("name == 'deflector'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 3")))
        self.assertEqual(4, len(cards.query("type == 'silver'")))

    def test_game_manager_deck_has_four_wormhole_cards(self):
        cards = self.class_under_test.deck.query("name == 'wormhole'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 4")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_anomaly_cards(self):
        cards = self.class_under_test.deck.query("name == 'anomaly'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 4")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_rewind_cards(self):
        cards = self.class_under_test.deck.query("name == 'rewind'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 5")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_reactor_cards(self):
        cards = self.class_under_test.deck.query("name == 'reactor'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 5")))
        self.assertEqual(4, len(cards.query("type == 'silver'")))

    def test_game_manager_deck_has_four_dark_energy_cards(self):
        cards = self.class_under_test.deck.query("name == 'dark_energy'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 6")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_future_shift_cards(self):
        cards = self.class_under_test.deck.query("name == 'future_shift'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 6")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_singularity_cards(self):
        cards = self.class_under_test.deck.query("name == 'singularity'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 7")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_antimatter_cards(self):
        cards = self.class_under_test.deck.query("name == 'antimatter'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 8")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_time_stop_cards(self):
        cards = self.class_under_test.deck.query("name == 'time_stop'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 9")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

    def test_game_manager_deck_has_four_nova_cards(self):
        cards = self.class_under_test.deck.query("name == 'nova'")
        self.assertEqual(4, len(cards))
        self.assertEqual(4, len(cards.query("fuel_cells == 10")))
        self.assertEqual(4, len(cards.query("type == 'bronze'")))

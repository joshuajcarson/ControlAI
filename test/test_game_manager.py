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

    def test_game_manager_deck_called_for_random_int_when_making_hand_for_player_one(self):
        indexes_for_player_one = [1, 3, 7, 23, 10]
        self.class_under_test.get_random_index_of_deck = unittest.mock.MagicMock(side_effect=indexes_for_player_one)
        self.class_under_test.draw_five_cards_for_player('one')
        player_one_cards = self.class_under_test.deck.iloc[indexes_for_player_one].query("location == 'player_one'")
        self.assertEqual(5, len(player_one_cards.index))
        self.assertEqual(5, self.class_under_test.get_random_index_of_deck.call_count)

    def test_game_manager_deck_called_for_random_int_when_making_hand_for_player_two(self):
        indexes_for_player_two = [1, 3, 7, 23, 10]
        self.class_under_test.get_random_index_of_deck = unittest.mock.MagicMock(side_effect=indexes_for_player_two)
        self.class_under_test.draw_five_cards_for_player('two')
        player_two_cards = self.class_under_test.deck.iloc[indexes_for_player_two].query("location == 'player_two'")
        self.assertEqual(5, len(player_two_cards.index))
        self.assertEqual(5, self.class_under_test.get_random_index_of_deck.call_count)

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

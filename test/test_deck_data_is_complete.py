import unittest

import control_ai.game_manager


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.class_under_test = control_ai.game_manager.GameManager()

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

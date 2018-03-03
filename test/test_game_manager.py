import unittest

import control_ai.game_manager

number_of_players = 2


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.class_under_test = control_ai.game_manager.GameManager(number_of_players)

    def test_game_manager_can_create_two_player_game_with_deck(self):
        self.assertEqual(number_of_players, self.class_under_test.number_of_players)

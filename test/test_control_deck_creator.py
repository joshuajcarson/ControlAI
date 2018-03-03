import unittest

import control_ai.control_card
import control_ai.control_deck_creator


class TestControlDeckCreator(unittest.TestCase):
    def setUp(self):
        self.class_under_test = control_ai.control_deck_creator.ControlDeckCreator()
        self.deck_created = self.class_under_test.create_deck()

    def test_create_deck_creates_deck_with_54_cards(self):
        self.assertEqual(54, self.deck_created.size)

    def test_all_objects_in_deck_are_control_cards(self):
        for card in self.deck_created:
            self.assertIsInstance(card, control_ai.control_card.ControlCard)

    def test_just_make_all_the_cards_rewind_for_now(self):
        for card in self.deck_created:
            self.assertEqual(card.name, 'REWIND')
            self.assertEqual(card.type, 'BRONZE')
            self.assertEqual(card.charge, 5)

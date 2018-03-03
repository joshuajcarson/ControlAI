import unittest

import control_ai.control_card

card_name = 'RIFT'
cell_type = 'SILVER'
cell_charge = 1


class TestControlCard(unittest.TestCase):
    def setUp(self):
        self.class_under_test = control_ai.control_card.ControlCard(card_name, cell_type, cell_charge)

    def test_card_name_is_from_constructor(self):
        self.assertEqual(card_name, self.class_under_test.name)

    def test_cell_type_is_from_constructor(self):
        self.assertEqual(cell_type, self.class_under_test.type)

    def test_cell_charge_is_from_constructor(self):
        self.assertEqual(cell_charge, self.class_under_test.charge)


if __name__ == '__main__':
    unittest.main()

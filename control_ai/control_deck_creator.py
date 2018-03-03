import numpy as np

import control_ai.control_card


class ControlDeckCreator(object):
    def __init__(self):
        self

    def create_deck(self):
        return np.repeat(control_ai.control_card.ControlCard("REWIND", "BRONZE", 5), 54)

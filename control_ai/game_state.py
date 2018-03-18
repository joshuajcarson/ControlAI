class GameState(object):
    def __init__(self, player, action, card_name):
        self.action = action
        self.player = player
        self.card_name = card_name

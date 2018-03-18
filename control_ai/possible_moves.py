import control_ai.game_state

class PossibleMoves(object):
    def __init__(self, player, action = 'draw', card_name = 'none'):
        self.game_state = control_ai.game_state.GameState(player, action, card_name)

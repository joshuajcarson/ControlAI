import control_ai.game_state

class PossibleMoves(object):
    def __init__(self, player):
        self.game_state = control_ai.game_state.GameState(player)

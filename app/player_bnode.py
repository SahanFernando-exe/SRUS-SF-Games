from app.player import Player

class PlayerBNode:
    def __init__(self, player):
        if not isinstance(player, Player):
            raise TypeError
        self._player = player
        self._lesser = None
        self._greater = None
    
    @property
    def player(self):
        return self._player
    
    @property
    def lesser(self):
        return self._lesser
    
    @lesser.setter
    def lesser(self, playernode):
        if playernode is None or isinstance(playernode, PlayerBNode):
            self._lesser = playernode
    
    @property
    def greater(self):
        return self._greater
    
    @greater.setter
    def greater(self, playernode):
        if playernode is None or isinstance(playernode, PlayerBNode):
            self._greater = playernode
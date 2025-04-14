from app.player import Player

class PlayerBNode:
    def __init__(self, player):
        if not isinstance(player, Player):
            raise TypeError
        self._player = player
        self._lesser = None
        self._greater = None
        self._parent = None
    
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player: Player):
        if player is not None and not isinstance(player, Player):
            raise TypeError
        self._player = player
    
    @property
    def lesser(self):
        return self._lesser
    
    @lesser.setter
    def lesser(self, playernode):
        if playernode is not None and not isinstance(playernode, PlayerBNode):
            raise TypeError
        self._lesser = playernode
        if playernode:
            playernode._parent = self
        
    @property
    def greater(self):
        return self._greater
    
    @greater.setter
    def greater(self, playernode):
        if playernode is not None and not isinstance(playernode, PlayerBNode):
            raise TypeError
        self._greater = playernode
        if playernode:
            playernode._parent = self

    @property
    def parent(self):
        return self._parent
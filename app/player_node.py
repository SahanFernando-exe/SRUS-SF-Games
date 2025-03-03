
class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._previous = None
        self._next = None

    def __str__(self):
        return (
        f"location: {id(self)}\n"
        f"  player: {self.player}\n"
        f"  previous: {self._previous.player if self._previous else 'None'}\n"
        f"  next: {self._next.player if self._next else 'None'}"
    )

    @property
    def key(self):
        return self.player.uid

    @property
    def player(self):
        return self._player

    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, playernode: 'PlayerNode'):
        self._previous = playernode
        playernode._next = self

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, playernode: 'PlayerNode'):
        self._next = playernode
        playernode._previous = self
class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._previous = None
        self._next = None

    def __str__(self):
        return f"location: {id(self)}\nplayer: {self._player}\nprevious: {self._previous}\nnext: {self._next}"

    @property
    def key(self):
        return self.player.uid

    @property
    def player(self):
        return self._player

    @property
    def previous(self):
        return self._previous

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, playernode):
        self._next = playernode.player
        playernode._previous = self._player
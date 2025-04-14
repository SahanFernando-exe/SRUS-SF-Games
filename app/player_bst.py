from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root
    
    def insert(self, player: Player, node:PlayerBNode = None):
        if not isinstance(player, Player):
            raise TypeError
        if not isinstance(node, (PlayerBNode, type(None))):
            raise TypeError
        
        new_node = PlayerBNode(player)
        if self.root is None:
            self._root = new_node
            return

        curr_node = node
        if curr_node is None:
            curr_node = self.root

        if player.name > curr_node.player.name:
            if curr_node.greater is None:
                curr_node.greater = new_node
                return
            self.insert(player, node=curr_node.greater)
        
        elif player.name < curr_node.player.name:
            if curr_node.lesser is None:
                curr_node.lesser = new_node
                return
            self.insert(player, node=curr_node.lesser)

        elif player.name == curr_node.player.name:
            curr_node.player = player
from app.player_node import PlayerNode

class PlayerList:
    def __init__(self, *player_nodes: PlayerNode):
        for node in player_nodes:
            if not isinstance(node, PlayerNode):
                raise TypeError(f"Expected PlayerNode, got {type(node).__name__}")
        self._head = None
        self._tail = None
        if player_nodes:
            self._head = player_nodes[0]
            self._tail = player_nodes[-1]
        node = None
        for i in player_nodes:
            if node:
                node.next = i
            node = i


    @property
    def is_empty(self):
        return self._head == None and self._tail == None

    def append(self, player_node):
        '''
        adds a player node to the end of the list
        '''
        if self.is_empty:
            self._tail = player_node
            self._head = player_node
            return
        self._tail.next = player_node
        self._tail = player_node
    

    def prepend(self, player_node):
        '''
        adds a player node to the start of the list
        '''
        if self.is_empty:
            self._tail = player_node
            self._head = player_node
            return
        player_node.next = self._head
        self._head = player_node
    

    def replace_at(self, player, index):
        '''
        adds a player node to the specified index of the list (list starts index 0)
        '''
        node = self.get_node_at(index)
        node._player = player
    

    def squeeze_behind(self, player_node_to_add, reference_player_node):
        '''
        *unimplemented
        adds a player node behind the specified playernode (closer to the tail)
        '''
        pass


    def squeeze_infront(self, player_node_to_add, reference_player_node):
        '''
        *unimplemented
        adds a player node infront of the specified playernode (closer to the head)
        '''
        pass


    def get_node_at(self, index: int):
        '''
        returns the node at specified index
        '''
        if index < 0:
            node = self._tail
            for i in range(abs(index)-1):
                node = node.next
            return node
        node = self._head
        for i in range(index):
            node = node.next
        return node
        
        
    def get_index_of(self, player_node):
        '''
        *unimplemented
        returns the index of specified node
        '''
        pass
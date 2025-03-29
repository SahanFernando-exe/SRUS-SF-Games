from app.player_node import PlayerNode
from app.player import Player

class PlayerList:
    def __init__(self, *player_nodes: PlayerNode):
        ids = []
        for node in player_nodes:
            if not isinstance(node, PlayerNode):
                raise TypeError(f"Expected PlayerNode, got {type(node).__name__}")
            if node.key in ids:
                raise KeyError(f'duplicate key in parsed nodes; key: {node.key}')
            ids.append(node.key)
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

    def __iter__(self):
        current = self._head
        while current:
            yield current.player
            current = current.next

    def __str__(self):
        text = ""
        node = self._head
        while True:
            if node is None:
                return text
            text += node.__str__()
            node = node.next

    def display(self, forward=True):
        text = "\nPlayerList{\n"
        node = self._head
        if not forward:
            node = self._tail
        while True:
            if node is None:
                return text + "}"
            text += node.display()
            if forward:
                node = node.next
            else:
                node = node.previous

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

    def remove_at(self, index):
        node = self.get_node_at(index)
        if node.next:
            node.next.previous = node.previous
        elif node.previous:
            node.previous.next = node.next

    def remove_by_key(self, key: str):
        node = self._head
        while True:
            if node.key == key:
                if node.next:
                    node.next.previous = node.previous
                elif node.previous:
                    node.previous.next = node.next
                return
            if not node.next:
                raise KeyError(f'key {key} not found at {node}')
            node = node.next

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
                node = node.previous
                if node is None:
                    raise IndexError("Index out of range")
            return node
        node = self._head
        for i in range(index):
            node = node.next
            if node is None:
                raise IndexError("Index out of range")
        return node
        
        
    def get_index_of(self, player_node):
        '''
        *unimplemented
        returns the index of specified node
        '''
        pass
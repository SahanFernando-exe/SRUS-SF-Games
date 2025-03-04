class PlayerList:
    def __init__(self, *player_node):
        self._head = None
        self._tail = None
        if player_node:
            self._head = player_node[0]
            self._tail = player_node[-1]
        node = None
        for i in player_node:
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
    
    def insert_at(self, player_node, index):
        '''
        adds a player node to the the specified index of the list (list starts index 0)
        '''
        next = self.get_node_at(index)
        previous = next.previous
        player_node.next = next
        player_node.previous = previous
    
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

    def get_node_at(self, index):
        '''
        returns the node at specified index
        '''
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
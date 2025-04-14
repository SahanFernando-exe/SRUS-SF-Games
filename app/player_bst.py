from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self._root = None

    def display(self, pnode=0, indent=0):
        if pnode == 0:
            node = self._root
        else:
            node = pnode
        if node is None:
            return "empty"
        name = node.player.name
        nlen = len(name)
        ind = indent + nlen

        greater = ''
        lesser = None
        if node.greater:
            greater = '\033[1;93m - greater: \033[1;97m' + self.display(pnode = node.greater, indent=ind + len(' - greater: '))
        if node.lesser:
            lesser = '\033[1;93m └ lesser: \033[1;97m' + self.display(pnode = node.lesser, indent=ind + len(' - lesser: '))
        if lesser:
            return f"{name}{greater}\n{' '*ind}{lesser}"
        return f"{name}{greater}"




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

    def search(self, name: str, node:PlayerBNode = None):
        curr_node = self.root
        if node:
            curr_node = node

        if curr_node is None:
            return None
    #    print(f"checking {name} against {curr_node.player.name}")
        if name == curr_node.player.name:
    #        print(f"found {curr_node.player.name}")
            return curr_node.player
        elif name > curr_node.player.name:
            curr_node = curr_node.greater
        elif name < curr_node.player.name:
            curr_node = curr_node.lesser
    #    print(f"researching {curr_node.player.name} for {name}")
        return self.search(name, node=curr_node)

    def rebalance(self):
        players = []
        # add lessers, then self, then greaters.
        least_node = self.root
        while True:
            if least_node.lesser is None:
                #append current least
                players.append(least_node.player)
                #rearrange
                if least_node is self.root:
                    if least_node.greater:
                        self._root = least_node.greater
                        least_node = self.root
                        continue
                    self._root = None
                    break
                if least_node.greater:
                    parent_node = least_node.parent
                    parent_node.lesser = least_node.greater
                    least_node = parent_node.lesser
                    continue
                else:
                    parent_node = least_node.parent
                    parent_node.lesser = None
                    least_node = parent_node
                    continue
            least_node = least_node.lesser
        #sorted players

        def resort(arr):
        #    print(arr)
            if len(arr) == 1:
                return arr
            if not arr:
                return []
            median = len(arr) // 2
            left = arr[:median]
            right = arr[median + 1:]
            median = arr[median]
        #    print(median, left, right)
            ls = [median]
            ls.extend(resort(left))
            ls.extend(resort(right))
            return ls


        for i in resort(players):
        #    print(i.name)
            self.insert(i)
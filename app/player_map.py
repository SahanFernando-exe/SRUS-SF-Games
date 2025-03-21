import binascii
import math
from app.player import Player

class PlayerMap:
    def __init__(self, size = 8, load_factor = 0.75):
        self._load_factor = load_factor
        self._item_count = 0
        self._bucket_count = 2**math.ceil(math.log2((1/load_factor)*size))
        self.map = [None] * self._bucket_count
        print(self.map)

    def __str__(self):
        string = "map:"
        for bucket in self.map:
            string += "\n"
            if bucket is None:
                string += "None"
            else:
                for player in bucket:
                    string += f"{player.__str__()}, "
                string = string[:-2]
        return string

    def add(self, player: Player):
        hash = self.hash_func(player.uid)
        index = hash % self._bucket_count

        if self.map[index] is not None:
            for iplayer in self.map[index]:
                if iplayer.uid == player.uid:
                    raise KeyError(f'Key {player.uid} already exists in map')

        if self.map[index] is None:
            self.map[index] = [player]
        else:
            self.map[index].append(player)
        self._item_count += 1
        print(f"appended:\n  {self.map}")
        if self._item_count/self._bucket_count > self._load_factor:
            self.resize()

    def retrieve(self, key):
        hash = self.hash_func(key)
        index = hash % self._bucket_count
        if self.map[index] is None:
            raise KeyError(f'Key {key} does not exist in map')
        for iplayer in self.map[index]:
            print(iplayer.uid)
            if iplayer.uid == key:
                print(f"found: {iplayer}")

    def hash_func(self, key):
        hash = 0
        for i, char in enumerate(str(key)):
            binary_str = format(ord(char), '08b')
            binary_int = int(binary_str) * (i+1)
            hash += binary_int
        return hash

    def resize(self):
        self._bucket_count = 2**math.ceil(math.log2((1/self._load_factor)*self._item_count))
        new_map = [None] * self._bucket_count
        for bucket in self.map:
            if bucket is not None:
                for player in bucket:
                    hash = self.hash_func(player.uid)
                    index = hash % self._bucket_count
                    if new_map[index] is None:
                        new_map[index] = [player]
                    else:
                        new_map[index].append(player)
        print(f"converted:\n  {self.map}\nto:\n  {new_map}")
        self.map = new_map

players = []
for i in range(10):
    players.append(Player(uid=f"{i}", name=f"player_{i}"))

q = Player(uid=f"fb", name=f"player")
w = Player(uid=f"bf", name=f"player")
e = Player(uid=f"a", name=f"player")


a = PlayerMap(size = 1)
a.add(players[0])
a.add(players[1])
a.add(players[2])
a.add(q)
a.add(w)
a.add(e)
print(a)
a.retrieve("player_2")
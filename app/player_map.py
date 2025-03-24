import math
from app.player import Player

class PlayerMap:
    def __init__(self, size = 8, load_factor = 0.75):
        self._load_factor = load_factor
        self._item_count = 0
        self._bucket_count = 2**math.ceil(math.log2((1/load_factor)*size))
        self.map = [None] * self._bucket_count

    def __str__(self):
        string = f"map with {self._item_count} items across {self._bucket_count} buckets:"
        digits = len(str(self._bucket_count))+2
        for i, bucket in enumerate(self.map):
            string += f"\n{i+1}: "
            if bucket is None:
                string += "Empty"
            else:
                for player in bucket:
                    string += f"{player.__str__()}, "
                string = string[:-2]
        return string

    @property
    def size(self):
        return self._item_count

    def hash_func(self, key):
        key = str(key)
        hash_val = 0
        for i, char in enumerate(key):
            binary_str = format(ord(char), '08b')
            binary_int = int(binary_str) * (10**i)
            hash_val += binary_int
        hash_val += int(sum(int(x)*i for i, x in enumerate(str(hash_val))))
        return hash_val

    def resize(self):
        self._bucket_count = 2**math.ceil(math.log2((1/self._load_factor)*self._item_count))
        new_map = [None] * self._bucket_count
        for bucket in self.map:
            if bucket is not None:
                for player in bucket:
                    index = self.hash_func(player.uid) % self._bucket_count
                    if new_map[index] is None:
                        new_map[index] = [player]
                    else:
                        new_map[index].append(player)
        print(f"converted:\n  {self.map}\nto:\n  {new_map}")
        self.map = new_map

    def retrieve(self, key):
        index = self.hash_func(key) % self._bucket_count
        if self.map[index] is None:
            raise KeyError(f'Key {key} does not exist in map')
        for iplayer in self.map[index]:
            if iplayer.uid == key:
                print(f"found: {iplayer}")

    def add(self, player: Player):
        index = self.hash_func(player.uid) % self._bucket_count

        if self.map[index] is not None:
            for iter_player in self.map[index]:
                if iter_player.uid == player.uid:
                    raise KeyError(f'Key {player.uid} already exists in map')

        if self.map[index] is None:
            self.map[index] = [player]
        else:
            self.map[index].append(player)
        print("appended")
        self._item_count += 1
        if self._item_count/self._bucket_count > self._load_factor:
            self.resize()

    def remove(self, key):
        index = self.hash_func(key) % self._bucket_count

        if self.map[index] is not None:
            for i, player in enumerate(self.map[index]):
                if player.uid == key:
                    self.map[index].pop(i)
                    if len(self.map[index]) == 0:
                        self.map[index] = None
                    self._item_count -= 1
                    print("removed")
                    if self._item_count / (self._bucket_count/2) < self._load_factor:
                        self.resize()
                    return
        raise KeyError(f'Key {key} does not exist in map')




players = []
for i in range(10):
    players.append(Player(uid=f"player_{i}", name=f"player_{i}"))

q = Player(uid=f"ab", name=f"player")
w = Player(uid=f"b", name=f"player")
e = Player(uid=f"ax", name=f"player")
r = Player(uid=f"aa", name=f"player")


a = PlayerMap(size = 1)
for i in players:
    a.add(i)
a.add(q)
a.add(w)
a.add(r)
a.remove("aa")
a.remove("b")
print(a)
a.retrieve("ab")
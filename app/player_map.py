import math
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

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
            elif isinstance(bucket, Player):
                string += f"Player: {bucket}"
            elif isinstance(bucket, PlayerList):
                string += f"PlayerList: "
                for player in bucket:
                    string += f"{player}, "
                string = string[:-2]
            else:
                print(type(bucket))
                raise TypeError
        return string

    def __len__(self):
        return self._item_count

    @property
    def distribution(self):
        count = 0
        for bucket in self.map:
            if bucket is None:
                count += 1
        return (self._bucket_count - count)/self._bucket_count

    def hash_func(self, key):
        key = str(key)
        hash_val = 5381  # DJB2 initial value
        for char in key:
            hash_val = (hash_val * 33) + ord(char)
        return hash_val

    def resize(self):
        self._bucket_count = 2**math.ceil(math.log2((1/self._load_factor)*self._item_count))
        nmap = PlayerMap(load_factor = self._load_factor)
        nmap._bucket_count = self._bucket_count
        nmap.map = [None] * self._bucket_count

        for bucket in self.map:
            if bucket is None:
                continue
            elif isinstance(bucket, Player):
                nmap.add(bucket)
            elif isinstance(bucket, PlayerList):
                for player in bucket:
                    nmap.add(player)
            else:
                raise TypeError
        self.map = nmap.map

    def __getitem__(self, key):
        index = self.hash_func(key) % self._bucket_count
        if self.map[index] is None:
            pass
        elif isinstance(self.map[index], Player):
            if self.map[index].uid == key:
                return self.map[index]
        elif isinstance(self.map[index], PlayerList):
            for player in self.map[index]:
                if player.uid == key:
                    return player
        else:
            raise TypeError
        raise KeyError(f'Key {key} does not exist in map')

    def add(self, player: Player):
        index = self.hash_func(player.uid) % self._bucket_count
        if self.map[index] is None:
            self.map[index] = player
        elif isinstance(self.map[index], Player):
            if self.map[index].uid == player.uid:
                raise KeyError(f'Key {player.uid} already exists in map')
            # make into player list
            self.map[index] = PlayerList(PlayerNode(self.map[index]), PlayerNode(player))
        elif isinstance(self.map[index], PlayerList):
            for iter_player in self.map[index]:
                if iter_player.uid == player.uid:
                    raise KeyError(f'Key {player.uid} already exists in map')
            #add into playerlist
            self.map[index].append(PlayerNode(player))
        else:
            raise TypeError

        self._item_count += 1
        if self._item_count/self._bucket_count > self._load_factor:
            self.resize()

    def __delitem__(self, key):
        index = self.hash_func(key) % self._bucket_count

        if self.map[index] is None:
            raise KeyError(f'Key {key} does not exist in map')

        elif isinstance(self.map[index], Player):
            if self.map[index].uid == key:
                self.map[index] = None
            else:
                raise KeyError(f'Key {key} does not exist in map')

        elif isinstance(self.map[index], PlayerList):
            self.map[index].remove_by_key(key)

        else:
            raise TypeError

        self._item_count -= 1
        if self._item_count / (self._bucket_count / 2) < self._load_factor:
            self.resize()




players = []
for i in range(180):
    players.append(Player(uid=f"{i}", name=f"player_{i}"))

q = Player(uid=f"ab", name=f"player")
w = Player(uid=f"b", name=f"player")
e = Player(uid=f"ax", name=f"player")
r = Player(uid=f"aa", name=f"player")


a = PlayerMap(size = 1)
for x, i in enumerate(players):
    a.add(i)

a.add(q)
a.add(w)
a.add(e)
a.add(r)
print(a)
print(a["ax"])
print(a.distribution)
from app.player_map import PlayerMap
from app.player import Player
import unittest

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        players = []
        for i in range(180):
            players.append(Player(uid=f"{i}", name=f"player_{i}"))
        hm = PlayerMap()
        for player in players:
            hm.add(player)

        q = Player(uid=f"ab", name=f"player")
        w = Player(uid=f"b", name=f"player")
        e = Player(uid=f"ax", name=f"player")
        r = Player(uid=f"aa", name=f"player")
        hm.add(q)
        hm.add(w)
        hm.add(e)
        hm.add(r)
        print(hm)
        print(hm["ax"])


    def test_init(self):
        pass

    def test_get(self):
        pass

    def test_add(self):
        pass

    def test_remove(self):
        pass

    def test_edit(self):
        pass

    def test_resize(self):
        pass


if __name__ == '__main__':
    unittest.main()
from app.player_map import PlayerMap
from app.player import Player
import unittest

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        players = []
        for i in range(1000):
            players.append(Player(uid=f"{i}", name=f"player_{i}"))
        self.playermap = PlayerMap()
        for player in players:
            self.playermap.add(player)

    def test_init(self):
        playermap = PlayerMap()
        self.assertIsInstance(playermap, PlayerMap)

    def test_get(self):
        self.assertEqual(self.playermap["5"].name, "player_5")

    def test_add(self):
        self.assertEqual(len(self.playermap), 1000)
        self.playermap.add(Player(uid="add", name="new_player"))
        self.assertEqual(len(self.playermap), 1001)

    def test_remove(self):
        self.assertEqual(len(self.playermap), 1000)
        del self.playermap["8"]
        self.assertEqual(len(self.playermap), 999)
        with self.assertRaises(KeyError):
            self.playermap["8"]

if __name__ == '__main__':
    unittest.main()
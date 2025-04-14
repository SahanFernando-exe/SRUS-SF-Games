from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode
from app.player import Player
import unittest

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.player_bst = PlayerBST()
        self.players = []
        for i in range(10):
            self.players.append(Player(i, f"player_{i}"))

    def test_init(self):
        self.assertIsInstance(self.player_bst, PlayerBST)
    
    def test_insert(self):
        self.player_bst.insert(self.players[3])
        self.player_bst.insert(self.players[5])
        self.player_bst.insert(self.players[1])
        self.player_bst.insert(self.players[7])
        self.player_bst.insert(self.players[6])
        self.player_bst.insert(self.players[8])
        self.player_bst.insert(self.players[2])
        new_player = Player(6, "player_5")
        self.player_bst.insert(new_player)
        self.assertEqual(self.player_bst.root.player.name, "player_3")
        self.assertEqual(self.player_bst.root.greater.player.name, "player_5")
        self.assertEqual(self.player_bst.root.greater.player.uid, '6')
        self.assertEqual(self.player_bst.root.lesser.player.name, "player_1")
        self.assertEqual(self.player_bst.root.lesser.greater.player.name, "player_2")
        self.assertEqual(self.player_bst.root.greater.greater.player.name, "player_7")
        self.assertEqual(self.player_bst.root.greater.greater.lesser.player.name, "player_6")
        self.assertEqual(self.player_bst.root.greater.greater.greater.player.name, "player_8")

    def test_search(self):
        self.player_bst.insert(self.players[3])
        self.player_bst.insert(self.players[5])
        self.player_bst.insert(self.players[1])
        self.player_bst.insert(self.players[7])
        self.player_bst.insert(self.players[6])
        self.player_bst.insert(self.players[8])
        self.player_bst.insert(self.players[2])
        new_player = Player(6, "player_5")
        self.player_bst.insert(new_player)
        self.assertEqual(self.player_bst.search("player_5").uid, "6")
        self.assertEqual(self.player_bst.search("player_7").uid, "7")

if __name__ == '__main__':
    unittest.main()
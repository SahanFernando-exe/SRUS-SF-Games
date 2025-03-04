from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player
import unittest

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.p1 = PlayerNode(Player(2,"1sdgs"))
        self.p2 = PlayerNode(Player(3,"2sdgs"))
        self.p3 = PlayerNode(Player(4,"3sdgs"))
        self.p4 = PlayerNode(Player(5,"4sdgs"))
        
    def test_append(self):
        self.player_list = PlayerList(self.p1, self.p2, self.p3)
        print(self.player_list)
        self.assertEqual(self.player_list, 3)

    def test_name(self):
        self.assertEqual(self.player.name, "Jeff")

    def test_change_error(self):
        with self.assertRaises(AttributeError):
            self.player.name = "Jack"

if __name__ == '__main__':
    unittest.main()
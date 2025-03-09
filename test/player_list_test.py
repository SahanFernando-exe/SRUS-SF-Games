from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player
import unittest

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        players = []
        for i in range(10):
            players.append(Player(i, f"player_{i}"))
        nodes = []
        for player in players:
            nodes.append(PlayerNode(player))
        self.nodes = nodes

    def test_init(self):
        self.player_list = PlayerList()
        self.assertIsInstance(self.player_list, PlayerList)

        self.player_list = PlayerList(self.nodes[2])
        self.assertIsInstance(self.player_list, PlayerList)

        self.player_list = PlayerList(self.nodes[2], self.nodes[5])
        self.assertIsInstance(self.player_list, PlayerList)

        with self.assertRaises(TypeError):
            PlayerList(23)

        with self.assertRaises(TypeError):
            PlayerList("something")

        with self.assertRaises(KeyError):
            PlayerList(self.nodes[2], self.nodes[2])

    def test_is_empty(self):
        self.empty_player_list = PlayerList()
        self.prefilled_player_list = PlayerList(self.nodes[2], self.nodes[4])

        self.assertEqual(self.empty_player_list.is_empty, True)
        self.assertEqual(self.prefilled_player_list.is_empty, False)

    def test_append(self):
        self.player_list = PlayerList()
        self.player_list.append(self.nodes[3])
        self.assertIs(self.player_list._tail, self.nodes[3])

        self.player_list = PlayerList(self.nodes[2], self.nodes[4])
        self.player_list.append(self.nodes[3])
        self.assertIs(self.player_list._tail, self.nodes[3])
    
    def test_prepend(self):
        self.player_list = PlayerList()
        self.player_list.prepend(self.nodes[3])
        self.assertIs(self.player_list._head, self.nodes[3])

        self.player_list = PlayerList(self.nodes[2], self.nodes[4])
        self.player_list.prepend(self.nodes[3])
        self.assertIs(self.player_list._head, self.nodes[3])

    def test_remove_at(self):
        self.player_list = PlayerList(self.nodes[2], self.nodes[4], self.nodes[7])
        self.player_list.remove_at(1)
        self.assertEqual(print(self.player_list), print(PlayerList(self.nodes[2], self.nodes[7])))

        self.player_list = PlayerList(self.nodes[2], self.nodes[4], self.nodes[7])
        self.player_list.remove_at(-2)
        self.assertEqual(print(self.player_list), print(PlayerList(self.nodes[2], self.nodes[7])))

    def test_remove_by_key(self):
        self.player_list = PlayerList(self.nodes[2], self.nodes[4], self.nodes[7])
        self.player_list.remove_by_key("4")
        self.assertEqual(print(self.player_list), print(PlayerList(self.nodes[2], self.nodes[7])))

if __name__ == '__main__':
    unittest.main()
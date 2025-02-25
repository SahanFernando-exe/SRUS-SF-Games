from app.player import Player
import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(4, "Jeff")

    def test_id(self):
        self.assertEqual(self.player.uid, 4)

    def test_name(self):
        self.assertEqual(self.player.name, "Jeff")

    def test_change_error(self):
        with self.assertRaises(AttributeError):
            self.player.name = "Jack"

if __name__ == '__main__':
    unittest.main()
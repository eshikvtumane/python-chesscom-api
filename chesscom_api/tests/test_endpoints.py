import unittest

from chesscom_api.api import ChessComApi


class PlayerEndpointTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.player_name = 'erik'
        cls.chess_com_api = ChessComApi()

    def test_get_player_success(self):
        result = self.chess_com_api.get_player_info(player_name=self.player_name)

        self.assertNotEqual(len(result), 2)
        self.assertFalse('message' in result)
        self.assertFalse('code' in result)

    def test_get_player_failed(self):
        result = self.chess_com_api.get_player_info(player_name='')

        self.assertEqual(len(result), 2)
        self.assertTrue('message' in result)
        self.assertTrue('code' in result)


if __name__ == '__main__':
    unittest.main()

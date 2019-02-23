import unittest

from chesscom_api.api import ChessComApi
from chesscom_api.endpoints.titled_players import TitledList


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.player_name = 'erik'
        cls.chess_com_api = ChessComApi()


class PlayerEndpointTestCase(BaseTestCase):
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


class TitledPlayersEndpointTestCase(BaseTestCase):
    def test_get_titled_players_success(self):
        result = self.chess_com_api.get_titled_players(title=TitledList.FIDE_Master)

        self.assertTrue('players' in result)
        self.assertIsInstance(result['players'], list)
        self.assertIsInstance(result['players'][0], str)

    def test_get_player_failed(self):
        result = self.chess_com_api.get_titled_players(title=self.player_name)

        self.assertEqual(len(result), 2)
        self.assertTrue('message' in result)
        self.assertTrue('code' in result)


if __name__ == '__main__':
    unittest.main()

import unittest

from chesscom_api.api import ChessComApi
from chesscom_api.endpoints.player_data.titled_players import TitledList


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
    def get_titled_players_success(self, title):
        result = self.chess_com_api.get_titled_players(title=title)

        self.assertTrue('players' in result)
        self.assertIsInstance(result['players'], list)
        self.assertIsInstance(result['players'][0], str)

    def test_get_grandmaster_players(self):
        self.get_titled_players_success(TitledList.Grandmaster)

    def test_get_women_grandmaster_players(self):
        self.get_titled_players_success(TitledList.Woman_Grandmaster)

    def test_get_international_master_players(self):
        self.get_titled_players_success(TitledList.International_Master)

    def test_get_woman_international_master_players(self):
        self.get_titled_players_success(TitledList.Woman_International_Master)

    def test_get_fide_master_players(self):
        self.get_titled_players_success(TitledList.FIDE_Master)

    def test_get_woman_fide_master_players(self):
        self.get_titled_players_success(TitledList.Woman_FIDE_Master)

    def test_get_national_master_players(self):
        self.get_titled_players_success(TitledList.National_Master)

    def test_get_woman_national_master_players(self):
        self.get_titled_players_success(TitledList.Women_National_Master)

    def test_get_candidate_master_players(self):
        self.get_titled_players_success(TitledList.Candidate_Master)

    def test_get_woman_candidate_master_players(self):
        self.get_titled_players_success(TitledList.Woman_Candidate_Master)

    def test_get_player_failed(self):
        with self.assertRaises(ValueError):
            self.chess_com_api.get_titled_players(title=self.player_name)


if __name__ == '__main__':
    unittest.main()

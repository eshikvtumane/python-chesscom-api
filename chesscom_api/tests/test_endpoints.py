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


class PlayerStatsEndpointTestCase(BaseTestCase):
    def test_get_player_stats_success(self):
        result = self.chess_com_api.player_data_endpoints.player_stats.get_data(username=self.player_name)

        self.assertTrue('chess960_daily' in result)
        self.assertTrue('chess_blitz' in result)
        self.assertTrue('chess_bullet' in result)
        self.assertTrue('chess_daily' in result)
        self.assertTrue('chess_rapid' in result)
        self.assertEqual(len(result), 5)


class PlayerOnlineStatusEndpointTestCase(BaseTestCase):
    def test_get_player_online_status_success(self):
        result = self.chess_com_api.player_data_endpoints.player_online_status.get_data(username=self.player_name)

        self.assertTrue('online' in result)
        self.assertIsInstance(result['online'], bool)


class PlayerCurrentDailyGamesEndpointTestCase(BaseTestCase):
    def test_get_player_current_daily_games_success(self):
        result = self.chess_com_api.player_data_endpoints.player_games_endpoints.current_daily_chess.get_data(
            username=self.player_name)

        self.assertTrue('games' in result)
        self.assertIsInstance(result['games'], list)


class PlayerToMoveDailyGamesEndpointTestCase(BaseTestCase):
    def test_get_player_to_move_daily_games_success(self):
        result = self.chess_com_api.player_data_endpoints.player_games_endpoints.to_move_daily_chess.get_data(
            username=self.player_name)

        self.assertTrue('games' in result)
        self.assertIsInstance(result['games'], list)


class PlayerListOfMonthlyArchivesEndpointTestCase(BaseTestCase):
    def test_get_player_list_of_monthly_archives_success(self):
        result = self.chess_com_api.player_data_endpoints.player_games_endpoints.list_of_monthly_archive.get_data(
            username=self.player_name)

        self.assertTrue('archives' in result)
        self.assertIsInstance(result['archives'], list)


class PlayerCompleteMonthlyArchivesEndpointTestCase(BaseTestCase):
    def test_get_player_complete_monthly_archives_success(self):
        result = self.chess_com_api.player_data_endpoints.player_games_endpoints.complete_monthly_archive.get_data(
            username=self.player_name, year=2009, month=4)

        self.assertTrue('games' in result)
        self.assertIsInstance(result['games'], list)

        result = self.chess_com_api.player_data_endpoints.player_games_endpoints.complete_monthly_archive.get_data(
            username=self.player_name, year=2009, month=10)

        self.assertTrue('games' in result)
        self.assertIsInstance(result['games'], list)


class PlayerMultiGamePngEndpointTestCase(BaseTestCase):
    def test_get_player_multi_game_png_success(self):
        result = self.chess_com_api.player_data_endpoints.player_games_endpoints.multi_game_png.get_data(
            username=self.player_name, year=2009, month=4)

        self.assertIsInstance(result, str)
        self.assertTrue('[Event' in result)


class PlayerListOfClubsEndpointTestCase(BaseTestCase):
    def test_get_player_list_of_clubs_success(self):
        result = self.chess_com_api.player_data_endpoints.participation.list_of_clubs.get_data(
            username=self.player_name)

        self.assertTrue('clubs' in result)
        self.assertIsInstance(result['clubs'], list)


if __name__ == '__main__':
    unittest.main()

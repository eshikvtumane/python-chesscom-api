from chesscom_api.endpoints.player_data.player_complete_monthly_archives import PlayerCompleteMonthlyArchivesEndpoint
from chesscom_api.endpoints.player_data.player_current_daily_chess import PlayerCurrentDailyChessEndpoint
from chesscom_api.endpoints.player_data.player_list_of_monthly_archives import PlayerListOfMonthlyArchivesEndpoint
from chesscom_api.endpoints.player_data.player_multi_game_pgn_monthly import PlayerMultiGamePngMonthlyEndpoint
from chesscom_api.endpoints.player_data.player_to_move_daily_chess import PlayerToMoveDailyChessEndpoint


class PlayerGamesEndpoints(object):
    def __init__(self):
        self.current_daily_chess = PlayerCurrentDailyChessEndpoint()
        self.to_move_daily_chess = PlayerToMoveDailyChessEndpoint()
        self.list_of_monthly_archive = PlayerListOfMonthlyArchivesEndpoint()
        self.complete_monthly_archive = PlayerCompleteMonthlyArchivesEndpoint()
        self.multi_game_png = PlayerMultiGamePngMonthlyEndpoint()

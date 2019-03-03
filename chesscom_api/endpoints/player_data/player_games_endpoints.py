from chesscom_api.endpoints.player_data.player_current_daily_chess import PlayerCurrentDailyChessEndpoint
from chesscom_api.endpoints.player_data.player_monthly_archives import PlayerMonthlyArchivesEndpoint
from chesscom_api.endpoints.player_data.player_to_move_daily_chess import PlayerToMoveDailyChessEndpoint


class PlayerGamesEndpoints(object):
    def __init__(self):
        self.current_daily_chess = PlayerCurrentDailyChessEndpoint()
        self.to_move_daily_chess = PlayerToMoveDailyChessEndpoint()
        self.monthly_archive = PlayerMonthlyArchivesEndpoint()

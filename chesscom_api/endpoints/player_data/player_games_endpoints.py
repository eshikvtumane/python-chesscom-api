from chesscom_api.endpoints.player_data.player_current_daily_chess import PlayerCurrentDailyChessEndpoint


class PlayerGamesEndpoints(object):
    def __init__(self):
        self.current_daily_chess = PlayerCurrentDailyChessEndpoint()

from chesscom_api.endpoints.player_data.player import PlayerEndpoint
from chesscom_api.endpoints.player_data.titled_players import TitledPlayersEndpoint


class PlayerDataEndpoints(object):
    def __init__(self):
        self.player = PlayerEndpoint()
        self.titled_players = TitledPlayersEndpoint()

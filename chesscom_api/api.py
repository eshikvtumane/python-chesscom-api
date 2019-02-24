from chesscom_api.endpoints.player_data.player_data_endpoints import PlayerDataEndpoints


class ChessComApi(object):
    def __init__(self):
        self.player_data_endpoints = PlayerDataEndpoints()

    def get_player_info(self, player_name):
        return self.player_data_endpoints.player.get_data(player_name)

    def get_titled_players(self, title):
        return self.player_data_endpoints.titled_players.get_data(title)

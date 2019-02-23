from chesscom_api.endpoints.player import PlayerEndpoint
from chesscom_api.endpoints.titled_players import TitledPlayersEndpoint


class ChessComApi(object):
    def get_player_info(self, player_name):
        player = PlayerEndpoint()
        return player.get_data(player_name)

    def get_titled_players(self, title):
        titled_players = TitledPlayersEndpoint()
        return titled_players.get_data(title)

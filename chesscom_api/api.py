from chesscom_api.endpoints.player import PlayerEndpoint


class ChessComApi(object):
    def get_player_info(self, player_name):
        player = PlayerEndpoint()
        return player.get_data(player_name)

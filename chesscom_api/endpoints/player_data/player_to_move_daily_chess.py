from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerToMoveDailyChessEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/games/to-move'
        super(PlayerToMoveDailyChessEndpoint, self).__init__()

    def get_data(self, username):
        self.endpoint_path_with_params = self.endpoint_name % username
        return super(PlayerToMoveDailyChessEndpoint, self).get_data()

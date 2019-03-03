from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerCurrentDailyChessEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/games'
        super(PlayerCurrentDailyChessEndpoint, self).__init__()

    def get_data(self, username):
        self.endpoint_path_with_params = self.endpoint_name % username
        return super(PlayerCurrentDailyChessEndpoint, self).get_data()

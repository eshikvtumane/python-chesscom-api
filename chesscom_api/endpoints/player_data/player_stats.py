from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerStatsEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/stats'
        super(PlayerStatsEndpoint, self).__init__()

    def get_data(self, username):
        self.endpoint_path_with_params = self.endpoint_name % username
        return super(PlayerStatsEndpoint, self).get_data()

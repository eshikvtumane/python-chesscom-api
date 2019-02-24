from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerEndpoint(BaseEndpoint):
    def __init__(self):
        super(PlayerEndpoint, self).__init__()
        self.endpoint_path = 'player/%s'

    def get_data(self, player_name):
        self.endpoint_path_with_params = self.endpoint_path % player_name
        return super(PlayerEndpoint, self).get_data()

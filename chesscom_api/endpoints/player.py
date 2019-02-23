from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerEndpoint(BaseEndpoint):
    def __init__(self):
        endpoint_name = 'player'
        super(PlayerEndpoint, self).__init__(endpoint_name)

    def get_data(self, player_name):
        self.get_url(player_name)
        return super(PlayerEndpoint, self).get_data()

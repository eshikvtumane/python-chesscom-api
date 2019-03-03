from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerOnlineStatusEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/is-online'
        super(PlayerOnlineStatusEndpoint, self).__init__()

    def get_data(self, username):
        self.endpoint_path_with_params = self.endpoint_name % username
        return super(PlayerOnlineStatusEndpoint, self).get_data()

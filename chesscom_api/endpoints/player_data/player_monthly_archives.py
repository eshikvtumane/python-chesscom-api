from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerMonthlyArchivesEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/games/archives'
        super(PlayerMonthlyArchivesEndpoint, self).__init__()

    def get_data(self, username):
        self.endpoint_path_with_params = self.endpoint_name % username
        return super(PlayerMonthlyArchivesEndpoint, self).get_data()

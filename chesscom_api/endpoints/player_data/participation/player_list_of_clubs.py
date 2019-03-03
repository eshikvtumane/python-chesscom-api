from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerListOfClubsEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/clubs'
        super(PlayerListOfClubsEndpoint, self).__init__()

    def get_data(self, username):
        """

        :param username:
        :return: dict
        """

        self.endpoint_path_with_params = self.endpoint_name % username
        result = super(PlayerListOfClubsEndpoint, self).get_data()
        return result

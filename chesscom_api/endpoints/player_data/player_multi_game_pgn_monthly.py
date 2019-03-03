from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerMultiGamePngMonthlyEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/games/%s/%s/pgn'
        super(PlayerMultiGamePngMonthlyEndpoint, self).__init__()

    def get_data(self, username, month, year):
        """

        :param username:
        :param month: int
        :param year: int
        :return: bytes
        """
        month_string = str(month)
        if 10 > month > 0:
            month_string = '0' + month_string

        self.endpoint_path_with_params = self.endpoint_name % (username, year, month_string)
        result = super(PlayerMultiGamePngMonthlyEndpoint, self).get_data(json=False)
        return str(result)

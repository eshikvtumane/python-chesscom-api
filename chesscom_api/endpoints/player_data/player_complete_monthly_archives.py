from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class PlayerCompleteMonthlyArchivesEndpoint(BaseEndpoint):
    def __init__(self):
        self.endpoint_name = 'player/%s/games/%s/%s'
        super(PlayerCompleteMonthlyArchivesEndpoint, self).__init__()

    def get_data(self, username, month, year):
        """

        :param username:
        :param month: int
        :param year: int
        :return:
        """
        month_string = str(month)
        if 10 > month > 0:
            month_string = '0' + month_string

        self.endpoint_path_with_params = self.endpoint_name % (username, year, month_string)
        return super(PlayerCompleteMonthlyArchivesEndpoint, self).get_data()

from enum import Enum

from chesscom_api.endpoints.base_endpoint import BaseEndpoint


class TitledList(Enum):
    """
    FIDE titles
    From Wikipedia article: https://en.wikipedia.org/wiki/FIDE_titles
    """

    Grandmaster = 'GM'
    Woman_Grandmaster = 'WGM'
    International_Master = 'IM'
    Woman_International_Master = 'WIM'
    FIDE_Master = 'FM'
    Woman_FIDE_Master = 'WFM'
    National_Master = 'NM'
    Women_National_Master = 'WNM'
    Candidate_Master = 'CM'
    Woman_Candidate_Master = 'WCM'


class TitledPlayersEndpoint(BaseEndpoint):
    def __init__(self):
        super(TitledPlayersEndpoint, self).__init__()
        self.endpoint_path = 'titled/%s'

    def get_data(self, title):
        """
        Get titled played list
        :param title: TitledList
        :return: list
        """
        self.valid(title)
        self.endpoint_path_with_params = self.endpoint_path % title.value
        return super(TitledPlayersEndpoint, self).get_data()

    def valid(self, title):
        if not isinstance(title, TitledList):
            raise ValueError('Title is not type TitledList.')

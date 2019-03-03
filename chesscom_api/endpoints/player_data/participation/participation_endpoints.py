from chesscom_api.endpoints.player_data.participation.player_list_of_clubs import PlayerListOfClubsEndpoint


class ParticipationEndpoints(object):
    def __init__(self):
        self.list_of_clubs = PlayerListOfClubsEndpoint()

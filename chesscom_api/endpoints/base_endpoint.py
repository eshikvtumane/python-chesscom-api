import six
import requests

if six.PY2:
    from urlparse import urljoin
elif six.PY3:
    from urllib.parse import urljoin


class BaseEndpoint(object):
    def __init__(self, endpoint_name):
        self.url = 'https://api.chess.com/pub/'
        self.endpoint_name = endpoint_name
        self.final_url = None

    def get_url(self, parameters=''):
        self.final_url = urljoin(self.url, self.endpoint_name)
        self.final_url = '%s/%s/' % (self.final_url, parameters)

    def get_data(self):
        response = requests.get(self.final_url)
        return response.json()

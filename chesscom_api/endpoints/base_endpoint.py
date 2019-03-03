import six
import requests

if six.PY2:
    from urlparse import urljoin
elif six.PY3:
    from urllib.parse import urljoin


class BaseEndpoint(object):
    def __init__(self):
        self.url = 'https://api.chess.com/pub/'
        self.endpoint_path = None
        self.endpoint_path_with_params = None
        self.final_url = None

    def get_url(self):
        self.final_url = urljoin(self.url, self.endpoint_path_with_params)

    def get_data(self, json=True):
        self.get_url()
        response = requests.get(self.final_url)

        if json:
            content = response.json()
        else:
            content = response.content

        return content

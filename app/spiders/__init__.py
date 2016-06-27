from tornado import gen, httpclient
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/51.0.2704.103 Safari/537.36'


class HttpMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class Spider:
    def __init__(self):
        pass

    @staticmethod
    def fetch(url, callback=None, raise_error=True, **kwargs):
        http_client = httpclient.AsyncHTTPClient()
        return http_client.fetch(url, callback=callback, raise_error=raise_error,
                                 user_agent=USER_AGENT, **kwargs)

    @staticmethod
    def get_bs4(markup, parser):
        return BeautifulSoup(markup, parser)

    @staticmethod
    def get_lxml_bs4(markup):
        return BeautifulSoup(markup, 'lxml')
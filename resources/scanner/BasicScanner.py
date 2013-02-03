#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import requests

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 08:52'



class BasicScanner(object):

    def __init__(self, url):
        self.url = url
        self.data = []

    def fetch(self):
        """
            Fetches the content from url
        """

        request = requests.get(self.url)
        request.raise_for_status()
        self.data = self.parse(request.text)

    def parse(self, content):
        """
            Do the Parse Work
            :param content: Content from Request
        """

        return None

    def run(self):

        self.fetch()
        if self.data:
            return self.data
        raise Exception("No Content Provided")
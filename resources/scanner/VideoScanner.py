#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Provides scanner for resolving video urls on a page
"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '11.02.13 - 18:06'


class Mp4Scanner(BasicScanner):
    """
        Looks for mp4 on a page
    """

    def __init__(self, url):
        super(Mp4Scanner, self).__init__(url)

        self.mp4re = re.compile(r'(http://.+\.\w{2,3}.*/.+\.mp4[^\"\'\.]*)')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.mp4re.findall(content)
        for url in matches:
            rtn.append(url)
        return rtn


class AviScanner(BasicScanner):
    """
        Looks for avi on a page
    """

    def __init__(self, url):
        super(AviScanner, self).__init__(url)

        self.avire = re.compile(r'(http://.+\.\w{2,3}.*/.+\.avi[^\"\'\.]*)')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.avire.findall(content)
        for url in matches:
            rtn.append(url)
        return rtn


class FlvScanner(BasicScanner):
    """
        Looks for flv on a page
    """

    def __init__(self, url):
        super(FlvScanner, self).__init__(url)

        self.flvre = re.compile(r'(http://.+\.\w{2,3}.*/.+\.flv[^\"\'\.]*)')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.flvre.findall(content)
        for url in matches:
            rtn.append(url)
        return rtn


class VideoScanner(Mp4Scanner, AviScanner, FlvScanner):
    """
        Mixes mp4,avi,flv scanner
    """

    def __init__(self, url):
        super(VideoScanner, self).__init__(url)

    def parse(self, content):
        """
            Redirect the content to its mixins
            :param content: Content from Request
        """
        rtn = []
        rtn.extend(Mp4Scanner.parse(self, content))
        rtn.extend(AviScanner.parse(self, content))
        rtn.extend(FlvScanner.parse(self, content))
        return rtn
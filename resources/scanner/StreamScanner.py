#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:37'

class Mp4Scanner(BasicScanner):
    def __init__(self, url):
        super(Mp4Scanner, self).__init__(url)

        self.mp4re = re.compile(r'(http://.+\.\w{2,3}.*/.+\.mp4[^\"\'\.]+)')

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
    def __init__(self, url):
        super(AviScanner, self).__init__(url)

        self.avire = re.compile(r'(http://.+\.\w{2,3}.*/.+\.avi[^\"\'\.]+)')

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
    def __init__(self, url):
        super(FlvScanner, self).__init__(url)

        self.flvre = re.compile(r'(http://.+\.\w{2,3}.*/.+\.flv[^\"\'\.]+)')

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




class StreamScanner(BasicScanner):
    def __init__(self, tag, type, episode):
        super(StreamScanner, self).__init__("http://www.animeavenue.net/%s-%s-%s/" % (tag, type, episode))

        self.re = re.compile(r'<div[\s\n\r]*class=[\'"]postTabs_divs.*[\'"].*>[\s\n\r]*<span[\s\n\r]*.*>.*<br[\s\n\r]*/>[\s\n\r]*<iframe[\s\n\r]*(?:SRC|src)=[\'"]([^\'">]+)[\'"].*>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for url in matches:
            mp = VideoScanner(url)
            rtn.extend(mp.run())
            # Just Loop until a mp4/flv/avi has been found
            if rtn:
                break
        return rtn

if __name__ == "__main__":
    gs = StreamScanner("canaan", "episode", "1")
    iframes = gs.run()
    print "%s" % iframes
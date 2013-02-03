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

        self.re = re.compile(r'(http://.+\.\w{2,3}.*/.+\.mp4)')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for url in matches:
            rtn.append(url)
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
            mp = Mp4Scanner(url)
            rtn.extend(mp.run())
            # Just Loop until a mp4 has been found
            if rtn:
                break
        return rtn

if __name__ == "__main__":
    gs = StreamScanner("fairy-tail", "episode", "167")
    iframes = gs.run()
    print "%s" % iframes
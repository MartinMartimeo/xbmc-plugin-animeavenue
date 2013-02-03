#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:08'

URL = "http://www.animeavenue.net/ongoing-series/"


class OngoingAnimeScanner(BasicScanner):

    def __init__(self):
        super(OngoingAnimeScanner, self).__init__(URL)

        self.re = re.compile(r'<li>[\s\n\r]*<a[\s\n\r]+href=[\'"][^\'">]+/category/([^\'">]+)/[\'"]>(.+)</a>[\s\n\r]*(\d*\:\d*\s*(?:am|pm))[\s\n\r]*.*</li>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for tag, caption, time in matches:
            rtn.append((tag, caption, time))
        rtn = sorted(rtn, key=lambda anime: anime[1])
        return rtn



if __name__ == "__main__":
    gs = OngoingAnimeScanner()
    animes = gs.run()
    print "%s" % animes
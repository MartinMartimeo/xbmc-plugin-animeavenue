#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 08:51'

URL = "http://www.animeavenue.net/anime-genres/"


class GenreScanner(BasicScanner):

    def __init__(self):
        super(GenreScanner, self).__init__(URL)

        self.re = re.compile(r'<li>[\s\n\r]*<a[\s\n\r]+href=[\'"]([^\'">]+\?genre=[^\'">]+)[\'"]>(.+)</a>[\s\n\r]*</li>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for url, genre in matches:
            rtn.append(genre)
        rtn = sorted(rtn)
        return rtn



if __name__ == "__main__":
    gs = GenreScanner()
    genres = gs.run()
    print "%s" % genres
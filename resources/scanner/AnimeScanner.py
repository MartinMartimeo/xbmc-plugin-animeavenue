#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 10:08'


class AnimeScanner(BasicScanner):

    def __init__(self, url):
        super(AnimeScanner, self).__init__(url)

        self.re = re.compile(r'<li>[\s\n\r]*<a[\s\n\r]+href=[\'"][^\'">]+/category/([^\'">]+)/[\'"]>(.+)</a>[\s\n\r]*</li>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for anime, caption in matches:
            rtn.append((anime, caption))
        rtn = sorted(rtn, key=lambda anime: anime[1])
        return rtn



if __name__ == "__main__":
    vs = AnimeScanner("http://www.animeavenue.net/anime-list/")
    animes = vs.run()
    print "%s" % animes
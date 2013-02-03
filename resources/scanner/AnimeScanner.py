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

        self.re = re.compile(r'<img[\s\n\r]*src=[\'"]([^\'">]+)[\'"][\s\n\r]*></a></div><div[^\>]+><div[^\>]+>[\s\n\r]*<h4>[\s\n\r]*<strong>[\s\n\r]*<a[\s\n\r]+href=[\'"][^\'">]+/category/([^\'">]+)/[\'"]>(.+)</a>[\s\n\r]*</strong>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for img, anime, caption in matches:
            rtn.append((img, anime, caption))
        return rtn



if __name__ == "__main__":
    vs = AnimeScanner("http://www.animeavenue.net/?genre=Adventure")
    animes = vs.run()
    print "%s" % animes
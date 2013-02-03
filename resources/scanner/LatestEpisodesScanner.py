#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 10:51'

URL = "http://www.animeavenue.net/"


class LatestEpisodesScanner(BasicScanner):

    def __init__(self):
        super(LatestEpisodesScanner, self).__init__(URL)

        self.re = re.compile(r'<div[\s\n\r]*class=[\'"]single-posts-latest-title[\'"][\s\n\r]*>[\s\n\r]*<a[\s\n\r]+href=[\'"][^\'">]+/([^\'">]+)-episode-(\d+)/[\'"][\s\n\r]+rel=[\'"]bookmark[\'"][\s\n\r]*>(.+)</a>[\s\n\r]*</div>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for tag, episode, caption in matches:
            rtn.append((tag, episode, caption))
        return rtn



if __name__ == "__main__":
    gs = LatestEpisodesScanner()
    animes = gs.run()
    print "%s" % animes
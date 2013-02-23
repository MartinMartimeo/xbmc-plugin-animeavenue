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

        self.re = re.compile(r'<div[\s\n\r]*class=[\'"]rawsubdub-overlay[\'"][\s\n\r]*>[\s\n\r]*<a[\s\n\r]+href=[\'"][^\'">]+/([^\'">]+)-(\w+)-(\d+)/[\'"][\s\n\r]+.+<img[\s\n\r]+src=[\'"].+/(\w+)\.png[\'"].*>.+<div[\s\n\r]*.*>[\s\n\r]+<a[\s\n\r]+href=[\'"][^\'">]+[\'"][\s\n\r]+title=["]([^">]+)["][\s\n\r]*>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for tag, type, episode, kind, caption in matches:
            rtn.append((tag, (type, kind), episode, caption))
        return rtn



if __name__ == "__main__":
    gs = LatestEpisodesScanner()
    animes = gs.run()
    for (tag, (type, kind), episode, anime) in animes:
        print "Anime: %s / Type: %s / Kind: %s / Episode: %s / Titel: %s" % (tag, type, kind, episode, anime)
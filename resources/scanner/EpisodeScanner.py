#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:19'




class EpisodeScanner(BasicScanner):

    def __init__(self, tag):
        super(EpisodeScanner, self).__init__("http://www.animeavenue.net/category/%s/" % tag)

        self.re = re.compile(r'<div[\s\n\r]*class=[\'"]search-results[\'"][\s\n\r]*>[\s\n\r]*<a[\s\n\r]+href=[\'"][^\'">]+/([^\'">]+)-(\w+)-(\d+)/[\'"][\s\n\r]+rel=[\'"]bookmark[\'"][\s\n\r]*>(.+)&nbsp;<span>.*</span>[\s\n\r]*</a>[\s\n\r]*</div>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for tag, type, episode, caption in matches:
            rtn.append((tag, type, episode, caption))
        rtn = sorted(rtn, key=lambda anime: "%s/%s" % (anime[1], anime[2].zfill(3)), reverse=False)
        return rtn



if __name__ == "__main__":
    gs = EpisodeScanner("da-capo-iii")
    animes = gs.run()
    print "%s" % animes
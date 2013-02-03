#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 10:51'

URL = "http://www.animeavenue.net/"


class SuggestionScanner(BasicScanner):

    def __init__(self):
        super(SuggestionScanner, self).__init__(URL)

        self.re = re.compile(r'<center>[\s\n\r]*<a[\s\n\r]+href=[\'"][^\'">]+/category/([^\'">]+)/[\'"]>[\s\n\r]*<img[^>]*src=[\'"]([^\'">]+)[\'"][^>]*title=[\'"]Watch\s*([^\'">]+)[\'"][^>]*>[\s\n\r]*</a>[\s\n\r]*</center>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)
        for tag, img, caption in matches:
            rtn.append((tag, caption, img))
        return rtn



if __name__ == "__main__":
    gs = SuggestionScanner()
    animes = gs.run()
    print "%s" % animes
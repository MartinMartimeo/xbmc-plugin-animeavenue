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
        self.thumbnail_re = re.compile(r'style=[\'"]float:left.*[\'"]><a[\s\n\r]*.*><img[\s\n\r]*src=[\'"]([^\'">]+)[\'"].*>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        episodes = []
        matches = self.re.findall(content)
        for tag, type, episode, caption in matches:
            episodes.append((tag, type, episode, caption))
        episodes = sorted(episodes, key=lambda anime: "%s/%s" % (anime[1], anime[2].zfill(3)), reverse=False)
        match = self.thumbnail_re.search(content)
        if match:
            thumbnail = match.group(1)
        else:
            thumbnail = None
        return {'episodes': episodes, 'thumbnail': thumbnail}



if __name__ == "__main__":
    gs = EpisodeScanner("da-capo-iii")
    animes = gs.run()
    print "%s" % animes
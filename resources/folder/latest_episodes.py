#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.scanner.LatestEpisodesScanner import LatestEpisodesScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:07'


def run(aa):

    vs = LatestEpisodesScanner()
    animes = vs.run()
    for (tag, type, episode, anime) in animes:
        aa.addDirectory("anime/%s/%s/%s" % (tag, type, episode), anime)
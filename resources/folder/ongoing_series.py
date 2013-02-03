#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.scanner.OngoingAnimeScanner import OngoingAnimeScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:08'


def run(aa):

    vs = OngoingAnimeScanner()
    animes = vs.run()
    for (tag, anime, time) in animes:
        aa.addDirectory("anime/%s" % tag, anime)
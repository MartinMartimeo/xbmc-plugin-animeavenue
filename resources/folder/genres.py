#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.scanner.GenreAnimeScanner import GenreAnimeScanner
from resources.scanner.GenreScanner import GenreScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 10:05'


def run(aa, genre=None):
    if not genre:
        gs = GenreScanner()
        genres = gs.run()
        for genre in genres:
            aa.addDirectory("genres/%s" % genre, genre)
    else:
        vs = GenreAnimeScanner("http://www.animeavenue.net/?genre=%s" % genre)
        animes = vs.run()
        for (img, tag, anime) in animes:
            aa.addDirectory("anime/%s" % tag, anime, icon=img)


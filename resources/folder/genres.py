#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.scanner.AnimeScanner import AnimeScanner
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
        vs = AnimeScanner("http://www.animeavenue.net/?genre=%s" % genre)
        animes = vs.run()
        for anime in animes:
            vs.addDirectory("anime/%s" % anime)


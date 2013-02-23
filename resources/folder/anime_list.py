#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.lib import storage
from resources.scanner.AnimeScanner import AnimeScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 10:47'



def run(aa):

    vs = AnimeScanner("http://www.animeavenue.net/anime-list/")
    animes = vs.run()
    for (tag, anime) in animes:
        # Image Present?
        image = storage.get(tag)
        # Add List Item
        aa.addDirectory("anime/%s" % tag, anime, image=image)

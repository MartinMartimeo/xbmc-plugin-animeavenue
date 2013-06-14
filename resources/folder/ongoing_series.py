#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Handler for Ongoing Series
"""
from resources.lib import storage
from resources.scanner.OngoingAnimeScanner import OngoingAnimeScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:08'


def run(aa):
    """
        Show Ongoing Series
    """

    vs = OngoingAnimeScanner()
    animes = vs.run()
    for (tag, anime, time) in animes:
        # Image Present?
        image = storage.cget(tag)
        # Add List Item
        aa.addDirectory("anime/%s" % tag, anime, image=image)
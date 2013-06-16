#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Handler for Anime Suggestions
"""
from resources.lib import storage
from resources.scanner.EpisodeScanner import EpisodeScanner
from resources.scanner.SuggestionScanner import SuggestionScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 10:50'


def run(aa):
    """
        Show Anime Suggestions
    """

    vs = SuggestionScanner()
    animes = vs.run()
    aa.setProgress(max=len(animes), title=aa.getString('suggestion_loading'))
    for (tag, anime, img) in animes:
        aa.incrProgress()

        # Load Image
        image = storage.cget(tag)
        if not image:
            vs = EpisodeScanner(tag)
            image = vs.run()["thumbnail"]

        # Add List Item
        aa.addDirectory("anime/%s" % tag, anime, image=image)
    aa.closeProgress()

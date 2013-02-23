#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.lib import storage
from resources.scanner.SuggestionScanner import SuggestionScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 10:50'



def run(aa):

    vs = SuggestionScanner()
    animes = vs.run()
    for (tag, anime, img) in animes:
        # Image Present?
        image = storage.get(tag)
        # Add List Item
        aa.addDirectory("anime/%s" % tag, anime, image=image)

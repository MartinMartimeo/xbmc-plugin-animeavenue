#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Handler for Latest Episodes
"""
from resources.lib import storage
from resources.scanner.BasicScanner import NoContentProvided
from resources.scanner.EpisodeScanner import EpisodeScanner
from resources.scanner.LatestEpisodesScanner import LatestEpisodesScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:07'


def run(aa):
    """
        Show Latest Episodes
    """

    vs = LatestEpisodesScanner()
    animes = vs.run()
    aa.setProgress(maxval=len(animes), title=aa.getString('latest_loading'))
    for (tag, (type, kind), episode, anime) in animes:
        aa.incrProgress()
        # Load Image
        image = storage.cget(tag)
        if not image:
            try:
                vs = EpisodeScanner(tag)
                image = vs.run()["thumbnail"]
            except NoContentProvided:
                image = None
        aa.addVideo("anime/%s/%s/%s" % (tag, type, episode), "%s Episode %s" % (anime, episode),
                    image=image,
                    icon=aa.asMediaPath('%s.png' % kind),
                    label="[%s]" % kind,
                    info={"episode": episode, "status": kind, "genre": "Anime", "title": anime})
    aa.closeProgress()
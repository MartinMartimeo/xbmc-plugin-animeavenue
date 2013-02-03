#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.scanner.AnimeScanner import AnimeScanner
from resources.scanner.EpisodeScanner import EpisodeScanner
from resources.scanner.StreamScanner import StreamScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:28'


def run(aa, tag=None, type=None, episode=None):

    if not tag:
        vs = AnimeScanner("http://www.animeavenue.net/anime-list/")
        animes = vs.run()
        for (tag, anime) in animes:
            aa.addDirectory("anime/%s" % tag, anime)
    elif not type:
        vs = EpisodeScanner(tag)
        animes = vs.run()
        for (tag, type, episode, anime) in animes:
            aa.addVideo("anime/%s/%s/%s" % (tag, type, episode), anime)
    else:
        if not episode:
            episode = type
            type = "episode"
        ts = StreamScanner(tag, type, episode)
        streams = ts.run()
        if streams:
            aa.resolveUrl(streams[0])
        else:
            aa.failResolve()



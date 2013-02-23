#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from resources.lib import storage
from resources.scanner.AnimeScanner import AnimeScanner
from resources.scanner.BasicScanner import NoContentProvided
from resources.scanner.EpisodeScanner import EpisodeScanner
from resources.scanner.StreamScanner import StreamScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:28'


def run(aa, tag=None, type=None, episode=None):
    if not tag:
        vs = AnimeScanner("http://www.animeavenue.net/anime-list/")
        animes = vs.run()
        for (tag, anime) in animes:
            # Image Present?
            image = storage.get(tag)
            # Add List Item
            aa.addDirectory("anime/%s" % tag, anime, image=image)
    elif not type:
        vs = EpisodeScanner(tag)
        data = vs.run()
        # Save Thumbernail
        storage.set(tag, data['thumbnail'])
        # Print Episodes
        for (tag, type, episode, anime) in data['episodes']:
            aa.addVideo("anime/%s/%s/%s" % (tag, type, episode), anime,
                        info={"episode": episode, "genre": "Anime", "title": anime})
    else:
        try:
            if not episode:
                episode = type
                type = "episode"
            ts = StreamScanner(tag, type, episode)
            streams = ts.run()
            if streams:
                aa.resolveUrl(streams[0])
            else:
                aa.failResolve()
        except NoContentProvided:
            aa.failResolve(aa.getString("no_video"))




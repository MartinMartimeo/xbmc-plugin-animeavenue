#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import urllib
import urlparse
import sys

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 08:36'

import xbmc, xbmcplugin, xbmcgui, xbmcaddon

# -- Constants ----------------------------------------------
ADDON_ID = 'plugin.video.animeavenue'

# -- I18n ---------------------------------------------------
language = xbmcaddon.Addon(id='plugin.video.tagesschau').getLocalizedString
strings = {'latest_episodes': language(70010),
           'anime_suggestions': language(70020),
           'ongoing_series': language(70030),
           'anime_list': language(70040),
           'genres': language(70050)}


class AnimeAvenue(object):
    """

    """

    def __init__(self):
        super(AnimeAvenue, self).__init__()

    def addDirectory(self, tag, caption):
        """
            Adds a Directory
        """
        url = 'plugin://' + ADDON_ID + '/?tag=' + tag
        li = xbmcgui.ListItem(caption)
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)

    def showRootDirectory(self):
        """
            Shows the Items in Root Directory
        """
        for tag in ["latest_episodes", "anime_suggestions", "ongoing_series", "anime_list", "genres"]:
            self.addDirectory(tag, strings[tag])


aa = AnimeAvenue()
aa.showRootDirectory()


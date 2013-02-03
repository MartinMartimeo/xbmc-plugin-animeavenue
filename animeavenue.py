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

# Framework based on xbmc-plugin.video.tagesschau

# -- Constants ----------------------------------------------
ADDON_ID = 'plugin.video.animeavenue'

# -- Settings -----------------------------------------------
settings = xbmcaddon.Addon(id=ADDON_ID)

# -- I18n ---------------------------------------------------
language = xbmcaddon.Addon(id=ADDON_ID).getLocalizedString
strings = {'latest_episodes': language(70010),
           'anime_suggestions': language(70020),
           'ongoing_series': language(70030),
           'anime_list': language(70040),
           'genres': language(70050)}


def get_params():
    paramstring = sys.argv[2]
    params = urlparse.parse_qs(urlparse.urlparse(paramstring).query)

    for key in params:
        params[key] = params[key][0]
    return params
params = get_params()

class AnimeAvenue(object):
    """

    """

    def __init__(self):
        super(AnimeAvenue, self).__init__()

    def addDirectory(self, folder, caption):
        """
            Adds a Directory
        """
        url = 'plugin://' + ADDON_ID + '/?folder=' + folder
        li = xbmcgui.ListItem(caption)
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)

    def showFolder(self, folder):
        """
            Shows a folder
        """
        args = folder.split("/")
        if not args:
            return self.showRootDirectory()
        arg = args[0]
        folder_module = __import__("resources.folder.%s" % arg)
        folder_module.run(self, *args[1:])

    def showRootDirectory(self):
        """
            Shows the Items in Root Directory
        """
        for tag in ["latest_episodes", "anime_suggestions", "ongoing_series", "anime_list", "genres"]:
            self.addDirectory(tag, strings[tag])


aa = AnimeAvenue()
folder = params.get("folder")
if folder:
    aa.showFolder(folder)
else:
    aa.showRootDirectory()

xbmcplugin.endOfDirectory(int(sys.argv[1]))

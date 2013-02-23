#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import os
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

# -- Pathes ----------------------------------------------
PLUGINDIR = settings.getAddonInfo('path')
RESOURCESDIR = os.path.join(PLUGINDIR, "resources")
MEDIADIR = os.path.join(RESOURCESDIR, "media")

# -- I18n ---------------------------------------------------
language = settings.getLocalizedString
strings = {'latest_episodes': language(70010),
           'anime_suggestions': language(70020),
           'ongoing_series': language(70030),
           'anime_list': language(70040),
           'genres': language(70050),
           'name': language(10000),
           'no_video': language(50010),
           'suggestion_loading': language(50020),
           'latest_loading': language(50030)}


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

    def addVideo(self, uri, caption, image=None, icon=None, info=None):
        """
            Adds a Video Entry
            :param caption: Caption to be displayed
            :param uri: The folder uri
            :param image: The Thumbernail Image (optional)
            :param icon: The Icon Image (optional)
            :param info: Additional Data passed to info (optional)
        """
        url = 'plugin://' + ADDON_ID + '/?folder=' + uri
        if image:
            li = xbmcgui.ListItem(caption, thumbnailImage=image)
        else:
            li = xbmcgui.ListItem(caption)
        li.setProperty('IsPlayable', 'true')

        # Set Icon
        if icon:
            li.setIconImage(icon)

        # Set Info
        if not info:
            info = {}
        li.setInfo(type="Video", infoLabels=info)

        # Add as Item
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=False)

    def addDirectory(self, folder, caption, image=None):
        """
            Adds a Directory
            :param caption: Caption to be displayed
            :param folder: The folder uri
            :param image: The Thumbernail Image (optional)
        """
        url = 'plugin://' + ADDON_ID + '/?folder=' + folder
        if image:
            li = xbmcgui.ListItem(caption, thumbnailImage=image)
        else:
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
        resources_module = __import__("resources.folder.%s" % arg)
        folder_module = getattr(resources_module, "folder")
        arg_module = getattr(folder_module, arg)
        arg_module.run(self, *args[1:])

    def showRootDirectory(self):
        """
            Shows the Items in Root Directory
        """
        for tag in ["latest_episodes", "anime_suggestions", "ongoing_series", "anime_list", "genres"]:
            self.addDirectory(tag, strings[tag])

    def resolveUrl(self, url):
        """
            Play Video
        """
        listitem = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listitem)

    def failResolve(self, message=None):
        """
            Just fail :(
        """
        listitem = xbmcgui.ListItem(path="")
        xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=False, listitem=listitem)

        if message:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok(strings['name'], message)

    def getString(self, key):
        return strings[key]

    def setProgress(self, max, title):

        dialog = xbmcgui.DialogProgress()
        dialog.create(self.getString('name'), title)
        self.progress = {"value": 0, "max": max, "dialog": dialog}

    def incrProgress(self, title=None):

        self.progress["value"] += 1
        self.progress["dialog"].update(self.progress["value"] * 100 / self.progress["max"])

    def closeProgress(self):

        self.progress["dialog"].close()
        self.progress = None

    def asMediaPath(self, path):

        return os.path.join(MEDIADIR, path)


aa = AnimeAvenue()
folder = params.get("folder")
if folder:
    aa.showFolder(folder)
else:
    aa.showRootDirectory()

xbmcplugin.endOfDirectory(int(sys.argv[1]))

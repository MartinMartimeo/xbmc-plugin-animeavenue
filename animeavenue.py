#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import os
import urlparse
import sys
from resources.scanner.BasicScanner import NoContentProvided

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 08:36'

import xbmc, xbmcplugin, xbmcgui, xbmcaddon

# Framework based on xbmc-plugin.video.tagesschau

# -- Constants ----------------------------------------------
from resources import ADDON_ID

# -- Settings -----------------------------------------------
settings = xbmcaddon.Addon(id=ADDON_ID)

# -- Pathes ----------------------------------------------
PLUGINDIR = settings.getAddonInfo('path')
RESOURCESDIR = os.path.join(PLUGINDIR, "resources")
MEDIADIR = os.path.join(RESOURCESDIR, "media")

# -- I18n ---------------------------------------------------
language = settings.getLocalizedString
strings = {'latest_episodes': language(30410),
           'anime_suggestions': language(30420),
           'ongoing_series': language(30430),
           'anime_list': language(30440),
           'genres': language(30450),
           'name': language(30000),
           'no_video': language(30110),
           'upcoming_episode': language(30120),
           'suggestion_loading': language(30210),
           'latest_loading': language(30220)}


def get_params():
    """
        Parse parameters from url
    """
    paramstring = sys.argv[2]
    params = urlparse.parse_qs(urlparse.urlparse(paramstring).query)

    for key in params:
        params[key] = params[key][0]
    return params


params = get_params()


class AnimeAvenue(object):
    """
        Main Class providing all the bindings to xbmc/xbmcgui
    """

    def __init__(self):
        super(AnimeAvenue, self).__init__()

    def createListItem(self, caption, image, icon):
        """
            Create an xbmcgui.Lisitem
            :param caption: Caption of Item
            :param image: The Thumbernail Image (optional)
            :param icon: The Icon Image (optional)
        """
        if image and icon:
            li = xbmcgui.ListItem(caption, thumbnailImage=image, iconImage=icon)
        elif image:
            li = xbmcgui.ListItem(caption, thumbnailImage=image)
        elif icon:
            li = xbmcgui.ListItem(caption, iconImage=icon)
        else:
            li = xbmcgui.ListItem(caption)
        return li

    def addVideo(self, uri, caption, label=None, image=None, icon=None, info=None):
        """
            Adds a Video Entry
            :param caption: Caption to be displayed
            :param label: Additional label to be displayed
            :param uri: The folder uri
            :param image: The Thumbernail Image (optional)
            :param icon: The Icon Image (optional)
            :param info: Additional Data passed to info (optional)
        """
        url = 'plugin://' + ADDON_ID + '/?folder=' + uri
        li = self.createListItem(caption=caption, image=image, icon=icon)
        li.setProperty('IsPlayable', 'true')

        # Label2
        if label:
            if label.startswith("[") and label.endswith("]"):
                li.setLabel2(label)
            else:
                li.setLabel2("[%s]" % label)

        # Set Info
        if not info:
            info = {}
        li.setInfo("video", infoLabels=info)

        # Add as Item
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=False)

    def addDirectory(self, folder, caption, image=None, icon=None):
        """
            Adds a Directory
            :param caption: Caption to be displayed
            :param folder: The folder uri
            :param image: The Thumbernail Image (optional)
            :param icon: The Icon Image (optional)
        """
        url = 'plugin://' + ADDON_ID + '/?folder=' + folder
        li = self.createListItem(caption=caption, image=image, icon=icon)
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
        try:
            arg_module.run(self, *args[1:])
        except NoContentProvided:
            aa.failResolve()

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

    def setProgress(self, maxval, title):
        """
            Show a Dialog Progress

            :param maxval: Absolute maximum value
            :param title: Title of Dialog
        """
        dialog = xbmcgui.DialogProgress()
        dialog.create(self.getString('name'), title)
        self.progress = {"value": 0, "max": maxval, "dialog": dialog}

    def incrProgress(self):
        """
            Increase absolute value of current dialog progress
        """
        self.progress["value"] += 1
        self.progress["dialog"].update(self.progress["value"] * 100 / self.progress["max"])

    def closeProgress(self):
        """
            Close current dialog progress
        """
        self.progress["dialog"].close()
        self.progress = None

    def asMediaPath(self, path):
        """
            Create path relative to media dir

            :param path: relative path from media root
        """
        return os.path.join(MEDIADIR, path)


aa = AnimeAvenue()
folder = params.get("folder")
if folder:
    aa.showFolder(folder)
else:
    aa.showRootDirectory()

xbmcplugin.endOfDirectory(int(sys.argv[1]))

#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Implements a cache get and cache set value and uses storageserver if available
"""
from resources import ADDON_ID

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '23.02.13 - 22:37'

try:
    import StorageServer

    cache = StorageServer.StorageServer(ADDON_ID, 7200)
except ImportError:
    StorageServer = None

    cache = {}


def cget(key):
    """
    Get a String from Cache
    :param key:
    :return:
    """

    # None
    if cache is None:
        return None

    # Dict
    if isinstance(cache, dict):
        return key in cache and cache[key] or None

    # StorageServer
    return cache.get(key)


def cset(key, value):
    """
    Set a String from Cache
    :param key:
    :return:
    """

    # None
    if cache is None:
        return None

    # Dict
    if isinstance(cache, dict):
        cache[key] = value
        return True

    # StorageServer
    return cache.set(key, value)




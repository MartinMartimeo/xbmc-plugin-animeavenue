#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '23.02.13 - 22:37'

try:
    import StorageServer
except:
    cache = None
cache = StorageServer.StorageServer("plugin.video.animeavenue", 7200)


def get(key):
    """
    Get a String from Cache
    :param key:
    :return:
    """
    if not cache:
        return None

    return cache.get(key)


def set(key, value):
    """
    Set a String from Cache
    :param key:
    :return:
    """
    if not cache:
        return None

    return cache.set(key, value)



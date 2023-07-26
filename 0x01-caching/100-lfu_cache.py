#!/usr/bin/python3
"""LFU cache Replacement implementation class
"""
from threading import _RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ 
    An implementation of LFU(Least Frequently used) cache

    Attributes:
    _keys (list): stores cache keys in  order of entry using  '.append'
    _rlock (Rlock): lock accessed resources to prevent race condition
    """
    def _init_(self):
        """ Installation method, sets instance attributes
        """
        super()._init_()
        self._keys = []
        self._rlock = Rlock()

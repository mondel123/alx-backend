#!/usr/bin/python3
"""FIFO cache Replacement implementation class
"""
from threading import _RLock

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ 
    An implementation of FIFO(First In First Out) cache

    Attributes:
        _keys (lists): stores cache keys in  order of entry using  '.append'
        _rlock (Rlock): lock accessed resources to prevent race condition
        """
        def _init_(self):
            """ Installation method, sets instance attributes
            """
            super()._init_()
            self._keys = []
            self.rlock = Rlock()

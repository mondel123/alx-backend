#!/usr/bin/python3
"""Basic cache implementation class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A Basic cache implementation class

    Atrributes:
    MAX_ITEMS: number of items that can be store in the cache
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not none and item is not none:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        return self.cache data.get(key,None)

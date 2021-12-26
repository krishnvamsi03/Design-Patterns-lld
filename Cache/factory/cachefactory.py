from storage.HashMapBase import HashMapBase
from policies.LRUPolicy import LRU 

class CacheFactory:
    def __init__(self, storage, eviction):
        self.storage = storage
        self.eviction = eviction

    def getStorage(self):
        if self.storage.lower() == "HashMap".lower():
            return HashMapBase(5)
        return HashMapBase(3)

    def getEviction(self):
        if self.eviction.lower() == "LRU".lower():
            return LRU()
        return LRU()
from factory.cachefactory import CacheFactory


class Cache:
    def __init__(self, storage, eviction):
        self.cache = CacheFactory(storage, eviction)
        self.storage = self.cache.getStorage()
        self.eviction = self.cache.getEviction()

    def put(self, key, value):
        try:
            self.storage.put(key, value)
            self.eviction.accessed(key)
        except Exception as error:
            print(error)
            print("Initiating eviction policy")
            removedKey = self.eviction.evict()
            print("Removed key is ", removedKey)
            self.storage.remove(removedKey)
            self.put(key, value)

    def get(self, key):
        try:
            val = self.storage.get(key)
            self.eviction.accessed(key)
            return val
        except Exception as error:
            print(error)

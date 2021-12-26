from storage.storage import Storage
import logging


class HashMapBase(Storage):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.map = {}

    def put(self, key, value):
        if key not in self.map:
            if not self.isFull():
                self.map[key] = value
            else:
                raise Exception("cache already full")
        else:
            print("Key already present")

    def get(self, key):
        if key in self.map:
            return self.map[key]
        else:
            raise Exception("Key not present")

    def remove(self, key):
        if key in self.map:
            del self.map[key]
        else:
            raise Exception("Key not present")

    def isFull(self):
        return len(self.map) == self.capacity

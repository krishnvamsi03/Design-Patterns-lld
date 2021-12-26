from abc import ABC, abstractmethod

class KeyValueStore(ABC):

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod 
    def search(self, attr, val):
        pass

    @abstractmethod
    def keys(self):
        pass
    
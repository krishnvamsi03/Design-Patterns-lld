from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, capacity):
        self.capacity = capacity

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def remove(self, key):
        pass

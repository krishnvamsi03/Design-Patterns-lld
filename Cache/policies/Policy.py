from abc import ABC, abstractmethod


class Policy(ABC):

    @abstractmethod
    def evict(self):
        pass

    @abstractmethod
    def accessed(self, key):
        pass

from policies.Policy import Policy
from utility.LinkedList import DoublyLinkedList


class LRU(Policy):
    def __init__(self):
        self.linkedList = DoublyLinkedList()
        self.map = {}

    def evict(self):
        key = self.linkedList.deleteNode()
        if key in self.map:
            del self.map[key]
            return key
        else:
            raise Exception("Fail to evict from mapper")
            return -1

    def accessed(self, key):
        if key in self.map:
            self.linkedList.addElementToLast(self.map[key])
        else:
            node = self.linkedList.createElement(key)
            if node:
                self.map[key] = node
            else:
                raise Exception("Fail to create element in LRU policy")

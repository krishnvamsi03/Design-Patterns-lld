from storage.keyvalue import KeyValueStore
from CustomException.exception import KeyNotFoundException


class HashMapStore(KeyValueStore):
    def __init__(self):
        self.store = {}
        self.attributes = {}
        self.attributeKeyMap = {}

    # Overriding put
    def put(self, key, value: dict):
        for attribute, val in value.items():
            if attribute not in self.attributes:
                self.attributes[attribute] = type(val)
            elif attribute in self.attributes and type(val) != self.attributes[attribute]:
                raise TypeError("Expected {} but got {}".format(
                    self.attributes[attribute], type(val)))

        for attr, val in value.items():
            if attr not in self.attributeKeyMap:
                self.attributeKeyMap[attr] = {attr}
            else:
                self.attributeKeyMap[attr].add(attr)

        self.store[key] = value

    # Overriding get
    def get(self, key):
        if key in self.store:
            return self.valueToCsv(self.store[key])
        return -1

    # Overriding delete
    def delete(self, key):
        if key in self.store:
            for attr, val in self.store[key]:
                del self.attributes[attr]
            del self.store[key]
            return "delete successfully"
        else:
            raise KeyNotFoundException()

    # Overriding search
    def search(self, attr, val):
        res = []
        if attr in self.attributeKeyMap:
            for key in self.attributeKeyMap[attr]:
                if self.store[key][attr] == val:
                    res.append(key)
        return res

    # Overriding keys
    def keys(self):
        return self.store.keys()

    def valueToCsv(self, value):
        res = ""
        for attribute, val in value.items():
            res += attribute + ":" + str(val) + ","
        res = res[:-1]
        return res

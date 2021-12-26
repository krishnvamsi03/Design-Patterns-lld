from Main import Cache
import random

if __name__ == "__main__":
    obj = Cache("HashMap", "LRU")

    for i in range(1, 8):
        obj.put(i, random.randint(1000, 100000))

    print("current state of cache is ", obj.storage.map)
    print("***********")
    for i in range(1, 6):
        print(obj.get(random.randint(3, 7)))
        obj.put(i, random.randint(1000, 100000))
        print("current state of cache is ", obj.storage.map)

from storage.hashmap import HashMapStore
from constants.MainConstants import Actions
from CustomException.exception import *


class Main():
    def __init__(self):
        self.store = HashMapStore()

    def getInputs(self):
        choice = ""
        while Actions(choice.lower()) != Actions.EXIT:
            inp = list(map(str, input().split(" ")))
            try:
                choice = inp[0]
                if Actions(choice.lower()) == Actions.PUT:
                    key = inp[1]
                    value = {}
                    n = len(inp)
                    for i in range(2, n - 1, 2):
                        if i + 1 < n:
                            value[inp[i]] = inp[i + 1]
                        else:
                            raise InputErrorException("In valid input format")
                    self.store.put(key, value)
                elif Actions(choice.lower()) == Actions.GET:
                    if len(inp) < 1 or len(inp[1]) == 0:
                        raise InputErrorException(
                            "In valid input for key or key not provided")
                    else:
                        key = inp[1]
                        print(self.store.get(key))
                elif Actions(choice.lower()) == Actions.DELETE:
                    if len(inp) < 1 or len(inp[1]) == 0:
                        raise InputErrorException(
                            "In valid input for key or key not provided")
                    else:
                        key = inp[1]
                        print(self.store.delete(key))
                elif Actions(choice.lower()) == Actions.KEYS:
                    print(self.store.keys())
            except TypeError as error:
                print(error)
            except InputErrorException as error:
                print(error)
            except Exception as error:
                print(error)


class InputErrorException(Exception):
    def __init__(self, message):
        self.message = message

    
class KeyNotFoundException(Exception):
    def __init__(self):
        self.message = "Key not found"
class NotRand:
    def __init__(self, values):
        self._values = values
        self._index = 0
        self._len = len(values)

    def next(self):
        if self._index == self._len: self._index = 0
        value = self._values[self._index]
        self._index += 1
        return value

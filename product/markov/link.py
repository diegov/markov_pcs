import random

#TODO Rename
class Link:
    """
    This is a simple convinience class to handle sequences of values which
    can be split in two. It's used when creating sequences where the total
    length of the sequence includes both the key and the continuation, so 
    we split at point x, and we get the key on the left of the split point
    and the continuation on the right.
    """
    def __init__(self, values):
        self._values = values
        self._length = len(values)

    def __len__(self):
        return self._length

    @property
    def length(self):
        return self._length

    @property
    def values(self):
        return self._values

    def split_at(self, index):
        left = self._values[0:index]
        right = self._values[index:len(self._values)]
        return [Link(left), Link(right)]

    @staticmethod
    def from_s(value):
        #TODO: There has to be a better way
        chars = []
        for c in value:
            chars.append(c)

        return Link(chars)

    def __eq__(self, other):
        if not isinstance(other, Link): return False
        if self._length != other._length:
            return False

        for i in range(0, self._length):
            if self._values[i] != other._values[i]:
                return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        initial = self._length * 10000000
        factor = 1
        for v in self._values:
            initial += (hash(v) * factor)
            factor *= 13

        return initial

    def __repr__(self):
        return "Link: " + str(self._values)


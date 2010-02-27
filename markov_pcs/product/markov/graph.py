from bucket import *
from types import ListType
from link import Link

class Graph:

    def __init__(self, split_at, random):
        self._graph = {}
        self._split_at = split_at
        self._random = random

    def add(self, sequence):
        #We take Link objects or normal lists
        if isinstance(sequence, Link):
            left, right = sequence.split_at(\
                self._split_at)
        else:
            left = sequence[:self._split_at]
            right =  sequence[self._split_at:]

        self._increment_count(left, right)

    def _increment_count(self, left, right):
        dict = self.get_dict(left)

        if not dict.has_key(right):
            dict[right] = 0
        val = dict[right]
        val += 1
        dict[right] = val

    def get_dict(self, key):
        #TODO: Use default dictionary?
        if not self._graph.has_key(key):
            self._graph[key] = Bucket()
        
        return self._graph[key]
    
    @property
    def sequences(self):
        return self._graph.keys()
    
    @property
    def dict(self):
        return self._graph

    def suggest_continuation(self, sequence, exclude = None):
        if not self._graph.has_key(sequence): return  None

        dct = self._graph[sequence]
        weights = dct.weights
        key = self.pick_by_weighted_random(weights, exclude)
        return key

    def pick_by_weighted_random(self, weights, exclude):
        max_val = -1
        max_key = None

        if exclude == None:
            exclude = IncludeNone()
        elif not (type(exclude) is set):
            exclude = set(exclude)
        
        #TODO: use set intersection here instead?
        for k in weights.keys():
            #TODO: There must be a more readable method to use here
            if exclude.issuperset([k]):
                continue

            weight = weights[k]
            if weight == None:
                continue
        
            val = self._random.next() * weight
            if val > max_val:
                max_val = val
                max_key = k
        
        if max_key:
            return max_key

        return None

    def __repr__(self):
        return 'Graph: ' + str(self._graph)

class IncludeNone:
    def issuperset(self, val):
        return False;


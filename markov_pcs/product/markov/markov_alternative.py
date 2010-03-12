from graph import *
from link import *
from std_random import *

class MarkovAlternative:
    def __init__(self, sequence_length, rand):
        if sequence_length <= 0: raise ArgumentError

        self._seq_len = sequence_length
        r = rand
        self._graph = Graph(sequence_length, r)

    @property
    def graph(self):
        return self._graph

    @property
    def seq_len(self):
        return self._seq_len

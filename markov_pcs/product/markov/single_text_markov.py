from link import *
from graph import *
from std_random import *

class SingleTextMarkov:
    def __init__(self, sequence_length, rand = StdRandom()):
        if sequence_length <= 0: raise ArgumentError

        self._seq_len = sequence_length
        r = rand
        self._graph = Graph(sequence_length, r)

    def add_text_block(self, text):
        t = []
        for c in text:
            t.append(c)
            if len(t) > self._seq_len:
                if len(t) > (self._seq_len + 1):
                    t = t[1:len(t)]
                l = Link(t)
                self._graph.add(l)

    @property
    def graph(self):
        return self._graph

    def slice_text(self, text_to_slice):
        segment = text_to_slice[ \
            len(text_to_slice) - self._seq_len:]
        if len(segment) < self._seq_len: return None
        return segment

    def __repr__(self):
        return "Single Text Markov: " + str(self._graph)


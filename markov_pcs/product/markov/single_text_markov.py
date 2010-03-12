from link import *
from graph import *
from std_random import *
from markov_alternative import MarkovAlternative

class SingleTextMarkov(MarkovAlternative):
    def __init__(self, sequence_length, rand = StdRandom()):
        MarkovAlternative.__init__(self, sequence_length, rand)

    def add_text_block(self, text):
        t = []
        for c in text:
            t.append(c)
            if len(t) > self._seq_len:
                if len(t) > (self._seq_len + 1):
                    t = t[1:len(t)]
                l = Link(t)
                self._graph.add(l)

    def __repr__(self):
        return "Single Text Markov: " + str(self._graph)


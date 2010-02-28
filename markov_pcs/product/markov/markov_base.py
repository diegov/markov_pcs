from link import *
from graph import *
from std_random import *
from text_stream import *
from single_text_markov import *
from types import ListType
import random

class MarkovBase:
    def __init__(self, stream, alternatives):
        self._stream = stream
        self._alternatives = alternatives
        #master graph
        self._graph = self._alternatives[0].graph

    def build_seq(self, length):
        result = None
        seqs = []

        #using first graph
        for seq in self._graph.sequences:
            seqs.append(seq)

        #pick sequences in random order
        random.shuffle(seqs)

        for seq in seqs:
            #stream is an immutable object, good for backtracking
            start = self._stream.append(seq)
            result = self.build_part(start, length - len(start))
            if result != None: break

        return result

    def build_part(self, current_value, remaining):
        if remaining <= 0: return current_value

        result = None
        for alt in self._alternatives:
            segment = current_value.segment_for(alt)
            #was alt.slice_text(current_value)
            if segment == None: continue

            excluded = set()

            while True:
                val = alt.graph.suggest_continuation(segment, excluded)
                if val == None: break 

                #immutable stream, returns None if the value cannot be appended
                new_value = current_value.append(val)
                if new_value != None:
                    rest = self.build_part(new_value, (remaining - len(val)))
                    if rest != None:
                        result = rest
                        break

                excluded.add(val)

            if result != None: break

        return result


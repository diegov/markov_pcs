from link import *
from graph import *
from std_random import *
from single_text_markov import *
from types import ListType
import random

class TextMarkov:  
    def __init__(self, lengths):
        b = []
        b.extend(lengths)
        b.sort(reverse=True)
        
        if len(b) == 0: raise Exception('You must provide at least one sequence length', '')

        self._alternatives = []
        for l in b:
            self._alternatives.append(SingleTextMarkov(l))

        #master graph
        self._graph = self._alternatives[0].graph

    def build_seq(self, length):
        result = None
        seqs = []

        #using first graph
        for s in self._graph.sequences:
            seqs.append(s)
            
        random.shuffle(seqs)

        for s in seqs:
            start = "".join(s.values)
            result = self.build_part(start, length - len(start))
            if result != None: break

        return result

    def build_part(self, current_value, remaining):
        if remaining <= 0: return current_value

        result = None
        for alt in self._alternatives:
            segment = alt.slice_text(current_value)
            if segment == None: continue

            excluded = set()

            while True:
                new_seq = Link.from_s(segment)
                val = alt.graph.suggest_continuation(new_seq, excluded)
                if val == None: break 

                new_value = ''.join(val.values)
                rest = self.build_part(current_value + new_value, (remaining - len(new_value)))
                if rest != None:
                    result = rest
                    break

                excluded.add(val)

            if result != None: break

        return result

    def add_text_block(self, text):
        for a in self._alternatives:
            a.add_text_block(text)


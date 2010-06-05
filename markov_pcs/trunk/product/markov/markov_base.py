from link import *
from graph import *
from std_random import *
from text_stream import *
from single_text_markov import *
from types import ListType
import random

class StackFrame:
    def __init__(self, current_value, remaining, alternatives, rand):
        self.excluded = set()
        self.current_alt_index = -1
        self.current_value = current_value
        self.remaining = remaining
        if rand != None:
            self.alternatives = []
            self.alternatives.extend(alternatives)
            rand.shuffle(self.alternatives)
        else: self.alternatives = alternatives

class MarkovBase:
    def __init__(self, stream, alternatives, randomise_alternatives=False, rand=None):
        self._stream = stream
        self._alternatives = alternatives
        self._randomise_alternatives = randomise_alternatives
        self._rand = rand
        #master graph
        self._graph = self._alternatives[0].graph

    def build_seq(self, length):
        result = None
        seqs = []

        #using first graph
        for seq in self._graph.sequences:
            seqs.append(seq)

        #pick sequences in random order
        self._rand.shuffle(seqs)

        print 'Total seqs:', len(seqs)

        for seq in seqs:
            #stream is an immutable object, good for backtracking
            print 'Using seq:', seq
            start = self._stream.append(seq)
            result = self.build_part(start, length - len(start))
            if result != None and len(result) >= length: break

        return result

    def build_part(self, current_value, remaining):
        if remaining <= 0: return current_value

        stack = []
        rnd = None
        if self._randomise_alternatives: rnd = self._rand
        current_frame = StackFrame(current_value, remaining, self._alternatives, rnd)
        stack.append(current_frame)

        while current_frame != None:
            if current_frame.remaining <= 0: break

            current_frame.current_alt_index += 1
            if current_frame.current_alt_index >= len(self._alternatives):
                if len(stack) > 0: current_frame = stack.pop()
                else: break
                continue

            alt = current_frame.alternatives[current_frame.current_alt_index]
            segment = current_frame.current_value.segment_for(alt)
            #was alt.slice_text(current_value)
            if segment == None: continue

            while True:
                val = alt.graph.suggest_continuation(segment, current_frame.excluded)
                if val == None: break 

                #TODO: rename excluded to 'done'?
                current_frame.excluded.add(val)
                
                new_value = current_frame.current_value.append(val)
                if new_value != None:
                    current_frame = StackFrame(new_value, (current_frame.remaining - len(val)), \
                                                   self._alternatives, rnd)
                    stack.append(current_frame)
                    break
        
        if current_frame == None: return None
        return current_frame.current_value

from link import *
from graph import *
from std_random import *
from text_stream import *
from single_text_markov import *
from markov_base import *
from std_random import StdRandom
from types import ListType
import random

class TextMarkov(MarkovBase):  
    def __init__(self, lengths, rand=StdRandom()):
        b = []
        b.extend(lengths)
        b.sort(reverse=True)

        if len(b) == 0: raise Exception('You must provide at least one sequence length', '')

        alternatives = []
        for l in b:
            alternatives.append(SingleTextMarkov(l, rand=rand))

        MarkovBase.__init__(self, TextStream(''), alternatives, True, rand=rand)
        
    def add_text_block(self, text):
        for a in self._alternatives:
            a.add_text_block(text)

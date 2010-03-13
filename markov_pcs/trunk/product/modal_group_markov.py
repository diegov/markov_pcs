from markov.markov_alternative import MarkovAlternative
from markov.markov_base import MarkovBase
from markov.std_random import StdRandom
from note_stream import NoteStream
from modal_group_alternative import ModalGroupAlternative
from markov.std_random import StdRandom

class ModalGroupMarkov(MarkovBase):
    def __init__(self, tone_system, note_lengths, rand=StdRandom()):
        alternatives = []

        for l in note_lengths:
            m = ModalGroupAlternative(tone_system, l, rand=rand)
            alternatives.append(m)

        MarkovBase.__init__(self, NoteStream(tone_system), alternatives, True, rand=rand)

    def add_notes(self, notes):
        for alternative in self._alternatives:
            alternative.add_notes(notes)

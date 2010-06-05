from modal_group import *
from markov.markov_alternative import MarkovAlternative
from markov.markov_base import MarkovBase
from markov.std_random import StdRandom

class ModalGroupAlternative(MarkovAlternative):
    def __init__(self, tone_system, note_sequence_length, rand = StdRandom()):
        #actual markov sequence length is always 2: 
        #previous mode, next mode. The no of notes in each modal group
        #is what we control here
        MarkovAlternative.__init__(self, 1, rand)
        self._tone_system = tone_system
        self._note_seq_len = note_sequence_length

    def add_notes(self, notes):
        length = len(notes)
        previous_group = None
        for i in range(self._note_seq_len, length + 1):
            current_notes = notes[i - self._note_seq_len : i]
            current_group = ModalGroup(self._tone_system, \
                                           pcs=self._tone_system.get_pitch_class_set(current_notes))
            if previous_group != None:
                l = Link([previous_group, current_group])
                self._graph.add(l)

            previous_group = current_group
            
    def __repr__(self):
        return "Modal Group Alternative: " + str(self._graph)

    @property
    def note_seq_len(self):
        """
        This is different from seq_len, which is always one since the sequence
        element is the modal group, not the notes. 
        This one is the actual count of notes in a sequence
        """
        return self._note_seq_len

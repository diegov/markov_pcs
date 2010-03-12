from markov.link import *
from modal_group import *

class NoteStream:
    def __init__(self, tone_system, \
                     local_notes = [], previous_stream = None, \
                     group_length = 2):
        self._tone_system = tone_system
        self._notes = local_notes
        self._previous_stream = previous_stream
        self._group_length = group_length

    def append(self, link):
        """
        Assumes the link object contains a single PitchClassSet or
        a set of notes
        """

        vals = link.values

        #Hacky, isinstance() now seems like a better option
        if not (len(vals) == 1 and hasattr(vals[0], "is_superset_of")):
            return NoteStream(self._tone_system, vals, self)

        group = ModalGroup(self._tone_system, pcs=vals[0])
        notes = self._segment(self._group_length)
        new_notes = group.generate_notes(notes)

        if new_notes == None: return None

        notes_to_add = new_notes[self._group_length:]
        return NoteStream(self._tone_system, notes_to_add, self)

    def segment_for(self, alternative):
        seg = self._segment(alternative.seq_length)
        if seg == None: return None
        
        return Link([ModalGroup(self._tone_system, notes=seg)])
                
    def _segment(self, seq_len):
        segment = self._notes[len(self._notes) - seq_len:]
        if len(segment) < seq_len:
            if self._previous_stream == None: return None
            prefix = self._previous_stream._segment(seq_len - len(segment))
            if prefix == None: return None
            
            segment = prefix + segment

        return segment

    def __len__(self):
        initial = len(self._notes)
        if self._previous_stream != None:
            initial += len(self._previous_stream)
        return initial

    @property
    def notes(self):
        val = []
        if self._previous_stream != None:
            val.extend(self._previous_stream.notes)
        val.extend(self._notes)

        return val

    def __repr__(self):
        val = str(self._notes)
        if self._previous_stream != None:
            val = str(self._previous_stream) + val
        return val


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
        TODO: Overlap is currently hardcoded to be one note, it should 
        be configurable
        """

        vals = link.values

        if not len(vals) == 1:
            return NoteStream(self._tone_system, vals, self)

        pcs = None

        #a Pcs, ModalGroup or list of notes is valid here
        if isinstance(vals[0], ModalGroup):
            pcs = vals[0].pcs
        else:
            #Hacky, isinstance() now seems like a better option
            if not hasattr(vals[0], "is_superset_of"):
                #Assume it's a list of notes with a single note then
                return NoteStream(self._tone_system, vals, self)
            pcs = vals[0]

        group = ModalGroup(self._tone_system, pcs=pcs)
        if len(self) >= self._group_length:
            notes = self._segment(self._group_length -1)
            notes_to_discard = self._group_length -1
        else: 
            notes = [0]
            notes_to_discard = 0

        new_notes = group.generate_notes(notes)

        if new_notes == None: return None

        notes_to_add = new_notes[notes_to_discard:]
        return NoteStream(self._tone_system, notes_to_add, self)

    def segment_for(self, alternative):
        seg = self._segment(alternative.note_seq_len)
        if seg == None: return None
        
        return Link([ModalGroup(self._tone_system, notes=seg, keep_notes=False)])
                
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
        prev = self._previous_stream
        #recursive approach was blowing the stack
        while prev != None:
            initial += len(prev._notes)
            prev = prev._previous_stream
        return initial

    @property
    def notes(self):
        #changed from recursive call
        val = []
        prev = self
        while prev != None:
            val_next = val
            val = []
            val.extend(prev._notes)
            val.extend(val_next)
            prev = prev._previous_stream

        return val

    def __repr__(self):
        val = str(self._notes)
        if self._previous_stream != None:
            val = str(self._previous_stream) + val
        return val


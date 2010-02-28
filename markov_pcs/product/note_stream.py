from markov.link import *
from modal_group import *

class NoteStream:
    def __init__(self, tone_system, \
                     local_notes = [], previous_stream = None):
        self._tone_system = tone_system
        self._notes = local_notes
        self._previous_stream = previous_stream

    def append(self, link):
        #We get Link objects here, we assume they contain string characters
        return NoteStream(link.values, self)

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

    def __repr__(self):
        val = str(self._notes)
        if self._previous_stream != None:
            val = str(self._previous_stream) + val
        return val


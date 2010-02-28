from link import *

class TextStream:
    def __init__(self, local_text = '', previous_stream = None):
        self._text = local_text
        self._previous_stream = previous_stream

    def append(self, link):
        #We get Link objects here, we assume they contain string characters
        return TextStream("".join(link.values), self)

    def __len__(self):
        initial = len(self._text)
        if self._previous_stream != None:
            initial += len(self._previous_stream)
        return initial

    def segment_for(self, alternative):
        seg = self._segment(alternative.seq_len)
        if seg == None: return None
        return Link.from_s(seg)

    def _segment(self, seq_len):
        segment = self._text[len(self._text) - seq_len:]
        if len(segment) < seq_len:
            if self._previous_stream == None: return None
            prefix = self._previous_stream._segment(seq_len - len(segment))
            if prefix == None: return None
            
            segment = prefix + segment

        return segment

    def __repr__(self):
        val = self._text
        if self._previous_stream != None:
            val = str(self._previous_stream) + val
        return val


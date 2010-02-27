from collections import defaultdict
from math import *

class ToneSystem:
    def __init__(self, octave_division):
        self._octave_division = octave_division
        self._half_division = int(ceil(octave_division/2))

    def get_interval(self, note_a, note_b):
        return self.simplify_interval(note_a - note_b)

    def simplify_interval(self, interval_value):
        return abs(((abs(interval_value) + self._half_division) \
                        % self._octave_division) - self._half_division)

    def get_pitch_class_set(self, notes):
        pcs = defaultdict(int)
        count = len(notes)
        for i in range(0, count - 1):
            for j in range(i + 1, count):
                ival = self.get_interval(notes[i], notes[j])
                pcs[ival] += 1
        return pcs

from pcs import Pcs
from markov.std_random import StdRandom
from math import ceil

class ToneSystem:
    """
    Tone system class, implementing clock arithmetric and pitch class set extraction
    """
    def __init__(self, octave_steps, rand=StdRandom()):
        if octave_steps == 0: raise 'octave step cannot be 0, that makes no sense!'

        self._octave_steps = octave_steps
        self._half_division = int(ceil(octave_steps/2))
        self._rand = rand

    def get_interval(self, note_a, note_b):
        """
        Returns the simplified, pitch class interval between the two notes
        """
        return self.simplify_interval(note_a - note_b)

    def simplify_interval(self, interval_value):
        """
        Converts an absolute interval into a pitch class interval
        """
        return abs(((abs(interval_value) + self._half_division) \
                        % self._octave_steps) - self._half_division)

    def get_pitch_class_set(self, notes):
        pcs = Pcs()
        count = len(notes)
        for i in range(0, count - 1):
            for j in range(i + 1, count):
                ival = self.get_interval(notes[i], notes[j])
                pcs[ival] += 1
        return pcs

    def get_pitch_in_base_octave(self, pitch):
        """
        Returns a non simplified pitch in the range of 0 .. (octave_steps -1), inclusive
        """
        return pitch % self._octave_steps

    @property
    def rand(self):
        return self._rand

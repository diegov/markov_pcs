from math import sqrt

class ModalGroup:
    def __init__(self, tone_system, notes = None, pcs = None):
        self._notes = notes
        if notes != None:
            if pcs != None: raise Exception("Can't specify both pcs " + \
                                                "and notes")
            pcs = tone_system.get_pitch_class_set(notes)
        self._pcs = pcs

    @staticmethod
    def get_note_count_from_pcs(pcs):
        total = sum(pcs.values())
        note_count = int(round(sqrt(2*total+0.25)+0.5))
        return note_count

    def __repr__(self):
        return "Modal Group: " + str(self._pcs)

    def __hash__(self):
        initial = hash(self._pcs)
        if self._notes != None:
            initial += hash(self._notes) * 23
        return initial
    
    def __eq__(self, other):
        if not isinstance(other, ModalGroup): return False
        if self._notes != None:
            return self._notes == other._notes
        return self._pcs == other._pcs

    def __ne__(self, other):
        return not self == other

from math import sqrt
from markov.link import Link

class ModalGroup:
    def __init__(self, tone_system, notes = None, pcs = None):
        self._notes = notes
        if notes != None:
            if pcs != None: raise Exception("Can't specify both pcs " + \
                                                "and notes")
            pcs = tone_system.get_pitch_class_set(notes)
        self._pcs = pcs
        self._tone_system = tone_system

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

    def generate_notes(self, base_notes):
        from note_stream import NoteStream
        base_pcs = self._tone_system.get_pitch_class_set(base_notes)
        if not self._pcs.is_superset_of(base_pcs): return None

        remaining_pcs = self._pcs - base_pcs

        #Unfold intervals and shuffle
        all_values = [k for k in remaining_pcs.keys() for i in range(0, remaining_pcs[k])]
        self._tone_system.rand.shuffle(all_values)

        sequence = self._recurse_note_completion(all_values, NoteStream(self._tone_system, base_notes))
        if sequence == None: return None
        #TODO: expand sequence each select value (the actual note)
        return sequence.notes

    def _recurse_note_completion(self, remaining_intervals, current_stream):
        if len(remaining_intervals) == 0: return current_stream
        for index in range(0, len(remaining_intervals)):
            i = remaining_intervals[index]
            for n in current_stream.notes:
                other_notes = self._notes_for_interval(n, i)
                for other_note in other_notes:
                    new_stream = current_stream.append(Link([other_note]))
                    #remove the used interval
                    new_intervals = [remaining_intervals[x] for x in range(0, len(remaining_intervals)) if x != index]
                    new_notes = new_stream.notes
                    new_pcs = self._tone_system.get_pitch_class_set(new_notes)
                    if self._pcs == new_pcs: return new_stream
                    if not self._pcs.is_superset_of(new_pcs): continue
                    
                    next_recurse_val = self._recurse_note_completion(new_intervals, new_stream)
                    if next_recurse_val != None: return next_recurse_val

        return None

    def _notes_for_interval(self, note, interval):
        n2a = note + interval
        n2b = note - interval
        simplified_a = self._tone_system.get_pitch_in_base_octave(n2a)
        simplified_b = self._tone_system.get_pitch_in_base_octave(n2b)
        if simplified_a == simplified_b: return [n2a]
        return [n2a, n2b]

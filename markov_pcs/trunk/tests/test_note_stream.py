from note_stream import *
from tone_system import ToneSystem
from markov.link import Link
import unittest

class NotReallyRand:
    def next(self):
        return 1
    def shuffle(self, list):
        pass

class NoteStreamTests(unittest.TestCase):
    """Unit tests for the NoteStream class."""

    def test_can_create(self):
        ts = ToneSystem(12)
        t = NoteStream(ts, [1,2,3,4])
        self.assertNotEqual(None, t)

    def test_can_append_modal_group(self): 
        ts = ToneSystem(12, rand=NotReallyRand())
        t = NoteStream(ts, [1,2,3,4], group_length=3)
        grp = ts.get_pitch_class_set([2,3,4,-1])
        t = t.append(Link([grp]))
        result = ts.get_pitch_class_set(t.notes)
        print "notes", t.notes
        self.assertEqual(ts.get_pitch_class_set([1,2,3,4,-1]), result)

    def test_can_create_segment(self):
        class Alt:
            pass

        ts = ToneSystem(12)

        t = NoteStream(ts, [1,2,3,4])
        alt = Alt()
        alt.seq_length = 3
        p = t.segment_for(alt)
        expected = Link([ModalGroup(ts, notes=[2,3,4])])
        self.assertEqual(expected, p)

    def test_can_get_notes(self):
        ts = ToneSystem(12)
        t = NoteStream(ts, [1,2,3,4])
        t = t.append(Link([5,6,7]))
        notes = t.notes
        self.assertEqual([1,2,3,4,5,6,7], notes)

if __name__ == "__main__":
    unittest.main()


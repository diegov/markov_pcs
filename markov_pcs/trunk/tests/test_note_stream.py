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
        t = NoteStream(ts, [1,2,3,4], group_length=4)
        grp = ts.get_pitch_class_set([2,3,4,-1])
        t = t.append(Link([grp]))
        print "Notes: ", t.notes
        result = ts.get_pitch_class_set(t.notes)
        self.assertEqual(ts.get_pitch_class_set([1,2,3,4,-1]), result)

    def test_can_append_modal_group_to_empty_stream(self): 
        ts = ToneSystem(12, rand=NotReallyRand())
        t = NoteStream(ts, [], group_length=3)
        grp = ts.get_pitch_class_set([2,3,4,-1])
        t = t.append(Link([grp]))
        result = ts.get_pitch_class_set(t.notes)
        self.assertEqual(ts.get_pitch_class_set([2,3,4,-1]), result)


    def test_can_create_segment(self):
        class Alt:
            pass

        ts = ToneSystem(12)

        t = NoteStream(ts, [1,2,3,4])
        alt = Alt()
        alt.note_seq_len = 3
        p = t.segment_for(alt)
        expected = Link([ModalGroup(ts, notes=[2,3,4], keep_notes=False)])
        self.assertEqual(expected, p)

    def test_can_get_notes(self):
        ts = ToneSystem(12)
        t = NoteStream(ts, [1,2,3,4])
        t = t.append(Link([5,6,7]))
        notes = t.notes
        self.assertEqual([1,2,3,4,5,6,7], notes)

    def test_will_return_non_segment_when_requesting_more_notes_than_available(self):
        class Alt:
            pass

        ts = ToneSystem(12)
        t = NoteStream(ts, [1,2])
        alt = Alt()
        alt.note_seq_len = 3
        p = t.segment_for(alt)
        self.assertEquals(None, p)

if __name__ == "__main__":
    unittest.main()


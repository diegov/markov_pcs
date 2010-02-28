from note_stream import *
from tone_system import ToneSystem
import unittest

class NoteStreamTests(unittest.TestCase):
    """Unit tests for the NoteStream class."""

    def test_can_create(self):
        ts = ToneSystem(12)
        t = NoteStream(ts, [1,2,3,4])
        self.assertNotEqual(None, t)

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

if __name__ == "__main__":
    unittest.main()


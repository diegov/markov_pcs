from tone_system import *
from modal_group_markov import *
from not_rand import NotRand
import unittest

class ModalGroupMarkovTests(unittest.TestCase):
    """Unit tests for the ModalGroupMarkov class."""

    def test_can_create(self):
        ts = ToneSystem(20, rand=NotRand())
        m = ModalGroupMarkov(ts, [1,2,3], rand=NotRand())
        self.assertNotEqual(None, m)

    def test_can_add_notes(self):
        ts = ToneSystem(20, rand=NotRand())
        m = ModalGroupMarkov(ts, [2,3,4], rand=NotRand())
        m.add_notes([1,9,3,5,1,6,7,9])
        result = m.build_seq(100)
        print "result:  "
        print "  ", [ts.get_pitch_in_base_octave(x) for x in result.notes]
        self.assertEqual(100, len(result))

if __name__ == "__main__":
    unittest.main()


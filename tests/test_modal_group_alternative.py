from modal_group import *
from tone_system import ToneSystem
from modal_group_alternative import *
import unittest

class NotReallyRand:
    def next(self):
        return 1
    def shuffle(self, list):
        pass

class ModalGroupAlternativeTests(unittest.TestCase):
    """Unit tests for the ModalGroupAlternative class."""

    def test_can_create(self):
        ts = ToneSystem(9)
        t = ModalGroupAlternative(ts, 3, rand=NotReallyRand())
        self.assertNotEqual(None, t)

    def test_seq_length_is_always_one(self):
        ts = ToneSystem(9)
        t = ModalGroupAlternative(ts, 3, rand=NotReallyRand())
        length = t.seq_len
        self.assertEqual(1, length)

    def test_can_add_notes(self):
        ts = ToneSystem(9)
        t = ModalGroupAlternative(ts, 3, rand=NotReallyRand())
        t.add_notes([0,2,3,4])
        t.add_notes([0,2,3,7])
        t.add_notes([0,2,3,7])
        t.add_notes([1,3,5,8])
        print "graph", t.graph
        result = t.graph.suggest_continuation(Link([ModalGroup(ts, notes=[1,3,5], keep_notes=False)]))
        expected = Link([ModalGroup(ts, notes=[3,5,8], keep_notes=False)])
        self.assertEquals(expected, result, '[1,3,5] did not result in [3,5,8]')

        result = t.graph.suggest_continuation(Link([ModalGroup(ts, notes=[1,4,2], keep_notes=False)]))
        expected = Link([ModalGroup(ts, notes=[2,1,6], keep_notes=False)])
        self.assertEquals(expected, result, '[1,4,2] did not result in [2,1,6]' )

if __name__ == "__main__":
    unittest.main()


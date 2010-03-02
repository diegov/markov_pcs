from tone_system import *
import unittest

class ToneSystemTests(unittest.TestCase):
    """Unit tests for the ToneSystem class."""

    def test_can_create(self):
        t = ToneSystem(13)
        self.assertNotEqual(None, t)

    def test_cant_create_with_0_steps(self):
        ok = False
        try:
            t = ToneSystem(0)
        except:
            ok = True
        self.assertTrue(ok, 'should have thrown in the constructor')

    def test_can_simplify_interval(self):
        """
        Test clock arithmetric with a cycle of 13
        """
        t = ToneSystem(13)
        self.assertEqual(1, t.get_interval(0, 12))
        self.assertEqual(2, t.get_interval(0, 11))
        self.assertEqual(6, t.get_interval(7, 26))

    def test_can_get_pitch_class_set(self):
        t = ToneSystem(17)
        pcs = t.get_pitch_class_set([1,2,17])
        self.assertEqual([1,2], pcs.keys())
        self.assertEqual(2, pcs[1])
        self.assertEqual(1, pcs[2])

    def test_can_get_pcs_for_octave_only_system(self):
        t = ToneSystem(1)
        pcs = t.get_pitch_class_set([1,2,17])
        self.assertEqual([0], pcs.keys())
        self.assertEqual(3, pcs[0])

    def test_can_return_note_from_base_octave(self):
        t = ToneSystem(12)
        note = t.get_pitch_in_base_octave(13)
        self.assertEqual(1, note, 'positive notes don\'t work')
        note2 = t.get_pitch_in_base_octave(-1)
        self.assertEqual(11, note2, 'negative notes don\'t work %i' % (note))

if __name__ == "__main__":
    unittest.main()


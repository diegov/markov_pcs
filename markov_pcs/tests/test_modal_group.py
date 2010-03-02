from modal_group import *
from tone_system import ToneSystem
import unittest

class NotReallyRand:
    def next(self):
        return 1
    def shuffle(self, list):
        pass

class ModalGroupTests(unittest.TestCase):
    """Unit tests for the ModalGroup class."""

    def test_can_create(self):
        ts = ToneSystem(9)
        t = ModalGroup(ts, notes=[1,2,3,4])
        self.assertNotEqual(None, t)

    def test_can_find_out_number_of_notes_from_number_of_intervals(self):
        #The actual tone system doesn't really matter, it's just 
        #easier to generate a pcs using a tone system than by hand
        ts = ToneSystem(9)
        
        #First one by hand, then automate
        pcs = ts.get_pitch_class_set([1,12,3,4,5])
        result = ModalGroup.get_note_count_from_pcs(pcs)
        self.assertEqual(5, result)

        for i in range(1,40):
            p = range(i, 41)
            expected = len(p)
            pcs = ts.get_pitch_class_set(p)
            result = ModalGroup.get_note_count_from_pcs(pcs)
            self.assertEqual(expected, result)

    def test_equals_identifies_equal_object_with_notes(self):
        ts = ToneSystem(9)
        mode1 = ModalGroup(ts, notes=[1,2,4])
        mode2 = ModalGroup(ts, notes=[1,2,4])
        self.assertEqual(mode1, mode2)
        mode2 = ModalGroup(ts, notes=[1,3,4])
        self.assertNotEqual(mode1, mode2)

    def test_equals_identifies_equal_objects_with_pcs_only(self):
        ts = ToneSystem(9)
        mode1 = ModalGroup(ts, pcs=ts.get_pitch_class_set([1,2,4]))
        mode2 = ModalGroup(ts, pcs=ts.get_pitch_class_set([1,3,4]))
        self.assertEqual(mode1, mode2)
        mode2 = ModalGroup(ts, pcs=ts.get_pitch_class_set([1,2,5]))
        self.assertNotEqual(mode1, mode2)

    def test_will_not_allow_pcs_and_notes_to_be_specified(self):
        ts = ToneSystem(23)
        ok = False
        try:
            mode = ModalGroup(ts, pcs=ts.get_pitch_class_set([1,2,4]), \
                                  notes=[1,2,4])
        except:
            ok = True

        self.assertTrue(ok, 'should have thrown in the constructor')

    def test_will_generate_notes_from_pcs(self):
        ts = ToneSystem(13, rand=NotReallyRand())
        expected = [1,2,4]
        expected_pcs = ts.get_pitch_class_set(expected)
        mode1 = ModalGroup(ts, pcs=expected_pcs)
        notes = mode1.generate_notes([6])
        self.assertEqual(expected_pcs, ts.get_pitch_class_set(notes))
        self.assertEquals(6, notes[0])

    def test_will_generate_notes_from_pcs_with_only_one_note_missing(self):
        ts = ToneSystem(13, rand=NotReallyRand())
        expected = [1,2,4]
        expected_pcs = ts.get_pitch_class_set(expected)
        mode1 = ModalGroup(ts, pcs=expected_pcs)
        notes = mode1.generate_notes([5,8])
        self.assertEqual(expected_pcs, ts.get_pitch_class_set(notes))
        self.assertEquals(5, notes[0])
        self.assertEquals(8, notes[1])

    def test_large_pcs_benchmark(self):
        ts = ToneSystem(42, rand=NotReallyRand())
        expected = [1,4,7,9,12,5,6,20]
        expected_pcs = ts.get_pitch_class_set(expected)
        mode1 = ModalGroup(ts, pcs=expected_pcs)
        notes = mode1.generate_notes([5,24])
        self.assertEqual(expected_pcs, ts.get_pitch_class_set(notes))
        self.assertEquals(5, notes[0])
        self.assertEquals(24, notes[1])

if __name__ == "__main__":
    unittest.main()


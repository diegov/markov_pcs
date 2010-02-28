from markov.text_stream import *
from markov.link import *
from not_rand import *
import unittest

class TextStreamTests(unittest.TestCase):
    """Unit tests for the TextStream class."""

    def test_can_create(self):
        p = TextStream('')
        self.assertNotEqual(None, p)

    def test_will_slice_text_correctly(self):
        class thing:
            pass
        alt = thing()
        alt.seq_len = 3

        ts1 = TextStream('this is the current value')
        ts2 = TextStream('this is the ').append(Link.from_s('curr')) \
                                       .append(Link.from_s('ent ')) \
                                       .append(Link.from_s('val')) \
                                       .append(Link.from_s('u')) \
                                       .append(Link.from_s('e'))

        print ts2

        seq1 = ts1.segment_for(alt)
        seq2 = ts2.segment_for(alt)
        expected = Link.from_s('lue')
        
        self.assertEqual(expected, seq1)
        self.assertEqual(expected, seq2)

    def test_will_return_none_when_not_enough_characters(self):
        class thing:
            pass
        alt = thing()
        alt.seq_len = 12

        ts1 = TextStream('this value')
        seq1 = ts1.segment_for(alt)
        self.assertEqual(None, seq1)
        

if __name__ == "__main__":
    unittest.main()

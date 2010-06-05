from markov.markov import *
from not_rand import *
import unittest

class MarkovTests(unittest.TestCase):
    """Unit tests for the Markov class."""

    def test_can_create(self):
        p = TextMarkov([4], rand=NotRand([1,2,3,4]))
        self.assertNotEqual(None, p)

    def test_return_text(self):
        p = TextMarkov([3,4,5], rand=NotRand([1,2,3,4]))
        p.add_text_block('the test should return a correct sequence, ' + \
                             "since there's enough data for it")
        result = p.build_seq(12)
        self.assertNotEqual(None, result)
        self.assertEqual(12, len(result))

if __name__ == "__main__":
    unittest.main()


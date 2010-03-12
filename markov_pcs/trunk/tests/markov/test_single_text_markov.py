from markov.single_text_markov import *
from not_rand import *
import unittest

class SingleTextMarkovTests(unittest.TestCase):
    """Unit tests for the SingleTextMarkov class."""

    def test_can_create(self):
        p = SingleTextMarkov(4)
        self.assertNotEqual(None, p)

    def test_will_log_the_right_numbers_of_keys(self):
        p = SingleTextMarkov(3, NotRand([1]))
        p.add_text_block('test')
        p.add_text_block('tesd')
        p.add_text_block('esda')
        p.add_text_block('dsak')
        p.add_text_block('esda')
        p.add_text_block('esdc')
        p.add_text_block('sdcz')
        val = p.graph
        self.assertNotEquals(None, p.graph)
        self.assertEquals(4, len(p.graph.dict.keys()))

if __name__ == "__main__":
    unittest.main()

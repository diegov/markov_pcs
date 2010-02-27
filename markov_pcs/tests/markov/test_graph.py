from markov.graph import *
import unittest
from not_rand import *

class GraphTests(unittest.TestCase):
    """Unit tests for the Graph class."""

    def test_add_one_value_and_get_weights(self):
        rand = NotRand([0.5])
        g = Graph(2, rand)
        g.add('tes')
        g.add('tec')
        g.add('tes')
        g.add('tac')
        g.add('tac')
        g.add('tis')
        
        val = g.suggest_continuation('te')
        self.assertEqual('s', val)

        val = g.suggest_continuation('ti')
        self.assertEqual('s', val)

        val = g.suggest_continuation('ta')
        self.assertEqual('c', val)

    def test_when_requesting_a_missing_key_it_returns_none(self):
        rand = NotRand([0.5])
        g = Graph(2, rand)
        g.add('tes')
                
        val = g.suggest_continuation('tx')
        self.assertEqual(None, val)

if __name__ == "__main__":
    unittest.main()


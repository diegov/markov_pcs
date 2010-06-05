from markov.bucket import *
import unittest

class BucketTests(unittest.TestCase):
    """Unit tests for the Bucket class."""

    def test_add_one_value_and_get_weights(self):
        b = Bucket()
        b['test_val'] = 1
        weights = b.weights
        self.assertEqual({'test_val': 1.0}, weights)

    def test_add_two_values_and_get_weights(self):
        b = Bucket()
        b['test_val'] = 3
        b['test_val2'] = 1
        weights = b.weights
        self.assertEqual({'test_val': .75, 'test_val2': .25}, weights)

    def test_knows_when_it_has_key(self):
        b = Bucket()
        b['test_val'] = 3
        b['test_val2'] = 1
        self.assertEqual(True, b.has_key('test_val2'))
        self.assertEqual(False, b.has_key('test_val3'))

if __name__ == "__main__":
    unittest.main()


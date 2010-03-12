from tone_system import *
from modal_group_markov import *
import unittest

class ModalGroupMarkovTests(unittest.TestCase):
    """Unit tests for the ModalGroupMarkov class."""

    def test_can_create(self):
        m = ModalGroupMarkov()
        self.assertNotEqual(None, m)

if __name__ == "__main__":
    unittest.main()


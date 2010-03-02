from modal_group import *
from pcs import Pcs
from tone_system import ToneSystem
import unittest

class PcsTests(unittest.TestCase):
    """Unit tests for the Pcs class."""

    def test_can_create(self):
        p = Pcs()
        self.assertNotEqual(None, p)

    def test_can_tell_subset(self):
        p = Pcs()
        p[1] = 12
        p[5] = 5
        
        p2 = Pcs()
        p[1] = 8
        p[5] = 5

        self.assertTrue(p.is_superset_of(p2))
        self.assertFalse(p2.is_superset_of(p))

    def test_can_subtract(self):
        p = Pcs()
        p[1] = 9
        p[5] = 5
        p[3] = 1
        
        p2 = Pcs()
        p2[1] = 8
        p2[5] = 5

        p3 = p - p2
        self.assertEqual({1: 1, 3: 1}, p3)

if __name__ == "__main__":
    unittest.main()


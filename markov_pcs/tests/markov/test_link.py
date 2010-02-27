from markov.link import *
import unittest

class LinkTests(unittest.TestCase):
    """Unit tests for the Link class."""

    def test_can_be_split_in_two(self):
        l1, l2 = Link(['a','b','c']).split_at(2)
        self.assertEqual(Link.from_s('ab'), l1)
        self.assertEqual(Link.from_s('c'), l2)

        l1, l2 = Link(['a','b','c', 'd', 'e']).split_at(2)
        self.assertEqual(Link.from_s('ab'), l1)
        self.assertEqual(Link.from_s('cde'), l2)

        l1, l2 = Link([1, 4, 6, 7]).split_at(1)
        self.assertEqual(Link([1]), l1)
        self.assertEqual(Link([4, 6, 7]), l2)

    def test_hashes_and_equals_are_consistent(self):
        for i in range(0, 50):
            for j in range(0, 200):
                l1 = Link([i, j, i, j])
                l2 = Link([i, j, i, j])
                self.assertTrue(l1 == l2)
                self.assertEqual(hash(l1), hash(l2))
                self.assertEqual(l1, l2)

    def test_when_two_objects_arent_equal_then_returns_false(self):
        for i in range(0, 50):
            for j in range(51, 200):
                l1 = Link([i, j, i, j])

                if j % 3 == 0: l2 = Link([i, i, i, j])
                elif j % 3 == 1: l2 = Link([j, j, i, j])
                else: l2 = Link([i, j, i])

                self.assertFalse(l1 == l2)

if __name__ == "__main__":
    unittest.main()


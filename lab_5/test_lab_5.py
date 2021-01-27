import unittest

from lab_5 import *


class TestGraph (unittest.TestCase):

    def testKMPSearch(self):
        result = kmp_search("abcd", "abceabcd")
        self.assertEqual(result, "4")

    def test_computeLPSArray(self):
        result = compute_array("898", 3, [0, 0, 0])
        self.assertEqual(result, [0, 0, 1])

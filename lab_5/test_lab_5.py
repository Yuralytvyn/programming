import unittest

from lab_5 import *


class TestGraph (unittest.TestCase):

    def test_kmp_search(self):
        result = kmp_search("abcd", "abceabcd")
        self.assertEqual(result, "4")

    def test_kmp_search1(self):
        result = kmp_search("zxc", "qwerty")
        self.assertEqual(result, None)

    def test_kmp_search2(self):
        result = kmp_search("", "qwerty")
        self.assertEqual(result, "0")


    def test_computeLPSArray(self):
        result = compute_array("898", 3, [0, 0, 0])
        self.assertEqual(result, [0, 0, 1])

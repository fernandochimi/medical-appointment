# coding: utf-8
import unittest


class TestMethods(unittest.TestCase):
    def sum(self):
        a = 1
        b = 2
        result = a + b
        self.assertEqual(result, 3)

import unittest
from Game.EditValues import *

class TestEditValues(unittest.TestCase):

    def test_set_min_value(self):
        set_min_value(10)
        self.assertEqual(get_min_value(), 10)

    def test_set_max_value(self):
        set_max_value(1000)
        self.assertEqual(get_max_value(), 1000)

    def test_get_min_value(self):
        self.assertEqual(get_min_value(), 1)

    def test_get_max_value(self):
        self.assertEqual(get_max_value(), 100)

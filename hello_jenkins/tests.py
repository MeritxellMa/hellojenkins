from django.test import TestCase

# Create your tests here.
import unittest
import random


class RandomTest(unittest.TestCase):
    def test(self):
        self.assertGreaterEqual(random.uniform(0, 1), 0.1)

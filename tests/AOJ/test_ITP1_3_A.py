import unittest

from src.AOJ.ITP1_3_A import resolve


class MyTestCase(unittest.TestCase):
    def test_many_hello(self):
        self.assertEqual("H\nH", resolve("H", 2))

import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_5_D import resolve


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_1(self):
        input = """30"""
        output = """ 3 6 9 12 13 15 18 21 23 24 27 30 """
        self.assertIO(input, output)

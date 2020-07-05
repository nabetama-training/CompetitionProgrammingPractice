import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_3_B import resolve


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
        input = """3
5
11
7
8
19
0"""
        output = """Case 1: 3
Case 2: 5
Case 3: 11
Case 4: 7
Case 5: 8
Case 6: 19"""
        self.assertIO(input, output)

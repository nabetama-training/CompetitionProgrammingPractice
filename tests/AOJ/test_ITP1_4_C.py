import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_4_C import resolve


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
        input = """1 + 2
56 - 18
13 * 2
100 / 10
27 + 81
0 ? 0"""
        output = """3
38
26
10
108"""
        self.assertIO(input, output)


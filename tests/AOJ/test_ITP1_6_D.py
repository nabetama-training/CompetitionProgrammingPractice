import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_6_D import resolve


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_1(self):
        input = """3 4
1 2 0 1
0 3 0 1
4 1 1 0
1
2
3
0
"""
        output = """5
6
9
"""
        self.assertIO(input, output)
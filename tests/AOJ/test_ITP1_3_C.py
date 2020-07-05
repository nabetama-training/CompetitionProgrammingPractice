import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_3_C import resolve


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
        input = """3 2
2 2
5 3
3 5
0 0"""
        output = """2 3
2 2
3 5
3 5"""
        self.assertIO(input, output)

import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_4_D import resolve


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
        input = """5
10 1 5 4 17"""
        output = """1 17 37"""
        self.assertIO(input, output)


import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_6_A import resolve


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
1 2 3 4 5"""
        output = """5 4 3 2 1"""
        self.assertIO(input, output)

    def test_2(self):
        input = """8
3 3 4 4 5 8 7 9"""
        output = """9 7 8 5 4 4 3 3"""
        self.assertIO(input, output)

    def test_3(self):
        input = """10
838 758 113 515 51 627 10 419 212 86"""
        output = "86 212 419 10 627 51 515 113 758 838"
        self.assertIO(input, output)

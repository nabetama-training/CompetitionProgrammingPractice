import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_2_D import resolve


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
        input = """5 4 2 2 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_2(self):
        input = """5 4 2 4 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_3(self):
        input = """5 4 5 3 1"""
        output = """No"""
        self.assertIO(input, output)
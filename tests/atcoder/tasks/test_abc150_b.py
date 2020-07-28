import sys
from io import StringIO
import unittest

from src.atcoder.tasks.abc150_b import resolve


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
        input = """10
ZABCDBABCQ"""
        output = """2"""
        self.assertIO(input, output)

    def test_2(self):
        input = """19
THREEONEFOURONEFIVE"""
        output = """0"""
        self.assertIO(input, output)

    def test_3(self):
        input = """33
ABCCABCBABCCABACBCBBABCBCBCBCABCB"""
        output = """5"""
        self.assertIO(input, output)

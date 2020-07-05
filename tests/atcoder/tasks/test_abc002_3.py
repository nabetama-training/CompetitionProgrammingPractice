import sys
from io import StringIO
import unittest

from src.atcoder.tasks.abc002_3 import resolve


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
        input = """1 0 3 0 2 5"""
        output = """5.0"""
        self.assertIO(input, output)

    def test_2(self):
        input = """-1 -2 3 4 5 6"""
        output = """2.0"""
        self.assertIO(input, output)

    def test_3(self):
        input = """298 520 903 520 4 663"""
        output = """43257.5"""
        self.assertIO(input, output)

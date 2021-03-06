import sys
from io import StringIO
import unittest

from src.atcoder.tasks.practice_1 import resolve


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
        input = """1
2 3
test"""
        output = """6 test"""
        self.assertIO(input, output)

    def test_2(self):
        input = """72
128 256
myonmyon"""
        output = """456 myonmyon"""
        self.assertIO(input, output)

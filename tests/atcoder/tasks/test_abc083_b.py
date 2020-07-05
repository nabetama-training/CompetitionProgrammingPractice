import sys
from io import StringIO
import unittest

from src.atcoder.tasks.abc083_b import resolve


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_1(self):
        input = """20 2 5"""
        output = """84"""
        self.assertIO(input, output)

    def test_input_2(self):
        input = """10 1 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_input_3(self):
        input = """100 4 16"""
        output = """4554"""
        self.assertIO(input, output)

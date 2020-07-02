import sys
from io import StringIO
import unittest

from src.atcoder.tasks.abc087_b import resolve


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
        input = """2
2
2
100"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        input = """5
1
0
150"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        input = """30
40
50
6000"""
        output = """213"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

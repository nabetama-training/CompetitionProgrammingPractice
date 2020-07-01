import sys
from io import StringIO
import unittest

from src.atcoder.tasks.abc001_a import resolve


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """15
10"""
        output = """5"""
        self.assertIO(input, output)

    def test_2(self):
        input = """0
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_3(self):
        input = """5
20"""
        output = """-15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

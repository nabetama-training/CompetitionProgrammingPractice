import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_11_D import resolve


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_1(self):
        input = """3
1 2 3 4 5 6
6 2 4 3 5 1
6 5 4 3 2 1
"""
        output = """No
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """3
1 2 3 4 5 6
6 5 4 3 2 1
5 4 3 2 1 6
"""
        output = """Yes
"""
        self.assertIO(input, output)

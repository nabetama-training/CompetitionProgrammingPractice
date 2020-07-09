import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_8_D import resolve


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
        input = """vanceknowledgetoad
advance
"""
        output = """Yes
"""

        self.assertIO(input, output)

    def test_2(self):
        input = """vanceknowledgetoad
advanced
"""
        output = """No
"""

        self.assertIO(input, output)

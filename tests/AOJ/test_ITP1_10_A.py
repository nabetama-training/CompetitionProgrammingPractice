import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_10_A import resolve


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertTrue(abs(float(out) - float(output)) < 0.0001)

    def test_1(self):
        input = """0 0 1 1
"""
        output = """1.41421356
"""

        self.assertIO(input, output)

    def test_2(self):
        input = """1.123 0.0 1.123 100.0
"""
        output = """100.0
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """123.4000 573.31 123.4000 573.31
"""
        output = """0.000000000000
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """-1234.5678 -3384.8899 333333.3 99999.88
"""
        output = """350177.196304262849
"""
        self.assertIO(input, output)

    def test_5(self):
        input = """0.01 -0.1134 -3.1414 55.7
"""
        output = """55.90229817744526
"""
        self.assertIO(input, output)

    def test_6(self):
        input = """0 0 0 100.0
"""
        output = """100.000000000000
"""
        self.assertIO(input, output)

    def test_7(self):
        input = """-3.141516 -25.3 2012.00 1979.710
"""
        output = """2842.685425721034
"""
        self.assertIO(input, output)

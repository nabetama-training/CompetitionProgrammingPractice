import sys
from io import StringIO
import unittest

from src.atcoder.tasks.abc001_c import resolve


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
        input = """2750 628"""
        output = """W 5"""
        self.assertIO(input, output)

    def test_2(self):
        input = """161 8"""
        output = """C 0"""
        self.assertIO(input, output)

    def test_3(self):
        input = """3263 15"""
        output = """NNW 1"""
        self.assertIO(input, output)

    def test_4(self):
        input = """1462 1959"""
        output = """SE 12"""
        self.assertIO(input, output)

    def test_5(self):
        input = """1687 1029"""
        output = """SSE 8"""
        self.assertIO(input, output)

    def test_6(self):
        input = """2587 644"""
        output = """WSW 5"""
        self.assertIO(input, output)

    def test_7(self):
        input = """113 201"""
        output = """NNE 3"""
        self.assertIO(input, output)

    def test_8(self):
        input = """2048 16"""
        output = """SSW 1"""
        self.assertIO(input, output)

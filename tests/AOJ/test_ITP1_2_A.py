import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_2_A import resolve



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
        input = """1 2"""
        output = """a < b"""
        self.assertIO(input, output)

    def test_2(self):
        input = """4 3"""
        output = """a > b"""
        self.assertIO(input, output)

    def test_3(self):
        input = """3 3"""
        output = """a == b"""
        self.assertIO(input, output)

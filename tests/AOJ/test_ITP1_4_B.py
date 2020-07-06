import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_4_B import resolve


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
        input = """2"""
        output = """12.566371 12.566371"""
        self.assertIO(input, output)

    def test_2(self):
        input = """3"""
        output = """28.274334 18.849556"""
        self.assertIO(input, output)

    def test_3(self):
        input = """34.1201"""
        output = """3657.383181 214.382911"""
        self.assertIO(input, output)
import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_2_C import resolve, bubble_sort, insertion_sort


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
        input = """3 8 1"""
        output = """1 3 8"""
        self.assertIO(input, output)

    def test_2(self):
        input = """3 8 8"""
        output = """3 8 8"""
        self.assertIO(input, output)

    def test_3(self):
        input = """8 3 1"""
        output = """1 3 8"""
        self.assertIO(input, output)

    def test_bubble_sort1(self):
        self.assertEqual([1, 3, 8], bubble_sort([3, 8, 1]))

    def test_bubble_sort2(self):
        self.assertEqual([0], bubble_sort([0]))

    def test_insertion_sort1(self):
        self.assertEqual([1, 3, 8], insertion_sort([3, 8, 1]))

    def test_insertion_sort2(self):
        self.assertEqual([0], insertion_sort([0]))

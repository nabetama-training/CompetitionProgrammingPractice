import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_11_C import resolve, Dice


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
        input = """1 2 3 4 5 6
6 2 4 3 5 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """1 2 3 4 5 6
6 5 4 3 2 1
"""
        output = """No
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """1 1 1 1 1 6
1 6 1 1 1 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_5(self):
        input = """1 2 3 4 5 6
6 2 4 3 5 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_6(self):
        input = """1 2 3 4 5 6
4 5 6 1 2 3
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_7(self):
        input = """1 2 3 4 5 6
2 1 4 3 6 5
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_8(self):
        input = """1 2 3 4 5 6
5 3 6 1 4 2
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_9(self):
        input = """1 2 3 4 5 6
6 4 5 2 3 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_10(self):
        input = """1 2 3 4 5 6
1 3 5 2 4 6
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_11(self):
        input = """1 2 3 4 5 6
1 5 4 3 2 6
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_12(self):
        input = """1 2 3 4 5 6
1 4 2 5 3 6
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_13(self):
        input = """1 2 3 4 5 6
4 2 1 6 5 3
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_14(self):
        input = """1 2 3 4 5 6
4 1 5 2 6 3
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_15(self):
        input = """1 2 3 4 5 6
4 5 6 1 2 3
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_16(self):
        input = """1 2 3 4 5 6
4 6 2 5 1 3
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_17(self):
        input = """1 2 3 4 5 6
6 2 4 3 5 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_18(self):
        input = """1 2 3 4 5 6
6 4 5 2 3 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_19(self):
        input = """1 2 3 4 5 6
6 5 3 4 2 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_20(self):
        input = """1 2 3 4 5 6
6 3 2 5 4 1
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_21(self):
        input = """1 2 3 4 5 6
3 2 6 1 5 4
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_22(self):
        input = """1 2 3 4 5 6
3 6 5 2 1 4
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_23(self):
        input = """1 2 3 4 5 6
3 5 1 6 2 4
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_24(self):
        input = """1 2 3 4 5 6
3 1 2 5 6 4
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_25(self):
        input = """1 2 3 4 5 6
5 1 3 4 6 2
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_26(self):
        input = """1 2 3 4 5 6
5 3 6 1 4 2
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_27(self):
        input = """1 2 3 4 5 6
5 6 4 3 1 2
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_28(self):
        input = """1 2 3 4 5 6
5 4 1 6 3 2
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_29(self):
        input = """1 2 3 4 5 6
2 1 4 3 6 5
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_30(self):
        input = """1 2 3 4 5 6
2 4 6 1 3 5
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_31(self):
        input = """1 2 3 4 5 6
2 6 3 4 1 5
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_32(self):
        input = """1 2 3 4 5 6
2 3 1 6 4 5
"""
        output = """Yes
"""
        self.assertIO(input, output)

    def test_33(self):
        dice = Dice([1, 2, 3, 4, 5, 6])
        self.assertFalse(dice == 'Not_a_Dice')

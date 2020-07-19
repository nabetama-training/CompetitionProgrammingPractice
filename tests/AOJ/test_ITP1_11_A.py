import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_11_A import resolve


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
        input = """1 2 4 8 16 32
SE
"""
        output = """8
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """1 2 4 8 16 32
EESWN
"""
        output = """32
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """1 2 3 4 5 6
SWNN
"""
        output = """4
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """1 2 3 4 5 6
SWNNEEES
"""
        output = """1
"""
        self.assertIO(input, output)

    def test_5(self):
        input = """1 2 3 4 5 6
SWNNEEESSEWWNNE
"""
        output = """5
"""
        self.assertIO(input, output)

    def test_6(self):
        input = """6 5 4 3 2 1
SSSSEEENNNWWSEWNNWNWESSE
"""
        output = """4
"""
        self.assertIO(input, output)

    def test_7(self):
        input = """1 2 3 4 5 6
S
"""
        output = """5
"""
        self.assertIO(input, output)

    def test_8(self):
        input = """7 8 9 10 11 12
W
"""
        output = """9
"""
        self.assertIO(input, output)

    def test_9(self):
        input = """13 14 15 16 17 18
N
"""
        output = """14
"""
        self.assertIO(input, output)

    def test_10(self):
        input = """19 20 21 22 23 24
E
"""
        output = """22
"""
        self.assertIO(input, output)

    def test_11(self):
        input = """1 2 3 4 5 6
SSSSSEEEWWWNNNSSSNEENNNWWWWEEEENNNNNNNSSNNSNSNSNSWEWEWENNN
"""
        output = """6
"""
        self.assertIO(input, output)

    def test_12(self):
        input = """1 2 3 4 5 6
NNSESSESSEEEWWEWNENNSEESSNEENENNWEEWWWEENNEENNWWENNNNNSSNNSNSNSNSWEWEWENNN
"""
        output = """5
"""
        self.assertIO(input, output)

    def test_13(self):
        input = """32 59 68 1 2 12
SESSWWNWNNSESSNWNWNNSESSWWNWWNSESSWWNWNNSESSEENWNNSESSWWNWNNSESSWWNWNNSESSSSNWNNSESSEWNWNNSESSWWNWSN
"""
        output = """2
"""
        self.assertIO(input, output)

    def test_14(self):
        input = """32 59 68 1 2 12
SSNWNNSESSNWNWNNSEWWSSWWNWWNSESSWNNWNNSESSSSNWNNSESSSSNWNNSESSWWNWNNSESSSSNWNNSESSEWNWSSSESSWWNWSNSE
"""
        output = """1
"""
        self.assertIO(input, output)

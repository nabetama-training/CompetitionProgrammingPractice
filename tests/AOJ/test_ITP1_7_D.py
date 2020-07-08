import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_7_D import resolve


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
        input = """3 2 3
1 2
0 3
4 5
1 2 1
0 3 2
"""
        output = """1 8 5
0 9 6
4 23 14
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """2 2 2
1 2
3 4
5 6
7 8
"""
        output = """19 22
43 50
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """2 3 4
1 2 3
0 1 3
1 2 3 4
1 0 2 1
1 0 3 2
"""
        output = """6 2 16 12
4 0 11 7
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """4 3 2
1 0 1
1 2 1
1 2 3
1 1 1
3 5
1 2
0 3
"""
        output = """3 8
5 12
5 18
4 10
"""
        self.assertIO(input, output)

    def test_5(self):
        input = """1 5 3
1 2 3 4 5
0 1 0
1 1 1
1 1 0
1 0 1
1 1 1
"""
        output = """14 11 11
"""
        self.assertIO(input, output)

    def test_6(self):
        input = """1 1 1
1
1
"""
        output = """1
"""
        self.assertIO(input, output)

    def test_7(self):
        input = """1 10 1
1 2 3 4 5 6 7 8 9 10
1
2
3
4
5
6
7
8
9
10
"""
        output = """385
"""
        self.assertIO(input, output)

    def test_8(self):
        input = """10 1 10
1
2
3
4
5
6
7
8
9
10
1 2 3 4 5 6 7 8 9 10
"""
        output = """1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100
"""
        self.assertIO(input, output)

    def test_9(self):
        input = """2 2 2
0 0
0 0
0 0
0 0
"""
        output = """0 0
0 0
"""
        self.assertIO(input, output)

    def test_10(self):
        input = """2 2 2
1 1
1 1
1 1
1 1
"""
        output = """2 2
2 2
"""
        self.assertIO(input, output)

    def test_11(self):
        input = """5 8 3
13 3 2 9 0 8 12 16
16 19 11 11 3 5 8 13
10 6 9 12 17 7 12 8
0 3 9 12 4 9 11 7
10 4 15 0 4 10 2 4
3 1 10
16 16 11
9 17 15
11 10 4
14 5 9
10 7 6
3 14 4
0 9 0
"""
        output = """320 553 325
688 896 667
683 753 592
440 621 350
391 483 473
"""
        self.assertIO(input, output)

    def test_12(self):
        input = """13 11 8
0 0 0 1 0 1 1 1 1 1 1
1 1 0 0 1 0 0 1 1 1 0
1 0 0 1 1 0 1 0 0 1 1
0 1 1 1 0 0 0 0 1 0 0
0 1 1 0 1 0 1 1 0 1 0
1 1 1 1 1 1 0 0 1 0 0
1 1 1 0 0 1 0 0 1 1 0
1 0 0 1 1 0 0 1 0 1 0
1 1 0 1 1 0 0 1 1 0 0
1 0 0 1 0 0 0 0 1 0 1
0 1 0 0 1 0 1 1 0 0 1
0 0 0 1 0 0 1 1 0 1 0
1 0 1 0 1 0 1 1 0 1 1
1 0 0 1 1 0 0 1
0 0 1 0 1 1 1 1
1 0 1 1 1 1 1 0
1 0 0 1 1 1 1 1
1 1 0 1 0 1 0 0
0 1 1 0 0 0 1 0
0 0 0 1 1 0 1 0
1 1 0 0 0 1 1 1
1 0 1 0 0 1 0 1
1 0 0 1 0 0 0 1
0 0 0 0 0 1 1 0
"""
        output = """4 2 2 3 2 4 5 4
5 2 2 3 2 4 2 5
4 1 0 5 3 3 3 3
3 0 3 2 3 4 3 3
4 2 2 4 3 4 4 3
5 2 4 4 4 5 4 4
4 1 4 3 3 3 3 4
5 2 0 4 2 3 2 4
5 2 2 3 3 5 3 5
3 0 1 2 2 3 2 3
2 2 1 2 2 4 4 2
3 1 0 3 2 2 3 3
5 2 1 5 3 4 4 3
"""
        self.assertIO(input, output)

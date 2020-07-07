import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_7_A import resolve


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
        input = """40 42 -1
20 30 -1
0 2 -1
-1 -1 -1"""
        output = """A
C
F
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """40 40 -1
39 40 -1
40 39 -1
20 45 -1
20 44 -1
-1 50 -1
-1 -1 -1"""
        output = """A
B
B
B
C
F
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """15 15 10
15 15 49
15 15 50
15 15 51
15 14 -1
-1 -1 -1"""
        output = """D
D
C
C
F
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """50 30 -1
30 50 -1
40 40 -1
35 50 -1
20 50 -1
30 40 -1
25 35 -1
35 25 -1
30 35 -1
35 30 -1
25 40 -1
30 49 -1
29 50 -1
50 29 -1
25 25 -1
26 24 -1
50 0 -1
0 50 -1
49 1 -1
1 49 -1
2 49 -1
32 32 -1
50 14 -1
15 15 50
15 15 100
15 15 80
15 15 65
29 29 100
29 29 80
29 29 65
15 15 50
15 15 49
15 15 0
15 15 -1
29 0 -1
29 0 40
29 0 29
-1 50 -1
50 -1 -1
0 0 -1
1 1 -1
15 14 -1
14 15 -1
29 0 -1
0 29 -1
-1 -1 -1
"""
        output = """A
A
A
A
B
B
C
C
B
B
B
B
B
B
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
D
D
D
F
F
F
F
F
F
F
F
F
F
F
"""

        self.assertIO(input, output)

import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_11_B import resolve


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
3
6 5
1 3
3 2
"""
        output = """3
5
6
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """11 12 13 14 15 16
10
11 12
12 14
12 16
13 12
13 16
14 16
14 12
15 16
16 14
16 13
"""
        output = """13
16
13
16
15
12
11
14
15
12
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """1 2 3 4 5 6
24
1 2
1 3
1 5
1 4
2 1
2 4
2 6
2 3
3 1
3 2
3 6
3 5
4 1
4 5
4 6
4 2
5 1
5 3
5 6
5 4
6 2
6 4
6 5
6 3
"""

        output = """3
5
4
2
4
6
3
1
2
6
5
1
5
6
2
1
3
6
4
1
4
5
3
2
"""
        self.assertIO(input, output)

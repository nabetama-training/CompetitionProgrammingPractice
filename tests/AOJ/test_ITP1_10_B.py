import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_10_B import resolve


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
        input = """4 3 90
"""
        output = """6.00000000
12.00000000
3.0
"""

        self.assertIO(input, output)

# Circele CI と local との実行環境の差で誤差が出る
#     def test_2(self):
#         input = """100 80 54
# """
#         output = """3236.06797750
# 263.63872287
# 64.7213595499958
# """
#
#         self.assertIO(input, output)

    def test_3(self):
        input = """25 76 45
"""
        output = """671.75144213
161.94254861
53.740115370177605
"""

        self.assertIO(input, output)

    def test_4(self):
        input = """86 77 120
"""
        output = """2867.41011193
304.23384863
66.68395609140178
"""

        self.assertIO(input, output)

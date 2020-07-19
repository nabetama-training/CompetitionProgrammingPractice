import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_10_C import resolve


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
        input = """5
70 80 100 90 20
3
80 80 80
0
"""
        output = """27.85677655436824
0.0
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """20
5 2 5 4 1 3 2 5 5 3 1 4 4 2 1 1 3 1 2 4
20
2 3 3 2 4 3 2 1 1 4 2 2 5 3 5 3 1 4 2 4
20
3 2 3 4 5 1 1 1 4 3 5 4 3 2 1 1 3 4 2 4
20
3 4 4 4 4 1 4 4 1 2 2 3 1 5 3 4 4 4 1 5
20
1 4 3 1 3 3 1 1 1 1 2 3 1 1 3 5 2 4 2 5
30
1 16 56 83 75 62 7 3 69 66 71 19 24 90 7 20 31 56 33 94 75 96 11 74 56 31 96 46 6 95
50
49 74 54 75 61 42 57 45 44 41 38 80 36 50 30 11 8 18 56 88 74 27 46 13 73 96 54 54 84 18 56 18 77 78 77 100 55 29 3 62 56 71 17 95 82 31 81 5 87 60
50
8 55 80 3 66 54 33 37 33 64 18 8 84 11 68 17 47 20 29 72 8 57 21 54 29 55 31 78 49 21 5 15 11 20 26 99 32 2 10 52 23 18 53 25 96 72 54 26 79 17
50
43 98 89 33 18 5 44 96 50 8 37 3 68 46 64 41 99 97 52 8 68 98 79 51 10 31 61 17 62 94 10 54 99 31 35 44 90 89 32 93 2 75 95 94 66 50 66 38 59 42
100
49 44 30 16 90 10 89 55 44 2 72 17 65 78 13 6 12 13 83 93 24 2 25 5 38 3 5 64 92 74 76 7 60 27 97 60 64 59 78 85 48 57 49 6 55 95 60 31 24 84 25 48 3 48 77 50 93 89 5 34 59 43 15 68 29 7 92 1 93 19 99 19 69 76 80 20 64 97 80 17 67 41 33 31 15 56 72 12 80 97 1 17 4 94 56 29 82 6 30 38
100
98 87 58 78 83 55 7 58 30 81 42 67 53 34 61 91 17 33 7 15 86 48 28 36 59 84 11 43 75 5 72 73 6 81 72 80 18 82 81 92 76 1 47 33 69 59 27 79 67 69 55 4 64 23 12 94 49 58 32 20 13 93 33 21 24 39 10 53 23 29 77 53 18 24 3 5 37 51 36 26 29 65 27 66 76 5 65 74 59 25 22 30 78 25 27 5 52 38 39 26
0
"""
        output = """1.4798648586948744
1.2083045973594573
1.3266499161421599
1.3143439428094914
1.3518505834595773
31.870031203136417
26.0967737469596
26.144406667583795
30.249257842135563
30.940386229004968
26.953151949261894
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """500
1 34 44 63 30 1 9 53 57 57 20 12 52 44 6 9 94 31 67 70 33 18 48 73 69 81 24 50 93 65 70 52 28 91 25 36 21 45 11 63 85 64 2 11 37 77 32 30 98 76 92 91 45 35 26 30 31 28 27 44 35 5 61 50 21 57 33 73 14 91 10 20 6 96 50 28 20 98 25 97 50 57 85 94 46 8 7 10 55 53 66 84 39 2 91 31 38 96 57 64 12 28 43 7 69 13 2 11 81 59 72 32 15 48 65 98 26 39 32 19 88 52 88 14 80 96 51 51 14 63 35 74 48 22 31 41 58 79 27 4 98 9 94 89 39 86 94 89 21 12 47 88 11 10 88 69 4 74 1 75 6 84 53 71 88 3 11 6 11 1 97 43 86 61 48 25 32 59 87 20 1 16 56 83 75 62 7 3 69 66 71 19 24 90 7 20 31 56 33 94 75 96 11 74 56 31 96 46 6 95 49 74 54 75 61 42 57 45 44 41 38 80 36 50 30 11 8 18 56 88 74 27 46 13 73 96 54 54 84 18 56 18 77 78 77 100 55 29 3 62 56 71 17 95 82 31 81 5 87 60 8 55 80 3 66 54 33 37 33 64 18 8 84 11 68 17 47 20 29 72 8 57 21 54 29 55 31 78 49 21 5 15 11 20 26 99 32 2 10 52 23 18 53 25 96 72 54 26 79 17 43 98 89 33 18 5 44 96 50 8 37 3 68 46 64 41 99 97 52 8 68 98 79 51 10 31 61 17 62 94 10 54 99 31 35 44 90 89 32 93 2 75 95 94 66 50 66 38 59 42 49 44 30 16 90 10 89 55 44 2 72 17 65 78 13 6 12 13 83 93 24 2 25 5 38 3 5 64 92 74 76 7 60 27 97 60 64 59 78 85 48 57 49 6 55 95 60 31 24 84 25 48 3 48 77 50 93 89 5 34 59 43 15 68 29 7 92 1 93 19 99 19 69 76 80 20 64 97 80 17 67 41 33 31 15 56 72 12 80 97 1 17 4 94 56 29 82 6 30 38 98 87 58 78 83 55 7 58 30 81 42 67 53 34 61 91 17 33 7 15 86 48 28 36 59 84 11 43 75 5 72 73 6 81 72 80 18 82 81 92
500
76 1 47 33 69 59 27 79 67 69 55 4 64 23 12 94 49 58 32 20 13 93 33 21 24 39 10 53 23 29 77 53 18 24 3 5 37 51 36 26 29 65 27 66 76 5 65 74 59 25 22 30 78 25 27 5 52 38 39 26 80 20 76 89 98 21 79 67 98 56 75 29 3 77 80 83 77 62 28 92 83 75 62 43 98 34 6 19 76 39 21 58 40 89 72 28 57 69 65 71 80 68 39 12 7 47 79 71 11 85 43 97 9 72 69 77 8 13 49 18 58 19 55 91 54 40 50 85 12 75 22 37 29 86 94 68 44 32 55 40 84 84 85 16 97 89 35 52 23 14 90 26 86 98 77 16 50 41 14 89 23 80 83 41 67 47 1 64 23 79 46 37 58 100 86 72 18 93 33 99 32 46 85 87 36 3 5 51 78 88 96 93 79 38 88 20 16 88 58 54 54 89 84 86 76 90 10 54 96 98 70 71 69 39 99 84 45 92 1 43 54 86 3 90 46 20 91 45 70 43 61 98 1 78 26 84 79 51 4 95 81 60 57 27 21 76 97 49 18 9 27 46 83 35 67 37 46 5 44 26 56 70 60 24 80 83 8 40 57 24 19 36 98 54 9 70 35 86 21 7 15 81 71 80 63 76 72 15 45 64 27 44 76 24 58 12 19 62 73 12 67 24 40 75 11 3 23 46 23 37 34 48 35 79 12 10 14 38 18 14 51 4 70 88 92 50 56 6 30 69 30 53 12 51 71 46 92 91 75 65 18 59 54 17 75 84 17 8 9 95 57 64 91 50 96 83 7 50 24 50 54 65 40 65 3 74 44 12 60 48 70 77 53 34 5 49 90 66 11 3 98 67 23 84 29 81 46 96 18 50 20 27 30 79 37 84 75 49 39 7 14 93 92 20 91 17 49 64 18 18 42 49 99 87 23 8 26 95 25 48 84 19 48 91 39 65 96 42 78 18 33 16 11 26 86 15 72 7 54 41 99 45 10 6 24 78 81 81 69 59 71 97 52 44 67 39 74 32 53 35 82 63 99 2 40 99 12 85 74 59 17 44 79 75 38 30 16 72 68 58 36 56 93 49 5 92 65 79 9 56 68 74 26 2 27 66 88 100 25 17
500
50 11 54 24 59 54 3 56 60 7 88 58 4 83 85 88 11 43 71 62 87 2 49 98 76 42 19 81 77 16 34 55 95 56 71 93 23 54 2 24 79 91 21 43 68 53 91 83 76 60 93 73 43 12 63 95 17 76 25 85 7 80 74 8 67 67 43 78 82 75 35 87 18 93 99 49 58 54 21 15 21 12 6 31 90 79 4 18 16 56 61 6 54 55 12 40 70 32 5 35 87 36 17 46 66 28 77 35 1 80 3 60 52 71 46 54 48 52 19 14 84 62 31 21 66 80 42 76 68 44 48 58 21 97 17 47 88 48 2 70 44 33 79 48 47 36 65 48 53 10 96 28 3 22 14 91 18 37 24 87 18 52 41 28 32 87 18 26 48 19 39 30 26 100 72 90 55 81 52 33 74 40 20 11 91 43 63 48 55 85 18 98 18 67 37 16 48 9 18 66 62 41 71 1 1 35 36 86 78 31 82 80 24 93 63 84 39 89 19 76 57 67 29 5 32 36 88 59 95 64 93 10 51 63 50 74 8 9 68 79 90 95 47 92 87 81 29 35 71 61 36 86 70 96 88 27 56 32 67 11 61 32 99 94 80 91 93 82 100 28 40 43 82 93 98 78 59 42 72 11 93 41 68 100 9 20 11 69 57 59 88 34 69 38 33 57 13 29 24 35 79 16 39 56 3 94 9 66 2 2 67 7 59 53 81 14 64 37 35 43 79 61 21 91 77 27 4 22 70 70 15 100 4 95 39 61 1 52 90 12 44 64 8 58 6 41 18 91 73 45 76 42 17 11 32 50 2 1 61 62 2 61 48 2 12 12 43 53 43 17 21 65 12 82 6 95 45 52 88 12 92 95 15 20 78 76 78 1 87 15 82 23 73 70 98 51 17 46 23 95 64 32 51 35 5 79 68 3 31 24 77 17 26 51 38 87 98 44 55 95 50 49 26 21 45 11 7 33 12 48 44 10 83 83 47 26 91 59 29 59 71 99 62 43 55 13 52 98 56 76 99 24 17 95 62 68 57 84 1 85 14 41 58 66 51 54 81 44 73 22 35 54 9 33 73 34 12 68 85 97 47 23 91 98 40 87 92 63 70 59 48 79 1 54 90 94 28 29 47 44
500
31 60 14 2 42 88 47 55 42 14 34 83 34 31 23 31 43 79 11 95 74 4 29 76 5 27 72 39 17 79 55 40 91 27 12 5 24 92 41 54 65 44 48 56 17 88 5 13 81 42 31 47 22 78 4 74 80 65 32 93 99 14 21 30 90 48 50 43 96 30 78 63 40 34 26 15 17 61 96 40 59 8 2 94 17 66 80 25 79 83 66 87 66 18 47 45 67 37 89 96 28 100 30 92 27 63 4 20 71 33 86 7 32 6 82 2 62 19 44 70 73 82 31 67 35 93 61 53 85 30 94 24 88 54 66 75 64 43 22 70 21 87 17 7 2 89 98 1 3 95 23 92 60 73 89 45 78 60 67 48 85 88 7 94 54 68 48 58 16 28 57 78 10 92 52 97 94 73 82 40 50 65 42 16 43 67 3 43 33 67 50 91 72 71 44 17 57 12 7 8 87 42 15 5 96 98 5 23 31 100 14 34 44 43 18 18 63 86 73 57 81 98 12 62 19 58 40 92 71 61 21 87 97 5 64 26 51 98 50 25 5 41 93 21 22 74 26 23 12 1 90 6 96 71 20 9 79 2 12 30 86 36 51 64 71 31 23 1 80 87 95 65 100 8 38 35 23 48 12 55 78 70 15 62 1 56 95 5 46 97 19 76 29 6 26 39 33 48 46 64 67 16 1 25 69 73 27 21 65 45 12 30 88 94 97 23 21 98 37 51 75 35 87 68 44 86 76 52 26 40 33 55 87 50 63 86 98 46 71 92 60 65 19 8 55 84 29 52 74 27 93 80 12 68 45 89 41 22 14 67 71 100 20 65 4 62 98 3 54 88 93 15 52 16 58 82 9 4 90 51 29 23 62 93 18 46 70 96 50 96 17 37 94 25 4 28 27 39 27 5 38 6 46 62 63 36 32 76 78 94 36 14 87 77 71 73 30 67 47 41 40 93 46 72 9 56 82 62 89 44 45 82 17 18 3 72 25 84 7 54 86 76 3 57 21 32 34 14 57 24 79 6 30 57 89 61 17 80 50 49 16 99 21 32 84 63 91 18 100 93 15 65 50 77 10 62 58 93 1 62 2 33 60 66 70 100 14 82 43 72 14 46 84 45 72 57 9 2 50 83
0
"""
        output = """29.69835625080959
28.599158309292946
28.831335383571812
29.45328361999729
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """1000
1 34 44 63 30 1 9 53 57 57 20 12 52 44 6 9 94 31 67 70 33 18 48 73 69 81 24 50 93 65 70 52 28 91 25 36 21 45 11 63 85 64 2 11 37 77 32 30 98 76 92 91 45 35 26 30 31 28 27 44 35 5 61 50 21 57 33 73 14 91 10 20 6 96 50 28 20 98 25 97 50 57 85 94 46 8 7 10 55 53 66 84 39 2 91 31 38 96 57 64 12 28 43 7 69 13 2 11 81 59 72 32 15 48 65 98 26 39 32 19 88 52 88 14 80 96 51 51 14 63 35 74 48 22 31 41 58 79 27 4 98 9 94 89 39 86 94 89 21 12 47 88 11 10 88 69 4 74 1 75 6 84 53 71 88 3 11 6 11 1 97 43 86 61 48 25 32 59 87 20 1 16 56 83 75 62 7 3 69 66 71 19 24 90 7 20 31 56 33 94 75 96 11 74 56 31 96 46 6 95 49 74 54 75 61 42 57 45 44 41 38 80 36 50 30 11 8 18 56 88 74 27 46 13 73 96 54 54 84 18 56 18 77 78 77 100 55 29 3 62 56 71 17 95 82 31 81 5 87 60 8 55 80 3 66 54 33 37 33 64 18 8 84 11 68 17 47 20 29 72 8 57 21 54 29 55 31 78 49 21 5 15 11 20 26 99 32 2 10 52 23 18 53 25 96 72 54 26 79 17 43 98 89 33 18 5 44 96 50 8 37 3 68 46 64 41 99 97 52 8 68 98 79 51 10 31 61 17 62 94 10 54 99 31 35 44 90 89 32 93 2 75 95 94 66 50 66 38 59 42 49 44 30 16 90 10 89 55 44 2 72 17 65 78 13 6 12 13 83 93 24 2 25 5 38 3 5 64 92 74 76 7 60 27 97 60 64 59 78 85 48 57 49 6 55 95 60 31 24 84 25 48 3 48 77 50 93 89 5 34 59 43 15 68 29 7 92 1 93 19 99 19 69 76 80 20 64 97 80 17 67 41 33 31 15 56 72 12 80 97 1 17 4 94 56 29 82 6 30 38 98 87 58 78 83 55 7 58 30 81 42 67 53 34 61 91 17 33 7 15 86 48 28 36 59 84 11 43 75 5 72 73 6 81 72 80 18 82 81 92 76 1 47 33 69 59 27 79 67 69 55 4 64 23 12 94 49 58 32 20 13 93 33 21 24 39 10 53 23 29 77 53 18 24 3 5 37 51 36 26 29 65 27 66 76 5 65 74 59 25 22 30 78 25 27 5 52 38 39 26 80 20 76 89 98 21 79 67 98 56 75 29 3 77 80 83 77 62 28 92 83 75 62 43 98 34 6 19 76 39 21 58 40 89 72 28 57 69 65 71 80 68 39 12 7 47 79 71 11 85 43 97 9 72 69 77 8 13 49 18 58 19 55 91 54 40 50 85 12 75 22 37 29 86 94 68 44 32 55 40 84 84 85 16 97 89 35 52 23 14 90 26 86 98 77 16 50 41 14 89 23 80 83 41 67 47 1 64 23 79 46 37 58 100 86 72 18 93 33 99 32 46 85 87 36 3 5 51 78 88 96 93 79 38 88 20 16 88 58 54 54 89 84 86 76 90 10 54 96 98 70 71 69 39 99 84 45 92 1 43 54 86 3 90 46 20 91 45 70 43 61 98 1 78 26 84 79 51 4 95 81 60 57 27 21 76 97 49 18 9 27 46 83 35 67 37 46 5 44 26 56 70 60 24 80 83 8 40 57 24 19 36 98 54 9 70 35 86 21 7 15 81 71 80 63 76 72 15 45 64 27 44 76 24 58 12 19 62 73 12 67 24 40 75 11 3 23 46 23 37 34 48 35 79 12 10 14 38 18 14 51 4 70 88 92 50 56 6 30 69 30 53 12 51 71 46 92 91 75 65 18 59 54 17 75 84 17 8 9 95 57 64 91 50 96 83 7 50 24 50 54 65 40 65 3 74 44 12 60 48 70 77 53 34 5 49 90 66 11 3 98 67 23 84 29 81 46 96 18 50 20 27 30 79 37 84 75 49 39 7 14 93 92 20 91 17 49 64 18 18 42 49 99 87 23 8 26 95 25 48 84 19 48 91 39 65 96 42 78 18 33 16 11 26 86 15 72 7 54 41 99 45 10 6 24 78 81 81 69 59 71 97 52 44 67 39 74 32 53 35 82 63 99 2 40 99 12 85 74 59 17 44 79 75 38 30 16 72 68 58 36 56 93 49 5 92 65 79 9 56 68 74 26 2 27 66 88 100 25 17
1000
50 11 54 24 59 54 3 56 60 7 88 58 4 83 85 88 11 43 71 62 87 2 49 98 76 42 19 81 77 16 34 55 95 56 71 93 23 54 2 24 79 91 21 43 68 53 91 83 76 60 93 73 43 12 63 95 17 76 25 85 7 80 74 8 67 67 43 78 82 75 35 87 18 93 99 49 58 54 21 15 21 12 6 31 90 79 4 18 16 56 61 6 54 55 12 40 70 32 5 35 87 36 17 46 66 28 77 35 1 80 3 60 52 71 46 54 48 52 19 14 84 62 31 21 66 80 42 76 68 44 48 58 21 97 17 47 88 48 2 70 44 33 79 48 47 36 65 48 53 10 96 28 3 22 14 91 18 37 24 87 18 52 41 28 32 87 18 26 48 19 39 30 26 100 72 90 55 81 52 33 74 40 20 11 91 43 63 48 55 85 18 98 18 67 37 16 48 9 18 66 62 41 71 1 1 35 36 86 78 31 82 80 24 93 63 84 39 89 19 76 57 67 29 5 32 36 88 59 95 64 93 10 51 63 50 74 8 9 68 79 90 95 47 92 87 81 29 35 71 61 36 86 70 96 88 27 56 32 67 11 61 32 99 94 80 91 93 82 100 28 40 43 82 93 98 78 59 42 72 11 93 41 68 100 9 20 11 69 57 59 88 34 69 38 33 57 13 29 24 35 79 16 39 56 3 94 9 66 2 2 67 7 59 53 81 14 64 37 35 43 79 61 21 91 77 27 4 22 70 70 15 100 4 95 39 61 1 52 90 12 44 64 8 58 6 41 18 91 73 45 76 42 17 11 32 50 2 1 61 62 2 61 48 2 12 12 43 53 43 17 21 65 12 82 6 95 45 52 88 12 92 95 15 20 78 76 78 1 87 15 82 23 73 70 98 51 17 46 23 95 64 32 51 35 5 79 68 3 31 24 77 17 26 51 38 87 98 44 55 95 50 49 26 21 45 11 7 33 12 48 44 10 83 83 47 26 91 59 29 59 71 99 62 43 55 13 52 98 56 76 99 24 17 95 62 68 57 84 1 85 14 41 58 66 51 54 81 44 73 22 35 54 9 33 73 34 12 68 85 97 47 23 91 98 40 87 92 63 70 59 48 79 1 54 90 94 28 29 47 44 31 60 14 2 42 88 47 55 42 14 34 83 34 31 23 31 43 79 11 95 74 4 29 76 5 27 72 39 17 79 55 40 91 27 12 5 24 92 41 54 65 44 48 56 17 88 5 13 81 42 31 47 22 78 4 74 80 65 32 93 99 14 21 30 90 48 50 43 96 30 78 63 40 34 26 15 17 61 96 40 59 8 2 94 17 66 80 25 79 83 66 87 66 18 47 45 67 37 89 96 28 100 30 92 27 63 4 20 71 33 86 7 32 6 82 2 62 19 44 70 73 82 31 67 35 93 61 53 85 30 94 24 88 54 66 75 64 43 22 70 21 87 17 7 2 89 98 1 3 95 23 92 60 73 89 45 78 60 67 48 85 88 7 94 54 68 48 58 16 28 57 78 10 92 52 97 94 73 82 40 50 65 42 16 43 67 3 43 33 67 50 91 72 71 44 17 57 12 7 8 87 42 15 5 96 98 5 23 31 100 14 34 44 43 18 18 63 86 73 57 81 98 12 62 19 58 40 92 71 61 21 87 97 5 64 26 51 98 50 25 5 41 93 21 22 74 26 23 12 1 90 6 96 71 20 9 79 2 12 30 86 36 51 64 71 31 23 1 80 87 95 65 100 8 38 35 23 48 12 55 78 70 15 62 1 56 95 5 46 97 19 76 29 6 26 39 33 48 46 64 67 16 1 25 69 73 27 21 65 45 12 30 88 94 97 23 21 98 37 51 75 35 87 68 44 86 76 52 26 40 33 55 87 50 63 86 98 46 71 92 60 65 19 8 55 84 29 52 74 27 93 80 12 68 45 89 41 22 14 67 71 100 20 65 4 62 98 3 54 88 93 15 52 16 58 82 9 4 90 51 29 23 62 93 18 46 70 96 50 96 17 37 94 25 4 28 27 39 27 5 38 6 46 62 63 36 32 76 78 94 36 14 87 77 71 73 30 67 47 41 40 93 46 72 9 56 82 62 89 44 45 82 17 18 3 72 25 84 7 54 86 76 3 57 21 32 34 14 57 24 79 6 30 57 89 61 17 80 50 49 16 99 21 32 84 63 91 18 100 93 15 65 50 77 10 62 58 93 1 62 2 33 60 66 70 100 14 82 43 72 14 46 84 45 72 57 9 2 50 83
0
"""
        output = """29.187966544451147
29.144769067535943
"""
        self.assertIO(input, output)
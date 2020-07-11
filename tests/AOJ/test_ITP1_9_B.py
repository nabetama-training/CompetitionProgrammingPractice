import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_9_B import resolve


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
        input = """aabc
3
1
2
1
vwxyz
2
3
4
-
"""
        output = """aabc
xyzvw
"""

        self.assertIO(input, output)

    def test_2(self):
        input = """aaa
2
1
2
aaaax
1
1
aaaax
2
1
2
aaaax
3
1
2
3
aaaax
4
1
2
3
4
-
"""
        output = """aaa
aaaxa
axaaa
aaaxa
aaaax
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij
100
2
10
3
3
7
8
10
11
13
9
2
10
3
3
7
8
10
11
13
9
2
10
3
3
7
8
10
11
13
9
2
10
1
3
17
81
10
11
13
9
2
10
3
3
78
8
10
11
133
9
2
101
3
3
7
8
10
11
13
9
2
198
3
3
7
8
10
111
13
9
2
10
3
3
7
88
10
11
50
9
2
10
1
3
7
8
10
11
13
9
2
10
3
3
1
8
10
11
13
9
-
"""
        output = """abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """aaafieiifififaiefaefaef
5
1
1
2
5
19
aaaffffififififoaieaiefopppzejfiaeiziisffe
10
2
4
5
7
8
1
1
10
3
5
aaazzzzzlllzqqererererefefmmmmvmvmvnajeifmnnzz
10
30
20
10
40
4
4
4
5
6
2
aaaaxaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
20
3
3
3
3
4
1
2
4
1
10
20
4
1
1
1
3
4
5
6
30
abcdefghijklmnopqrstuvwxyz
10
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
-
"""
        output = """eiifififaiefaefaefaaafi
fffififififoaieaiefopppzejfiaeiziisffeaaaf
mvnajeifmnnzzaaazzzzzlllzqqererererefefmmmmvmv
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
defghijklmnopqrstuvwxyzabc
"""
        self.assertIO(input, output)

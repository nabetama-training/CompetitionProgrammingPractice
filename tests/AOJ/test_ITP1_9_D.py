import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_9_D import resolve


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
        input = """abcde
3
replace 1 3 xyz
reverse 0 2
print 1 4
"""
        output = """xaze
"""

        self.assertIO(input, output)

    def test_2(self):
        input = """xyz
3
print 0 2
replace 0 2 abc
print 0 2
"""
        output = """xyz
abc
"""

        self.assertIO(input, output)

    def test_3(self):
        input = """abcdef
3
print 0 5
reverse 2 4
replace 0 4 zzzzz
"""
        output = """abcdef
"""

        self.assertIO(input, output)

    def test_4(self):
        input = """abcdefghij
15
reverse 3 7
print 1 8
replace 1 3 xyz
print 1 8
replace 4 6 fff
print 1 8
replace 5 5 o
print 1 8
reverse 3 7
print 1 8
replace 8 9 xy
print 0 9
reverse 3 8
reverse 0 5
print 0 9
"""
        output = """bchgfedi
xyzgfedi
xyzfffdi
xyzfofdi
xydfofzi
axydfofzxy
fzxyxaofdy
"""

        self.assertIO(input, output)

    def test_5(self):
        input = """abcdefghijklmnopqrstuvwxyz
16
replace 3 8 ffffff
replace 5 9 ooooo
replace 0 0 x
replace 25 25 y
reverse 3 8
reverse 2 5
reverse 11 19
reverse 8 12
reverse 0 25
replace 8 9 xy
print 0 25
reverse 0 25
replace 0 25 yyyyoyyyyyyyyyyyoooyyyyyyy
print 0 25
reverse 0 25
print 0 25
"""
        output = """yyxwvulmxypqrfoktsfocooobx
yyyyoyyyyyyyyyyyoooyyyyyyy
yyyyyyyoooyyyyyyyyyyyoyyyy
"""
        self.assertIO(input, output)

    def test_6(self):
        input = """aaaaaaaaaa
16
replace 0 4 xxxxx
replace 5 9 yyyyy
print 0 9
print 0 0
print 9 9
reverse 0 9
reverse 0 0
reverse 9 9
reverse 5 5
print 0 9
reverse 4 5
print 0 9
reverse 4 5
print 0 9
reverse 4 5
print 0 9
"""
        output = """xxxxxyyyyy
x
y
yyyyyxxxxx
yyyyxyxxxx
yyyyyxxxxx
yyyyxyxxxx
"""
        self.assertIO(input, output)

    def test_7(self):
        input = """zzzzzzz
23
replace 0 0 x
replace 6 6 y
print 0 6
reverse 0 0
reverse 1 1
reverse 6 6
print 0 6
print 0 0
reverse 0 6
print 0 6
replace 3 3 i
reverse 0 6
print 0 6
reverse 0 6
print 0 6
replace 1 2 ab
replace 4 5 nm
print 0 6
reverse 0 6
print 0 6
reverse 0 4
reverse 2 5
print 0 6
"""
        output = """xzzzzzy
xzzzzzy
x
yzzzzzx
xzzizzy
yzzizzx
yabinmx
xmnibay
biaxmny
"""
        self.assertIO(input, output)

import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_8_C import resolve


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
        input = """This is a pen.
"""
        output = """a : 1
b : 0
c : 0
d : 0
e : 1
f : 0
g : 0
h : 1
i : 2
j : 0
k : 0
l : 0
m : 0
n : 1
o : 0
p : 1
q : 0
r : 0
s : 2
t : 1
u : 0
v : 0
w : 0
x : 0
y : 0
z : 0
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """The University of Aizu team visited Governor Sato at the Fukushima Prefectural Office on May 26 to report the result of their first participation at the ACM-ICPC World Finals (April 2009, Sweden).
Coach Yutaka Watanobe and 2 contestants, Mr. Takashi Tayama and Mr. Yuki Hirano, visited the Governor accompanying with Vice President Nicolay Mirenkov, who made an introduction of the team to the Governor. Coach Watanobe explained the atmosphere of the contest and the team's performance using pictures and documents he brought. The team received a compliment from the Governor showing his gratitude to the team for proving the University through the contest competing with other world-renowned universities. The Governor also expressed his high expectation to the team to make further achievement in the future. The team was encouraged by his words and reaffirmed their determination to pass the preliminary round within Japan in July and the Asia Regionals in November to go to the Finals again.
Before the visit to the Governor, the team also met Vice Governor Matsumoto and Vice Governor Uchibori, and they commended the team for the achievement.
"""
        output = """a : 75
b : 7
c : 32
d : 29
e : 119
f : 20
g : 21
h : 55
i : 71
j : 2
k : 6
l : 15
m : 37
n : 66
o : 79
p : 20
q : 0
r : 67
s : 40
t : 102
u : 25
v : 23
w : 13
x : 3
y : 12
z : 1
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """ABCD E F Z
x 
y
z
"""
        output = """a : 1
b : 1
c : 1
d : 1
e : 1
f : 1
g : 0
h : 0
i : 0
j : 0
k : 0
l : 0
m : 0
n : 0
o : 0
p : 0
q : 0
r : 0
s : 0
t : 0
u : 0
v : 0
w : 0
x : 1
y : 1
z : 2
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """349832489 237492374 928374983412412 .....<><><><><...!!!!
()()()()---=============
...
93243248320840932048032840@@@\"\"\"
"""
        output = """a : 0
b : 0
c : 0
d : 0
e : 0
f : 0
g : 0
h : 0
i : 0
j : 0
k : 0
l : 0
m : 0
n : 0
o : 0
p : 0
q : 0
r : 0
s : 0
t : 0
u : 0
v : 0
w : 0
x : 0
y : 0
z : 0
"""
        self.assertIO(input, output)

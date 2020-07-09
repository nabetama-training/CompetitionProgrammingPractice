import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_8_B import resolve


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
        input = """123
55
1000
0
"""
        output = """6
10
1
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """123434134414
999999999999999999
234823492348923949234
1134842394
12349
219349
2394295922
2134324009823984932973957384823684234729917374928374
89237497289349179374923947926525620343
8412634873268747123
2987489327983
1000000000000000000000001
0
"""
        output = """34
162
97
39
19
28
47
253
196
86
79
2
"""

        self.assertIO(input,output)

    def test_3(self):
        input = """123434134414
999999999999999999
234823492348923949234
1134842394
12349
219349
2394295922
2134324009823984932973957384823684234729917374928374
89237497289349179374923947926525620343
8412634873268747123
2987489327983
587423874100000123420402030401234230420340
10004030401010203040001023040103204023043040
8888949249823984932973957384823684234729917374928374
89237497289349179374923947926525620343
841263489823984932973957384823684234729917374928374
89237497289349179374923947926525620343
8412634873268747123
2987489327983
587423874173268747123
2987489327983
58742387419237
11112001029199101002311020374723874100746
888381001039823984932973957384823684234729917374928374
89237497289349179374923947926525620343
8412634873268747123
2987489327983
5874238741874743274972347
1
1
1
1
2
2
3
4
45
23
3
2
2
2134
111
1111111111111111111111111111111111111
13243
384
384837493
234923
2
2134
111
1111111111111111111111111111111111111
13243
384
384834837493
234923
2
2134
111
1111111111111111111111111111111111111
13243
384
384837493
234923994829374921734
23744837493
234923
2
2134
111
1111111111111111111111111111111111111
13243
384
384837493
234923994829374921734
23749234893298473274
23483274832
2384374
384
82374
9993949292939499293949293949923949394234999939492929394992939492939499239493942349999394929293949929394929394992394939423499993949292939499293949293949923949394234999234893298473274
23483274832
2384374
384
82374
9993949292939499293949293949923949394234999939492929394992939492939499239493942349999394929293949929394929394992394939423499993949292939499293949293949923949394234997493
234923994829374921734
23749234893298473274
23483274832
2384374
384
82374
99939492929394992939492939499239493942349999394929293949929394929394992394939423499993949292939499293949293949924837493
234923
2
2134
111
1111111111111111111111111111111111111
13243
384
384837493
234923994829374921734
23749234893298473274
23483274832
2384374
384
82374
9993949292939499293949293949923949394234999939492929394992939492939499239493942349999394929293949929394929394992394934837493
234923
2
2134
111
1111111111111111111111111111111111111
13243
384
384837493
234923994829374921734
23749234893298473274
23483274832
2384374
384
82374
999394929293949929394929394992394939423499993949292939499293949293949923949394234999939492929394992939492939499239493942349999394929293949929394929394992394939423499942349999394929293949929394929394992394939423499394939423499993949292939499293949293949923949394234999939492929394992939492939499239493942349
22
2
2
0
"""
        output = """34
162
97
39
19
28
47
253
196
86
79
102
59
294
196
270
196
86
79
99
79
70
111
274
196
86
79
127
1
1
1
1
2
2
3
4
9
5
3
2
2
10
3
37
13
15
49
23
2
10
3
37
13
15
64
23
2
10
3
37
13
15
49
104
54
23
2
10
3
37
13
15
49
104
100
46
31
15
24
1093
46
31
15
24
1032
104
100
46
31
15
24
729
23
2
10
3
37
13
15
49
104
100
46
31
15
24
757
23
2
10
3
37
13
15
49
104
100
46
31
15
24
1858
4
2
2
"""

        self.assertIO(input,output)

    def test_4(self):
        input = """1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
1811111111111111111111111111111111111111111111111111111111111111111111111111111111011111111111111111111111111111111111111111111111111111111111111111111111111111111011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111177711111111111111111111111111111111111111111181111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
98398798238974910987000838749823794798237497293749872398798749749874972394797979711010873
0
"""
        output = """1000
1029
520
"""

        self.assertIO(input,output)
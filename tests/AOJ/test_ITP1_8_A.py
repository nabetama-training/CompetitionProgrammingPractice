import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_8_A import resolve


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
        input = """fAIR, LATER, OCCASIONALLY CLOUDY.
"""
        output = """Fair, later, occasionally cloudy.
"""
        self.assertIO(input, output)

    def test_2(self):
        input = """a
"""
        output = """A
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """s1061159 m5061126 d8061103
"""
        output = """S1061159 M5061126 D8061103
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """tHE uNIVERSITY OF aIZU TEAM VISITED gOVERNOR sATO AT THE fUKUSHIMA pREFECTURAL oFFICE ON mAY 26 TO REPORT THE RESULT OF THEIR FIRST PARTICIPATION AT THE acm-icpc wORLD fINALS (aPRIL 2009, sWEDEN). cOACH yUTAKA wATANOBE AND 2 CONTESTANTS, mR. tAKASHI tAYAMA AND mR. yUKI hIRANO, VISITED THE gOVERNOR ACCOMPANYING WITH vICE pRESIDENT nICOLAY mIRENKOV, WHO MADE AN INTRODUCTION OF THE TEAM TO THE gOVERNOR. cOACH wATANOBE EXPLAINED THE ATMOSPHERE OF THE CONTEST AND THE TEAM'S PERFORMANCE USING PICTURES AND DOCUMENTS HE BROUGHT. tHE TEAM RECEIVED A COMPLIMENT FROM THE gOVERNOR SHOWING HIS GRATITUDE TO THE TEAM FOR PROVING THE uNIVERSITY THROUGH THE CONTEST COMPETING WITH OTHER WORLD-RENOWNED UNIVERSITIES. tHE gOVERNOR ALSO EXPRESSED HIS HIGH EXPECTATION TO THE TEAM TO MAKE FURTHER ACHIEVEMENT IN THE FUTURE. tHE TEAM WAS ENCOURAGED BY HIS WORDS AND REAFFIRMED THEIR DETERMINATION TO PASS THE PRELIMINARY ROUND WITHIN jAPAN IN jULY AND THE aSIA rEGIONALS IN nOVEMBER TO GO TO THE fINALS AGAIN. bEFORE THE VISIT TO THE gOVERNOR, THE TEAM ALSO MET vICE gOVERNOR mATSUMOTO AND vICE gOVERNOR uCHIBORI, AND THEY COMMENDED THE TEAM FOR THE ACHIEVEMENT.
"""
        output = """The University of Aizu team visited Governor Sato at the Fukushima Prefectural Office on May 26 to report the result of their first participation at the ACM-ICPC World Finals (April 2009, Sweden). Coach Yutaka Watanobe and 2 contestants, Mr. Takashi Tayama and Mr. Yuki Hirano, visited the Governor accompanying with Vice President Nicolay Mirenkov, who made an introduction of the team to the Governor. Coach Watanobe explained the atmosphere of the contest and the team's performance using pictures and documents he brought. The team received a compliment from the Governor showing his gratitude to the team for proving the University through the contest competing with other world-renowned universities. The Governor also expressed his high expectation to the team to make further achievement in the future. The team was encouraged by his words and reaffirmed their determination to pass the preliminary round within Japan in July and the Asia Regionals in November to go to the Finals again. Before the visit to the Governor, the team also met Vice Governor Matsumoto and Vice Governor Uchibori, and they commended the team for the achievement.
"""
        self.assertIO(input, output)


import sys
from io import StringIO
import unittest

from src.AOJ.ITP1_9_A import resolve


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
        input = """computer
Nurtures computer scientists and highly-skilled computer engineers
who will create and exploit "knowledge" for the new era.
Provides an outstanding computer environment.
END_OF_TEXT
"""
        output = """3
"""

        self.assertIO(input, output)

    def test_2(self):
        input = """aizu
aaa aizu xxx xx x xxx aizu y yyyy a a a a a a aizu 
aaa aa xxx WWW AAA aize aiza AIZZ AAA III a i z u aizu aizu aizu
SSS SS S aizu AAAAAAA a a a a a x x x x aizu zia uzia uzia aizu aizu aizu aizu
Aizu hyoooon pupupupu ohohohoh
aa eee fff eee fff ee f f f f f f f AIZU bebebebebebe ai zu a izu aiz u
Aizu aizu Aizu AIzU
end_of_text
END_OF_TEXP
aizu Aizu
END_OF_TEXT
"""
        output = """20
"""
        self.assertIO(input, output)

    def test_3(self):
        input = """aaaaaaaaaa
bb bb bb aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa
aaa aaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa
aaaaaaaaaa xxx xxxxxxxxx aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa
aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa b b b b b b b aaaaaaaaaa aaaaaaaaaa
aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaaa a a a a 
aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa
aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa a a a a 
aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa x
aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa x x x x
aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa x x xaaaaaaaaaa
END_OF_TEXT
"""
        output = """50
"""
        self.assertIO(input, output)

    def test_4(self):
        input = """x
sfjioeixi x oeif  x oie  xx foe xx x xx fiwej x
aaasfjioeixi x oeif  x oie  xx foe xx x xx fiwej x
xxkxooxx yyy aaaa aa a a  a a  a a a x xxxx xx x x x xxx x x xxx
xoixxx  bb b ba aa a a  a a  a a a x xxxx xx x x x xxx x x xxx
sfjioeixi x oeif  x oie  xx foe xx x 
xx fiwxxkxooxx yyy aaaa aa a a  a a  a a a x xxxx xx  xx x xxx x x xxxejx 
xoixxx  bb b ba aa a a  a a  a a a x xxxx xx x x x xxx x x xxx
s x x x
x
  x
x
fjioeixi x oeif  x oie  xxxxkxooxx yyy 
aaaa aa a a  a a  a a a x xxxx xx x x x xxx x x xxx foe xx x xx fiwej x
aaaa aa a a  a a  a a a x xxxx xx x x x xxx x x xxx
END_OF_TEXT
"""
        output = """55
"""
        self.assertIO(input, output)

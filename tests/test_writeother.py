
import unittest
from PyToTex.texhandler import TexHandler

class TestWriteOther(unittest.TestCase):
    def test_writeTitle(self):
        with TexHandler("./tests/Tex") as th:
            th.write_section("hello")
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\usepackage{graphicx}"'\n'
            r"\usepackage{rotating}"'\n'
            r"\usepackage[margin=25mm]{geometry}"'\n'            
            r"\begin{document}"'\n'
            r"\section{hello}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)
        

if __name__ == '__main__':
    unittest.main()
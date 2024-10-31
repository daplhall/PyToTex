import unittest
from PyToTex.texhandler import TexHandler


class TestWriteTable(unittest.TestCase):

    def test_WriteTableFromList(self):
        """
            tests if we can write a table from python list
        """
        with TexHandler('./tests/Tex') as th:
            list = [
                [1,2,3,4,5],
                [6,7,8,9,1]
            ]
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = r"\documentclass{article}"'\n'\
            r"\begin{document}"'\n'\
            r"\begin{table}[h]"'\n'\
            '\t'r"\centering"'\n'\
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'\
            '\t\t'r"\hline\hline"'\n'\
            '\t\t'r"1 & 2 & 3 & 4 & 5 \\"'\n'\
            '\t\t'r"\hline"'\n'\
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'\
            '\t\t'r"\hline"'\n'\
            '\t'r"\end{tabular}"'\n'\
            r"\end{table}"'\n'\
            r"\end{document}"'\n'
        self.assertEqual(f, answer)

    def test_WriteTableFromListDecimals(self):
        """
            tests if we can write a table from python list
        """
        with TexHandler('./tests/Tex') as th:
            list = [
                [1.1, 2.2, 3.3, 4.4, 5.2],
                [6.11, 7.124, 8.4343, 9.12312321, 1.12312313213]
            ]
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = r"\documentclass{article}"'\n'\
            r"\begin{document}"'\n'\
            r"\begin{table}[h]"'\n'\
            '\t'r"\centering"'\n'\
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'\
            '\t\t'r"\hline\hline"'\n'\
            '\t\t'r"1.10 & 2.20 & 3.30 & 4.40 & 5.20 \\"'\n'\
            '\t\t'r"\hline"'\n'\
            '\t\t'r"6.11 & 7.12 & 8.43 & 9.12 & 1.12 \\"'\n'\
            '\t\t'r"\hline"'\n'\
            '\t'r"\end{tabular}"'\n'\
            r"\end{table}"'\n'\
            r"\end{document}"'\n'
        self.assertEqual(f, answer)

    def test_WriteTableFromListMixed(self):
        """
            tests if we can write a table from python list
        """
        with TexHandler('./tests/Tex') as th:
            list = [
                [1, 2.2, 3.3, 4.4, 5.2],
                [6.11, 7.124, 8, 9.12312321, 1123]
            ]
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = r"\documentclass{article}"'\n'\
            r"\begin{document}"'\n'\
            r"\begin{table}[h]"'\n'\
            '\t'r"\centering"'\n'\
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'\
            '\t\t'r"\hline\hline"'\n'\
            '\t\t'r"1 & 2.20 & 3.30 & 4.40 & 5.20 \\"'\n'\
            '\t\t'r"\hline"'\n'\
            '\t\t'r"6.11 & 7.12 & 8 & 9.12 & 1123 \\"'\n'\
            '\t\t'r"\hline"'\n'\
            '\t'r"\end{tabular}"'\n'\
            r"\end{table}"'\n'\
            r"\end{document}"'\n'
        self.assertEqual(f, answer)

   # def test_WriteTableFromListWithFile(self):
   #     """
   #         tests if we can write a table from python list to specific file
   #     """
   #     with texhandler('./tests/Tex') as th:
            ## add
   #         list = [
   #             [1,2,3,4,5],
   #             [6,7,8,9,1]
   #         ]
   #         th.write_table(list) 


if __name__ == '__main__':
    unittest.main()
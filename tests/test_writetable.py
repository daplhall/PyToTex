import sys
sys.path.append("./PyToTex")

import unittest
import numpy as np
import pandas as pd
from PyToTex.texhandler import TexHandler


class TestWriteTable(unittest.TestCase):

    def test_TableFromList(self):
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
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromListCrocked(self):
        """
            tests if we can write a table from python list
        """
        with TexHandler('./tests/Tex') as th:
            list = [
                [1,2,3,4,5],
                [6,7,8]
            ]
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromListDecimals(self):
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
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1.10 & 2.20 & 3.30 & 4.40 & 5.20 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6.11 & 7.12 & 8.43 & 9.12 & 1.12 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromListMixed(self):
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
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2.20 & 3.30 & 4.40 & 5.20 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6.11 & 7.12 & 8 & 9.12 & 1123 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromListWide(self):
        """
            tests if we can write a wide table from python list
        """
        with TexHandler('./tests/Tex') as th:
            list = [
                [1, 2, 3, 4,    5,  10, 43, 432, 423, 234, 234,  1],
                [6, 7, 8, 9, 1123, 123,  3,  12,   6,   5, 345, 53]
            ]
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'\
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c|c|c|c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 10 & 43 & 432 & 423 & 234 & 234 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1123 & 123 & 3 & 12 & 6 & 5 & 345 & 53 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromListLonger(self):
        """
            tests if we can write a long table from python list
        """
        with TexHandler('./tests/Tex') as th:
            list = [
                [1,2,3,4,5],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1],
                [6,7,8,9,1]
            ]
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromNumpy1DRow(self):
        """
            tests if we can write a table from a 1D numpy array (assumed by code as a row)
        """
        with TexHandler('./tests/Tex') as th:
            list = np.array([1,2,3,4,5])
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromNumpy1DColmn(self):
        """
            tests if we can write a table from a 1D numpy array (assumed by code as a row)
        """
        with TexHandler('./tests/Tex') as th:
            list = np.array([[1],[2],[3],[4],[5]])
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"2 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"3 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"4 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromNumpy(self):
        """
            tests if we can write a table from numpy array
        """
        with TexHandler('./tests/Tex') as th:
            list = np.array([
                    [1,2,3,4,5],
                    [1,2,3,4,5]
                ])
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromMixed(self):
        """
            tests if we can write a table from numpy array with mixed floats
        """
        with TexHandler('./tests/Tex') as th:
            list = np.array([
                    [1.123,2,3.123,4.123,5.123],
                    [1.123,2.123,3,4.123,5.123]
                ])
            th.write_table(list) 
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1.12 & 2 & 3.12 & 4.12 & 5.12 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1.12 & 2.12 & 3 & 4.12 & 5.12 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)
        
    def test_TableFromPandas(self):
        dataframe = pd.DataFrame({
            "A": [1,1,1,1,1],
            "B": [2,2,2,2,2],
            "C": [3,3,3,3,3],
            "D": [4,4,4,4,4],
            "E": [5,5,5,5,5],
            "F": [6,6,6,6,6]
        })
        with TexHandler('./tests/Tex') as th:
            th.write_table(dataframe)
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c|c}"'\n'
            '\t\t'r"A & B & C & D & E & F \\"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableFromDict(self):
        data = {
            "A": [1,1,1,1,1],
            "B": [2,2,2,2,2],
            "C": [3,3,3,3,3],
            "D": [4,4,4,4,4],
            "E": [5,5,5,5,5],
            "F": [6,6,6,6,6]
        }
        with TexHandler('./tests/Tex') as th:
            th.write_table(data)
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c|c}"'\n'
            '\t\t'r"A & B & C & D & E & F \\"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"1 & 2 & 3 & 4 & 5 & 6 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)
        
    def test_TableFromDictException(self):
        """Testing that that we catch the valueerror from pandas conversion"""
        data = {
            "A": [1,1,1,1,1],
            "B": [2,2,2,2,2],
            "C": [3,3,3,3,3],
            "D": [4,4,4,4,4],
            "E": [5,5,5,5,5],
            "F": [6,6,6,6]
        }
        with self.assertRaises(ValueError):
            with TexHandler('./tests/Tex') as th:
                th.write_table(data)

    def test_TableOptions(self):
        """
            testing the table options 
        """
        list = [
            [1.123123,2,3,4,5],
            [6,7,8,9,1]
        ]
        with TexHandler('./tests/Tex', 
                        colmnOptions={
                            "headerSeperator": r"\hline\hline\hline", 
                            "rowSeperator": r"\hline\hline", 
                            'decimals': 4,
                            'colmSeperator': False
                        }
        ) as th:
            th.write_table(list)
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{ccccc}"'\n'
            '\t\t'r"\hline\hline\hline"'\n'
            '\t\t'r"1.1231 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

    def test_TableOptionsColmSeperator(self):
        """
            testing the table options 
        """
        list = [
            [1.123123,2,3,4,5],
            [6,7,8,9,1]
        ]
        with TexHandler('./tests/Tex', 
                        colmnOptions={
                            'colmSeperator': True
                        }
        ) as th:
            th.write_table(list)
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\begin{document}"'\n'
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{c|c|c|c|c}"'\n'
            '\t\t'r"\hline\hline"'\n'
            '\t\t'r"1.12 & 2 & 3 & 4 & 5 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t\t'r"6 & 7 & 8 & 9 & 1 \\"'\n'
            '\t\t'r"\hline"'\n'
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)
if __name__ == '__main__':
    unittest.main()
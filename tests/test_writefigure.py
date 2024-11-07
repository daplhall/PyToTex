import unittest
import numpy as np
import matplotlib.pyplot as plt
from PyToTex.texhandler import TexHandler

class TestWriteFigure(unittest.TestCase):
    def test_writefigure(self):
        with TexHandler("./tests/Tex") as th:
            x = np.arange(0,100)
            y = np.sqrt(x)
            fig, ax = plt.subplots()
            ax.plot(x, y)
            th.write_plot(fig)
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\usepackage{graphicx}"'\n'
            r"\usepackage{rotating}"'\n'
            r"\usepackage[margin=25mm]{geometry}"'\n'            
            r"\begin{document}"'\n'
            r"\begin{figure}[h]"'\n'
            r"\centering"'\n'
            '\t\t'r"\includegraphics[width=0.6\textwidth]{./tests/Tex/plots/plot_0.png}"'\n'
            r"\end{figure}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)
        

if __name__ == '__main__':
    unittest.main()
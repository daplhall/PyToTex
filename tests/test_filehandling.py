import os
import unittest
import PyToTex.texhandler as texhandler

from contextlib import contextmanager

class TestFilehandler(unittest.TestCase):
    
    @contextmanager # TODO Read about
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))


    def test_OpenMainTex(self):
        """
            testing if the opening and closing works 
        """
        with self.assertNotRaises(FileNotFoundError):
            with texhandler.TexHandler('./tests/Tex') as th:
                pass

    def test_NewFile(self):
        with texhandler.TexHandler('./tests/Tex') as th:
            th.set_file('test.tex')
            exists = os.path.isfile('./tests/Tex/test.tex')
            self.assertEqual(exists, True)


    def test_writeTexInput(self):
        """
            tests if we can write a table from python list
        """
        with texhandler.TexHandler('./tests/Tex') as th:
            th.set_file('test.tex')
        f = open('./tests/Tex/main.tex','r').read()
        answer = (
            r"\documentclass{article}"'\n'
            r"\usepackage{graphicx}"'\n'
            r"\usepackage{rotating}"'\n'
            r"\begin{document}"'\n'
            r"\input{test.tex}"'\n'
            r"\end{document}"'\n'
        )
        self.assertEqual(f, answer)

if __name__ == '__main__':
    unittest.main()
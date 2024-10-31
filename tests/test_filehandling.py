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


if __name__ == '__main__':
    unittest.main()
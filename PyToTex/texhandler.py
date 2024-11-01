import os
import matplotlib.pyplot as plt
from numpy import ndarray
from pandas import DataFrame, Index

class TexHandler():
    """
        Interfaces:
            TexHandler() -> use hardcoded format
            TexHandler.with_packages(file) -> class method for different constructor that overwrites the hardcoded format
            TexHandler.write_table(data,file:optional) -> writes a table from list or array
            TexHandler.write_plot(fig:plt.figure, texsize: optional, file:optional) -> write a plot into the 
            TexHandler.set_file(file) -> set default file
            TexHandler.append(file: [IOWrapper, path]) -> adds a file to the handler.
            TexHanlder.set_texfolder(folderdir)

            __enter__() -> prepares the files to be written to
            __exit__() -> finishes the main file and closes all files that the handler handles
    """

    def __init__(self, texdir:str = None):
        if texdir:
            self._texdir = texdir
        else:
            self._texdir = r"./Tex"
        if not os.path.exists(self._texdir):
            os.mkdir(self._texdir)
        self._filehandlers = []
    
    def __enter__(self):
        ## This could be split into a sub folder, one where you write it as a class to be compiled and one where you just write a tex file with out begin document and such
        maintex = open(self._texdir + "/main.tex",'w')
        self._currentFile = maintex
        self._mainhandler = maintex
        self._mainhandler.write(
            r"\documentclass{article}"'\n'
        )
        ## TODO write packages
        self._mainhandler.write(
            r"\begin{document}"'\n'
        )
        ## TODO write the header into the main.tex
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        for filehanlder in self._filehandlers:
            # TODO  add that files are added to input as main.tex
            filehanlder.close()
        self._mainhandler.write(
            r"\end{document}"'\n'
        )
        self._mainhandler.close()

    @classmethod
    def with_packages(cls, file):
        pass
    
    def write_table(self, data, file = None):
        """
        we assume that 1d numpy arrays are a row
        """ 
        header = ()
        if isinstance(data, dict):
            try:
                data = DataFrame(data)
            except ValueError as e:
                raise ValueError("When passing a dict, the elements must be the same size")
        if isinstance(data, DataFrame):
            header = data.keys()
            data = data.values
        K = len(header)
        if isinstance(data, ndarray):
            if len(data.shape) == 1:
                data = data[None,:]
            _, M = data.shape
        else:
            M, Mtemp = K, 0
            for row in data:
                Mtemp = len(row)
                if Mtemp > M:
                    M = Mtemp
        ## find max dimmensions, if its a ndarray or pandas then use shortcuts
        self._mainhandler.write(
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{"
        )
        for j in range(M):
            self._mainhandler.write("c|" if j != M - 1 else r"c}"'\n')
        ## TODO HEADER
        if (isinstance(header, Index) and not header.empty) or header:
            self._mainhandler.write("\t\t")
            for j, colmn in enumerate(header):
                self._mainhandler.write(colmn + " & " if j != K-1 else colmn+r" \\"'\n')
        self._mainhandler.write("\t\t"r"\hline\hline"'\n')
        for row in data:
            K = len(row)
            self._mainhandler.write("\t\t")
            for j, element in enumerate(row):
                self._mainhandler.write(f"{element:.0f}" if element%1 == 0 else f"{element:.2f}") # TODO this might need to be an option such that if you want .2 decimals on all numbers then you should have the option
                self._mainhandler.write(" & " if j != K - 1 else '')
                if j == K-1:
                    self._mainhandler.write(r" \\"'\n')
            self._mainhandler.write("\t\t"r"\hline"'\n')  
        self._mainhandler.write(
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
        )

    def write_plot(self, fig:plt.figure, file = None):
        pass

    def set_file(self, file):
        pass
    
    def append(self, file):
        pass
    

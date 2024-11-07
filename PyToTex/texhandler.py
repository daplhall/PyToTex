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

    def __init__(self, texdir:str = None, colmnOptions:dict = {}):
        """TODO I should check if there is an option in colm options that is not supposed to be there"""
        if texdir:
            self._texdir = texdir
        else:
            self._texdir = r"./Tex"
        if not os.path.exists(self._texdir):
            os.mkdir(self._texdir)
        self._filehandlers = []
        self.deci = colmnOptions["decimals"] if "decimals" in colmnOptions else r"2"
        self.headersep = colmnOptions["headerSeperator"] if "headerSeperator" in colmnOptions else r'\hline\hline'
        self.rowsep = colmnOptions["rowSeperator"] if "rowSeperator" in colmnOptions else r'\hline'
        self.colmsep = '' if 'colmSeperator' in colmnOptions and colmnOptions["colmSeperator"] == False else '|'
        self._plotdir = texdir + '/plots'
        if not os.path.exists(self._plotdir):
            os.mkdir(self._plotdir)
        self._figcount = 0

    
    def __enter__(self):
        ## This could be split into a sub folder, one where you write it as a class to be compiled and one where you just write a tex file with out begin document and such
        maintex = open(os.path.abspath(self._texdir + "/main.tex"),'w')
        self._mainhandler = self._currentFile = maintex
        self._mainhandler.write(
            r"\documentclass{article}"'\n'
        )
        # TODO be handled by with_packages
        self._mainhandler.write(
            r"\usepackage{graphicx}"'\n'
        )
        ## TODO write packages
        self._mainhandler.write(
            r"\begin{document}"'\n'
        )
        ## TODO write the header into the main.tex
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        for filehandler in self._filehandlers:
            # TODO  add that files are added to input as main.tex
            self._mainhandler.write(r"\input"f"{{{os.path.basename(filehandler.name)}}}""\n")
            filehandler.close()
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
        self._currentFile.write(
            r"\begin{table}[h]"'\n'
            '\t'r"\centering"'\n'
            '\t'r"\begin{tabular}{"
        )
        for j in range(M):
            self._currentFile.write("c"+self.colmsep if j != M - 1 else r"c}"'\n')
        ## TODO HEADER
        if (isinstance(header, Index) and not header.empty) or header:
            self._currentFile.write("\t\t")
            for j, colmn in enumerate(header):
                self._currentFile.write(colmn + " & " if j != K-1 else colmn+r" \\"'\n')
        self._currentFile.write("\t\t"f"{self.headersep}"'\n')
        for row in data:
            K = len(row)
            self._currentFile.write("\t\t")
            for j, element in enumerate(row):
                self._currentFile.write(f"{element:.0f}" if element%1 == 0 else f"{element:.{self.deci}f}") # TODO this might need to be an option such that if you want .2 decimals on all numbers then you should have the option
                self._currentFile.write(" & " if j != K - 1 else '')
                if j == K-1:
                    self._currentFile.write(r" \\"'\n')
            self._currentFile.write("\t\t"f"{self.rowsep}"'\n')  
        self._currentFile.write(
            '\t'r"\end{tabular}"'\n'
            r"\end{table}"'\n'
        )

    def set_plotdir(self, dir:str):
        """dir is relative to texdir"""
        pass

    def write_plot(self, fig:plt.figure, file = None):
        figureDir = self._plotdir + f'/plot_{self._figcount}.png'
        fig.savefig(figureDir)
        self._figcount += 1
        self._currentFile.write(
            r"\begin{figure}[h]"'\n'
            r"\centering"'\n'
            "\t\t"r"\includegraphics[width=0.6\textwidth]"f"{{{figureDir}}}"'\n'
            r"\end{figure}"'\n'
        )


    def set_file(self, file:str):
        """
            #TODO if the file has no extention we need to assume its .tex 
        """
        file = os.path.abspath(self._texdir + '/' + file)
        if self._mainhandler.name == file:
            self._currentFile = self._mainhandler
            return self._currentFile
        for handler in self._filehandlers:
            if  handler.name == file:
                self._currentFile = handler
                return self._currentFile
        f = open(file, 'w')
        self._filehandlers.append(f)
        self._currentFile = self._filehandlers[-1]
        return self._currentFile
    
    def compile(self):
        pass

    def close_file(self, file):
        """should close a file an pop it from file handlers"""
        pass
    
    def write_section(self, title):
        self._currentFile.write(r"\section"f"{{{title}}}\n")

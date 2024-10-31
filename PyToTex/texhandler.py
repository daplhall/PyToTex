import os
import matplotlib.pyplot as plt

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
        maintex = open(self._texdir + "/main.tex",'w')
        self._filehandlers.append(maintex)
        self._currentFile = maintex

    def __exit__(self, exc_type, exc_value, exc_traceback):
        for filehanlder in self._filehandlers:
            # TODO  add that files are added to input as main.tex
            filehanlder.close()

    @classmethod
    def with_packages(cls, file):
        pass
    
    def write_table(self, data, file = None):
        pass

    def write_plot(self, fig:plt.figure, file = None):
        pass

    def set_file(self, file):
        pass
    
    def append(self, file):
        pass
    

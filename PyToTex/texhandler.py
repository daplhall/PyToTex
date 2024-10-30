class TexHandler():
    """
        Interfaces:
            TexHandler() -> use hardcoded format
            TexHandler.with_packages(file) -> class method for different constructor that overwrites the hardcoded format
            TexHandler.write_table(data,file:optional) -> writes a table from list or array
            TexHandler.write_plot(fig:plt.figure, texsize: optional, file:optional) -> write a plot into the 
            TexHandler.set_file(file) -> set default file
            TexHandler.append(file: [IOWrapper, path]) -> adds a file to the handler.

            __enter__() -> prepares the files to be written to
            __exit__() -> finishes the main file and closes all files that the handler handles
    """

    
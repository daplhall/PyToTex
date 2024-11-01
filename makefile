LATEX     := pdflatex

TEX_BUILD_DIR := .\build
TEX_DIR   	  := .\tests\tex
PDF  	      := main.pdf

SOURCES  := $(wildcard $(TEX_DIR)/*.tex)

$(PDF): $(SOURCES)
	-@mkdir $(TEX_BUILD_DIR)
	$(LATEX) main.tex --aux-directory=$(TEX_BUILD_DIR) --include-directory=$(TEX_DIR) \
		--c-style-errors --interaction=nonstopmode
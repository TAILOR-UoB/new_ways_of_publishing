# Formatting tools

```{mermaid}
flowchart LR
  
    E1("External resources"):::external -.-> A1
    A1{{"Authoring tool"}} --> I1("Text + Figures +\nCode + Tables + ..."):::input
    subgraph "Quarto, pdflatex, xelatex, pandoc, ..." 
      direction LR
      I1 --> P1{{"Formatting tool"}}
      P1 --> O1["Formatted\nOutput"]:::output
    end
    classDef external fill:#eee;
    classDef input fill:#ffa;
    classDef output fill:#faa;
```

### Jupyter Book

Jupyter Book[^jbook] is one of the main projects of the Executable Books
Project[^ebookp], together with the other project MyST Markdown[^myst]. The
Executable Books Project is an international collaboration to build open source
tools for publishing computational documents based on the Jupyter
ecosystem[^jupyter]. Jupyter Book can read markdown, MyST Markdown, Jupyter
notebooks and
[reStructuredText](https://docutils.sourceforge.io/rst.html)[^rst]. It is based
on the [Sphinx documentation engine](https://www.sphinx-doc.org/en/master/)
being able to produce html websites, pdf, and computational narratives. It
supports multiple programming languages in the Jupyter notebooks provided that
a Jupyter kernel exist (e.g. Python, Julia, Rubi, Haskell, and many other
languages[^kernels]).
Websites that include computational narratives can also bennefit from live
environments thanks to the integration of Binder, Thebe and Google
Colab[^colab]. It supports multiple types of narrative content like highlighted
notes, code cells, quotations, epigraphs, glossaries, index of terms,
footnotes, references, grids, cards, dropdown menus, tab content, maths,
equations, proofs, theorems, algorithms, and more. The Jupyter Book system has
been used in multiple ocasions to publish online material, an extensive gallery
can be found at https://executablebooks.org/en/latest/gallery/. This website
has been created with Jupyter Book and serves as an example of some of its
functionalities.

[^jbook]: https://jupyterbook.org/en/stable/intro.html
[^ebookp]: https://executablebooks.org/en/latest/
[^myst]: https://executablebooks.org/en/latest/tools/#tools-myst
[^juypter]: https://jupyter.org/
[^rst]: https://docutils.sourceforge.io/rst.html
[^kernels]: https://github.com/jupyter/jupyter/wiki/Jupyter-kernels
[^colab]: https://colab.research.google.com/

%- [Jupyter{book}](https://jupyterbook.org/en/stable/intro.html)
%  - Sub-project from the Executable Books Project which also stewards the MyST
%    Markdown project.
%  - Based on the 
%  - MyST Markdown, Jupyter notebooks,
%    [reStructuredText](https://docutils.sourceforge.io/rst.html)
%    ([the default plaintext markup language used in Sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer))
%  - Provides its own 
%  - Live environments with Binder, Thebe
%  - Output website and pdf
%  - Examples of websites created with Jupyter Books can be found at
%    
%  - Create the strcuture of the project with `jupyter-book create mynewbook/`
%  - Built with `jupyter-book build mynewbook/`
%  - Does not have preview mode, requires opening the generated html files in
%    the `_build` path, `python -m http.server 8000 -d _site/`
%  - Uses Sphinx under the hood

### Quarto

[Quarto](https://quarto.org) is another open-source publishing system with the
objective of facilitating the collaboration to create scientific content.
Quarto is sponsored by Posit[^posit], and follows the development of the R Markdown
publishing system extending the focus from the programming language R to
Python, R, Julia and Observable. It supports Jupyter notebooks, markdown and
their own extension Quarto markdown. The conversion to different output formats
is done with pandoc[^pandoc], which is able to produce presentations (Reveal.js),
dashboards, websites, blogs, books, PDFs, Microsoft Word, ePub and more. Quarto
is integrated into multiple authoring environments like Microsoft Visual
Studio, Jupyter Lab, Rstudio[^rstudio], and Atlassian Confluence[^confluence]
among others. 

[^posit]: https://posit.co
[^pandoc]: https://pandoc.org/
[^rstudio]: https://posit.co/download/rstudio-desktop/
[^confluence]: https://www.atlassian.com/software/confluence

%- [Quarto](https://quarto.org): 
%  - Quarto supports dynamic content with Python, R, Julia and Observable
%  - programming languages.
%  - Quarto uses pandoc to convert the input artefacts to its output.
%  - Quarto supports plain text markdown, Jupyter notebooks and an augmented
%  - markdown, 
%  - Integration with Posit Connect (former RMarkdown), Atlassian Confluence, Visual
%    Studio, 
%  - Built with `quarto render`
%  - Has a preview mode `quarto preview` which autobuilds and updates when
%    changes in the source files are detected.

### R markdown

[R markdown](https://rmarkdown.rstudio.com/) is a flavoured markdown type with
special focus on the R programming language and a publishing system. The
publishing system uses R markdown files (with extension `.rmd`) or standard
markdown and can produce various output formats including HTML, PDFs, Microsoft
Word documents, Beamer presentations, HTML5 slides, scientific articles and
books (with the the help of the bookdown R package[^bookdown]). It also support
other programming languages including Python, SQL and others with a language
engine[^engines]. R markdown is also integrated in Rstudio[^rstudio].

%- [Rmarkdown](https://rmarkdown.rstudio.com/):
%  - Input R markdown files (.rmd)
%  - Output formats include HTML, PDF, MS Word, Beamer, HTML5 slides, books (see
%    examples of books build with markdown in
%    [bookdown](https://bookdown.org/)), scientific articles, websites.
%	- Supports multiple languages including R, Python and SQL (see
%    [other language engines]()).
%  - Posit Connect

[^bookdown]: https://bookdown.org/
[^engines]: https://bookdown.org/yihui/rmarkdown/language-engines.html

### Bookdown

[Bookdown](https://bookdown.org/) is an open-source R package that facilitates
the creation of books from R Markdown documents. It is an extension for R
Markdown to work with long documents. The rest of the functionalities are
shared with R Markdown. A list of books written with Bookdown can be found at
https://bookdown.org/home/archive/.

%- [Bookdown](https://bookdown.org/) package
%  - It is an R package
%  - It is based on R Markdown
%  - Input R Markdown
%  - Output formats pdf, LaTeX, HTML, EPUB, and Word.
%  - Integartion with RStudio IDE
%  - Programming languages R, C/C++, Python, Fortran, Julia, Shell scripts and
%    SQL, among others.

### D2L book

D2L book is a Python package and a toolkit to build online and printed books.
The package was mainly developed for the publication of the book [Dive into
Deep Learning](https://d2l.ai/){cite}`zhang2023dive`, which had multiple
collaborators mostly from Amazon. It is mainly focused for content that
includes computational narratives in Python. The input files are mainly MyST
markdown and Jupyter Notebooks. The publishing part is made with pandoc and
Sphinx allowing the creation of websites and pdf documents.

%- [Dive into Deep Learning](https://d2l.ai/) an interactive book with multiple
%authors mainly from Amazon .
%  - [d2l-book](https://github.com/d2l-ai/d2l-book) is the Python package used
%    to build and publish the D2L book.
%  - Programming language Python
%  - Output website and pdf
%  - Uses Markdown, Jupyter Notebooks, Sphinx, and pandoc

### Sphinx

Sphinx[^sphinx] is an open-source documentation engine that is based on
Docutils[^docutils]; extending it to multi-page documentation. Docutils is an
open-source text processing system that uses the plain text easy-to-read
reStructuredText to create documentation in multiple formats, such as HTML,
LaTeX, Linux man pages[^man], OpenDocument[^odf], or XML[^xml]. Sphinx supports
reStructuredText and MyST markdown as input files and can generate multiple
output formats including HTML, LaTeX, PDF, ePub, and Texinfo[^texinfo] (the
official documentation format of the GNU project[^gnu]).

[^sphinx]: https://www.sphinx-doc.org/en/master/
[^docutils]: https://docutils.sourceforge.io/
[^odf]: https://en.wikipedia.org/wiki/OpenDocument
[^xml]: https://en.wikipedia.org/wiki/XML
[^texinfo]: https://www.gnu.org/software/texinfo/
[^gnu]: https://www.gnu.org/
[^man]: https://linux.die.net/man/


(sec:formatting-tools)=
# Formatting tools

**Formatting tools** take input artefacts produced by authoring tools and
produce publishable formatted output.  While many of the authoring tools
discussed in the previous section are well-known, there have been many recent
developments in formatting tools that deserve to be better known in the
academic community as they take opportunities for publishing training material
to the next level. In the previous section we described the two type of
paradigms  *Single-In-Single-Out (SISO)*, and *Single-In-Multi-Out (SIMO)*. In
this section we describe some _formatting tools_ that can be used for the SIMO
paradigm.

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

(sec:pandoc)=
## Pandoc

[Pandoc](https://pandoc.org/) is a tool to convert files between multiple
markup formats. Pandoc is used within more generic tools such as Quarto. 
It is customizable thanks to a Haskell library
and a template system to feet your needs. It is able to generate
bibliographies, footnotes, LaTeX math, tables, definitions, and most common
publication assets. Some supported formats are lightweight markup (Markdown,
reStructuredText, AsciiDoc, Textile, Emacs Org-Mode, ...), HTML,
Ebooks, TeX, word processing (docx, rtf, odt), wiki markup, slide show
(LaTeX Beamer, reveal.js, Microsoft PowerPoint, ...), and even PDF (via
pdflatex, lualatex, xelatex, latexmk and others).


## Sphinx

[Sphinx](https://www.sphinx-doc.org/en/master/) is an open-source documentation engine that is based on
[Docutils](https://docutils.sourceforge.io/); extending it to multi-page documentation. Docutils is an
open-source text processing system that uses the plain text easy-to-read
reStructuredText to create documentation in multiple formats, such as HTML,
LaTeX, [Linux man pages](https://linux.die.net/man/), [OpenDocument](https://en.wikipedia.org/wiki/OpenDocument), or [XML](https://en.wikipedia.org/wiki/XML). Sphinx supports
reStructuredText and MyST markdown as input files and can generate multiple
output formats including HTML, LaTeX, PDF, ePub, and
[Texinfo](https://www.gnu.org/software/texinfo/) (the
official documentation format of the [GNU project](https://www.gnu.org/)).

(sec:jupbook)=
## Jupyter Book

[Jupyter Book](https://jupyterbook.org/en/stable/intro.html) is one of the main projects of the [Executable Books
Project](https://executablebooks.org/en/latest/), together with the other project [MyST
Markdown](https://executablebooks.org/en/latest/tools/#tools-myst). The
Executable Books Project is an international collaboration to build open source
tools for publishing computational documents based on the
[Jupyter](https://jupyter.org/)
ecosystem. Jupyter Book can read markdown, MyST Markdown, Jupyter
notebooks and
[reStructuredText](https://docutils.sourceforge.io/rst.html). It is based
on the [Sphinx documentation engine](https://www.sphinx-doc.org/en/master/)
being able to produce html websites, pdf, and computational narratives. It
supports multiple programming languages in the Jupyter notebooks provided that
a [Jupyter kernel](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) exist (e.g. Python, Julia, Rubi, Haskell, and many other
languages).
Websites that include computational narratives can also bennefit from live
environments thanks to the integration of Binder, Thebe and Google
[Colab](https://colab.research.google.com/). It supports multiple types of narrative content like highlighted
notes, code cells, quotations, epigraphs, glossaries, index of terms,
footnotes, references, grids, cards, dropdown menus, tab content, maths,
equations, proofs, theorems, algorithms, and more. The Jupyter Book system has
been used in multiple ocasions to publish online material, an extensive gallery
can be found at https://executablebooks.org/en/latest/gallery/. This website
has been created with Jupyter Book and serves as an example of some of its
functionalities.

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

(sec:rmd)=
## R markdown

[R markdown](https://rmarkdown.rstudio.com/) is a flavoured markdown type with
special focus on the R programming language and a publishing system. The
publishing system uses R markdown files (with extension `.rmd`) or standard
markdown and can produce various output formats including HTML, PDFs, Microsoft
Word documents, Beamer presentations, HTML5 slides, scientific articles and
books (with the the help of the [bookdown R package](https://bookdown.org/). It also support
other programming languages including Python, SQL and others with a [language
engine](https://bookdown.org/yihui/rmarkdown/language-engines.html). R markdown
is also integrated in [Rstudio](https://posit.co/download/rstudio-desktop/).

%- [Rmarkdown](https://rmarkdown.rstudio.com/):
%  - Input R markdown files (.rmd)
%  - Output formats include HTML, PDF, MS Word, Beamer, HTML5 slides, books (see
%    examples of books build with markdown in
%    [bookdown](https://bookdown.org/)), scientific articles, websites.
%	- Supports multiple languages including R, Python and SQL (see
%    [other language engines]()).
%  - Posit Connect

(sec:bookdown)=
## Bookdown

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

(sec:qmd)=
## Quarto

[Quarto](https://quarto.org) is another open-source publishing system with the
objective of facilitating the collaboration to create scientific content.
Quarto is sponsored by [Posit](https://posit.co), and follows the development of the R Markdown
publishing system extending the focus from the programming language R to
Python, R, Julia and Observable. It supports Jupyter notebooks, markdown and
their own extension Quarto markdown. The conversion to different output formats
is done with [pandoc](https://pandoc.org/), which is able to produce presentations (Reveal.js),
dashboards, websites, blogs, books, PDFs, Microsoft Word, ePub and more. Quarto
is integrated into multiple authoring environments like Microsoft Visual
Studio, Jupyter Lab, [Rstudio](https://posit.co/download/rstudio-desktop/), and [Atlassian Confluence](https://www.atlassian.com/software/confluence)
among others. 

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


(sec:revealjs)=
## Reveal.js

[Reveal.js](https://revealjs.com/) is an open source framework for HTML
presentations. It supports features like animations, export to PDF, an
intuitive navigation of the slides, speaker notes, Markdown support, LaTeX
support, laser-like pointer, and drawing tools. The presentations can be edited
with any HTML editor or with the online visual editor [](https://slides.com/).
The folloiwng HTML code is a fully working *reveal.js* presentation

```html
<html>
  <head>
    <link rel="stylesheet" href="dist/reveal.css" />
    <link rel="stylesheet" href="dist/theme/white.css" />
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
        <section>Slide 1</section>
        <section>Slide 2</section>
      </div>
    </div>
    <script src="dist/reveal.js"></script>
    <script>
      Reveal.initialize();
    </script>
  </body>
</html>
```

*Reveal.js* is also supported by
multiple formatting tools like *Quarto*, *Jupyter Notebook*, and *pandoc* that
which convert markdown files to reveal.js presenations.


:::{admonition} D2L-Book: A Toolkit for Hands-on Books
Building on several of these formatting tools, 
[d2l-book](https://github.com/d2l-ai/d2l-book) is a Python package and a toolkit to build online and printed books, 
in support of the [Dive into Deep Learning](https://d2l.ai/) book {cite}`zhang2023dive`. 
The authoring formats are mainly MyST markdown and Jupyter Notebooks. 
Formatting is done with pandoc and Sphinx.

%- [Dive into Deep Learning](https://d2l.ai/) an interactive book with multiple
%authors mainly from Amazon .
%  - [d2l-book](https://github.com/d2l-ai/d2l-book) is the Python package used
%    to build and publish the D2L book.
%  - Programming language Python
%  - Output website and pdf
%  - Uses Markdown, Jupyter Notebooks, Sphinx, and pandoc
:::


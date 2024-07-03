# Publishing systems

Publishing systems are tools or platforms that allow the generation of
publishing outputs (e.g. html, slides, posters, and pdfs) from a set of input
artefacts (e.g. plain text, markdown, LaTeX, tables, figures). In this Section
we divide the systems into three paradigms *Single-In-Single-Out (SISO)*,
*Single-In-Multi-Out (SIMO)* and *Multiple-In-Multiple-Out (MIMO)*. In this
roadmap we only focus on the second type, as it is covers the most adopted and
flexible systems for authoring training material.

## Single-In-Single-Out

Publishing systems have usually specialised in generating only one type of
output provided one or more types of input files. This is one of the most
common approaches when producing an article. The text, figures, tables and
other artefacts are assembled with some authoring tool and compiled with a
specialised publishing system to produce a printable pdf. Once it has been
accepted a presentation may require parts of the original artefacts and a
different publishing system. It is then common to have a duplicate of the same
content with mild modifications in a separate environment. The same process is
often repeated if a poster, computational notebooks, or a website need to be
created. We refer to this paradigm of publishing system as Single-In-Single-Out
as each system works independently, while the authors need to keep up to date
copies of similar content in each of them.

```{mermaid}
%%{ init : { "flowchart" : { "curve" : "stepBefore" }}}%%

flowchart LR
  
    S1("External sources\nVarious modifications"):::empty -.-> I1
    S1 -.-> I2
    S1 -.-> I3
    S1 -.-> I4
    I1("Text + Figures + \n Code + ... v.1"):::input --> P1{{"Publishing system 1"}}
    I2("Text + Figures + \n Code + ... v.2"):::input --> P2{{"Publishing system 2"}}
    I3("Text + Figures + \n Code + ... v.3"):::input --> P3{{"Publishing system 3"}}
    I4("Text + Figures + \n Code + ... v.4"):::input --> P4{{"Publishing system 4"}}
    P1 --> O1["Published \n Paper \n (PDF)"]
    P2 --> O2["Presentation \n Slides \n (PPTX/PDF)"]
    P3 --> O3["Poster \n (PPTX/PDF)"]
    P4 --> O4["Computational \n Notebook \n (Colab)"]
    style O1 fill:#fca
    style O2 fill:#bff
    style O3 fill:#f99
    style O4 fill:#bfb
    classDef input fill:#ffa;
    classDef empty fill:#aaa,stroke:#333,stroke-dasharray: 5 5;
```

Common examples of this type of paradigm is the authoring and publishing
workflows followed by creating documents with Microsoft Word[^word], Libre
Office Writer[^writer], LaTeX[^latex]; sets of slides with Microsoft
PowerPoint[^powpoint], LibreOffice Impress[^impress], LaTeX Beamer[^beamer],
Reveal.js[^reveal], or Google Slides; posters with Microsoft Publisher, Google
Slides, LaTeX, etc.

[^word]: https://www.microsoft.com/en-gb/microsoft-365/word
[^latex]: https://www.latex-project.org/
[^writer]: https://www.libreoffice.org/discover/writer/

[^powpoint]: https://www.microsoft.com/en-gb/microsoft-365/powerpoint
[^impress]: https://www.libreoffice.org/discover/impress/
[^beamer]: https://ctan.org/pkg/beamer
[^reveal]: https://revealjs.com/

## Single-In-Multiple-Out

More modern publishing systems allow the generation of multiple types of
publication formats from a joint set of input artefacts. We refer to this
paradigm as Single-In-Multiple-Out (SIMO). This paradigm offers multiple
benefits, among them: (1) keep all the artefacts in a unique
location facilitates finding the required documents, (2) keeping a unique
source of history changes and versions which is useful for auditing and
transparency, (3) not duplicating artefacts that are not changed between
different publishing systems.

```{mermaid}
%%{ init : { "flowchart" : { "curve" : "stepBefore" }}}%%

flowchart LR
    I1("Text + Figures + \n Code + ..."):::input --- dummy2{{"Publishing system"}}
    dummy2 --> O1["Published \n Paper \n (PDF)"]
    dummy2 --> O2["Presentation \n Slides \n (PPTX/PDF)"]
    dummy2 --> O3["Poster \n (PPTX/PDF)"]
    dummy2 --> O4["Computational \n Notebook \n (Colab)"]
    classDef input fill:#ffa;
    style O1 fill:#fca
    style O2 fill:#bff
    style O3 fill:#f99
    style O4 fill:#bfb
```

Nowadays, this type of publishing systems are getting more common being able to
produce multiple types of outputs from the same sources. In this roadmap we
focus on the state-of-the-art publishing systems that fall into this category.
The same roadmap is an example of one of such systems (Jupyter Book), while the
rest of the document and use cases also include Quarto. The following
subsections describe what are the main characteristics of the most adopted
ones.

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

## Multiple-In-Multiple-Out

Another paradigm that has not been explored in this roadmap is the
Multiple-In-Multiple-Out (MIMO) that considers the storage of different
artefacts in different platforms and allows the composition of the necessary
artefacts to publish different output types.

```{mermaid}
%%{ init : { "flowchart" : { "curve" : "stepBefore" }}}%%

flowchart LR
    I1("<center>Text</center>"):::input --- dummy1( ):::empty
    I2("Figures"):::input --- dummy1
    I3(Code):::input --- dummy1
    I4(...):::input --- dummy1
    dummy1 --> C:::foo
    C{{"Composition"}} --- dummy2( ):::empty
    dummy2 --> O1["Published \n Paper \n (PDF)"]
    style C fill:#f9f
    dummy2 --> O2["Presentation \n Slides \n (PPTX/PDF)"]
    dummy2 --> O3["Poster \n (PPTX/PDF)"]
    dummy2 --> O4["Computational \n Notebook \n (Colab)"]
    style O1 fill:#fca
    style O2 fill:#bff
    style O3 fill:#f99
    style O4 fill:#bfb
    classDef input fill:#ffa;
    classDef empty width:0px,height:0px,fill:#000;
```

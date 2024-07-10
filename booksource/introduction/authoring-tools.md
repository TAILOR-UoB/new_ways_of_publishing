(sec:aut)=
# Authoring tools

**Authoring tools** facilitate the creation of input artefacts (e.g. plain
text, markup language, tables, figures, code, or equations) which will be
compiled and rendered by a _formatting tool_ to generate publishable outputs.
For example, a markup language editor to create $\LaTeX$ is an authoring tool,
while `pdflatex`, `XeLaTeX`, or `LuaTeX` are formatting tools that compile
input artefacts to pdf. These tools need to integrate metadata about the format
in which the artefacts need to be formatted in different output types.
For example, the font of the text and its position, the position of figures,
tables and other elements. In this roadmap we focus on authoring tools that
can be used for the purpose of multi-output publishing systems. We provide some
guidelines on the type of files that need to be considered during the authoring
process, which tools can directly help on the generation of those artefacts. We
consider the collaboration of teams in the authoring process as a desirable
feature.

```{mermaid}
flowchart LR
  
    E1("External resources"):::external -.-> A1
    subgraph "Vim, NeoVim, Notepad" 
      direction LR
      A1{{"Authoring tool"}} --> I1("Text + Code +\nTables + ..."):::input
    end
    I1 --> P1{{"Formatting tool"}}
    P1 --> O1["Formatted\nOutput"]:::output
    classDef external fill:#eee;
    classDef input fill:#ffa;
    classDef output fill:#faa;
```

Authoring tools that do not incorporate part of the formatting are rare, as it
is common to provide at least a preview of the formatted output.
Examples of authoring that can be separated from the formatting step are simple
text editors like vim, NeoVim, Notepad, and general-purpose Integrated
Development Environments (IDEs).

## Authoring with formatting

There are **authoring tools** that incorporate a **formatting tool**.  While in
some situations it is a good practice to separate the two aspects, some
computer programs integrate them in one tool that may (or may not) provide
access to the intermediate artefacts. For example, Overleaf
provides an online collaborative authoring platform that integrates with
_pdfLatex_ in the back-end. 

```{mermaid}
flowchart LR
  
    E1("External resources"):::external -.-> A1
    subgraph "IDE + Quarto, HackMD, Notion, Typst, Overleaf..." 
      direction LR
      A1{{"Authoring tool"}} --> I1("Text + Figures +\nCode + Tables + ..."):::input
      I1 --> P1{{"Formatting tool"}}
      P1 --> O1["Formatted\nOutput"]:::output
    end
    classDef external fill:#eee;
    classDef input fill:#ffa;
    classDef output fill:#faa;
```

### WYSIWYG (What You See Is What You Get)

WYSIWYG editors provide an interface to write rich text
documents like Microsoft Word, Libre office, or Google Docs. Such
files are difficult to convert automatically to other formats as they do not
separate the source text from the presentation layer. Benefits include
the possibility of collaborative editing, which comes at the expense of reduced 
control over formatting.

```{mermaid}
flowchart LR
  
    E1("External resources"):::external -.-> A1
    subgraph "Libre Office, Google Docs, Microsoft Word, ..." 
      direction LR
      A1{{"Authoring and Formatting tool"}} --> O1["Formatted\nOutput"]:::output
    end
    classDef external fill:#eee;
    classDef input fill:#ffa;
    classDef output fill:#faa;
```


## Markup language editors

These editors separate the source text from the publishable output. 
Unlike WYSIWYG editors they typically have a 
dual-pane user interface with one pane displaying the editable source and 
the other pane providing a preview. 
[Overleaf](https://www.overleaf.com/) is an online collaborative
authoring tool that allows the edition of $\LaTeX$ files, managing the errors
and generating PDF files with a $\LaTeX$ compiler. However the free tier has
some collaboration limitations. [HackMD](https://hackmd.io/),
[Notion](https://www.notion.so/) and [Typst](https://typst.app/) are other
online collaborative text editing tools that can be used for authoring
publishable material and work with markdown files. 


### Integrated Development Environments

The separation of the source code and the publishable outputs is something that
all Integrated Development Environments (IDEs) provide. These are tools for
writing computer programs that commonly require a compilation phase which is
usually integrated in the same tool. The idea of authoring tools that can
create generic input artefacts that are later combined by a formatting tool
is very similar to the common process followed in programming compiled
programming languages. This has facilitate the adoption of IDEs as authoring
tools. Microsoft Visual Studio and [Posit
Workbench](https://posit.co/products/enterprise/workbench/)(formerly
[RStudio](https://posit.co/download/rstudio-desktop/)) have tools to work with
the `Quarto` environment. Both of them provide options for collaborative and 
contemporaneous editing.

### Computational narrative editors

Jupyter Notebooks are documents that offer **computational narratives** by
interlacing formatted markdown text and executable code cells, providing
the output as additional content. The idea has been adopted by other platforms
that have created similar notebook environments. Most of these platforms can
convert the resulting computational narratives into various formats like html,
pdf, or text documents. Jupyter Notebook and
[JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) offer the official
environment for the original Jupyter Notebooks. All of the following projects
offer cloud-based platforms to edit Jupyter notebooks or similar. [Google
Colab](https://colab.research.google.com/) is hosted by
Google and free for low-intensive programs, [Kaggle
Notebooks](https://www.kaggle.com/notebooks) is 
hosted by Kaggle which focuses on Python for Data Science, and Machine
Learning, offering a free solution to participate into Kaggle competitions.
[Microsoft Azure Notebooks](https://notebooks.azure.com/) is hosted in Azure
and focused on Data Science and Machine Learning with
CPUs and GPUs available. It supports various programming languages Python, R,
F\# and Julia, among others. Other platforms that are similar to support
functionalities similar to Jupyter Notebook are [CoCalc](https://cocalc.com/),
[JetBrains Datalore](https://datalore.jetbrains.com/),
[Deepnote](https://deepnote.com/), [Hex](https://hex.tech/),
[Pluto.jl](https://plutojl.org/), [Nextjournal](https://nextjournal.com/), and
[Starboard](https://starboard.gg/).  In particular JetBrains Datalore
integrates with the JetBrains ecosystem tools such as the IDEs
[PyCharm](https://www.jetbrains.com/pycharm/) and
[IntelliJ](https://www.jetbrains.com/idea/).


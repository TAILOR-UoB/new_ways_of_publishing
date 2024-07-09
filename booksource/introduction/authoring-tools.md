(sec:aut)=
# Authoring tools

**Authoring tools** are computer programs or platforms that provide a user
interface to arange all sorts of input artefacts (e.g. plain text, markup
language, tables, figures, code, or equations) in a way that can be formated
later. These tools need to integrate metadata about the format in which the
different artefacts need to be shown in different output forms. For example,
the font of the text and its position, the position of figures, tables and
other elements. 

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
is common to require at least a previsualisation of the formatted output.
Examples of authoring that can be separated from the formatting step are simple
text editors like vim, NeoVim, Notepad, and general purpose Integrated
Development Environments (IDEs).


%**Authoring tools** are tools that help the creation of authoring input artefacts
%which will be compiled by a _formatting tool_ to generate publishable
%outputs. For example, a markup language editor to create $\LaTeX$ is an authoring tool,
%while `pdflatex`, `XeLaTeX`, or `LuaTeX` are publishing systems that compile
%input artefacts to pdf. In this roadmap we focus on authoring tools that
%can be used for the purpose of multioutput publishing systems. We provide some
%guidelines on the type of files that need to be considered during the authoring
%process, which tools can directly help on the generation of those artefacts. We
%consider the collaboration of teams in the authoring process as a desirable
%feature.
%
%%## Types of authoring artefacts
%%
%%- LaTeX markup (1984) created by Leslie Lamport while working at Standford
%%  Research Institute.
%%- setext (1992) or Structure Enhanced Text developed by Ian Feldman
%%- Textile (2002)
%%- reStructuredText (2002)
%%- Markdown (2004) a markup language to create formatted text using plain text that is
%%  both human and machine readable.
%%- R Markdown
%%- Quarto Markdown
%%- MyST Markdown is a community-driven
%
%
%## Markup language editors
%
%Other editors consider a separation between the source code and the publishable
%output. [Overleaf](https://www.overleaf.com/) is an online collaborative
%authoring tool that allows the edition of $\LaTeX$ files, managing the errors
%and generating PDF files with a $\LaTeX$ compiler. However the free tier has
%some collaboration limitations. [HackMD](https://hackmd.io/),
%[Notion](https://www.notion.so/) and [Typst](https://typst.app/) are other
%online collaborative text edition tools that can be used for authoring
%publishable material and work with markdown files. Although, these tools may
%have differences in the markdown syntax which makes difficult the reuse of the
%generated on different platforms.
%
%```{mermaid}
%flowchart LR
%  
%    E1("External resources"):::external -.-> A1
%    subgraph "Vim, NeoVim, Notepad" 
%      direction LR
%      A1{{"Authoring tool"}} --> I1("Text + Code +\nTables + ..."):::input
%    end
%    I1 --> P1{{"Formatting tool"}}
%    P1 --> O1["Formatted\nOutput"]:::output
%    classDef external fill:#eee;
%    classDef input fill:#ffa;
%    classDef output fill:#faa;
%```
%

## Authoring with formatting tools

There are **authoring tools** that incorporate a **formatting tool**.  While in
some situations it is a good practice to separate the two aspects, some
computer programs integrate them in one tool that may (or may not) provide
access to the intermediate artefacts. For example, softwares like Microsoft
Word are authoring tools that already provide the formated output durint the
authoring process. Another typical example in academic environments is Overleaf
that provides an online collaborative authoring platform that integrates with
_pdfLatex_ in the back end. 

### WYSIWYG (What You See Is What You Get)

Text editors are one of the most important tools for authoring material
publishable material. Some editors provide an interface to write rich text
documents like Microsoft Word, Libre office, or Google Docs. However, those
files are difficult to convert automatically to other formats as they do not
separate the source text from the presentation layer. Some of their benefits
is that multiple people can edit concurrently these types of files as the
syntax is usually hidden to the user, making difficult the generation of
compilation or format errors.

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

### Integrated Development Environments

The separation of the source code and the publishable outputs is something that
all the Integrated Development Environments (IDEs) excel. These are tools for
writing computer programs that commonly require a compilation phase which is
usually integrated in the same tool. The idea of authoring tools that can
create generic input artefacts that are later combined by a formatting tool
is very similar to the common process followed in programming compiled
programming languages. This has facilitate the adoption of IDEs as authoring
tools. Microsoft Visual Studio, [Posit
Workbench](https://posit.co/products/enterprise/workbench/)(formerly
[RStudio](https://posit.co/download/rstudio-desktop/)) have tools to work with
the `Quarto` environment. Both of them provide options for multiple
collaborators editing content at the same time.

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

### Computational narrative editors

Jupyter Notebooks are documents that offer computational narratives by
interlacing formated markdown text and code cells that are executed, providing
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


%%## Real time collaboration
%%
%%Visual Studio Live Share
%%
%%## Interactive code
%%
%%- [Jupyter Widgets](https://jupyter.org/widgets): 
%%- [htmlwidgets for R](http://www.htmlwidgets.org/):
%%- [Observable JS](https://observablehq.com/@observablehq/observable-javascript): Tool to
%%run Javascript code dynamically that supports D3, Lodash and Apache Arrow.
%%- [Shiny](https://shiny.posit.co/): Run Python or R code in the browser.
%%Check the [Python example documentation](https://shiny.posit.co/py/docs/overview.html).
%%[Pyodide](https://pyodide.org/en/stable/) is a port of Python and other packages compiled to
%%[WebAssembly](https://webassembly.org/). Some examples of supported
%%packages are  regex, pyyaml, lxml and scientific Python packages including
%%numpy, pandas, scipy, matplotlib, and scikit-learn.
%%WebAssembly is a binary format for compiled programs.
%%- [Shinylive: Shiny + WebAssembly](https://shiny.posit.co/py/docs/shinylive.html):
%%
%%
%%## Collaboration tools
%%
%%Available tools in the last decade
%%
%%- [Noteable](https://noteable.io/): cloud-based real-time collaboration tool
%%for data science, machine learning and others. Focused on Python, R and
%%SQL. Free for individual users.
%%- [Paperspace Gradient](https://gradient.paperspace.com/): ...
%%- [Apache Zeppelin](https://zeppelin.apache.org/): ... Built-in code editor.
%%- [Count.co](https://count.co/): ...
%%
%%## Online communication
%%
%%- Microsoft Teams
%%- Zoom
%%- [Kumospace](https://www.kumospace.com/) offers virtual locations to interact
%%  with other users online.
%%
%%## Examples
%%
%%- Simply Logical: Intelligent Reasoning by Example (Fully Interactive
%%  Online Edition) {cite}`flach2022simply` of the Simply Logical textbook
%%  {cite}`flach1994simply`.
%%
%%
%%## More
%%
%%Check the following resources for additional tools and examples that can be
%%added into this document
%%
%%-Streamlit vs. Dash vs. Shiny vs. Voila vs. Flask vs. Jupyter
%%Comparing data dashboarding tools and frameworks [^1]
%%- Check [Researchers14](https://www.researchers14.ac.uk/) a group of
%%  Universities representing 65% of research communities in the UK that shares
%%  good practices in research development.
%%
%%[^1]: https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila
%%
%%
%%- Project management tools for planning, assigning and tracking tasks like
%%  Trello, Airtable, GitHub project, Todoist.
%%- Web-based conference management softtware systems Microsoft Conference
%%  Management Toolkit, EasyChair, OpenReview
%%- Sharing documents Microsoft SharePoint and One Drive, Google drive, Dropbox,
%%  Slack
%%- Concurrent text editors Overleaf, Google docs, Microsoft Sharepoint
%%- Version control GitHub, GitLab, BitBucket
%%- Real time communication some with videocall Slack, Microsoft Teams
%%- Video edition
%%- Public databases: huggingface, OpenML, UCI Machine Learning Repository,
%%  Hugging Face a platform for collaboration among machine learning
%%  practitioners by sharing datasets, models and applications.
%%- Search engines for scientific publications: Google Scholar, PubMed, PubPeer,
%%  Semantic Scholar, DBLP, Elsevier Scopus, Microsoft Academic
%%- Text search engines: Google, Bing, Yahoo!, Yandex, DuckDuckGo, Baidu 
%%- Interactive and graphical search engines: Litmaps, scite, 
%%- Notes taking: Obsidian, HackMD, CodiMD (host your own version of HackMD),
%%  GitBook, Notion, Evernote, Todoist, 
%%  - Notion: No offline support, very flexible, but not the best for each of its
%%    functionalities.
%%  - Obsidian: Offline but paid online sync, the canvas functionality allows you
%%    to organise ideas between them in a virtual plane that resembles a physical
%%    surface.
%%  - Pandoc to convert between different file formats (e.g. Word Document to
%%    Markdown). This is one of the integral parts of Quarto publishing system.


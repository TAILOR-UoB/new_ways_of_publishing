(sec:pub)=
# Publishing workflows

The **publishing workflow** is the process in which external resources are prepared and
collated together with the help of an **authoring tool** and subsequently
rendered with a **formatting tool** to generate a publishable output that can be
delivered in various forms. 
This is visualised by the following figure.[^pub:excl]

[^pub:excl]: In this roadmap we do not cover **(1)** the process of
generating the external resources and **(6)** the delivery system.
However, note that the delivery system may have some impact on the formatted artefact, 
even within the same format. For example, hyperlinks should ideally be handled differently 
for printed and online PDFs. 

```{mermaid}
---
Publishing workflow
---
flowchart LR
  
    E1("(1)\nExternal resources"):::external -.-> A1
    A1{{"(2)\nAuthoring tool"}} --> I1("(3)\nText + Figures +\nCode + Tables + ..."):::input
    I1 --> P1{{"(4)\nFormatting tool"}}
    P1 --> O1["(5)\nFormatted\nOutput"]:::output
    O1 -.-> D1{{"(6)\nDelivery system"}}:::delivery
    classDef external fill:#eee,stroke:#666,stroke-width:2px,stroke-dasharray: 5 5;
    classDef input fill:#ffa;
    classDef output fill:#faa;
    classDef delivery stroke:#666,stroke-width:2px,stroke-dasharray: 5 5;
```
An example of a publishing workflow is the following. A research group may
carry out an investigation which ends up with **(1)** data, figures, analyses,
and results, those resources are put together with an **(2)** authoring tool
like Overleaf which produces an **(3)** organised hierarchy of files and text
that includes formatting information, then using a **(4)** formatting tool like
pdfLaTeX all the artefacts are combined into a **(5)** pdf document that can be
**(6a)** printed as a stand-alone document, or **(6b)** included into the
proceedings of a conference. 

:::{note}
For the purposes of this roadmap we emphasise the difference between the _authoring_
and the _formatting_ steps of the full publishing workflow. The authoring step
consists in creating a structured composition of input artefacts that are
necessary to generate the intended publication through formatting. 
:::

The creation of research or academic material usually involves the production
of slides, documents, posters and other output formats from the same material.
In this roadmap, we are interested in workflows to generate this multitude of
outputs minimising the _authoring_ effort. Here, we describe two types of
paradigms which were discussed in the previous TAILOR deliverable D9.3 {cite}`sokol21`:
[](sec:SISO) (SISO) and [](sec:SIMO) (SIMO). 


%% MPN: I have removed this as it was complicated  and may not be necessary
%
% The process of creating the input artefacts is often distributed over different apps or environments,
% non-linear and may involve redundancies (e.g., multiple copies of the same image for the paper, slides, etc.). 
% Keeping all versions of the artefacts up to date constitutes a challenge, as parts of the artefacts are
% re-used and adapted to be used within their respective authoring contexts.
%
%```{mermaid}
%flowchart LR
%  
%    I1("Source code"):::input -.->|Part of the code| MS
%    I1 & I3{{"Analysis"}} --> M1("Results"):::input
%    M1 --> I3
%    I3 --> M2("Figures + Tables + \n ..."):::input
%    I4["Other sources"]:::external --> M2
%    M1 -.->|Part of the results| MS("Figures + Code + \n Tables + ..."):::input
%    M2 -.->|Subset| MS
%    classDef input fill:#ffa;
%    classDef external fill:#aaa,stroke:#333,stroke-dasharray: 5 5;
%```

(sec:SISO)=
## Single-In-Single-Out

_Formatting tools_ commonly specialise in generating only one type of
output from one or more input files. This is one of the most
common approaches when producing an article for publication in a journal or 
conference proceedings. The text, figures, tables and
other artefacts are assembled with some authoring tool and compiled with a
specialised formatting tool to produce a printable pdf. 

Once the paper has been accepted by a conference, a presentation will need to be prepared, 
often using different _formatting tools_. It is then common to have duplicates of the same
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
    I1("Text + Figures + \n Code + ... v.1"):::input --> P1{{"Formatting tool 1"}}
    I2("Text + Figures + \n Code + ... v.2"):::input --> P2{{"Formatting tool 2"}}
    I3("Text + Figures + \n Code + ... v.3"):::input --> P3{{"Formatting tool 3"}}
    I4("Text + Figures + \n Code + ... v.4"):::input --> P4{{"Formatting tool 4"}}
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

Common examples of this type of paradigm are the authoring and publishing
workflows for creating
- text documents with [Microsoft Word](https://www.microsoft.com/en-gb/microsoft-365/word), [Libre
Office Writer](https://www.libreoffice.org/discover/writer/), [LaTeX](https://www.latex-project.org/); 
- slide decks with [Microsoft PowerPoint](https://www.microsoft.com/en-gb/microsoft-365/powerpoint), [LibreOffice Impress](https://www.libreoffice.org/discover/impress/), [LaTeX Beamer](https://ctan.org/pkg/beamer),
[Reveal.js](https://revealjs.com/), or [Google Slides](https://workspace.google.com/intl/en_uk/products/slides/); and 
- posters with [Microsoft Publisher](https://www.microsoft.com/en-gb/microsoft-365/publisher), Google Slides, LaTeX, etc.

(sec:SIMO)=
## Single-In-Multiple-Out

More recent publishing systems allow the generation of multiple types of
publication formats from a joint set of input artefacts. We refer to this
paradigm as Single-In-Multiple-Out (SIMO). This paradigm offers various
benefits, among them: 
- keeping  the artefacts in a single, well-defined location which facilitates consistency, management and findability; 
- keeping a unique source of history changes and versions which is useful for auditing and
transparency; and 
- not duplicating artefacts that are not changed between different publishing systems.

```{mermaid}
%%{ init : { "flowchart" : { "curve" : "stepBefore" }}}%%

flowchart LR
    I1("Text + Figures + \n Code + ..."):::input --- dummy2{{"Formatting tool"}}
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

Nowadays, the SIMO type of formatting tool is becoming more common, and we 
focus on the state-of-the-art formatting tools that fall into this category in this roadmap.
The roadmap document itself is an example of one particular tool (`Jupyter Book`), while the
rest of the document and use cases also include examples built with `Quarto`. A description of these
and other publishing tools is provided with more detail in the next section
[](sec:formatting-tools).

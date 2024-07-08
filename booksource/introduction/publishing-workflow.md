# Publishing workflow

The `publishing workflow` is the full process in which authors produce results
and the correspoinding input artefacts that will be necessary to make a
publication, and the `publication system` that is involved to compile all the
material into the final publication. 

In this `Roadmap` we want to emphasize the difference between the `authoring`
and the `formatting` parts of the full `publication workflow`. The `authoring`
consists on creating a structured composition of input artefacts that are
necessary to generate the objective publication. The authoring may also
be able to generate an output, but this one may differ slightly on the final
output generated by the publication system. The differences may have a
technical origin, or the editors may need to do some changes for the final
publication.

```{note}
I remved the Output preview of the authoring tool. I need to change the text.
```

```{mermaid}
flowchart LR
  
    E1("External resources"):::external -.-> A1
    A1{{"Authoring tool"}} --> I1("Text + Figures +\nCode + Tables + ..."):::input
    I1 --> P1{{"Formatting tool"}}
    P1 --> O1["Formatted\nOutput"]:::output
    O1 -.-> D1{{Delivery system}}:::delivery
    classDef external fill:#eee,stroke:#666,stroke-width:2px,stroke-dasharray: 5 5;
    classDef input fill:#ffa;
    classDef output fill:#faa;
    classDef delivery stroke:#666,stroke-width:2px,stroke-dasharray: 5 5;
```

 The process of creating the input artefacts is commonly distributed,
 non-linear and may generate redundant information. Keeping all the versions of
 the artefacts updated may be a challenge, as parts of the artefacts are
 re-used and adapted to be used within the authoring tools.

```{mermaid}
flowchart LR
  
    I1("Source code"):::input -.->|Part of the code| MS
    I1 & I3{{"Analysis"}} --> M1("Results"):::input
    M1 --> I3
    I3 --> M2("Figures + Tables + \n ..."):::input
    I4["Other sources"]:::external --> M2
    M1 -.->|Part of the results| MS("Figures + Code + \n Tables + ..."):::input
    M2 -.->|Subset| MS
    classDef input fill:#ffa;
    classDef external fill:#aaa,stroke:#333,stroke-dasharray: 5 5;
```

### Formatting tools

Formatting tools format the input files into publishing outputs outputs (e.g.
html, slides, posters, and pdfs) from a set of input artefacts (e.g. plain
text, markdown, LaTeX, tables, figures). In this Section we divide the tools
into three paradigms *Single-In-Single-Out (SISO)*, *Single-In-Multi-Out
(SIMO)* and *Multiple-In-Multiple-Out (MIMO)*. In this roadmap we only focus on
the second type, as it is covers the most adopted and flexible systems for
authoring training material.

## Single-In-Single-Out

_Formatting tools_ have usually specialised in generating only one type of
output provided one or more types of input files. This is one of the most
common approaches when producing an article. The text, figures, tables and
other artefacts are assembled with some authoring tool and compiled with a
specialised formatting tool to produce a printable pdf. Once it has been
accepted a presentation may require parts of the original artefacts and a
different _formatting tools_. It is then common to have a duplicate of the same
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

Nowadays, this type of formatting tools are getting more common being able to
produce multiple types of outputs from the same sources. In this roadmap we
focus on the state-of-the-art formatting tools that fall into this category.
The same roadmap is an example of one of such tools (Jupyter Book), while the
rest of the document and use cases also include Quarto. A description of these
and other publishing tools is described with more detail in the next Section.

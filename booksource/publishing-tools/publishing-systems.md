# Publishing systems

Publishing systems are tools or platforms that allow the generation of
publishing outputs from a specific set of input artefacts. Common input
artefacts are plain text, markdown, LaTeX, tables, figures, references among
others, while the common outpus are html websites, slides, posters, printable
documents and others. 


- [Quarto](https://quarto.org): 
  - Quarto supports dynamic content with Python, R, Julia and Observable
  - programming languages.
  - Quarto uses pandoc to convert the input artefacts to its output.
  - Quarto supports plain text markdown, Jupyter notebooks and an augmented
  - markdown, 
  - Integration with Posit Connect (former RMarkdown), Atlassian Confluence, Visual
    Studio, 
- [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/):
- [Jupyter{book}](https://jupyterbook.org/en/stable/intro.html)
  - MyST Markdown, Jupyter notebooks, reStructuredText
  - Provides its own 
  - Live environments with Binder, Thebe
  - Output website and pdf
- [Pluto.jl](https://plutojl.org/):
- [Rmarkdown](https://rmarkdown.rstudio.com/):



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
    style O2 fill:#ffb
    style O3 fill:#f99
    style O4 fill:#bfb
    classDef empty width:0px,height:0px;
```


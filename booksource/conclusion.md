(sec:conclusion)=
# Outlook: towards collaborative MIMO authoring

Technology has moved far beyond the printing press, yet academic publishing 
is to a large extent still informed by the legacy format of printable documents. 
The growth of the World Wide Web is enabling the modernisation of teaching material
which can be accessed from a large variety of devices. It also provides a
platform for dynamic and interactive material that is automatically adjusted to
the publishing medium. 
This roadmap has been written to help AI researchers embrace these new ways of publishing 
and the new modes of learning that they facilitate. 

It should also be said that the rapid growth of web technologies creates a
transitional environment for software and publishing tools that are still being
developed and do not address all the requirements of such systems. Publishing
systems like `Jupyter Book` and `Quarto` are among the most curated ones but are
under heavy development. 
In a year from now they will have many new features that will push the boundaries even further. 
The challenge is for all of us to keep abreast of these developments and to make sure that 
we use the best tools for our purposes, 
while keeping in mind that this should not just be driven by the technological push 
but strike a balance with well-understood educational needs. 

One area where current technology does not quite meet users' needs is in collaborative authoring. 
Markdown-based formatting tools such as `Quarto` offer maximum freedom how the authoring artefacts are produced, 
which some will see as an advantage but also means that a collaborative environment for authoring 
markdown files (e.g., [HackMD](https://hackmd.io/)) is separate from `Quarto` formatting. 
This situation is similar to LaTeX authoring prior to 2011 when Overleaf and ShareLaTeX were developed. 
Interestingly, the collaborative features in Overleaf such as commenting and tracked changes followed the model set by WYSIWYG editors such as Microsoft Word and Google Docs. 
A good collaborative environment combined with the flexibility of the Single-In-Multi-Out paradigm would pave the way to the **Multi-In-Multi-Out (MIMO)** publishing paradigm that was already envisaged in the 
TAILOR deliverable D9.3 {cite}`sokol21`. 
Such a system would pull together different authoring artefacts, possibly from different locations, and composes them in all the required output formats. 

```{mermaid}
%%{ init : { "flowchart" : { "curve" : "stepBefore" }}}%%

flowchart LR
    I1("<center>Text</center>"):::input --- C{{"Composition"}}:::foo
    classDef input fill:#ffa;
    style C fill:#f9f
    I2("Figures"):::input --- C:::foo
    I3(Code):::input --- C:::foo
    I4(...):::input --- C:::foo
    C --> O1["Published \n Paper \n (PDF)"]
    C --> O2["Presentation \n Slides \n (PPTX/PDF)"]
    C --> O3["Poster \n (PPTX/PDF)"]
    C --> O4["Computational \n Notebook \n (Colab)"]
    style O1 fill:#fca
    style O2 fill:#bff
    style O3 fill:#f99
    style O4 fill:#bfb
```

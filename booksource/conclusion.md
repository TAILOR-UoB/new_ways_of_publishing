(sec:conclusion)=
# Conclusion

Publishing teaching material nowadays goes beyond printable documents. The
growth of the World Wide Web is enabling the modernisation of teaching material
which can be accessed from a large variety of devices. It also provides a
platform for dynamic and interactive material that is automatically adjusted to
the publishing medium. However, the rapid growth of web technologies creates a
dynamic environment for software and publishing tools that are still being
developed and do not address all the requirements of such systems. Publishing
systems like Jupyter Book and Quarto are among the most curated ones but are
under heavy development. In this deliverable, we provided a roadmap to
publishing online material with guidelines on state-of-the-art tools, examples
and use cases. We focused on the publishing paradigm SIMO
(Single-Input-Multiple-Output) which can be easily tackled with Quarto (with
some current limitations). Another paradigm that has not been explored is the
MIMO (Multiple-Input-Multiple-Ouput) in which a composition tool is able to
collate different types of input artefacts (potentially from different sources)
and group them automatically to generate different types of publishable
outputs. Another limitation of available solutions is the lack of good
real-time collaboration functionalities in the state-of-the-art tools. This
complicates the creation of material with multiple authors involved. Platforms
like Overleaf, Google Docs, and Typst are examples of good collaboration tools
but lack the flexibility of the proposed SIMO paradigm. New platforms with
similar functionalities for Quarto and Jupyter Book need to be created.


%Another paradigm that has not been explored in this roadmap is the
%**Multiple-In-Multiple-Out (MIMO)** that considers the storage of different
%artefacts in different platforms and allows the composition of the necessary
%artefacts to publish different output types.
%
%```{note} To be added
%
%- Adding input artefacts automatically incorporates in the correct place
%- Files can be distributed in different platforms
%```
%
%```{mermaid}
%%%{ init : { "flowchart" : { "curve" : "stepBefore" }}}%%
%
%flowchart LR
%    I1("<center>Text</center>"):::input --- C{{"Composition"}}:::foo
%    classDef input fill:#ffa;
%    style C fill:#f9f
%    I2("Figures"):::input --- C:::foo
%    I3(Code):::input --- C:::foo
%    I4(...):::input --- C:::foo
%    C --> O1["Published \n Paper \n (PDF)"]
%    C --> O2["Presentation \n Slides \n (PPTX/PDF)"]
%    C --> O3["Poster \n (PPTX/PDF)"]
%    C --> O4["Computational \n Notebook \n (Colab)"]
%    style O1 fill:#fca
%    style O2 fill:#bff
%    style O3 fill:#f99
%    style O4 fill:#bfb
%```
%
%```{note}
%The following text is shared with the current deliverable report. We need to
%change or adapt both of them.
%```
%

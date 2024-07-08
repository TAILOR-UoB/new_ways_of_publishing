# Conclusion

Another paradigm that has not been explored in this roadmap is the
**Multiple-In-Multiple-Out (MIMO)** that considers the storage of different
artefacts in different platforms and allows the composition of the necessary
artefacts to publish different output types.

```{note} To be added

- Adding input artefacts automatically incorporates in the correct place
- Files can be distributed in different platforms
```

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

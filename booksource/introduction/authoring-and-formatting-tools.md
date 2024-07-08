# Authoring + formatting

## WYSIWYG (What You See Is What You Get)

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

## Integrated Development Environments

The separation of the source code and the publishable outputs is something that
all the Integrated Development Environments (IDE) excel. These are tools for
writing computer programs that commonly require a compilation phase which is
usually integrated in the same tool. The idea of authoring tools that can
create generic input artefacts that are later combined by a formatting tool
is very similar to the common process followed by IDEs. This has facilitate the
adoption of IDEs as authoring tools. Microsoft Visual Studio, [Posit
Workbench](https://posit.co/products/enterprise/workbench/)(formerly
[RStudio](https://posit.co/download/rstudio-desktop/)) have tools to work with
the `Quarto` environment. Both of them provide options for multiple
collaborators editing content at the same time.

```{mermaid}
flowchart LR
  
    E1("External resources"):::external -.-> A1
    subgraph "Posit (or MS VS) + Quarto, HackMD, Notion, ..." 
      direction LR
      A1{{"Authoring tool"}} --> I1("Text + Figures +\nCode + Tables + ..."):::input
      I1 --> P1{{"Formatting tool"}}
      P1 --> O1["Formatted\nOutput"]:::output
    end
    classDef external fill:#eee;
    classDef input fill:#ffa;
    classDef output fill:#faa;
```


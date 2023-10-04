# Use case scenarios

## Terminology

### Available artefacts

- LaTeX content for: publication, slides (beamer), poster, tables, graphs.
- Markdown content
- Word documents
- Power point slides
- Bibliography: bib, rib,
- CSV files
- Images in various formats: bitmap, vector graphics.
- Graphviz.
- Videos
- Source code
- Notebooks

### Desired outcome

- Publication
- Slides
- Poster
- Website
- Book
- MOOC
- Documentation
- Educational material


### Desired properties

- Printable
- Static
- Dynamic
- Cross-platform

## Use case examples

### LaTeX files and want a website

#### Short description

I have all the LaTeX files of a publication, thesis or book and want to
generate a static website.

#### Current artefacts

- LaTeX files
- Figures
- Tables
- bib files

#### Desired outcome

- Static website

#### Possible solutions

Pandoc can convert each individual tex file into markdown


```
pandoc -s input_file.tex -o output_file.md
```

#### Problems

- Some LaTeX commands may not be rendered
- Tables may not be automatically rendered
- importat command ignores the text during the conversion
- The LaTeX directive \`\' breaks blocks

## Use case examples

### Power point slides to cross-platform

#### Short description

I have all the material of a course in the form of power point slides, and I am
planning to provide the slides in a cross-platform format that can be
visualised in any web browser (even in a phone).

#### Current artefacts

- Power point slides
- Images
- Videos

#### Desired outcome

- Dynamic cross-platform slides

#### Possible solutions

There are some tools that can semi-automatically generate Reveal JS slides from
the Power point content. This will require manual labour to adjust most of the
format.

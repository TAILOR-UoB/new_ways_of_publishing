(sec:use)=
# Some itineraries through the landscape

Now that we have charted the landscape of new ways of authoring and publishing online material, 
and given a number of examples of "places to visit", 
we are ready to describe some "itineraries" through the landscape:  
practical use cases that people who want to create or update training material might encounter. 

On the one hand, somebody may want to use `Quarto` to develop new training material, which is covered in [](sec:use:qua). 
But perhaps a more common use case is that somebody already has material in a legacy format which they want to transform into a more interactive and multi-purpose form. 
We give a concrete example of how to do this in [](sec:use:lat). 

We remind the reader that the fully rendered courses can be viewed on 
[the companion website](https://tailor-uob.github.io/training-material/).

:::{note}
There are of course many other possible itineraries through the landscape! 
Please get in touch if you have ideas for additional use cases for this roadmap.
::: 


%## Terminology
%
%### Available artefacts
%
%- LaTeX content for: publication, slides (beamer), poster, tables, graphs.
%- Markdown content
%- Word documents
%- Power point slides
%- Bibliography: bib, rib,
%- CSV files
%- Images in various formats: bitmap, vector graphics.
%- Graphviz.
%- Videos
%- Source code
%- Notebooks
%
%### Desired outcome
%
%- Publication
%- Slides
%- Poster
%- Website
%- Book
%- MOOC
%- Documentation
%- Educational material
%
%
%### Desired properties
%
%- Printable
%- Static
%- Dynamic
%- Cross-platform
%
%## Use case examples
%
%### LaTeX files and want a website
%
%#### Short description
%
%I have all the LaTeX files of a publication, thesis or book and want to
%generate a static website.
%
%#### Current artefacts
%
%- LaTeX files
%- Figures
%- Tables
%- bib files
%
%#### Desired outcome
%
%- Static website
%
%#### Possible solutions
%
%Pandoc can convert each individual tex file into markdown
%
%
%```
%pandoc -s input_file.tex -o output_file.md
%```
%
%#### Problems
%
%- Some LaTeX commands may not be rendered
%- Tables may not be automatically rendered
%- importat command ignores the text during the conversion
%- The LaTeX directive \`\' breaks blocks
%
%## Use case examples
%
%### Power point slides to cross-platform
%
%#### Short description
%
%I have all the material of a course in the form of power point slides, and I am
%planning to provide the slides in a cross-platform format that can be
%visualised in any web browser (even in a phone).
%
%#### Current artefacts
%
%- Power point slides
%- Images
%- Videos
%
%#### Desired outcome
%
%- Dynamic cross-platform slides
%
%#### Possible solutions
%
%There are some tools that can semi-automatically generate Reveal JS slides from
%the Power point content. This will require manual labour to adjust most of the
%format.

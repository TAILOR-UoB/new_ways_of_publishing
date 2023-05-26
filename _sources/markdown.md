(sec:markdown)=
# Markdown Files

Whether you write your book's content in Jupyter Notebooks (`.ipynb`) or
in regular markdown files (`.md`), you'll write in the same flavor of markdown
called **MyST Markdown**.
This is a simple file to help you get started and show off some syntax.

## What is MyST?

MyST stands for "Markedly Structured Text". It
is a slight variation on a flavor of markdown called "CommonMark" markdown,
with small syntax extensions to allow you to write **roles** and **directives**
in the Sphinx ecosystem.

For more about MyST, see [the MyST Markdown Overview](https://jupyterbook.org/content/myst.html).

## Sample Roles and Directives

Roles and directives are two of the most powerful tools in Jupyter Book. They
are kind of like functions, but written in a markup language. They both
serve a similar purpose, but **roles are written in one line**, whereas
**directives span many lines**. They both accept different kinds of inputs,
and what they do with those inputs depends on the specific role or directive
that is being called.

Here is a "note" directive:

```{note}
Here is a note
```

It will be rendered in a special box when you build your book.

Here is an inline directive to refer to a document: {doc}`markdown-notebooks`.

## Diagrams

We have installed an extension to draw diagrams from text using `Mermaid`. The
following is an example of the code necessary to generate the diagram below.

````md
```{mermaid}
flowchart TD
  A[square node A] --> B(round edges node B)
  A --> C([stadium node C])
  B --> D[[subroutine node D]]
  B --> E[(database node E)]
  B --> F((circle F))
  C --> F
```
````

```{mermaid}
flowchart TD
  A[square node A] --> B(round edges node B)
  A --> C([stadium node C])
  B --> D[[subroutine node D]]
  B --> E[(database node E)]
  B --> F((circle F))
  C --> F
```

You can find the basic syntax for flowcharts at
[mermaid](https://mermaid.js.org/syntax/flowchart.html).

It is possible to add other diagram plugin extensions. See other options in
[sphinx-diagrammers](https://opencomputinglab.github.io/SubjectMatterNotebooks/diagram/sphinx-diagrammers.html).

## Mindmaps

With [Mermaid](https://mermaid.js.org/intro/) it is possible to generate other
types of diagrams, the following is an example for a
[mindmap](https://mermaid.js.org/syntax/mindmap.html).

```{mermaid}
mindmap
  root((Data Science))
    Statistics
      Surveys
      Experiments
    Scientific Computing
    Scientific Methods
      Hypothesis Testing
      Evaluation
    Processes
      Parallel Programming
      Crawlers
    Algorithms
    Systems
      High Performance Computing
      Personal Computers
      Distributed Computing
```

## Cross-references

{ref}`figure-example-1`


```{figure} images/example.svg
:name: figure-example-1

Caption of the example figure ex1
```

{ref}`table-example-1`

```{table} Caption of the table ex1
:name: table-example-1
| header 1 | header 2 |
| -------- | -------- |
|    a     |    b     |
```

This is a reference to Equation {eq}`equation-example-1`

```{math}
:label: equation-example-1

E = mc^2
```

## Videos

We can insert videos in the middle of a markdown file by using `html` and and
`iframe` like the following example

```html
<iframe width="560" height="315"
src="https://www.youtube.com/embed/4kwEMHZJx5A" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share"
allowfullscreen></iframe>
```

which renders the following video

<iframe width="560" height="315"
src="https://www.youtube.com/embed/4kwEMHZJx5A" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share"
allowfullscreen></iframe>


## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).



(sec:static)=
# Static content

Some of the most essential functionalities of any authoring tool and publishing
system is the ability to create publishing material from text, tables and
figures. In this Section we provide several examples on how to produce this
content in `Jupyter Book` and `Quarto` publishing systems.

Both systems are capable of reading `Markdown` and `Jupyter Notebooks` and
convert them to a variety of output formats. They support particular versions
of `Markdown` as there is no current specification that has been fixed.
`Quarto` has its own `Quarto markdown` with extension `.qmd`, while `Jupyter
Book` uses `MyST Markdown`.

## Markdown

`Markdown` is a markup language to create formatted text from plain text that can
be easily read by humans. Markdown was initiated in 2004 by John Gruber and
Aaron Swartz to convert plain text to html {cite}`krewinkel2017`. However,
there is still no consensus on concrete specification because of unsolved
issues[^issues], which has created diverging versions of markdown. In 2014 an
unambiguous specification was released by Markdown contributors under the name
of CommonMark.

[^issues]: https://talk.commonmark.org/t/issues-we-must-resolve-before-1-0-release-6-remaining/1287

## Jupyter Notebooks

`Jupyter Notebooks` are computational notebooks that integrate textual
narrative with `MyST Markdown` with cells of code that can be executed to show
computational results between the text. This format has been widely adopted by
multiple authoring and publishing systems like `Quarto`, `Jupyter Lab`, `Google
Colab`.

(sec:ro:di)=
## Roles and Directives

MyST Markdown provides roles and directives in order to extend the basic
functionalities of Markdown. By defining a set of terms and how to interpret
the code on it via extensions, which may be already integrated in Jupyter Book.

Roles are used in-line and have the form `` {rol-name}`role content` `` for
example the role `` {math}`E=mc^2` `` is rendered as {math}`E=mc^2`.

Similarly, directives are multi-line versions of the form

````
```{directive-name} arguments
:key1: val1
:key2: val2

Content of 
the directive
```
````

Examples of directives can be found in {ref}`sec:notes`.

(sec:notes)=
## Notes

Notes are a type of directive supported by Jupyter Book. They allow you to
create information boxes with a colored title, and main content.

````
```{note}
Here is a note
```
````

```{note}

Here is a note
```

Other types of notes can be created with the directives `attention`, `caution`,
`danger`, `error`, `important`, `warning`, `tip`, `seealso`, and more that can
be found at https://mystmd.org/guide/directives. The following are three
examples.

```{tip}

Tip note
```

```{attention}

Attention note
```

```{error}

Error note
```

## Diagrams

With additional directives it is possible to create diagrams from plain text.
There are multiple sphinx plugins that can be installed in `Jupyter Book` and
some that are already integrated in `Quarto`.
In this section we show some examples.
The [Mermaid](https://mermaid.js.org/) diagramming and charting tool allows the
creation of a multitude of diagrams including [flowcharts](sec:mer:fc),
[sequences](sec:mer:sd), [mindmaps](sec:mer:mm) and more. There is an online
live editor that allows the exploration of various examples, modification and
creation of new diagrams in the following link https://mermaid.live/edit.
[WaveDrom](https://wavedrom.com/) is another rendering engine to draw [timing
diagrams](sec:wd).

(sec:mer:fc)=
### Mermaid flowchart

```{mermaid} 
flowchart TD
  A[square node A] --> B(round edges node B)
  A --> C([stadium node C])
  B --> D[[subroutine node D]]
  B --> E[(database node E)]
  B --> F((circle F))
  C --> F
```

(sec:mer:sd)=
### Mermaid sequence diagram

```{mermaid}
sequenceDiagram
	participant Alice
	participant Bob
	Alice->John: Hello John, how are you?
	loop Healthcheck
			John->John: Fight against hypochondria
	end
	Note right of John: Rational thoughts <br/>prevail...
	John-->Alice: Great!
	John->Bob: How about you?
	Bob-->John: Jolly good!
```

(sec:mer:mm)=
### Mermaid mindmap

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

(sec:wd)=
### WaveDrom timming diagrams

[WaveDrom](https://wavedrom.com/) can draw timming diagrams.

```{wavedrom}
{ signal : [
  { name: "clk",  wave: "p......" },
  { name: "bus",  wave: "x.34.5x",   data: "head body tail" },
  { name: "wire", wave: "0.1..0." },
]}
```

## Cross-references

Published documents often have internal references to other content in the
document. In `Jupyter Book` when inserting an image with the following
directive

````
```{figure} images/example.svg
:name: figure-example-1

Caption of the example figure ex1
```
````

which is rendered as 

```{figure} images/example.svg
:name: figure-example-1

Caption of the example figure ex1
```

is possible to reference the image with the role `{numref}`Figure %s <figure-example-1>``
which will show a reference like {numref}`Figure %s <figure-example-1>`. The
same can be done for tables like {numref}`table-example-1`, equations like
Equation {eq}`equation-example-1` and Sections {ref}`Introduction <sec:intro>`.

```{table} Caption of the table ex1
:name: table-example-1

| header 1 | header 2 |
| -------- | -------- |
|    a     |    b     |
```

```{math}
:label: equation-example-1

E = mc^2
```

`Quarto` has its own way to make cross references which can be consulted in
their documentation ([Quarto cross
references](https://quarto.org/docs/authoring/cross-references.html)).

## Code segments

Another common aspect of documents in STEM (Science, technology, engineering,
and mathematics) is the publication of short extracts of pseudocode or source
code. `Markdown` languages usually support the highlight of code based on the
different programming language specifications.

For example the following code is for Python

```python
print("Hellow world!")
```

while the following code is written in `ANSI C`

```c
#include <stdio.h>

int main() {
  printf("Hello world!");
  return 0;
}
```

## Inline-tabs

Some interactive books that contain code may be directed to audience with
different background programming knowledge. For those cases, `MyST Markdown`
can create tabs to select which content to see. The following is an example of
`Python` and `C++` code:

````{tab} Python
```python
def main():
    return
```
````
````{tab} C++
```c++
int main(const int argc, const char **argv) {
  return 0;
}
```
````

A second example shows how chaning the tab in one of the tabs affects other
code segments.

````{tab} Python
```python
print("Hello World!")
```
````

````{tab} C++
```c++
#include <iostream>

int main() {
  std::cout << "Hello World!" << std::endl;
}
```
````

(sec:citations)=
## Citations

It is possible to make citations to a bibliography that is stored in a
`bibtex` file. For example, the following syntax: `` {cite}`ruby` `` will
generate the following citation: {cite}`ruby`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

## Videos

The wide spread of personal computers, smart phones and tables has accelerated
the content of audiovisuals in the internet and streaming services.
Furthermore, It is common that in academic and teaching contexts the same
lessons are repeated multiple times to different audiences. This makes recorded
audiovisual content well suited to reduce the limited time commitment of the
teachers, while maximising the reach of the content. There are multiple online
services to host video material with [YouTube](https://youtube.com),
[Vimeo](https://vimeo.com/), and [SlidesLive](https://slideslive.com) being the
most well known.

Most video hosting services offer ways to embed their videos into any `html`
website by using the `iframe` tag. The following is an example of a video
hosted in `YouTube`

```html
<iframe width="560" height="315"
src="https://www.youtube.com/embed/4kwEMHZJx5A" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share"
allowfullscreen></iframe>
```

which is rendered like this

<iframe width="560" height="315"
src="https://www.youtube.com/embed/4kwEMHZJx5A" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share"
allowfullscreen></iframe>

## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).

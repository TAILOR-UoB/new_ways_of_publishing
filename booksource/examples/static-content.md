(sec:static)=
# Static content

Prior to the World Wide Web, **static content** was the only type of content that could be 
published. It is primarily content that can be printed 
without loss of information, the most common forms of which are text, tables and
figures. 
More broadly, static content is authored once after which it is formatted and rendered the same every time. 
We therefore also include basic video and audio in this category. 
In this section we provide several examples on how to produce static
content in `Jupyter Book` and `Quarto`. 

Both formatting systems are capable of reading `Markdown` and `Jupyter Notebooks` and
convert them to a variety of output formats. They support particular versions
of `Markdown` as there is no Markdown standard yet.
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
## Callout Blocks

Callout Blocks are special boxes with a colored title and a main textual
content. These can be created with different directives with `{note}` being a
common example.

````
```{note}

Here is a note.
```
````

```{note}

Here is a note.
```

The content of a callout block can be hidden by adding the optional tag `:class: dropdown`

````
```{note}
:class: dropdown

Hidden text.
```
````

```{note}
:class: dropdown

Hidden text.
```

Other types of notes can be created with the directives `attention`, `caution`,
`danger`, `error`, `important`, `warning`, `tip`, `seealso`, and more that can
be found at https://mystmd.org/guide/directives. The following are three
examples.

```{tip}

Tip note.
```

```{attention}

Attention note.
```

```{error}

Error note.
```

It is possible to personalise your own notes with `{admonition}`

```{admonition} This is a warning block
:class: warning

with personalised title and body text.
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
diagrams](sec:wd). Some examples can be found below.

(sec:mer:fc)=
### Mermaid flowchart

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

(sec:mer:sd)=
### Mermaid sequence diagram

Example of a sequence diagram with Mermaid showing the interactions between a
web developer, the hosting and a client web browser.

````
```{mermaid}
sequenceDiagram
	participant Web developer
	participant Hosting server
  participant Client web browser
	Web developer->>Hosting server: Upload webpage source files
  Client web browser->>Hosting server: Request specific web page
  Hosting server->>Client web browser: Provide requested web page
	loop Read
			Client web browser->Client web browser: User navigates the page
	end
  Note right of Client web browser: User clicks a link
  Client web browser->>Hosting server: Request another page
  Hosting server->>Client web browser: Provide requested web page
```
````

```{mermaid}
sequenceDiagram
	participant Web developer
	participant Hosting server
  participant Client web browser
	Web developer->>Hosting server: Upload webpage source files
  Client web browser->>Hosting server: Request specific web page
  Hosting server->>Client web browser: Provide requested web page
	loop Read
			Client web browser->Client web browser: User navigates the page
	end
  Note right of Client web browser: User clicks a link
  Client web browser->>Hosting server: Request another page
  Hosting server->>Client web browser: Provide requested web page
```

(sec:mer:mm)=
### Mermaid mindmap

````
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
````

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
### WaveDrom timing diagrams

[WaveDrom](https://wavedrom.com/) can draw timing diagrams.

````
```{wavedrom}
{ signal : [
  { name: "clk",  wave: "p......" },
  { name: "bus",  wave: "x.34.5x",   data: "head body tail" },
  { name: "wire", wave: "0.1..0." },
]}
```
````

```{wavedrom}
{ signal : [
  { name: "clk",  wave: "p......" },
  { name: "bus",  wave: "x.34.5x",   data: "head body tail" },
  { name: "wire", wave: "0.1..0." },
]}
```

## Cross-references

Published documents often have internal references to other content in the
document. By default, all the titles have their own anchor points (move the
mouse cursor on top of a title to see a `#` symbol indicating a clickable
anchor point). It is possible to reference sections within the same page by
creating a link  writing the full title in lower case and dashes instead of
spaces like `[](cross-references)` which creates a link like
[](cross-references). With this method it is not possible to reference other
pages; e.g. the link [](#conclusions) should not work but [](static-content)
does work. A more flexible method is to manually indicate anchor points in
titles, figures, tables and other content. By adding a label before a title as
follows

```markdown
(my-label)=
# Section title
```

the section can be references with `[](my-label)` or the more flexible role
``{ref}`my-label` ``. For example the code ``[](sec:conclusion)`` and
``{ref}`sec:conclusion` `` will generate a link to the [](sec:conclusion).

| Code                                | Result                          |
|:------------------------------------|:--------------------------------|
| ``[](sec:conclusion)``                    | [](sec:conclusion)                    |
| ``[Textual description](sec:conclusion)`` | [Textual description](sec:conclusion) |
| ``{ref}`sec:conclusion` ``                | {ref}`sec:conclusion` |


Labels can also be added to figures, tables and equations within their own
directive tags. For example, in the `{figure}` directives the tag `name`
specifies the label.

````
```{figure} images/example.svg
:name: fig:ex:1

Caption of the example figure ex1
```
````

The previous code generates the next figure that can be referenced in multiple
ways.

```{figure} images/example.svg
:name: fig:ex:1

Caption of the example figure number 1
```

| Code                                | Result                          |
|:------------------------------------|:--------------------------------|
| ``[](fig:ex:1)``                    | [](fig:ex:1)                    |
| ``[Textual description](fig:ex:1)`` | [Textual description](fig:ex:1) |
| ``{ref}`fig:ex:1` ``                | {ref}`fig:ex:1` |
| ``{numref}`fig:ex:1` ``             | {numref}`fig:ex:1` |
| ``{numref}`Figure %s and more text <fig:ex:1>` ``             | {numref}`Figure %s and more text <fig:ex:1>` |


Tables use the tag `name`

````
```{table} Caption of the table ex1
:name: tab:ex:1

| header 1 | header 2 |
| -------- | -------- |
|    a     |    b     |
```
````

```{table} Caption of the table ex1
:name: tab:ex:1

| header 1 | header 2 |
| -------- | -------- |
|    a     |    b     |
```

| Code                                | Result                          |
|:------------------------------------|:--------------------------------|
| ``[](tab:ex:1)``                    | [](tab:ex:1)                    |
| ``[Textual description](tab:ex:1)`` | [Textual description](tab:ex:1) |
| ``{ref}`tab:ex:1` ``                | {ref}`tab:ex:1` |
| ``{numref}`tab:ex:1` ``             | {numref}`tab:ex:1` |
| ``{numref}`Figure %s and more text <tab:ex:1>` ``             | {numref}`Figure %s and more text <tab:ex:1>` |

Finally, equations use the tag `label`

````
```{math}
:label: eq:ex:1

E = mc^2
```
````

```{math}
:label: eq:ex:1

E = mc^2
```

And can only be referenced by their number

| Code                                | Result                          |
|:------------------------------------|:--------------------------------|
| ``[](eq:ex:1)``                    | [](eq:ex:1)                    |
| ``{eq}`eq:ex:1` ``                | {ref}`eq:ex:1` |


`Quarto` has its own way of making cross references which can be consulted in
their documentation ([Quarto cross
references](https://quarto.org/docs/authoring/cross-references.html)).

## Code segments

Another common aspect of documents in STEM (Science, technology, engineering,
and mathematics) is the publication of short extracts of pseudocode or source
code. `Markdown` languages usually support the highlight of code based on the
different programming language specifications.

For example the following code is for Python

```python
print("Hello world!")
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

Some interactive books that contain code may be aimed at diverse audiences with
different background programming knowledge. For those cases, `MyST Markdown`
can create tabs to select which content to display. The following is an example of
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

Tab choices persist across code segments: 

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
## Citations and bibliography

It is possible to add citations and a bibliography using a `bibtex` file. For
example, the references in this webpage are all stored in the
[](../references.bib) file. The bibliography can be inserted in any particular
section with the directive `{bibliography}`. The current [](sec:references)
section contains the following markdown content:

````
(sec:references)=
# References

```{bibliography}
```
````

Once a bibliography has been added in the document, it is possible to cite any
of the references with the `{cite}` role. The following role `` {cite}`sokol21`
`` will generate the citation {cite}`sokol21`, which provides information about
the reference when hovering the mouse over it. The list of references in the
bibliography will only contain those reference that are cited at least once in
the whole website.

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

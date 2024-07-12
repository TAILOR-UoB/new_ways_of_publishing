---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
launch_buttons:
  thebe: true
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(launch:thebe)=

(sec:com:nar)=
# Dynamic content

**Dynamic content** is content that includes computational code that is
executed when the website/book is built. With extra configurations, the content
can be re-run in real time locally or with a third party service like MyBiner,
Google Colab, or others. This type of content is very useful for educational
material in science, technology, engineering and mathematics. Jupyter Notebooks
and other programming environments that integrate a textual narrative,
computational cells and their results are really common. Publishing systems
like `Jupyter Book` and `Quarto` support multiple ways to write this type of
material by using directives (See [](sec:ro:di)) for code in markdown files, or
directly using Jupyter Notebooks.  This section serves as an example of the
functionalities that can be integrated in a Markdown file in a Jupyter Book. We
also indicate what are the differences in the _Quarto_ publishing system when
necessary.

## Configuration

Adding dynamic content that changes during the execution requires the
specification of a **kernel** which is able to read the code indicated in the
apropiate directives and produce an ouptut result. This configuration differs
slighly depending on the platform and the type of file (e.g. markdown and
Jupyter Notebook).

### Jupyter Notebook files

*Jupyter Notebooks* are web-based documents that combine a textual narrative
(written in a markup language) with computational elements (supporting a
multitude of programming languages). The code of the notebooks can be executed
with the help of a
[kernel](https://docs.jupyter.org/en/latest/projects/kernels.html); a
*programming language specific* process that can interpret the code, run it and
provide the results to the authoring application. The default kernel is the
[ipykernel](https://github.com/ipython/ipykernel) built on top of
[IPython](https://ipython.org/). Common functionalities added via the code
cells are the generation of figures, tables, plots, and interactive elements
and the analysis of data. Jupyter Notebooks have a file extension `.ipynb` and
can be edited with authoring tools like *Jupyter Notebook*, *Jpyter Lab*,
*Google Colab*, and most *integrated development environments* (IDEs) like
*PyCharm*, *Microsoft Visual Studio*, *Posit*, and *RStudio* (See more in the
section
[](sec:aut:com:nar)). 

In *Jupyter Book* and *Quarto* projects the configuration of **Jupyter
Notebooks** is general across the project. However, *Quarto* requires a *Raw*
cell at the beginning of the notebook with the `title`, `author`, and any
additional options that you want to include in order to be rendered. The
following is a configuration example for *Quarto*

```yaml
---
title: Title of the page
authors: "Miquel Perello Nieto"
date: "July 11th, 2024"
format: 
  html: default
  pdf: default
  refealjs: default
---
```

(sec:com:nar:con)=
### Markdown files

In **Jupyter Book**, **Markdown** files with dynamic content require a YAML
configuration in the header indicating some parameters about
the type of file and the kernel to use. There are kernels for different
programming languages like R, Python, Julia, and more. For example, the
markdown file for this page has been configured to run Python3 with the
following `yaml` configuration

```yaml
---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
```

The header can be generated automatically with the help of the jupyter-book
tool by running the following command in a terminal at the root of the project

```shell
jupyter-book myst init markdownfile.md --kernel kernelname
```

Additional documentation can be found at
https://jupyterbook.org/en/stable/file-types/myst-notebooks.html.

In **Quarto**, 
Running Python code in the **Quarto** publishing system requires the `jupyter`
Python package and the specification of the `python` command to use in the
`YAML` header or in the `_quarto.yml` configuration file.

```yaml
jupyter: python3
```

(sec:mar:liv)=
### Live code

In **Jupyter Books**, [Thebe](https://thebe.readthedocs.io/en/stable/) offers a
solution to launch the kernel in the current page (without the need to jump to
a third party website). By default, this *Jupyter Book* has been configured to
run Thebe with the third party service *MyBinder*.  It is also necessary to add
the following line of code before the first title of the markdown document

```
(launch:thebe)=
```

In order to start the live code with *Thebe* it is necessary to click on the
upper right side menu the `spaceship` and the `Live code` button in the
drop down menu.

```{figure} images/thebe_live_code.png
:name: figure-launch-live-code

Menu to launch Live Code with Thebe
```

Then the code will be launched in your configured server (in this case
MyBinder) and a new loading text will be shown at the top of the current page
with several steps, building the code, publishing and launching.  Depending on
the configured server this process may take more or less time to complete, and
could even fail to launch.

```{figure} images/thebe_steps.svg
:name: figure-thebe-steps
:width: 400px

Steps that Live Code will show as it prepares the running environment.
```

Once the kernel is ready, any Python code that is written in a `{code-cell}`
with `ipython3` will have the option to be modified and re-run in real time.
The current page is an example in which you can modify all the cells. 

**Quarto** does not currently support _Thebe_, but it supports launching the
code in a third party environment like _MyBinder_ by adding the following
`yaml` configuration in the header of the Markdown file


```yaml
code-links: binder
```

**Quarto** has good integration with [Shiny](https://shiny.posit.co/) which has
additional functionalities that can bee seen in Section [](sec:exa:run).


(sec:com:nar:sim)=
## Simple examples

In Jupyter Books by using the `code-cell` directive it is possible to execute
code and print out its response.

````
```{code-cell}
print("Hello world!")
```
````

When your book is being built, the contents of any `{code-cell}` block will be
executed with the default Jupyter kernel. The outputs will be displayed in-line
with the rest of your content.

```{code-cell}
print("2 + 2 = ", 2 + 2)
```

It is possible to modify the behaviour of `code-cells` by adding `tags`. For
example the tag `hide-input` will make the code hidden until it is clicked with
the mouse.

````
```{code-cell} ipython3
:tags: [hide-input, thebe-init]

# Python code
```
````

The following code is an example

```{code-cell} ipython3
:tags: [hide-input, thebe-init]

import numpy as np

np.random.seed(42)

hidden_text = f"The result of this draw of a six sided dice is {np.random.randint(1, 6)}"
```

The previous example generates a random number between 1 and 6 and stores the
result in a variable. The content of the variable can be printed in a separate
cell

```{code-cell} ipython3
print(hidden_text)
```

The following code is a very simple example on how to create a lineplot which
can be easily modified in a Live environment.

```{code-cell} ipython3
import matplotlib.pyplot as plt

plt.plot([0, 1, 2, 6], [0, 4, 2, 5], 'o-')
```

(sec:com:nar:tab)=
## Exploration of tables

In data analysis it is common to inspect large amounts of data which in certain
cases is stored in a tabular form. Pandas is a Python library that is able to
produce `Data Frames` (similar to the `Data Frames` from the `R` programming
language), and can produce summaries and visualisations in various output
formats. The following example shows the recorded temperatures (Celsius) in
Bristol as shown in the Wikipedia article[^bristol].

[^bristol]: https://en.wikipedia.org/wiki/Bristol

```{code-cell} ipython3
import pandas

features = ['Record low', 'Record high'] 
date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
        'Nov', 'Dec']
data = [[-14.4, 14.2], [-9.7, 18.3], [-8.3, 21.7], [-4.7, 25.7], [-2.0, 27.4],
        [0.6, 32.5], [4.7, 34.5], [3.9, 33.3], [0.6, 28.3], [-3.2, 26.8],
        [-6.5, 17.5], [-11.9, 15.8]]
df = pandas.DataFrame(data=data, index=date, columns=features)

df.style.background_gradient(cmap='coolwarm', vmin=df.min().min(), vmax=df.max().max())

```

The cells are not independent, and following computations can be performed
making reference to variables instantiated in previous cells. The following
example shows some statistics of the previous table.

```{code-cell} ipython3
df.describe()
```

(sec:com:nar:plo)=
## Static plots

Figures generated with plotting libraries can also be rendered and shown as
static images (e.g. matplotlib, pyplot, bokeh). The following is an example
with the previous temperatures rendered with Matplotlib.

```{code-cell} ipython3
import matplotlib.pyplot as plt
plt.plot(df, '-o')
plt.ylabel('Temperature ($^{\circ}C$)')
plt.title('Min. and Max. recorded temperatures in Bristol')
plt.grid()
```

Or the following examples of 3D surfaces from the [Matplotlib
documentation](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html#sphx-glr-gallery-mplot3d-trisurf3d-2-py).


```{code-cell} ipython3
from bpython.examples import matplotlib_trisurf3d_2

matplotlib_trisurf3d_2()
```

## Code listing

It is possible to print the source code of any Python function with the package
`inspect`. The following is an example for a function in the `bpython` package.

```{code-cell} ipython3
def function_example(a: float, b: float):
    """Sums two numbers

    Parameters
    ----------
    a : float
      First number to sum
    b : float
      Second number to sum
    """
    return a + b
```

Then it is possible to get the function documentation

```{code-cell} ipython3
import inspect

documentation = inspect.getdoc(function_example)
print(documentation)
```

or its source code

```{code-cell} ipython3
source = inspect.getsource(function_example)
print(source)
```

(sec:complexcode)=
## Reuse of complex code

In order to reuse complex code across the website, it is recommended to write a 
package with the functions. In the case of the current roadmap, we have created
a package `bpython` in the folder
[/lib/book-python/](https://github.com/TAILOR-UoB/new_ways_of_publishing/tree/main/lib/book-python).
It can be installed after the requirements with 

```bash
pip install -e /lib/book-python/
```

The `-e` option keeps the library in its current folder, allowing the
modification of the library during the development of the website. In this way,
every time that the virtual environment is loaded the library is loaded anew.
The following code should print the current version of this auxiliary library.

```{code-cell} ipython3
import bpython

print(f"The current BPython version is {bpython.__version__}")
```

Another example with a complex 3D surface visualisation from the Matplotlib
documentation was already shown in the Section [](sec:com:nar:plo).


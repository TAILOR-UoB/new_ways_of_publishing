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

# Running code

Jupyter Book also lets you write text-based notebooks using MyST Markdown.
See [the Notebooks with MyST Markdown documentation](https://jupyterbook.org/file-types/myst-notebooks.html) for more detailed instructions.
This page shows off a notebook written in MyST Markdown.

## An example cell

With MyST Markdown, you can define code cells with a directive like so:

```{code-cell}
print(2 + 2)
```

When your book is built, the contents of any `{code-cell}` blocks will be
executed with your default Jupyter kernel, and their outputs will be displayed
in-line with the rest of your content.

```{seealso}
Jupyter Book uses [Jupytext](https://jupytext.readthedocs.io/en/latest/) to convert text-based files to notebooks, and can support [many other text-based notebook files](https://jupyterbook.org/file-types/jupytext.html).
```

## Create a notebook with MyST Markdown

MyST Markdown notebooks are defined by two things:

1. YAML metadata that is needed to understand if / how it should convert text files to notebooks (including information about the kernel needed).
   See the YAML at the top of this page for example.
2. The presence of `{code-cell}` directives, which will be executed with your book.

That's all that is needed to get started!

## Quickly add YAML metadata for MyST Notebooks

If you have a markdown file and you'd like to quickly add YAML metadata to it, so that Jupyter Book will treat it as a MyST Markdown Notebook, run the following command:

```
jupyter-book myst init path/to/markdownfile.md
```

(sec:complexcode)=
# Complex code package

In order to reuse complex code across the book, we are developing a Python
package `bpython` in the folder `/lib/book-python/`. It is installed
automatically after the requirements with

```bash
pip install -e /lib/book-python/
```

Then, the functions can be used in the MyST markdown files.

```{code-cell} ipython3
import bpython

print(f"The current BPython version is {bpython.__version__}")
```

# Code listing

It is possible to print the source code of any Python function with the package
`inspect`. The following is an example for a function in the `bpython`
package.

```{code-cell} ipython3
import inspect
from bpython.examples import python_function_example

lines = inspect.getsource(python_function_example)
print(lines)
```

# Example from Matplotlib documentation

The following function is an example that plots surfaces in triangular mesh.
The original code can be found in the Matplotlib documentation
[More triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html#sphx-glr-gallery-mplot3d-trisurf3d-2-py)


```{code-cell} ipython3
from bpython.examples import matplotlib_trisurf3d_2

matplotlib_trisurf3d_2()
```

# Example from Pandas documentation

The following is an example of a table generated with Pandas from its documentation
[Formatting the Display](https://pandas.pydata.org/docs/user_guide/style.html#Formatting-the-Display)

```{code-cell} ipython3
from bpython.examples import pandas_table_weather

pandas_table_weather()
```

# Interactive visualisations

## Plotly

```{code-cell} ipython3
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 marginal_y="violin", marginal_x="box", trendline="ols",
                 template="simple_white")
fig.show()
```

## IPyWidgets


```{code-cell} ipython3
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles
m = Map(
  basemap=basemap_to_tiles(
    basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"
  ),
  center=(52.204793, 360.121558),
  zoom=4
)
m.add_layer(Marker(location=(52.204793, 360.121558)))
display(m)
```

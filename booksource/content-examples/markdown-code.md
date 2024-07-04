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

(launch:thebe)=

(sec:com:nar)=
# Computational narratives

Computational narratives are very useful for educational material in science,
technology, engineering and mathematics. Jupyter Notebooks and other
programming environments that integrate a textual narrative, computational
cells and their results are really common. Publishing systems like Jupyter Book
and Quarto support multiple ways to write this type of material by using
directives (See [](sec:ro:di)) for code in markdown files, or directly using
Jupyter Notebooks. This section serves as an example of the functionalities
that can be integrated in a Markdown file.

(sec:com:nar:con)=
## Configuration

In `Jupyter Book` it is necessary to add a YAML configuration in the header of
a markdown file indicating some parameters about the type of file and the
kernel to use. The markdown file for this page which contains Python code needs
the following header.

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

which can be automatically generated with the jupyter-book tool

```shell
jupyter-book myst init markdownfile.md --kernel kernelname
```

Additional documentation can be found at
https://jupyterbook.org/en/stable/file-types/myst-notebooks.html.

Running Python code in the `Quarto` publishing system requires the `jupyter`
Python package and the specification of the `python` command to use in the
`YAML` header or in the `_quarto.yml` configuration file.

```yaml
jupyter: python3
```

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

(sec:int:plo)=
## Interactive plots

Some libraries can produce figures that can be interacted with. For example
Plotly provides tools like zooming, selection, hover information, filtering,
and more. The following example shows the sepal length and width of flowers
from the Iris dataset. Notice that it is possible to remove some classes from
the visualisation by clicking on the species in the legend, it is possible to
get additional information on the summary statistics or the individual samples
by hovering with the mouse, it is possible to select a rectangular subregion to
zoom in, download the plot as a `png`, and more. 

```{code-cell} ipython3
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 marginal_y="violin", marginal_x="box", trendline="ols",
                 template="simple_white")
fig.show()
```

(sec:map)=
## Maps

The Python library `ipyleaflet` is able to draw maps using the JavaScript
library Leaflet which are interactive and mobile-friendly.

```{code-cell} ipython3
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles
m = Map(
  basemap=basemap_to_tiles(
    basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"
  ),
  center=(51.4545, -2.5879),
  zoom=4
)
m.add_layer(Marker(location=(51.4545, -2.5879)))
display(m)
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
## Reuse of code

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

(sec:live)=
## Live code

With the help of [Thebe](https://thebe.readthedocs.io/en/stable/) it is
possible to add interactive code inline. By default, this Jupyter Book has been
configured to run Thebe with MyBinder whenever a section specifies in the Yaml
header the following tags.

```
kernelspec:
  display_name: Python 3
  language: python
  name: python3
```

And by adding before the first title of the document the following code

```
(launch:thebe)=
```

You can see the markdown source code of this page as an example.

In order to start the live code with `Thebe` it is necessary to click on the
upper right side menu the `spaceship` and the `Live code` button in the
dropdown.

![launch live code](./images/thebe_live_code.png)

Then the code will be launched in your configured server (in this case
MyBinder) and a new loading text will be shown at the top of the current page
with several steps, building the code

![thebe building](./images/thebe_building.png)

then publishing

![thebe publish](./images/thebe_publishing.png)

and finally launching it

![thebe launch](./images/thebe_launching.png)

Depending on the configured server this process may take more or less time to
complete, and could even fail to launch with the following message

![thebe failed](./images/thebe_failed.png)


Then, any python code that is written in a `code-cell` with `ipython3` will
have the option to be run (and modified) in real time by the reader. The
current page is an example in which you can modify all the previous cells. The
following cells are additional short examples.

```{code-cell} ipython3
import matplotlib.pyplot as plt

plt.plot([0, 1, 2, 6], [0, 4, 2, 5], 'o-')
```

```{code-cell} ipython3
:tags: [hide-input, thebe-init]

import numpy as np

np.random.seed(42)

hidden_text = f"The result of a draw of a six sided dice is {np.random.randint(1, 6)}"
```

```{code-cell} ipython3
print(hidden_text)
```

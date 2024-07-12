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

(sec:exa:run)=
# Interactive content

Programming examples shown in the previous sections are executed during the
compilation of the publication and their result is embedded into the resulting
publication file. We have also seen that with *Thebe* it is possible to have
live code that can be modified and re-run to generate different results.
However, it requires a third party server (e.g. Google Colab, MyBinder,
SageMaker Studio Lab, or others). On the other hand, there are methods to
run code in the same web browser used for viewing the formatted content, 
without the need of an external computation resource. 
In this section we demonstrate how this can be achieved with
Shinylive and other libraries. 

(sec:int:plo)=
## Plots with Plotly

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
## Maps with IpyLeaflet

The Python library [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/)
can display maps using the JavaScript library Leaflet which are interactive
and mobile-friendly.

```{code-cell} ipython3
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles
m = Map(
  basemap=basemap_to_tiles(
    basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"
  ),
  center=(51.4545, -2.5879),
  zoom=4
)
m.add_layer(Marker(location=(51.4545, -2.5879), draggable=False))
display(m)
```

## Jupyter Widgets

[Jupyter Widgets](https://ipywidgets.readthedocs.io/en/latest/) provide a set
of interfaces to interact with Python code.  Some of the interfaces are
buttons, sliders, In a _Live environment_ this interactions result in the code
being executed.

```{code-cell} ipython3
import ipywidgets as widgets

a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))
```

The results of the interactions with the widgets can be used in the following code
cells.

```{code-cell} ipython3
display(a)
```

%In a live environment the output of this cell will show the selected number
%squared
%
%```{code-cell} ipython3
%from ipywidgets import interact
%
%def f(x):
%  return x**2
%
%interact(f, x=10)
%```


## Shinylive: Shiny + WebAssembly

[Shinylive](https://shiny.posit.co/py/docs/shinylive.html) is a technology that
unifies [Shiny](https://shiny.posit.co/) and [WebAssembly](https://webassembly.org/).
WebAssebmly is a binary format for compiled programs that can run in the web
browser at near-native speeds. [Pyodide](https://pyodide.org/en/stable/) is a
port of Python and various packages compiled in WebAssembly.

It is possible to edit Shiny applications in the online editor
https://shinylive.io/py/editor/. Once the application has been finished it is
possible to copy a link to the end result. By default, Shiny provides an
interface with a code editor on the top left, an output console at the bottom
left and a user interface on the right to output the application result. The
following example uses the output console and not the user interface.

<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMVAJwEtyAKAcgAk4AbT4gAgHditTgBMAhCwCUAHQhgAvgF0gA"
data-external="1" width="100%" height="400px">
</iframe>

It is possible to modify the code and obtain the result on the output console.
For example, you may want to try and change `print('Hello world!')` by
`print(2+2)` and click `Re-run app` (or press `(Ctrl)-Shift-Enter`).

(sec:shi:jup)=
### Shinylive in Jupyter Book

Jupyter Books (like this roadmap) need to edit the application in the online
editor and embed the final application using the resulting url and an
`<iframe>`. For example the following iframe

```
<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAMwCdiYACAZwAsBLCbJjmVYnTJMAgujxMArhwA6EOWlQB9aUwC8UjligBzOEpoAbaQBMAFNIxsATGZlgAEhwlQIJpmTauA1iyY1BDzpsLh0mAGVObgBCewBKOLkFdHVRdDNFFWcmADlSOESIMABfAF0gA"
data-external="1" width="100%" height="400px">
</iframe>
```

which is rendered as follows

<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAMwCdiYACAZwAsBLCbJjmVYnTJMAgujxMArhwA6EOWlQB9aUwC8UjligBzOEpoAbaQBMAFNIxsATGZlgAEhwlQIJpmTauA1iyY1BDzpsLh0mAGVObgBCewBKOLkFdHVRdDNFFWcmADlSOESIMABfAF0gA"
data-external="1" width="100%" height="400px">
</iframe>

All the code for the previous example is encoded in the URL as a GET method. It
is possible to modify the code in the editor, and generate the new URL by
clicking the Share button on the top right corner. This provides a link to the
editor (including editor, console and user interface (ui)) or only the
application (ui).


Furthermore, the original source code could be store in a Github Gist and
provide the gist id in the url. For example, the following GitHub Gist
https://gist.github.com/wch/e62218aa28bf26e785fc6cb99efe8efe with
`id=e62218aa28bf26e785fc6cb99efe8efe` can be deployed with 

```
<iframe src="https://shinylive.io/py/editor/#gist=e62218aa28bf26e785fc6cb99efe8efe"
data-external="1" width="100%" height="400px">
</iframe>
```

which results in the following application

<iframe src="https://shinylive.io/py/editor/#gist=e62218aa28bf26e785fc6cb99efe8efe"
data-external="1" width="100%" height="400px">
</iframe>

There are multiple prebuild common Python packages like Matplotlib, Numpy,
Seaborn, Scipy, and scikit-learn (See list of packages for Pyodide 0.25.1 at
https://shiny.posit.co/py/docs/shinylive.html#installed-packages). This makes
it flexible to create plots with interactive parts like the following histogram
of random points.

<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACGKM1AG2LK5oBGWbN14soAZxbcyAHQh0GzFhACu9bOKkRU8gGaNiMFhIAWNCJsVNWAQXR4WjSgBM4jR6prz5aVAH0vFgBeFi8sKABzOH89Li8XAAp5FlSwmgwLVFUyfwl+N0ZkyFl8FlKAOXUBdxZiPRYBCwlSxwAGRwBGNo6WACY2gEo8FLTw4hzs3NEyYpnS4flBnwh5NwaJdwA3d0SsnMcJzgOTOAkJGlJBxFHUgAEjqduWO+cIQqweWaguMmDS2wscwSMjESKMWALZ7raRfRLXZ5pFSYCHvIwYTZwJKdACcADYABxtImdZYQJFIgAeIRY3TaLAA1LSAKwsABUyIwqJc6O5EESABYAMwAdjJiLSehokUcUGpoRkGNUAhmEnhEtScowwNmlMc+zIGH5wxYbggFzI2GCABVGKo4GSKWlnGRVIxyVLIitfOgafZUIk-IEaI5Nowdh5TXABKpIja7Q75GAAL4AXSAA" data-external="1"
width="100%" height="400px">
</iframe>

Or a simple line plot which can be easily modified.

<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACGKM1AG2LK5oBGWbN14soAZxbcyAHQgAzRsRgsJACxoRsLOg2YsAgujwtGlACZxGpgK4158tKgD69lgF4W9rFADmcC4KXPYWABTyLFHeNBjEtpwJLqJkEWApsmAAlHjyWY4QVgpq1gBu1mFaqAmm8YlkphJwEhI0pFmIkdEAAnXVchDRLN3mhdZYPKlQXGQemYYs-BBw0pOZ+YPRRau8YR1dQ1HmZLaMgzITu8AADKYAjKYATKYAbAC6pjemACxPpgDsHxYAHJiABaYEbJzoTxGdBhZxuGiNMrWLJgAC+byAA" data-external="1"
width="100%" height="400px">
</iframe>

### Shinylive in Quarto

Shiny and `Quarto` are both developed by Posit (formerly RStudio). Quarto
integrates very well with Shinylive being able to embed any Shinylive
application in a Markdown file by writing the source code directly in a
directive of the type `{shinylive-python}`. There are some options that can be
adjusted in the header, and the code goes directly below. The following example
in `Quarto` would render as the first example of the previous subsection
[](sec:shi:jup).

````
```{shinylive-python}
#| standalone: true
#| components: [editor, viewer]
#| viewerHeight: 480

from shiny import App, ui

app_ui = ui.page_fluid(ui.h2("Hi, and thanks for trying Shiny!"))

app = App(app_ui, None)
```
````

More complex examples are demonstrated in the following sections. 

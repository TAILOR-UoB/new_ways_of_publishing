(sec:con:run)=
# Running code in the web browser

Programming examples shown in the previous sections are executed during the
compilation of the publication and their result is embedded into the resulting
publication file. We have also seen that with "Thebe" it is possible to have
live code that can be modified and re-run to generate different results.
However, it requires a third party server (e.g. Google Colab, MyBinder,
SageMaker Studio Lab, or others). On the other hand, there are some methods to
run code in the same web browser without the need of an external computation
resource. In this Section we demonstrate how this can be achieved with
Shinylive.

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

Shiny and Quarto are both developed by Posit (formerly RStudio). Quarto
integrates very well with Shinylive being able to embed any Shinylive
application in a Markdown file by writing the source code directly in a
directive of the type `{shinylive-python}`. There are some options that can be
adjusted in the header, and the code goes directly below. The following example
in Quarto would render as the first example of the previous subsection
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

More complex examples are shown in use case scenarios [](sec:use:qua) and
[](sec:use:lat).
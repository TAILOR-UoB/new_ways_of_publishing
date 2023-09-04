---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(launch:thebe)=

# Thebe

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

Then, any python code that is written in a `code-cell` with `ipython3` will
have the option to be run (and modified) in real time by the reader.

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

## Example with Plotly

```{code-cell} ipython3
import plotly.io as pio
import plotly.express as px
import plotly.offline as py

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="sepal_length")
fig
```

## Example with IPyWidgets

```{code-cell} ipython3
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

def f(m, b):
    plt.figure(2)
    x = np.linspace(-10, 10, num=1000)
    plt.plot(x, m * x + b)
    plt.ylim(-5, 5)
    plt.show()

interactive_plot = interactive(f, m=(-2.0, 2.0), b=(-3, 3, 0.5))
output = interactive_plot.children[-1]
output.layout.height = '350px'
interactive_plot
```

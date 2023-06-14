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

# Interactive code cells

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

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

---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: iR
  language: R
  name: ir
---

# Examples with R

Section under development.

It is possible to run `R` code by installing a kernel with `CRAN`

```R
install.packages('IRkernel')
IRkernel::installspec()
```

The last command installs the kernel for Jupyter with the default name `ir`.

Then, in order to run code in a markdown file it is necessary to indicate the
kernel in the `yaml` configuration as follows:

```
kernelspec:
  display_name: iR
  language: R
  name: ir
```

Once the kernel is loaded, we can write `R` code in any cell as

````
```{code-cell} R
"Hello world!"
```
````

which will generate the following cell and output

```{code-cell} R
"Hello world!"
```

```{code-cell} R
5 + 10 - 3
```

```{code-cell} R
var1 <- 5
var2 <- 10
var3 <- -3

print(var1 + var2 + var3)
```

```{code-cell} R
x <- c(0, 1, 3, 7, 10)
y <- c(1, 4, 8, 6, 7)

plot(x, y, type="b", xlab="time", ylab="value")
```

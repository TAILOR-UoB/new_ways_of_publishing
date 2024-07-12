# Appendix B: Development environment

In order to build this website first you need to `clone` or `fork` the source
repository. You can find a link to the repository by clicking on the GitHub
logo at the top of this page and `Repository` in the pop-up menu (or click on
the following link https://github.com/TAILOR-UoB/new_ways_of_publishing).

You can then `fork` or `clone` the respository and follow the instructions
provided by GitHub.

Once you have a local version of the repository you need to create a virtual
environment with all the dependencies. The following instructions have been
designed for an **Ubuntu 20.04** machine, but will probably work in most
operating systems.

Create a virtual environmnet with `Python3.9` at the root of the repository by
opening a terminal at the root of the repository and running the following
command

````shell
python3.9 -m venv venv
```

then activate the virtual environment

```shell
source /venv/bin/activate
```

We have created a `Makefile` that can help in all the following steps, here we
provide details about the process without using the `Makefile` and indicate
wahat 

upgrade pip and install all the required dependencies

````{tab} shell
```shell
pip install --upgrade pip
pip install -r requirements.txt
```
````
````{tab} Makefile
```shell
make install
```
````


```shell
pip install --upgrade pip
pip install -r requirements.txt
```

You will also need to install an additional python library that serves as an
example to include your own Python code in the book

```shell
pip install -e lib/book-python/
```

The book can then be build by running the following command

```shell
jupyter-book build booksource
```



Once the virtual environment has been generated and loaded (`source
/venv/bin/activate`), the book can be built with the shell command

```bash
make build
```

The previous build will compile only the source files that have changed. Some
of the table of contents on other pages may still be out of date. To fully
build the book from anew run the shell command

```bash
make cleanbuild
```

In case of wanting to run Jupyter Notebooks, you will need to create a kernel
of the current virtual environment and load it from the Notebook.

```bash
pip install ipykernel
python -m ipykernel install --user --name data-science
```

Then, you can open the notebooks with the following command

```bash
jupyter notebook
```

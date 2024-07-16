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

```shell
python3.9 -m venv venv
```

then activate the virtual environment

```shell
source /venv/bin/activate
```

We have created a `Makefile` that can help in all the following steps. We
provide below instructions with and without the `Makefile` in different tabs.

First, upgrade pip and install all the required dependencies. One of the
dependencies is a local Python library `lib/book-python` that facilitates parts
of the roadmap.

````{tab} Shell
```shell
pip install --upgrade pip
pip install -r requirements.txt
pip install -e lib/book-python/
```
````

````{tab} Makefile
```shell
make install
```
````

%% Another method to do the tabs
%`````{tab-set}
%````{tab-item} Shell
%
%```{code-block} shell
%pip install --upgrade pip
%pip install -r requirements.txt
%pip install -e lib/book-python/
%```
%````
%
%````{tab-item} Makefile
%
%```{code-block} shell
%make install
%```
%````
%`````


Then, the book can be built with

````{tab} Shell
```shell
jupyter-book build booksource
```
````

````{tab} Makefile
```shell
make build
```
````

The previous build will compile only the source files that have changed.
However, the table of contents in pages that have not changed won't be updated.
To fully build the book from anew it is necessary to clean the previous files.

````{tab} Shell
```shell
jupyter-book clean booksource
jupyter-book build booksource
```
````

````{tab} Makefile
```shell
make clean-build
```
````

The local version of the website is stored in `booksource/_build/html/`. The
html files can be explored with a web browser. However, some of the
functionalities will not work without a proper web server. For example, Python
has its own light version of a web service that can be started locally with the
following command

````{tab} Shell
```shell
python -m http.server 9000 -d booksource/_build/html/
```
````

````{tab} Makefile
```shell
make serve
```
````

If successful you should be able to access the website locally at
http://localhost:9000.

The `PDF` version of the website needs to be rendered a part from the website,
and it will overwrite the `HTML` website with a one page version of it. The
resulting `PDF` is then moved into the `booksource/assets/documents/` folder.

````{tab} Shell
```shell
jupyter-book build booksource/ --builder pdfhtml
cp booksource/_build/pdf/book.pdf booksource/assets/documents/nwop_book.pdf
```
````

````{tab} Makefile
```shell
make build-pdf
```
````

In order to get the website back you will need to run again the `build`
process.

In this roadmap we did not use any Jupyter Notebook. However, in case of
wanting to edit one you will need to create a kernel of the current virtual
environment and load it from the Notebook.

````{tab} Shell
```shell
pip install ipykernel
python -m ipykernel install --user --name data-science
```
````

````{tab} Makefile
```shell
make create-kernel
```
````

Then, you can open `Jupyter Notebook` and edit any notebooks inside the folder
`booksource` with the following command

```bash
jupyter notebook ./booksource/
```

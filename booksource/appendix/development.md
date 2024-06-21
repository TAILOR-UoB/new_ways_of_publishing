# Appendix: Development environment

In order to build this website you will need to create a virtual environment
with `Python3.9` with the dependencies indicated in the `requirements.txt`
file. You can do that by running the following code in a shell.

```bash
python3.9 -m venv venv
source /venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
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

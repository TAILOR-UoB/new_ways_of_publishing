(sec:todos)=
# TODOs

- [x] MPN: Add tick boxes.
- [ ] MPN: Fix problem with ~~strikethrough~~ text
  [MyST documentation](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#strikethrough)
- [ ] MPN: Fix problem exporting pdf with `--builder pdfhtml` [Jupyterbook
  documentation](https://jupyterbook.org/en/stable/advanced/pdf.html#build)
- [ ] MPN: Fix problem exporting pdf with `--builder pdflatex` [Jupyter book
  documentation](https://jupyterbook.org/en/stable/advanced/pdf.html#book-style-pdf)
- [x] MPN: Fix problem with bibliography generating multiple columns for the
  full page (see [](sec:citations)). Fixed, see notes.
- [ ] MPN: Fix issue installing the interactive R kernel in a GitHub action

# Notes

- MPN: It is possible to build a pdf of the full book with the following
  command `jupyter-book build booksource/ --builder pdfhtml`. However, the
  resulting document has sentences cut by the middle horizontally (like showing
  only the upper part of a ~~striked text~~).
- MPN: There are issues with the bibliography with `docutils<=0.18,<20`, I had
  to dowgrade to `doccutils==0.17.1` while the problems are fixed. You can find
  more details at [Jupyter{book} Citations and
  bibliographies](https://jupyterbook.org/en/stable/content/citations.html#).

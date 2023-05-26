(sec:citations)=
# Markdown citations

MPN: I have moved the example of citations to a different page until I fix the
issue of the bibliography dividing the page into multiple columns.

## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`ruby` `` will render like
this: {cite}`ruby`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

## References

```{bibliography}
```

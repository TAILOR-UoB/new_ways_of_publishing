# Shinylive: Shiny + WebAssembly

WebAssembly is a binary format for compiled programs that can run in the web
browser at near-native speeds. Pyodide is a port of Python and various packages
compiled in WebAssembly.

Shiny provides an interface with an editor, output console and a user interface
to run R or Python code.


<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMVAJwEtyAKAcgAk4AbT4gAgHditTgBMAhCwCUAHQhgAvgF0gA"
data-external="1" width="100%" height="400px">
</iframe>


```
<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAMwCdiYACAZwAsBLCbJjmVYnTJMAgujxMArhwA6EOWlQB9aUwC8UjligBzOEpoAbaQBMAFNIxsATGZlgAEhwlQIJpmTauA1iyY1BDzpsLh0mAGVObgBCewBKOLkFdHVRdDNFFWcmADlSOESIMABfAF0gA"
data-external="1" width="100%" height="400px">
</iframe>
```

<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAMwCdiYACAZwAsBLCbJjmVYnTJMAgujxMArhwA6EOWlQB9aUwC8UjligBzOEpoAbaQBMAFNIxsATGZlgAEhwlQIJpmTauA1iyY1BDzpsLh0mAGVObgBCewBKOLkFdHVRdDNFFWcmADlSOESIMABfAF0gA"
data-external="1" width="100%" height="400px">
</iframe>

All the code for the previous example is encoded in the URL as a GET method. It
is possible to modify the code in the editor, and generate the new URL by
clicking the Share button on the top right corner. This provides a link to the
editor (including editor, console and user interface (ui)) or only the
application (ui).


The code can be a Github Gist code by providing the gist id. For example, the
following GitHub Gist https://gist.github.com/wch/e62218aa28bf26e785fc6cb99efe8efe
with id=e62218aa28bf26e785fc6cb99efe8efe can be deployed with 

```
<iframe src="https://shinylive.io/py/editor/#gist=e62218aa28bf26e785fc6cb99efe8efe"
data-external="1" width="100%" height="400px">
</iframe>
```

<iframe src="https://shinylive.io/py/editor/#gist=e62218aa28bf26e785fc6cb99efe8efe"
data-external="1" width="100%" height="400px">
</iframe>

<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACGKM1AG2LK5oBGWbN14soAZxbcyAHQh0GzFhACu9bOKkRU8gGaNiMFhIAWNCJsVNWAQXR4WjSgBM4jR6prz5aVAH0vFgBeFi8sKABzOH89Li8XAAp5FlSwmgwLVFUyfwl+N0ZkyFl8FlKAOXUBdxZiPRYBCwlSxwAGRwBGNo6WACY2gEo8FLTw4hzs3NEyYpnS4flBnwh5NwaJdwA3d0SsnMcJzgOTOAkJGlJBxFHUgAEjqduWO+cIQqweWaguMmDS2wscwSMjESKMWALZ7raRfRLXZ5pFSYCHvIwYTZwJKdACcADYABxtImdZYQJFIgAeIRY3TaLAA1LSAKwsABUyIwqJc6O5EESABYAMwAdjJiLSehokUcUGpoRkGNUAhmEnhEtScowwNmlMc+zIGH5wxYbggFzI2GCABVGKo4GSKWlnGRVIxyVLIitfOgafZUIk-IEaI5Nowdh5TXABKpIja7Q75GAAL4AXSAA" data-external="1"
width="925px" height="400px">
</iframe>



<iframe src="https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACGKM1AG2LK5oBGWbN14soAZxbcyAHQgAzRsRgsJACxoRsLOg2YsAgujwtGlACZxGpgK4158tKgD69lgF4W9rFADmcC4KXPYWABTyLFHeNBjEtpwJLqJkEWApsmAAlHjyWY4QVgpq1gBu1mFaqAmm8YlkphJwEhI0pFmIkdEAAnXVchDRLN3mhdZYPKlQXGQemYYs-BBw0pOZ+YPRRau8YR1dQ1HmZLaMgzITu8AADKYAjKYATKYAbAC6pjemACxPpgDsHxYAHJiABaYEbJzoTxGdBhZxuGiNMrWLJgAC+byAA" data-external="1"
width="925px" height="400px">
</iframe>

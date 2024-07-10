# New Ways of Publishing: A Roadmap to Authoring Online Training Material

This website provides a set of guidelines to publish online training material
using state-of-the-art web authoring tools, and also serves as an example itself.

It has been prepared as a deliverable of the 
[TAILOR Network of Trustworthy AI through Integrating Learning, Optimisation and Reasoning](https://tailor-network.eu) 
as part of Work Package 9: Network Collaboration. 

## Usage

### Building the website

If you'd like to develop and/or build the website, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. Run `pip install -e /lib/book-python/` (these are some Python tools
   for the book)
4. (Optional) Edit the books source files located in the `booksource/` directory
5. Run `jupyter-book clean booksource/` to remove any existing builds
6. Run `jupyter-book build booksource/`

A fully-rendered HTML version of the book will be built in `booksource/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/perellonieto/booksource/graphs/contributors).

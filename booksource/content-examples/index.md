# Content Examples

In this Section we provide multiple examples of the type of content that can be
generated with publishing systems like `Jupyter Book` and `Quarto`. We divided
the different content into three types. The basic content is the most common
textual narratives that include figures, tables, and other static elements. We
also include videos in that section as videos are a common resource in
internet.

## Basic content

To generate basic content with a publication system and accessing the
resulting content online usually follows the steps shown in the diagram below.
**(1)** The publication system compiles all the source documents and creates a
static publication website, **(2)** the static website is sent to an online
hosting service which is properly organised, **(3)** a user requests access to
the website to the host server from a computer or other device, **(4)** the
hosting service serves the required documents to the client.

```{figure} images/static.svg
:name: fig-cli-sta

Diagram of files and communication for content that is show in the bew browser
as static content (the content could be printed).
```

Most of this type of content is described in section [](sec:basic) and part of
the section [](sec:com:nar).

## Interactive with a third party

Online content in STEM fields commonly involve programming, sometimes being an
important part of the training material. Platforms like Jupyter notebooks allow
the creation of computational narratives that can be interactive, and can be
modified and re-run changing the visualisation outcomes. This type of content
requires a different architecture in which a computational node is involved to
create an execution environment that can run and serve any changes in the
source code. The first five steps mentioned above are the same, but additional
steps are necessary. **(6)** The client has the option of interacting with
certain parts of the website (e.g. changing the source code of some
computational narrative cells), **(7)** a new session is started in a third
party computational node that instantiates all the necessary dependencies to
execute the changes and re-running the necessary parts, **(8)** the third party
server serves all the changes to the client.

```{figure} images/interactive_server.svg
:name: fig-ser-int

Diagram of files and communication for content that is show in the bew browser
as static content but the content can be modified and rerun but requires a
session with a (third party) server.
```

This may require the payment of a third party service that includes execution
of code. There are some free services like `MyBinder` or `Google Colab` that
offer a free tier. The end of section [](sec:com:nar) provides some guidelines
on how to generate this type of content.

## Interactive within the client

```{figure} images/interactive_client.svg
:name: fig-cli-int

Diagram of files and communication for content that is show in the bew browser
as static content but the content can be modified and re-run within the client
web browser (no further communication is necessary with external servers).
```


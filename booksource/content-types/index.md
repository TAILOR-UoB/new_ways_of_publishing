(sec:con)=
# Types of content

In this Section we provide multiple examples of the type of content that can be
generated with publishing systems like `Jupyter Book` and `Quarto`. We divided
the different content into three types. The basic content is the most common
textual narratives that include figures, tables, and other static elements. We
also include videos in that section as videos are a common resource in
internet.

(sec:con:bas)=
## Basic content

To generate basic content with a publication system and accessing the resulting
content online usually follows the steps shown in the diagram below.  **(1)**
The publication system compiles all the source documents and creates a static
publication website, **(2)** the static website is sent to an online hosting
service which **(3)** is properly organised, **(4)** a user requests access to
the website to the host server from a computer or other device, **(5)** the
hosting service serves the required documents to the client.

```{figure} images/static.svg
:name: fig-cli-sta
:width: 550px

Diagram of files and communication for content that is show in the web browser
as static content (the content could be printed).
```

Most of this type of content is described in section [](sec:basic) and part of
the section [](sec:com:nar).

(sec:con:ser)=
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
:width: 500px

Diagram of files and communication for content that is show in the bew browser
as static content but the content can be modified and rerun but requires a
session with a (third party) server.
```

This may require the payment of a third party service that includes execution
of code. The process commonly requires starting a computational instance which
is often slow and may end up in connection issues. There are services like
`MyBinder` or `Google Colab` that offer a free tier. The full section
[](sec:com:nar) can be run in third party servers which also includes
guidelines on how to generate this type of content in subsection
[](sec:mar:liv).

(sec:con:cli)=
## Interactive within the web browser

There are some ways to create interactive content within the web browser based
on static content. The benefit of this type of content is that it can be hosted
by multiple hosting services that offer free static hosting, not requiring
computational nodes on the server side. Content of this type uses the
computational resources of the client web browser in order to modify its
content. The series of steps are the same as the basic content [](sec:con:bas)
but any subsequent interactions are done in the client's computer.

```{figure} images/interactive_client.svg
:name: fig-cli-int
:width: 350px

Diagram of files and communication for content that is show in the bew browser
as static content but the content can be modified and re-run within the client
web browser (no further communication is necessary with external servers).
```

One of the drawbacks of this method is that it may require longer loading times
as additional files need to be downloaded even if no interaction is intended.
The section [](sec:con:run) provides a guideline with examples of this type of
content.

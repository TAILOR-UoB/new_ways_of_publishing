(sec:exa)=
# From static and dynamic to interactive content

In this section we provide a range of examples of the kinds of content that can be
authored with publishing systems such as `Jupyter Book` and `Quarto`. 
We consider three different types of content: 
- [](sec:static) is rendered during the creation of the website/book and is kept static; 
- [](sec:com:nar) includes computational code cells that are rendered during the creation of the
website/book but can be modified and re-run on demand;  and 
- [](sec:exa:run) provides interactive elements such as buttons, sliders, interactive figures and
more. 
Many more examples can be found in the documentation of [Quarto](https://quarto.org/docs/guide/) and
[Jupyter Book](https://jupyterbook.org/en/stable/intro.html).

(sec:exa:com:inf)=
## Computational infrastructure

An important consideration when designing online teaching material is the location 
where the material will be hosted and served. 
The host capabilities may affect the type of content that can be included.
For example, the content of this roadmap is being hosted as a static webpage thanks to the
free service offered by [GitHub pages](https://pages.github.com/). However,
most free hosting services do not provide computational capabilities for
dynamic or interactive functionalities. For instance, the
[](sec:com:nar) material is visualised as a static web page by Github pages 
but the same content can be run by a third party server for its dynamic functionalities. 
Services such as *MyBinder* and *Google Colab*, offer free tier versions but they may be slow
or fail to run for various reasons (e.g. connection errors or high server
workload). Parts of the [](sec:exa:run) of the roadmap may also require a third party
service. Additional information about these requirements is specified when
showcasing each example.

%## remove
%
%An important consideration when designing online teaching material is where the
%content is going to be hosted. 
%
%The price of web hosting services may vary
%depending on the
%
%Some types of dynamic and interactive content
%may require a hosting that can run programming code on demand., or use a third
%party service. 
%
%The content of this website is hosted as static content in GitHub Pages,
%however some of the examples shown in this section require a third party server
%that is able to run computational code on demand. For that reason, next Section
%[](sec:exa:com:inf) describes some of the limitations and considerations when
%We provide some considerations to keep in mind.
%
%
%
%
%
%(sec:exa:bas)=
%### Non-interactive content
%
%To generate basic content with a publication system and accessing the resulting
%content online usually follows the steps shown in the diagram below.  **(1)**
%The publication system compiles all the source documents and creates a static
%publication website, **(2)** the static website is sent to an online hosting
%service which **(3)** is properly organised, **(4)** a user requests access to
%the website to the host server from a computer or other device, **(5)** the
%hosting service serves the required documents to the client.
%
%```{figure} images/static.svg
%:name: fig-cli-sta
%:width: 550px
%
%Diagram of files and communication for content that is show in the web browser
%as static content (the content could be printed).
%```
%
%Most of this type of content is described in section [](sec:static) and part of
%the section [](sec:com:nar).
%
%(sec:exa:ser)=
%### Interactive with a third party
%
%Online content in STEM fields commonly involve programming, sometimes being an
%important part of the training material. Platforms like Jupyter notebooks allow
%the creation of computational narratives that can be interactive, and can be
%modified and re-run changing the visualisation outcomes. This type of content
%requires a different architecture in which a computational node is involved to
%create an execution environment that can run and serve any changes in the
%source code. The first five steps mentioned above are the same, but additional
%steps are necessary. **(6)** The client has the option of interacting with
%certain parts of the website (e.g. changing the source code of some
%computational narrative cells), **(7)** a new session is started in a third
%party computational node that instantiates all the necessary dependencies to
%execute the changes and re-running the necessary parts, **(8)** the third party
%server serves all the changes to the client.
%
%```{figure} images/interactive_server.svg
%:name: fig-ser-int
%:width: 500px
%
%Diagram of files and communication for content that is show in the bew browser
%as static content but the content can be modified and rerun but requires a
%session with a (third party) server.
%```
%
%This may require the payment of a third party service that includes execution
%of code. The process commonly requires starting a computational instance which
%is often slow and may end up in connection issues. There are services like
%`MyBinder` or `Google Colab` that offer a free tier. The full section
%[](sec:com:nar) can be run in third party servers which also includes
%guidelines on how to generate this type of content in subsection
%[](sec:mar:liv).
%
%(sec:exa:cli)=
%### Interactive within the web browser
%
%There are some ways to create interactive content within the web browser based
%on static content. The benefit of this type of content is that it can be hosted
%by multiple hosting services that offer free static hosting, not requiring
%computational nodes on the server side. Content of this type uses the
%computational resources of the client web browser in order to modify its
%content. The series of steps are the same as the basic content [](sec:exa:bas)
%but any subsequent interactions are done in the client's computer.
%
%```{figure} images/interactive_client.svg
%:name: fig-cli-int
%:width: 350px
%
%Diagram of files and communication for content that is show in the bew browser
%as static content but the content can be modified and re-run within the client
%web browser (no further communication is necessary with external servers).
%```
%
%One of the drawbacks of this method is that it may require longer loading times
%as additional files need to be downloaded even if no interaction is intended.
%The section [](sec:exa:run) provides a guideline with examples of this type of
%content.

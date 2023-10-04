---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
---

# Interactive code cells

Some teaching material may benefit from providing access to interactive code
that can be a demonstration on how something is calculated or computed.
In some occasions, having access to the computer code that has generated certain
figures can be very useful for the learning process.
We can list different ways in which providing the code can be useful for
different scenarios:

- Provide static code and the figure generated to understand or replicate by
  the user.
- Provide a cell of code and the generated figure that can be modified by the
  user to better understand how the changes in the code affect the outcome.
- Provide a widgets and buttons to interact with a figure and better understand
  how certain parameters affect the output. In this case the objective is not
  to learn how it was programmed, but to understand better a concept.

We also need to differentiate how the code can be run and modified in the
browser:

- The code is static and is shown just as an example.
- The code can be modified and run again provided that a server (another
  dedicated machine) is available to run the code.
- The code can be modified and run again in the client's web browser.

The previous methods of delivery have their own benefits and drawbacks.

**Explain the drawbacks and bennefits here**

- Static: Pros: Can be easily printed in a pdf or other output artefacts. Cons:
  It does not provide interaction, which may be crucial to better understand
  some concepts.
- Dynamic in a server: Pros: It can be easily printed in a pdf or other output
  artefacts and the user can modify the code to better understand some
  concepts. Cons: It requires a dedicated server that somebody needs to keep up
  to date, or free of charge but may not be reliable.
- Dynamic in the client: Pros: A static version of the code can be printed as
  an ouptut artifact. The code can be modified and run without the need of a
  dedicated server. Cons: The webpage may need to download additional binary
  code that needs to be run in the client's browser. The current options to
  generate figures require some obfuscated code.


List of todos

```
Adding a section # TODO breaks all the subsections in this Chapter
```

- Think about examples out of the fields of computer science, mathematics or
  physics

With the help of [Thebe](https://thebe.readthedocs.io/en/stable/) it is
possible to add interactive code inline. By default, this Jupyter Book has been
configured to run Thebe with MyBinder whenever a section specifies in the Yaml
header the following tags.

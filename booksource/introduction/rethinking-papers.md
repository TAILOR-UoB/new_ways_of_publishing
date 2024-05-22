# Rethinking papers

Notes from ICLR 2021 Workshop Rethinking ML Papers

https://rethinkingmlpapers.github.io/papers/

## In Defense of the Paper by Owen Lockwood

{cite}`lockwood_defense_2021`

- Explosion of papers in Machine Learning since 2012 (possibly due to
  Artificial Neural Networks).
- Publication process has been broken and requires a new reconceptualization
- Common problems
  1. Publish or perish (Mental health impact {cite}`bira_mental_2019`, research quality
     {cite}`aitkenhead_peter_2013`).
  2. Explainability (missattribution {cite}`henderson_deep_2018`, HARking
     (Hypothesizing after the resulst are known) or poor
     methodological practices {cite}`kerr_harking_1998`, {cite}`gencoglu_hark_2019`.
  3. Interpretability (errors, obfuscated, lack of review incentives)
- Accessibility vs inclusivity
- Hybrid conferences
- Democratize compute resources
- Break non-specialised conferences into specialised ones
- Hypothesis lock box (in other fields)
- pre-registration
- Improve reviewing system (e.g. paying, rating, eliminate double blind)


References

- Previous work Sculley et al. 2018, review with case studies o problems and
  solutions
- Lipton & Steinhardt 2018 overview of existing problems but not much about
  solutions

## Curating Publications as Artefacts — Exploring Machine Learning Research in an Interactive Virtual Museum

- Check publication cycle by {cite}`bjork_lifecycle_2005`
	- Browsing existing scientific knowledge
	- Performing research
	- Convert into publication format
	- Communicating and disseminating the research
	- Adding new scientific knowledge
  - Repeat

- Check {cite}`bjork_study_2011` for innovative publication formats including
  web and hyperlinks.
- Check the initiative of the Visualization for AI Explainability workshops,
  next one 7th workshop at IEEE VIS in St. Pete Beach, Florida. Which requires
  blogposts as a submission method.

## Distill

- It was a scientific journal that operated between 2016 and 2021.
- The editorial team announced an indefinite hiatus because of frictions
  between being a journal but encouraging authors self-publishing habits.
- Distill can still be used as a template [distillpub/template](https://github.com/distillpub/template)
- Distill is based on HTML, CSS and JavaScript and requires loading the distill
  JavaScript library in the header. 

## Machine learning research communication via illustrated and interactive web articles

## I❤LA -- Compilable Markdown for Linear Algebra

Markdown text that can be converted into MathJax, Python, C++, LaTeX and
MATLAB.

## You Only Write Thrice -- Creating Documents, Computational Notebooks and Presentations From a Single Source

## Exhibit -- Converting my PhD thesis to HTML

Some of the main drawbacks of pdf publications

- Designed for printing
- Difficult to browse in some devices
- Huge document with multiple pages, difficult to move between sections

Bennefits of HTML

- Can be browsed in multiple devices
- Sections divided into smaller pages that are easy to navigate

How can LaTeX be converted into html?

- TeX4ht very hard (30 to 40 hours)
- Need more automatic tools




## Diagrammatic summaries for neural architectures

## ModulOM -- Disseminating Deep Learning Research with Modular Output Mathematics

## SPICES -- Survey papers as interactive cheatsheet embeddings

- Invitation notes to researchers from different fields
- Collection of important problems to be solved
- Source material for faster, better, and up-to-date teaching
- Agenda for research directions
- Concise list of citations

Good survey

- Balance between own and community's contributions
- Non-biased narrative

Interesting work to look at

- Proceedings as 2D doc2vec embeddings
- Check awesome github repositories
- Cheatsheets

Important aspects of surveys

- Most of the contributions are in the form of a graph G(V,E)
- WISE rule of reading papers
  - Why does this paper exist?
  - Iconoclasm: Resist attribution of importance of the paper based on authors
  - Situanality / semantic neighborhood: Find context of the paper
  - Experimental revalidation: check experiments and results

SPICES method to write a good survey paper

-


## On augmenting the references section with a citation network visualization

## Fairness and Friends

## Scientific dissemination via comic strip -- A case study with SacreBLEU

## Convolution Can Incur Foveation Effects

## Open-source blogging with Automunge

## The Mimosa Manifesto


- Platform to make questions, hypothesis and answers
- People can contribute with their results
- People can answer the question which adds to the count, and can provide
  evidences that are incorporated into the explanation.

Similar platforms

- Hypergraph: peer to peer platform to share results to own network and export
  paper
- Octopus: Online publishing platform for scholarly research. Funded by UKRI. 
- Mimosa:

### Octopus

Octopus is managed by Jisc and Octopus Publishing CIC.
[Jisc](https://www.jisc.ac.uk/) is a not-for-profit company focused ontertiary
education, research and innovation based in Bristol, London, Manchester, Oxford
and other UK locations. The research published in
Octopus is open access licensed and the platform is published under the open
source license GPLv3. All Octopus publications have a CC-BY 4.0 license.

- Designed to publish all the research work from theory, data to analysis.
- Requires the following information:
  - Title
  - Text and references
  - List of co-authors and emails
  - Funders and acknowledgements
  - Conflicts of interest
  - Institutional affiliations
  - Related topics and/or publications already in Octopus

The publication types that are currently supported are

- **Research problem**: Propose a problem or question and what it is currently
  known about it.
- **Rationale/Hypothesis**: A potential solution to a problem that needs to be
  validated.
- **Method**: A description of a process that can be used to test a hypothesis.
  It can benefit from the definition of a protocol in
  [protocols.io](protocols.io).
- **Results**: Raw data or summarised results collected following a previous
  method. The analysis of results needs to be reported in a separate
  publication type. The data can not be hosted in Octopus and needs to be
  linked in a specialist repository.
- **Analysis**: Manipulations and interpretations of results (e.g. statistical
  analysis).
- **Interpretation**: Conclusions that can be drawn from an analysis.
- **Real World Application**: How findings have been applied in a real world
  solution (e.g. case studies).
- **Peer Review**: Careful constructive critique to a previously published
  work potentially requiring relevant references. Authors of the original work
  can reversion based on the peer review including accreditation.

## A snapshot of the academic research culture in 2023 and how it might be improved

{cite}`hsing_snapshot_2023`

- A work with Octopus and how it can fix some of the current issues with
  academic research.
- Division of research process into 8 steps that can be published independently
  and referenced (interconnected).
- Principle of open research as defined by the Open Knowledge Foundation:
  ``Knowledge is open if anyone [has the freedoms] to access, use, modify, and
  share it -- subject, at most, to measures that preserve provenance and
  openness.''
- Other consideration Findable, Accessible, Interoperable, and Reusable (FAIR)
  principles for data. {cite}`wilkinson_fair_2016`
- The peer-review process encourages not sharing ongoing research until it has
  been curated, submitted and successfully accepted for publication. This may
  lead to hidding information, or data manipulation to achieve results that are
  accepted by a high impact publisher.


- Most prominent barriers for not sharing research reported during interviews
  and survey:
  - Lack of time which is redirected to publishing on high impact journals,
    networking, and other activities that directly benefit their careers.
  - Fear of scooping in a highly competitive research culture. The credit is
    commonly obtained from the final publication, and the process to reach is
    not valued (e.g. proposing an hypothesis), while institutions value high
    and dramatic stories which are not possible in the earlier stages of
    a research process.
  - There is an inequitable access to the resources that is being led by rich
    countries. Other researchers with no funding are excluded from the
    discussions on how the research should be led.
- Preasure that lead to questionable research practices (QRPs)
  - Focus on the quantity of published papers rather than quality.
  - Presure to obtain novel and positive results (hidding unsuccessful
    research).
- Factors that lead to certain topics and types of research being favoured
  - No clear factors were found, but the relation to the QRPs mentioned above
    show that positive results and easy to publish articles are favoured.
- More openly collaborative ways of thinking and working
  - Focus on the process and not on the output.
  - Value negative or null results.
  - Recognise different forms of contributions.
  - Recognise other type of work done by the authors like teaching,
    administration, fundraising, mentoring...
  - Assessment should be scrutinised and assessed.
  - Necessity of feedback during the full process, as at the moment the
    feedback is obtained in the last stages of publication. On the other hand,
    early feedback could be useful but it is perceived as a potential risk for
    retribution.


## Interactive Media for Understanding ML Methods -- A Case-Study on Graph Neural Networks



# Appendix: Open Courses

The idea of Open Courses is to take some of the principles of Open Research and
adapt for the creation of online training material. Open Research is a set of
principles to promote sharing research outcomes in a way that makes research
reproducible and more transparent. There are at least four aspects that are
considered:

- **Open Code** (Open source licenses)
- **FAIR Data** (Findable Accessible Interoperable Reusable)
- **Research Profile** (e.g. ORCID)
- **Open Access** of publications (Green, Gold, Hybrid, Diamond)

New ways of publishing potentially needs to consider all of the aforementioned
points as the objective is to publish training material online with maximum
reach. For transparency and accessibility the source code of the course should
be open and any data used in the course should adhere to best practices. The
authors of the course may also benefit from an open research profile which
would give credibility to their content, transparency and increase the
visibility to other work created by the same authors.

## Open Code

As indicated for the datasets, publishing the code of the training material
online does not entitle the way in which the course material can be used. When
the course is created it is automatically protected by copyright. The course
source code material without a license can not be used. It is important then to
understand what are the licenses available and to add them to the course
material properly. The information provided in this roadmap is a personal
overview and should not be taken as legal advise, additional information can be
found at https://opensource.guide/legal/. Furthermore, an interactive guide on
how to choose a license is available at https://choosealicense.com/.

One of the most common licenses for open-source is `Creative Commons`. It has
lots of variations depending on the flexibility that you want to provide to the
users. The Creative Common licenses are short named with acronyms, and
understanding them makes much easier their interpretation.  

- **0 (No rights Reserved, Public Domain)**: There are no restrictions on how
  the code is used nor shared.
- **BY (By Attribution)**: Any use of the code needs to attribute the original
  work and author/s.
- **SA (Share-Alike)**: Any use of the code even if modified needs to keep the
  same license as the original work.
- **ND (No Derivatives)**: The work is shared as a whole and can not be
  modified.
- **NC (Non Commercial)**: The work can not be used for commercial uses.

The following are some common Creative Commons licenses:

- **CC-0**: No Rights Reserved, allows the distribution without accreditation, it
  is commonly used to share tabular data or other databases from which
  knowledge could be derived.
- **CC-BY**: Attribution, allows the use of the work even for commercial
  purposes but requires the attribution of the original form (e.g. with a
  citation). It is recommended for the widest dissemination of work.
- **CC-BY-SA**: Attribution-ShareAlike, allows the use of the work even for commercial
  purposes but requires the attribution and the same type of license to any
  derivatives.
- **CC-BY-ND**: Attribution-NoDerivatives, allows the use of the code as it is
  even for commercial uses, but does not allow the modification of the code. It
  also requires the accreditation of the original author.
- **CC-BY-NC**: Attribution-NonCommercial), allows the use and modification of
  the code for non-commercial use, subject to accreditation of the author and
  does not require the same license on its derivatives.
- **CC-BY-NC-SA**: Attribution-NonComercial-ShareAlike, allows the use and
  modification of the work for non commercial applications, requires
  accreditation of the original work and authors and the derived code needs to
  use the same license as the original.
- **CC-BY-NC-ND**: Attribution-NonComercial-NoDerivatives, allows the use of
  the code without modifications for non commercial uses and requires
  accreditation of the original work and authors.
- **The Restrictive License Template**: is a license developed by the
  Australian Government Open Access Licensing framework for material that
  contains personal or other confidential information. It can include multiple
  restrictions on its use like time limits, permissions or ethics required, or
  contractual arrangements). See more at
  https://library.unimelb.edu.au/Digital-Scholarship/restrictive-licence-template

Other common licenses for software are

- **MIT** ([license](https://opensource.org/license/mit)) allows the use of the
  Software free of charge, with no restrictions but under the condition that
  there is an accreditation of the original software and authors and that the
  permission notice is included in all the copies or substantial portions of
  the Software.
- **Apache** (Apache License, Version 2.0)
  ([license](https://www.apache.org/licenses/LICENSE-2.0))
- **GPL** (General Public License) guarantees the end users the four freedoms
  to run, study, share and modify the Software.

And the BSD license which includes several versions

- **BSD 0-clause** (aka BSD Zero Clause License) allows the use, copy,
  modification and/or distribution of the Software for any purposes with or
  without fees.
- **BSD 2-clause license** (aka "Simplified BSD License" or "FreeBSD
  License") same as 0-clause but requires to retain the copyright notice, the
  list of conditions and a disclaimer in the source code and in the
  documentation or other materials provided if used in its binary form.
- **BSD 3-clause** (aka "BSD License 2.0", "Revised BSD License", "New BSD
  License", or "Modified BSD License") same as 2-clause license but does not
  allow the endorsement or promotion of products in the name of the original
  copyright holders and contributors without specific prior written permission.
- **BSD 4-clause** (aka original "BSD License") same as 3-clause license but
  all advertising material that mentiones the use of the original sofware must
  display the following acknowledgement: This product includes software
  developed by the \<copyright holder\>.

## FAIR Data

The FAIR (Findable Accessible Interoperable Reusable) principles of sharing
data were defined by a consortium of scientists and organisations, and
published in the journal Scientific Data {cite}`Wilkinson2016-so`. In STEM
fields it is very common to share datasets with the students in order to better
understand the training material. It is important to ensure that any data
shared online in this manner is correctly licensed. The four principles that
shape the acronym are:

- **Findable**: Additional metadata is added in order to easily identify and
  find the data with a search engine. The metadata needs to contain clear
  information and the data requires a unique identifier.
- **Accessible**: There is a specific protocol that can be followed to retrieve
  the metadata of the data of interest (even if the data is not available). The
  metadata is also understandable by humans and can be processed by machines.
  The data is stored in a trusted repository that ensures its accessibility for
  a particular period of time.
- **Interoperable**: The metadata follows a formal structure that is commonly
  accepted by multiple parties. Ideally the metadata has a vocabulary that
  follows the FAIR principles and can form a knowledge representation.
- **Reusable**: It is clearly specified how the data can be reused by others,
  including a license and any usage limitations.

### Data format and storage

Data should be stored in such a way that is easy to understand by humans,
machine readable and accessible; including metadata human and computer
readible. The data should be stored in open file formats facilitating the
accessibility, and not requiring propertary applications to be opened. Should
provide good documentation (e.g. a README plain text file), and be stored in a
trusted dat repository for long term storage.

Some examples of data repositories are:

- [figshare](https://figshare.com/) allows to upload any file format and assigns a
  DOI identifier for citations.
- [Mendeley Data](https://data.mendeley.com/) allows the storage of public or
  private data, keeps versioning and ensures long-term storage by Data
  Archiving & Networked Services[^DANS].
- [Zenodo](https://zenodo.org/) is a general-purpose open-access repository
  that facilitates making the repository private and can automatically make it
  open once an associated paper is published. No restrictions on the file type
  and datasets up to 50 GB.
- [The Open Science Framework](https://osf.io/dashboard)[^OSF] is an
  open-source research management and collaboration tool to facilitate the
  documentation of a full project lifecycle.
%- University of Cambridge Apollo https://www.repository.cam.ac.uk/home
%- University of Bristol https://data.bris.ac.uk/data/

[^OSF]: https://osf.io/dashboard
[^DANS]: https://www.nwo.nl/en/data-archiving-and-networked-services-dans

%- Make machine readible and accessible
%- Use open file formats.
%- File formats that do not require a propertary application to be opened.
%- File formats that store plain information
%- Metadata human readible and computer readible
%- Provide good documentation (e.g. README plain text file)
%- Trusted data repository for long term storage

### Data Licenses

%Why a license
%
%- Business organisations and start-ups can not use it
%- Provide certainty on its use cases
%- The simpler the better for reuse
%- It is not enough making data publicly available, it requires a license to
%  provide legal clarity on its potential use.
%- Open data should be licenses in order to be publicly available, usable and
%sharable.
%- Without license, User do not have permission to access, use and share under copyright and
%  database laws.

Publishing a dataset online does not entitle the ways in which the data can be
used. When the data is generated it is automatically protected by copyright and
without a license, users do not have permission to access, use and share under
copyright and database laws. For example, in 2015, ~54% of the open data in
open data catalogues across the European Union was not truly open as it was not
licensed[^1].

[^1]: https://data.europa.eu/elearning/en/module4/#/id/co-01

There are multiple licenses to choose from, and as legal documents they may
differ in some small details. In order to facilitate the understanding of the
licenses and maximise the use of your material it is advisable to use well
known licenses. 

Some of the most common licenses are the Creative Commons. Similar principles
shown previously in the open-source licenses section apply here. For example
the **Open Data Commons by Attribution License (ODC-BY v4.0**) allows to copy,
distribute and use a database, produce new works derived from it, modify,
transform and build upon it subject to attribution to the original work. A
similar license that forces any derived work to be shared under the same
license is the **Creative Commons by Attribution share-alike (CC-BY-SA v4.0)**.
On the other hand, a less restrictive license for public domain is the **CC0**
which does not require attribution.

The licenses can also be created to fit particular purposes, or to facilitate
its adoption in certain organisations. This is the case for some governments may
create their own open data licenses to facilitate its adoption among
governmental organisations. Some examples of governmental licenses are the UK
Open Government License[^uk], the French Government open License[^fr] and the
Singapore Open Data Licence[^sg].

[^uk]: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
[^fr]: https://etalab.gouv.fr/licence-ouverte-open-licence
[^sg]: https://beta.data.gov.sg/open-data-license

The European Union offers an online data licensing assistant[^eu] 

[^eu]: https://data.europa.eu/en/training/licensing-assistant

The following video provides some quick guidelines on Data Sharing by the UK
Reproducibility Network. The animation is shared under a CC BY license. Other
UKRN primers are available at https://www,ukrn.org/primers.

<iframe width="560" height="315"
src="https://www.youtube.com/embed/wjWAUrvA6c4?si=WHTBIe0DCSzvLWLD"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Research Profile

The authoring of any material should clearly and uniquely identify the identity
of the contributors. In printing material it was common to use the name and
surnames of the authors as an identification. However, in multiple occasions
this is not enough for disambiguation. With more recent online tools it is
possible to disambiguate authors by providing additional information and
creating unique identifiers for each of them. Webpages like ORCID[^ORCID]
(Open Researcher and Contributor ID) provide unique identifiers for researchers
and connect them with their contributions. Other identifiers are
the Scopus Author Profile[^scopus] by Elsevier, ResearcherID[^clarivate] from
Clarivate, the Digital Author Identifier (DAI)[^DAI] by the Dutch research
system, among others.

[^scopus]: https://www.elsevier.com/en-gb/products/scopus/author-profiles
[^ORCID]: https://info.orcid.org/ 
[^clarivate]: https://clarivate.com/products/scientific-and-academic-research/research-discovery-and-workflow-solutions/researcher-profiles/
[^DAI]: https://en.wikipedia.org/wiki/Digital_Author_Identifier

## Open Access

We provide a short introduction to Open Access for completeness of the Open
Research principles, which is mainly directed for research publications.
However, we believe this principle may be considered if the training material
is reused for a research publication. Open Access is a broad international
movement that specifies a set of principles to make research free of access and
online, defined as "digital, online, free of charge, and free of most copyright
and licensing restrictions.". One of the main objectives is to publish research
work under the CC-BY license. If the material for a course is later reused to
publish a book or some other type of publication it may be necessary to know
what are the possible licensing restrictions.

```{figure} images/open-access-logo-png-transparent.png
:name: figure-open-access
:width: 200px

Open Access logo
```

There are multiple types of Open Access models that are used by journals.
However, the most common ones are gold, green and hybrid OA journals, while
some journals are hybrid. In all the cases the article is free to read but they
have the following differences.

**Gold OA**: The article is free to read, but the authors need to pay the
publisher, requiring an external funding. The 'Article Processing Charge' costs
an average of £2,000 and can reach £10,000.

**Green OA**: The author accepted manuscript can be hosted in some repository
(e.g. Pure is a repository of scholarly works for the Universtiy of Bristol).
The publisher retains the final version in their website. The article has a
CC-BY license and there is no embargo on its use. Additional considerations may
be required by the authors, for example the inclusion of a statement in the
publishers submission, like in the case of the University of Bristol
recomendation:

```
  "For the purpose of open access, the author(s) has applied a Creative Commons
  Attribution (CC BY) licence to any Author Accepted Manuscript version arising
  from this submission."
```

**Diamond OA**: These are crowd-funded by libraries and scholarly organisations
that pay for the processing charges. Then in the same manner as the **Green
OA**, the accepted manuscript can be hosted in a repository, while the final
copy is available in the publisher's website.

%Most of the journals that accept OA can be found in the website
%https://doaj.org/ .


## More about Open Research

Additional sources of information about open research can be found in the
following links:

- [Open Research at Bristol
  (UOB)](https://openresearchbristol.blogs.bristol.ac.uk/)
- [Open Access for journal articles (UOB)](https://www.bristol.ac.uk/staff/researchers/open-access/open-access-for-journal-articles/)
- [Research Data Evaluation Guide
  (UOB)](https://www.bristol.ac.uk/media-library/sites/library/documents/research-support/research-data/guidance/sharing/Research%20Data%20Evaluation%20Guide.pdf)
- [Managing research data (UOB)](https://www.bristol.ac.uk/staff/researchers/data/)
- [Dealing with sensitive data
  (UOB)](https://www.bristol.ac.uk/staff/researchers/data/dealing-with-sensitive-data/)


%# Old text to be removed
%
%Open research has multiple benefits as the work gets wider visibility,
%promoting new collaborations.
%
%The university, funders and publishers may have specific polices that are
%enforced in your publications.
%
%Major funders require information about a research data at application stage,
%and a 'Data Management Plan' (See [Writing a data management
%plan](https://www.bristol.ac.uk/staff/researchers/data/writing-a-data-management-plan/)).
%Usually covers
%
%- What type of data will be generated
%- How the data will be organised (e.g. naming conventions, version control,
%  ...)
%- How will the data be stored and for how long it will be maintained.
%- What data will **not** be shared, or any period of exclusive use.
%

# Knowledge graph references

## General overview

### Seminars
- CS 520 Knowledge graph seminar [Course page with video links](https://web.stanford.edu/class/cs520/)
- Knowledge Graphs to Fight Covid 19 Meetup [First meetup](https://www.youtube.com/watch?v=HkVfGikcjOo) [Second meetup](https://www.youtube.com/watch?v=1-_845yREno)
- Graphs4Good GraphHack. Community Effort to Build a Knowledge Graph to Fight COVID-19 [video](https://www.youtube.com/watch?v=yYVPvUZkvKQ)

### Talks
- Natural Language Search with Knowledge Graphs - Trey Grainger, Lucidworks [video](https://www.youtube.com/watch?v=5noi2VM9F-g)

### Reviews
- Shaoxiong Ji, Shirui Pan et al. A Survey on Knowledge Graphs: Representation, Acquisition and Applications (2020) [paper](https://arxiv.org/abs/2002.00388)
- Graph Technology Landscape 2020. Great overview of raising industry of graph technologies. [blog post](https://graphaware.com/graphaware/2020/02/17/graph-technology-landscape-2020.html)


## Knowledge graphs related to COVID-19

- COVID-19 Research Knowledge Graph. Knowledge graph build from CORD-19 dataset by JPL NASA group [github](https://github.com/nasa-jpl-cord-19/covid19-knowledge-graph)
- Covid-19-Community. This project is a community effort to build a Neo4j Knowledge Graph (KG) that links heterogenous data about COVID-19 to help fight this outbreak! It serves as a sandbox and incubator project and the best ideas will be incorporated into the Covid-19-Net KG. [github](https://github.com/covid-19-net/covid-19-community)
- COVID❋GRAPH. A voluntary initiative of graph enthusiasts and companies with the goal to build a knowledge graph with relevant information about the COVID-19 and the SARS-CoV-2 virus. [initiative page](https://covidgraph.org)
- CoViz. A tool buld by AI2 for exploring associations between concepts appearing in the COVID-19 Open Research Dataset. Searching for a term displays a network of top related terms mined from the corpus. [website](https://coviz.apps.allenai.org)
- Knowledge Graph of COVID-19 Literature. Knowledge graph build by IBM as a part of its Corpus Processing Service. This knowledge graph integrates COVID-19 data from various sources. [Search on graph, data and reports](https://ds-covid19.res.ibm.com/about)
- BioGrakn Knowledge Graph. Collection of knowledge graphs of biomedical data. Build as demonstation by GraknLabs [github](https://github.com/graknlabs/biograkn) [blog post](https://blog.grakn.ai/biograkn-accelerating-biomedical-knowledge-discovery-with-a-grakn-knowledge-graph-84706768d7d4) [BioGrakn COVID github](https://github.com/graknlabs/biograkn-covid)
- COVID-19 Knowledge Graph: a computable, multi-modal, cause-and-effect knowledge model of COVID-19 pathophysiology. [paper](https://doi.org/10.1101/2020.04.14.040667) [github](https://github.com/covid19kg/covid19kg)

## Annotated data related to Covid-19
- COVID-19 Annotated Data by SciBiteLabs. Annotated Data for the COVID-19 Open Research Dataset Challenge. [github](https://github.com/SciBiteLabs/CORD19)
- PubTator collections on COVID-19. Pubtator provides automated annotations of biomedical entities in scientific publications. NLM/NCBI BioNLP Research Group presents recent results of applying PubTator on the literature about COVID-19 and other coronaviruses. In particular, they feature results on two specific data collections: LitCovid and CORD-19. Pubtator annotations are provided for six entity types (gene/protein, drug/chemical, disease, cell type, species and genomic variants) in two formats (BioC JSON and BioC XML). [github](https://github.com/ncbi-nlp/PubTator-Covid19) [site](https://covid19.pubannotation.org)
- CORD-19-on-FHIR. A Linked Data version of the COVID-19 Open Research Dataset (CORD-19) data. [github](https://github.com/fhircat/CORD-19-on-FHIR)


## Ontologies and knowledge databases
- Unified Medical Language System. The UMLS integrates and distributes key terminology, classification and coding standards, and associated resources. The UMLS includes 3 knowledge sources: metathesaurus (terms and codes from many vocabularie), semantic network (semantic types and their relationships), SPECIALIST Lexicon and Lexical Tools: (A large syntactic lexicon of biomedical and general English and tools for normalizing strings, generating lexical variants, and creating indexes.)  [website](https://www.nlm.nih.gov/research/umls/index.html)
- STRING. Protein-Protein Interaction Networks. [website](https://string-db.org/)
- PharmaGKB. A pharmacogenomics knowledge resource that encompasses clinical information including clinical guidelines and drug labels, potentially clinically actionable gene-drug associations and genotype-phenotype relationships. [website](https://www.pharmgkb.org/)
- The Immune Epitope Database. IEDB catalogs experimental data on antibody and T cell epitopes studied in humans, non-human primates, and other animal species in the context of infectious disease, allergy, autoimmunity and transplantation. [website](http://www.iedb.org/)
- Evidence and Conclusion Ontology (ECO). An ontology of evidence types for supporting conclusions in scientific research [page on bioportal](https://bioportal.bioontology.org/ontologies/ECO/?p=summary)
- Library of ontologies provided by Bioportal [catalog](https://bioportal.bioontology.org/ontologies)

## Building knowledge graph, information extraction

### Language models
- BioBERT. BERT trained on Pubmed data by DMIS-lab team. [github](https://github.com/dmis-lab/biobert) [paper](http://doi.org/10.1093/bioinformatics/btz682) [implementations list on paperwithcode](https://www.paperswithcode.com/paper/biobert-a-pre-trained-biomedical-language)
- SciBERT. A BERT model for scientific text from AI2. [github](https://github.com/allenai/scibert) [paper](https://arxiv.org/abs/1903.10676)
- CovidBERT. Model CovidBERT trained by DeepSet on AllenAI's CORD19 Dataset of scientific articles about coronaviruses. Impemented as a part of Transformers library [github](https://github.com/huggingface/transformers/blob/master/model_cards/gsarti/covidbert-nli/)
- BlueBERT. A BERT model pre-trained on PubMed abstracts and clinical notes (MIMIC-III).  Provided by NLM/NCBI BioNLP Research Group [github](https://github.com/ncbi-nlp/bluebert) [paper](https://arxiv.org/abs/1906.05474)

### Open information extraction
- Open IE. System from the University of Washington (UW) and Indian Institute of Technology,Delhi (IIT Delhi). System is used by JPL NASA group [github](https://github.com/dair-iitd/OpenIE-standalone)
- Stanford Open IE. System from Stanford Unversity, part of Stanford CoreNLP. [project page](https://nlp.stanford.edu/software/openie.html)
- Graphene. System outperforms state-of-the-art Open IE systems in the construction of correct n-ary predicate-argument structures. [github](https://github.com/Lambda-3/Graphene) [paper](https://arxiv.org/pdf/1807.11276v1.pdf)
- Another unsupervised approach for open relation extraction task is self-organazing maps: Elena Manishina et al. Unsupervised relation extraction from scientific texts using a self-organizing maps [paper](https://oatao.univ-toulouse.fr/19106/)

### Named Entity Extraction
- BERN. BioBERT-based multi-type NER tool that also supports normalization of extracted entities. Build by DMIS-lab [github](https://github.com/dmis-lab/bern) [paper](https://ieeexplore.ieee.org/document/8730332)
- SciSpacy. A full pipeline and models for scientific/biomedical documents NER models. It includes biomedical NER models [website](https://spacy.io) [github](https://github.com/explosion/spaCy) [notebook with NER model](https://github.com/nasa-jpl-cord-19/Biomolecular-Named-Entities/blob/master/SciSpacy%20NER.ipynb)

### Weak supervision and relation extration
- Snorkel. The system for programmatically building and managing training data. It is build by team from Stanford unversity, many companies (Google, facebook etc.) are broadly using it [website](https://www.snorkel.org). 
- Short review of weak supervioson approached to relation extraction task: Alisa Smirnova and Philippe Cudré-Mauroux. 2018. Relation Extraction Using Distant Supervision: A Survey. [paper](https://dl.acm.org/doi/10.1145/3241741)
- A great example of using weak supervision (snorkel particularly) for biomedical information extraction (including numerical data): Kuleshov, V., Ding, J., Vo, C. et al. A machine-compiled database of genome-wide association studies, 2019 [paper](https://www.nature.com/articles/s41467-019-11026-x) [github](https://github.com/kuleshov/gwaskb)
- Another example of using weak supervision from BenevolentAI team, well-funded startup is building AI system for drug discovery: Julien Fauqueur et al. Constructing large scale biomedical knowledge bases from scratch with rapid annotation of interpretable patterns [paper](https://arxiv.org/abs/1907.01417)

### Relation extraction
- SpERT. BERT-based model with SOTA performance. [paper](http://arxiv.org/abs/1909.07755) [github](https://github.com/markus-eberts/spert)
- GraphREL. An end-to-end relation extraction model which uses graph convolutional networks (GCNs) to jointly learn named entities and relations. [paper](https://www.aclweb.org/anthology/P19-1136) [github](https://paperswithcode.com/paper/graphrel-modeling-text-as-relational-graphs)
- SemRep. It might be a good option if you want something can work work right out of the box.  It is the NLM triple extraction tool built on top of MetaMap. It comes with the usual UMLS license shenanigans and is not necessarily the latest and greatest, but works reasonably well IME. [webpage](https://semrep.nlm.nih.gov)
- OpenNRE. An open-source and extensible toolkit that provides a unified framework to implement relation extraction models (including few-shot and document-level models). [demosite](http://opennre.thunlp.ai/#/) [github](https://github.com/thunlp/OpenNRE) [paper](https://arxiv.org/abs/1909.13078)

### Relation descriptions, schema standarts
- MI2CAST.  Minimum Information about a Molecular Interaction CAusal STatement  This checklist defines both the required core information, as well as a comprehensive set of other contextual details valuable to the end user and relevant for reusing and reproducing causal molecular interaction information. [paper](https://www.preprints.org/manuscript/202004.0480/v1) [github](https://github.com/MI2CAST/MI2CAST)
- BEL. The Biological Expression Language captures causal, correlative, and associative relationships between biological entities along with the experimental/biological context in which they were observed as well as the provenance of the publication from which the relation was reported. [language tutorial](https://cthoyt.gitbook.io/bel/) [github](https://github.com/pybel/pybel)

### Other scientific document processing
- SciWING. A modern framework from WING-NUS to facilitate Scientific Document Processing. It is built on PyTorch and includes many pre-trained models for fundamental tasks in Scientific Document Processing: Logical Structure Recovery, Header Normalisation, Citation String Parsing, Citation Intent Classification, keyphrase extraction and others. [site](https://www.sciwing.io) [github](https://github.com/abhinavkashyap/sciwing) [paper](https://arxiv.org/abs/2004.03807)

### Evaluation
- BLUE. The Biomedical Language Understanding Evaluation benchmark consists of five different biomedicine text-mining tasks (including NER & RE) with ten corpora. Here, we rely on preexisting datasets because they have been widely used by the BioNLP community as shared tasks. [paper](https://arxiv.org/abs/1906.05474) [github](https://github.com/ncbi-nlp/BLUE_Benchmark)

### End-to-end systems
- INDRA (Integrated Network and Dynamical Reasoning Assembler). An an automated model assembly system, funded by DAPRA, draws on natural language processing systems and structured databases to collect mechanistic and causal assertions, represents them in a standardized form (INDRA Statements), and assembles them into various modeling formalisms including causal graphs and dynamical models. [website](http://www.indra.bio) [COVID19 model](https://emmaa.indra.bio/all_statements/covid19/#about)

## Graph analysis
- Neo4j Graph Data Science Library. [website](https://neo4j.com/graph-data-science-library/) [github](https://github.com/neo4j/graph-data-science)


## Graph embeddings
- Heterogeneous Graph Transformer. Graph neural network architecture from Microsoft and University of California. HGT can deal with large-scale heterogeneous and dynamic graphs [paper](https://arxiv.org/abs/2003.01332) [github](https://github.com/acbull/pyHGT)
- OpenKE. An open toolkit for knowledge embedding (OpenKE), which provides a unified framework and various fundamental models to embed knowledge graphs into a continuous low-dimensional space. [paper](https://www.aclweb.org/anthology/D18-2024/) [github](https://github.com/thunlp/OpenKE)
- BioNEV. This work aims to systematically evaluate recent advanced graph embedding techniques on biomedical tasks. Authors compile 5 benchmark datasets for 4 biomedical prediction tasks (see paper for details) and use them to evaluate 11 representative graph embedding methods [paper](https://arxiv.org/pdf/1906.05017.pdf) [github](https://github.com/xiangyue9607/BioNEV)
- PyTorch-BigGraph. An embedding system from Facebook that incorporates several modifications to traditional multi-relation embedding systems that allow it to scale to graphs with billions of nodes and trillions of edges. [paper](http://arxiv.org/abs/1903.12287) [github](https://github.com/facebookresearch/PyTorch-BigGraph)
- BioKEEN. A package for training and evaluating biological knowledge graph embeddings built on PyKEEN. [github](https://github.com/smartdataanalytics/biokeen) ([parent package - PyKEEN](https://github.com/smartdataanalytics/pykeen))

# 4-week project plan

**Project:** Are existing cell-type annotations consistent and reliable enough to be used as ground truth for training future models?
**Scope (agreed with Arianna, 20 Nov):** human blood / PBMC, data from CELLxGENE Census (other sources allowed if useful). No specific model in mind; the question is about the labels themselves.
**Timeline:** Fri 20 Nov → Thu 17 Dec 2026. Presentation date, format and length: *ask the professor* (see `notes/questions.md`).

Tick the boxes as you go (edit this file on GitHub or locally and commit). Each week ends with a short update email to Arianna.

## The four questions

| # | Question | Measured how | Notebook |
|---|----------|--------------|----------|
| 1 | **Granularity:** how specific are each study's labels? | Number of labels and Cell Ontology depth per dataset | `02` |
| 2 | **Biological identity:** do labelled cells express the right marker genes? | CellMarker 2.0 marker scores per labelled population | `04` |
| 3 | **Cross-study agreement:** do studies call the same cells the same thing? | Train on study A, predict study B; exact / compatible / conflict. I i dont find datasets I should check the pretrained models themselves: GeneFormer OR scGPT | `05` |
| 4 | **Explanation:** are disagreements due to annotation strategy or ontology usage? | Annotation strategy table + author labels vs CL terms | `06` |

## Overview

| Week | Dates | Goal | Checkpoint |
|------|-------|------|------------|
| 1 | Fri 20 – Thu 26 Nov | Basics, papers, tools | You can explain the pipeline and ran notebook 00 |
| 2 | Fri 27 Nov – Thu 3 Dec | Data, ontology, annotation strategies | Datasets chosen, Finding 1 draft, strategy table |
| 3 | Fri 4 – Thu 10 Dec | Findings 2, 3, 4 | One draft figure per finding |
| 4 | Fri 11 – Thu 17 Dec | Final figures, slides, rehearsal | Talk rehearsed twice, repo tagged |

If you fall behind: in Week 3, Findings 1, 2 and 4 (strategy part) are enough for a solid talk; present Finding 3 as a pilot. Never cut rehearsal days.

---

## Week 1 · Fri 20 – Thu 26 Nov · Foundations

**Fri 20 Nov: set up**
- [x] Clone this repo: `git clone https://github.com/juliavikr/celltype-annotation-reliability.git`
- [x] Install Miniconda, then `conda env create -f environment.yml` and `conda activate celltype-rel`
- [x] Check: `pytest` passes (3 tests), `jupyter lab` opens
- [x] Email the professor about presentation date, format, length, audience

**Sat 21 – Sun 22 Nov: biology basics + Luecken & Theis (2019)**
- [x] Watch a short intro to DNA → RNA → protein and to single-cell RNA-seq (search "10x Genomics single cell explained")
- [x] Read chapters 1–2 of the free book *Single-cell best practices* (sc-best-practices.org), the updated version of the Luecken paper
- [x] Luecken: first pass (abstract, figures, headings), then the pre-processing section and the clustering / cluster annotation section
- [x] Fill in `notes/glossary.md` and `notes/papers/luecken.md`

**Mon 23 Nov: hands-on**
- [ ] Notebook `00_learning_pbmc3k`: run the scanpy PBMC 3k tutorial, explaining each step in your own words
- [ ] Label the clusters by hand using marker genes

**Tue 24 Nov: Pasquini et al. (2021)**
- [ ] Read section 2: marker-database methods, correlation with a reference, supervised classifiers
- [ ] In `notes/papers/pasquini.md`, make a table: method family · input needed · example tool · weak spot
- [ ] Note the cell *type* vs cell *state* distinction, a source of disagreement

**Wed 25 Nov: Hu et al. (2023), CellMarker 2.0**
- [ ] Read the abstract, database construction and statistics; skim the web tools
- [ ] On the website, look up B cell, CD14+ monocyte and NK cell: how many markers each? Do sources agree?
- [ ] Download the human marker table to `data/raw/cellmarker2_human.xlsx`
- [ ] Fill in `notes/papers/hu.md`

**Thu 26 Nov: ontologies + manual vs automated**
- [ ] Browse the Cell Ontology on EBI OLS: B cell → parents up to "cell", children down
- [ ] Read the README of `chanzuckerberg/cellxgene-ontology-guide`; try `src/celltype_rel/ontology.py` in a notebook
- [ ] In notebook 00, run CellTypist and compare with your manual labels
- [ ] Weekly update to Arianna (done · learned · unclear · next)

## Week 2 · Fri 27 Nov – Thu 3 Dec · Data, ontology, strategies

**Fri 27 Nov: meet CELLxGENE**
- [ ] On cellxgene.cziscience.com open 2–3 blood datasets in the Explorer; colour by `cell_type`; also look at the authors' own label columns
- [ ] Read the CELLxGENE schema page on `cell_type_ontology_term_id`, `assay`, `disease`, `is_primary_data`

**Sat 28 Nov: metadata (notebook 01)**
- [ ] Pull the blood metadata from Census; record the Census version in `notes/log.md`
- [ ] Choose 4–6 datasets from different studies (10x, >20,000 cells); justify in `notes/datasets.md`

**Sun 29 – Mon 30 Nov: Finding 1 (notebook 02)**
- [ ] Labels per dataset, ontology depth, heatmap of which dataset uses which label
- [ ] Group labels by lineage (T, B, NK, myeloid); draw the T-cell sub-tree marking each dataset's terms

**Tue 1 Dec: expression data (notebook 03)**
- [ ] Download the chosen datasets via Census; also the original files (with author labels) if size allows
- [ ] Quick UMAP per dataset coloured by `cell_type`

**All week, ~1 h a day: annotation strategy table**
- [ ] For each chosen dataset, read the paper's methods section: how were cells annotated?
- [ ] Fill `data/processed/annotation_strategies.csv` (template in `notes/annotation_strategies_template.csv`)

**Wed 2 – Thu 3 Dec: markers + checkpoint**
- [ ] Prepare the CellMarker blood marker list mapped to CL IDs (notebook 04, first cells)
- [ ] Write `notes/findings.md` section 1
- [ ] Weekly update to Arianna with the Finding 1 heatmap and the strategy table

## Week 3 · Fri 4 – Thu 10 Dec · Findings 2, 3, 4

**Fri 4 – Sat 5 Dec: Finding 2, biological identity (notebook 04)**
- [ ] Marker scores per cell; % of each labelled population whose own markers score highest
- [ ] Look closely at unsupported populations: doublets? wrong label? marker missing?
- [ ] Figure: dot plot of canonical markers vs labels, one panel per dataset

**Sun 6 – Tue 8 Dec: Finding 3, cross-study agreement (notebook 05)**
- [ ] Train on A, predict B, for every pair
- [ ] Classify each prediction as exact / compatible / conflict with `relation()`
- [ ] Figure: dataset × dataset heatmap + stacked bar of the three categories

**Wed 9 Dec: Finding 4, explanation (notebook 06)**
- [ ] Do same-strategy pairs agree more than mixed pairs?
- [ ] Author label vs CL term: how often did mapping make labels broader or change them?
- [ ] 2–3 worked examples of specific populations

**Thu 10 Dec: synthesis**
- [ ] One paragraph + one number per finding in `notes/findings.md`
- [ ] Main message in one sentence
- [ ] Weekly update to Arianna with draft figures; ask which matter most for the talk

## Week 4 · Fri 11 – Thu 17 Dec · Results and presentation

**Fri 11 Dec: freeze the analysis**
- [ ] Re-run all notebooks top to bottom from a fresh kernel
- [ ] Final figures to `figures/` (PNG + PDF, big fonts, the takeaway as the title)
- [ ] Fill in the README results section

**Sat 12 – Sun 13 Dec: slides (adjust to the professor's format)**
1. Title
2. Why labels matter: models learn from them as ground truth
3. How cells are annotated (Luecken, Pasquini)
4. Marker genes and CellMarker 2.0
5. Cell Ontology and how CELLxGENE standardizes labels
6. Sources of variability
7. Data: blood datasets and their annotation strategies
8. Finding 1: granularity
9. Finding 2: biological identity
10. Finding 3: cross-study agreement
11. Finding 4: what explains the disagreements
12. Verdict: usable as ground truth, and under which conditions?
13. Limitations and next steps
14. Thanks + repo link

**Mon 14 Dec:** send slides to Arianna for comments; rehearse alone once with a timer
**Tue 15 – Wed 16 Dec:** apply comments; rehearse twice (once with a listener); prepare answers to likely questions (why blood? why CellMarker? error or biology?)
**Thu 17 Dec:** `git tag v1.0-presentation && git push --tags`

---

## Daily habits
- Commit at the end of each working day: `git add -A && git commit -m "what changed" && git push`
- One line per day in `notes/log.md`: did · learned · stuck on
- Stuck for more than 45 min → write down the question and what you tried, then ask

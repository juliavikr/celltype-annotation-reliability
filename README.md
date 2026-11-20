# How reliable are cell-type annotations?

Public single-cell RNA-seq datasets label every cell with a cell type ("B cell", "CD14-positive monocyte", …).
This project asks whether those labels are **consistent and reliable enough to be used as ground truth** for training future models.

**Scope:** human blood / PBMC · data from [CELLxGENE Census](https://chanzuckerberg.github.io/cellxgene-census/) · labels compared through the [Cell Ontology](https://github.com/chanzuckerberg/cellxgene-ontology-guide) · marker genes from CellMarker 2.0.

## Questions
1. **Granularity:** how specific are different studies' labels for the same cell populations?
2. **Biological identity:** do cells labelled as type X express X's known marker genes?
3. **Cross-study agreement:** does a classifier trained on one study reproduce another study's labels? Are disagreements near misses (parent/child terms) or real conflicts?
4. **Explanation:** can disagreements be explained by differences in annotation strategy or in ontology usage?

The day-by-day plan is in [PLAN.md](PLAN.md).

## Repository layout
```
PLAN.md               4-week plan with checklists
notebooks/            analysis, run in numeric order
src/celltype_rel/     reusable helpers (Cell Ontology lookups, …)
tests/                small checks for the helpers (run: pytest)
notes/                glossary, paper notes, daily log, questions, findings
figures/              final figures
results/              small result tables
data/                 not tracked by git; see data/README.md
```

## Setup
```bash
git clone https://github.com/juliavikr/celltype-annotation-reliability.git
cd celltype-annotation-reliability
conda env create -f environment.yml
conda activate celltype-rel
pytest            # should report 3 passed
jupyter lab
```

## Notebooks
| # | Notebook | Purpose |
|---|----------|---------|
| 00 | `00_learning_pbmc3k` | Learning: the standard scanpy workflow and manual annotation |
| 01 | `01_census_metadata` | Pull blood cell metadata from Census; choose datasets |
| 02 | `02_ontology_granularity` | Finding 1: label granularity |
| 03 | `03_download_expression` | Expression data (and original author labels) |
| 04 | `04_marker_support` | Finding 2: marker support for labels |
| 05 | `05_label_transfer` | Finding 3: cross-study agreement |
| 06 | `06_explain_discrepancies` | Finding 4: annotation strategy and ontology usage |

## Results
_In progress._

## References
- Luecken MD, Theis FJ (2019). Current best practices in single-cell RNA-seq analysis: a tutorial. *Mol Syst Biol* 15:e8746.
- Pasquini G, Rojo Arias JE, Schäfer P, Busskamp V (2021). Automated methods for cell type annotation on scRNA-seq data. *Comput Struct Biotechnol J* 19:961–969.
- Hu C, Li T, Xu Y, et al. (2023). CellMarker 2.0. *Nucleic Acids Res* 51:D870–D876.
- CZ CELLxGENE: [cellxgene-ontology-guide](https://github.com/chanzuckerberg/cellxgene-ontology-guide), [Census](https://chanzuckerberg.github.io/cellxgene-census/)

*Supervision (scientific): Arianna. Student: Julia.*

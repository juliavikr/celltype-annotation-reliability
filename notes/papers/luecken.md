# Luecken & Theis (2019): Current best practices in scRNA-seq analysis

## Main point (2–3 sentences, own words)
A scRNA-seq is based on choises you do for the analysis: quality control, normalisation, correction, gene selection, dimensionality reduction, clustering and annotation. Each step has several different methods that will effect the result/outcome. This paper proposed the best methd for each step based on studies that compared the methods. It also makes clear that cell-type labels come at the end of this chain, from a partly subjective process of clustering cells and naming the clusters using marker genes.
## Key ideas
- Lables arent meadured, they are assigned. Cells are grouped into clusters based by similar gene expression. A person or an automated tool labels these clusters based on the marker genes (a gene that is expressed at a much higher level in one spesific cluster of cells compared to all other cells)
- The number of clusters is a choice. Level of detail in the lable depens on the analyst. Ex. Whether you get "T cells" or "CD4+ and CD8+ T cells"
- A cluster is only valid if it can be explained biologically. Clustering algorithms produce groups even from random data, so it has to make sense biologically.
- Use the ranking of marker genes and not p-values as evidence.
- A gene is a marker only relative to other cells in the dataset, so the same cell can get different marker genes in different stuides.
- Annotation strategies differs.
- Use raw or normalized counts for testing gene expression and reduced data (PCA) for clustering and maps.

## What it means for my project
- The study explains why granularity varies between studies. The clustering resulation and the annotators goal decide how spesific each label are. (for example "T cell" vs "CD8-positive, alpha-beta memory T cell"). I should explain difference in detail not just errors.
- I can check labels the way the paper annotates clusters, by testing whether cells labelled X express X's known markers (from CellMarker 2.0)

- For "ground truth": the paper supports treating labels as expert estimates rather than true facts. Their reliability depends on how they were made, which supports the motivation for my project.

- Limitation: the paper is from 2019, before CELLxGENE Census and today's standard Cell Ontology labelling. Some tools have been replaced; for example, Leiden is now commonly used instead of Louvain. An updated version is Heumos et al. 2023, Nature Reviews Genetics.
- The Leiden algorithm is an upgraded method for grouping similar cells together, fixing a major bug in the older Louvain method where unrelated cells could accidentally get stuck in the same group.

## Questions
- 

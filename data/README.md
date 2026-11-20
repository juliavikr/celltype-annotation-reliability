# data/

Not tracked by git. Recreate it by running the notebooks in order.

| Path | Made by | Content |
|------|---------|---------|
| `raw/cellmarker2_human.xlsx` | manual download | CellMarker 2.0 human marker table (http://bio-bigdata.hrbmu.edu.cn/CellMarker → Download) |
| `processed/blood_obs.parquet` | `01_census_metadata` | Cell metadata for healthy human blood, CELLxGENE Census |
| `processed/<dataset_id>.h5ad` | `03_download_expression` | Expression for the chosen datasets |
| `processed/markers_blood.csv` | `04_marker_support` | Markers mapped to Cell Ontology IDs |
| `processed/annotation_strategies.csv` | by hand (Week 2) | How each study annotated its cells |

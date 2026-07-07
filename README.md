# Open Infra GIS Tools

**Open Infra GIS Tools** is an early-stage open-source toolkit for practical, production-oriented GIS workflows used in infrastructure-scale geospatial data processing, environmental monitoring, spatial data quality control, and public-service use cases.

The project focuses on small, reusable, non-sensitive tools that GIS analysts and infrastructure data teams can adapt without starting from scratch.

## Why this project exists

GIS is not only a technical tool. It helps people understand where risks are, how infrastructure may be affected, and where preventive action should be prioritized.

Infrastructure, utility, municipal, and public-data teams often need to combine desktop GIS tools, spatial databases, OGC services, public datasets, and field-oriented workflows. In practice, many of these workflows remain scattered across local scripts, manual QGIS steps, SQL snippets, or undocumented GeoServer configurations.

This repository aims to turn recurring GIS problems into clean, reusable, openly licensed examples.

## Main focus areas

- Oracle Spatial / SDO_GEOMETRY helper SQL
- QGIS Python automation scripts
- GeoServer and OGC service publishing notes
- WMS/WFS service checks and layer inventory tools
- Public geospatial data workflows
- NASA Black Marble / VIIRS night-time lights analysis
- Spatial quality control and CRS/SRID consistency checks
- Infrastructure exposure, proximity, and preventive planning workflows

## Tool catalog

The initial toolkit is organized around 20 practical GIS utilities and workflow documents:

| # | Tool / workflow | Area | Status |
|---|---|---|---|
| 1 | Oracle Spatial Geometry Validation SQL | Oracle Spatial | Starter available |
| 2 | Oracle Spatial Metadata & Spatial Index Checker | Oracle Spatial | Starter available |
| 3 | Oracle Spatial SRID and Geometry Type Audit | Oracle Spatial | Starter available |
| 4 | Oracle Spatial Length / Area Summary Reporter | Oracle Spatial | Starter available |
| 5 | Oracle Spatial Duplicate Geometry Detector | Oracle Spatial | Starter available |
| 6 | QGIS KML/KMZ Batch Merge Tool | QGIS | Starter available |
| 7 | QGIS Vector Folder Inventory Reporter | QGIS | Starter available |
| 8 | QGIS Project CRS Consistency Checker | QGIS | Starter available |
| 9 | QGIS Geometry Validation and Error Export Tool | QGIS | Starter available |
| 10 | QGIS Export Layers to Single GeoPackage Tool | QGIS | Starter available |
| 11 | QGIS Clip Dataset by Boundary Tool | QGIS | Starter available |
| 12 | QGIS Area and Length Summary Tool | QGIS | Starter available |
| 13 | QGIS Nearest Asset / Proximity Analysis Tool | QGIS | Starter available |
| 14 | QGIS Batch Style Apply Tool | QGIS | Starter available |
| 15 | QGIS Layer Field / Attribute Audit Tool | QGIS | Starter available |
| 16 | WMS/WFS Service Health Checker | OGC Services | Starter available |
| 17 | WFS Layer Downloader to GeoJSON | OGC Services | Starter available |
| 18 | GeoServer Publishing Checklist | GeoServer | Documentation available |
| 19 | GeoServer GetCapabilities Layer Inventory Tool | OGC Services | Starter available |
| 20 | NASA Black Marble / VIIRS Night-Time Lights Workflow | Public Data | Documentation available |

See [`docs/tool-catalog.md`](docs/tool-catalog.md) for details.

## Repository structure

```text
docs/
  geoserver/
  public-data/
  roadmap.md
  tool-catalog.md
examples/
  public-geospatial-data/
scripts/
  qgis/
  ogc/
sql/
  oracle-spatial/
.github/
  ISSUE_TEMPLATE/
```

## Data safety

This project must only contain generic, public, placeholder, or non-sensitive examples.

Do not add:

- Corporate or private datasets
- Internal database schemas or table names
- Credentials, tokens, IP addresses, or internal server URLs
- Operational infrastructure data
- Personal data
- Restricted service endpoints

Use placeholders such as `YOUR_TABLE`, `YOUR_GEOMETRY_COLUMN`, `YOUR_WMS_URL`, and `YOUR_OUTPUT_FOLDER`.

## Project status

This is an early-stage open-source project. The current goal is to establish a useful starter toolkit and documentation structure. The tools are intentionally small and practical so they can be reviewed, improved, and adapted by GIS professionals.

## License

This project is licensed under the MIT License.

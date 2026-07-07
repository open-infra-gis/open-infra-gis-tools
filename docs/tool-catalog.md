# Tool Catalog

This catalog defines the initial 20-tool package for Open Infra GIS Tools.

## Oracle Spatial / SQL

### 1. Oracle Spatial Geometry Validation SQL
Generic validation examples for SDO_GEOMETRY columns.

### 2. Oracle Spatial Metadata & Spatial Index Checker
Checks geometry metadata and spatial index presence.

### 3. Oracle Spatial SRID and Geometry Type Audit
Audits SRID and SDO_GTYPE distribution.

### 4. Oracle Spatial Length / Area Summary Reporter
Produces basic length and area summaries.

### 5. Oracle Spatial Duplicate Geometry Detector
Finds potential duplicate geometries using geometry WKT/hash patterns.

## QGIS Automation

### 6. QGIS KML/KMZ Batch Merge Tool
Merges multiple KML/KMZ files into GeoPackage outputs grouped by geometry type.

### 7. QGIS Vector Folder Inventory Reporter
Scans vector files and creates an inventory CSV.

### 8. QGIS Project CRS Consistency Checker
Reports CRS mismatches in the current QGIS project.

### 9. QGIS Geometry Validation and Error Export Tool
Finds invalid geometries and exports error features.

### 10. QGIS Export Layers to Single GeoPackage Tool
Exports project layers into one GeoPackage.

### 11. QGIS Clip Dataset by Boundary Tool
Clips selected input data by a boundary layer.

### 12. QGIS Area and Length Summary Tool
Creates area and length summaries for vector layers.

### 13. QGIS Nearest Asset / Proximity Analysis Tool
Calculates nearest-feature distances for proximity analysis.

### 14. QGIS Batch Style Apply Tool
Applies QML styles to matching layers.

### 15. QGIS Layer Field / Attribute Audit Tool
Audits field names, types, and basic attribute completeness.

## OGC Services / GeoServer

### 16. WMS/WFS Service Health Checker
Checks OGC GetCapabilities response status and response time.

### 17. WFS Layer Downloader to GeoJSON
Downloads WFS features to GeoJSON using generic service parameters.

### 18. GeoServer Publishing Checklist
A practical publishing checklist for production-aware GeoServer workflows.

### 19. GeoServer GetCapabilities Layer Inventory Tool
Parses GetCapabilities XML and exports layer names/titles.

## Public Data / Risk & Resilience

### 20. NASA Black Marble / VIIRS Night-Time Lights Workflow
Uses night-time lights as supporting geospatial context for environmental monitoring, disaster impact assessment, and infrastructure resilience.

## Safety note

All examples must remain generic and non-sensitive. Do not add internal service URLs, private datasets, credentials, operational infrastructure data, or personal data.

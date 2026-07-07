# Roadmap

Open Infra GIS Tools is an early-stage open-source GIS toolkit focused on infrastructure-scale geospatial workflows, environmental monitoring, spatial data quality, and public-service use cases.

The goal of this roadmap is to organize practical, reusable, and non-sensitive GIS workflows that can help infrastructure teams, GIS analysts, municipalities, utilities, and public-data users turn complex spatial datasets into actionable information.

## Initial priorities

- Add Oracle Spatial / SDO_GEOMETRY helper SQL examples
- Add QGIS automation scripts for WMS/WFS processing
- Document GeoServer + Oracle Spatial production setup
- Create reusable examples for environmental monitoring and infrastructure exposure analysis
- Add NASA Black Marble / VIIRS night-time lights analysis workflows
- Improve documentation for GIS analysts and public-infrastructure teams

## Guiding principles

- Use non-sensitive and reusable examples
- Focus on practical production GIS workflows
- Support open geospatial tools and public datasets
- Help teams turn complex spatial data into actionable information
- Make infrastructure and environmental GIS workflows easier to reproduce, document, and share
- Keep examples understandable for both developers and GIS professionals
- Avoid treating proxy indicators as direct proof; use them as supporting geospatial context

## Planned modules

### Oracle Spatial

Reusable SQL examples for infrastructure-scale Oracle Spatial workflows.

Planned examples include:

- SDO_GEOMETRY validation
- Geometry repair patterns
- Coordinate transformation
- Spatial joins
- Length and area calculations
- Spatial index checks
- Infrastructure reporting examples
- Data quality control queries
- Large dataset performance notes

### QGIS automation

Python and QGIS workflow examples for public geospatial data processing and spatial quality control.

Planned examples include:

- WMS/WFS extraction
- Clipping by administrative boundaries
- Raster/vector processing
- Layer styling
- Geometry checks
- Batch processing workflows
- Public dataset preparation
- Environmental monitoring map outputs

### GeoServer

Practical documentation for publishing and managing spatial data services in production-oriented GIS environments.

Planned topics include:

- Oracle Spatial datastore configuration
- WMS/WFS publishing
- Layer styling
- Coordinate reference system notes
- Performance considerations
- Common troubleshooting cases
- Large infrastructure dataset publishing notes
- Service organization and documentation practices

### Environmental and infrastructure risk workflows

Reusable GIS examples for environmental monitoring, infrastructure exposure, and preventive planning.

Planned examples include:

- Wildfire exposure context
- Land-cover analysis
- Elevation-based spatial context
- Asset proximity checks
- Preventive maintenance planning
- Natural event monitoring support
- Infrastructure exposure analysis
- Spatial indicators for risk-aware decision-making

### NASA Black Marble / VIIRS night-time lights

Practical workflows using NASA Black Marble / VIIRS night-time lights data as a supporting geospatial indicator for infrastructure resilience, environmental monitoring, and disaster impact context.

Potential use cases include:

- Monitoring changes in night-time lights before and after natural events
- Supporting disaster impact assessment and recovery monitoring
- Understanding urban activity and settlement patterns
- Comparing night-time light intensity with infrastructure or service areas
- Identifying areas where significant light changes may require further operational review
- Creating QGIS examples for clipping, styling, temporal comparison, and spatial quality control

Night-time lights should not be treated as direct proof of outages or service conditions. The purpose is to use them as supporting spatial context for risk awareness, infrastructure resilience, environmental monitoring, and preventive planning.

## Current repository structure

```text
docs/
  roadmap.md
sql/
  oracle-spatial/
scripts/
  qgis/
  wms-wfs/
examples/
  public-geospatial-data/
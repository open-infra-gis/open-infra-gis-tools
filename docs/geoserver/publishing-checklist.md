# GeoServer Publishing Checklist

This checklist helps GIS teams publish spatial layers through GeoServer in a more consistent and production-aware way.

## Data readiness

- Geometry column exists and is valid
- Feature count is known
- CRS/SRID is known
- Spatial index exists where applicable
- Sensitive attributes are removed
- Layer has been tested in desktop GIS

## Oracle Spatial checks

- Metadata exists in `USER_SDO_GEOM_METADATA`
- SRID matches expected coordinate system
- Geometry type is consistent
- Spatial index exists and is valid
- Invalid geometries are reviewed before publishing

## Datastore setup

- Use a clear datastore name
- Use read-only database users where possible
- Avoid exposing credentials in documentation
- Separate test and production configurations
- Test connection before publishing

## Layer publishing

- Confirm layer name, title, and abstract
- Set native and declared CRS correctly
- Compute bounding boxes
- Test WMS preview
- Test WFS output if enabled
- Apply readable style
- Review exposed attributes

## Performance

- Confirm spatial indexes
- Limit unnecessary attributes
- Use bounding box filtering
- Use scale-dependent styles for heavy layers
- Consider tile caching for WMS

## Security

- Remove sensitive attributes
- Use layer/workspace permissions
- Avoid publishing internal URLs in public examples
- Review WFS access carefully

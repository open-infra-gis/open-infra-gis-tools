# Data Safety Guidelines

Open Infra GIS Tools must remain safe for open-source use.

## Do not publish

- Corporate datasets
- Private infrastructure data
- Personal data
- Internal server URLs
- IP addresses
- Credentials or tokens
- Database connection strings
- Internal schema, table, or column names
- Restricted service endpoints
- Operational logs

## Use instead

- Public datasets
- Synthetic examples
- Placeholder names
- Generic local file paths
- Public OGC service examples
- Documentation that describes the workflow without exposing sensitive sources

## Example placeholders

```text
YOUR_SCHEMA
YOUR_TABLE
YOUR_ID_COLUMN
YOUR_GEOMETRY_COLUMN
YOUR_WMS_URL
YOUR_WFS_URL
YOUR_INPUT_FOLDER
YOUR_OUTPUT_FOLDER
```

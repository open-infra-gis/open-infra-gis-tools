/*
  Open Infra GIS Tools
  File: sql/oracle-spatial/validate_geometry.sql

  Purpose:
  Practical Oracle Spatial / SDO_GEOMETRY validation examples for
  infrastructure-scale GIS datasets.

  Notes:
  - Replace YOUR_SCHEMA, YOUR_TABLE, ID_COLUMN, and GEOM_COLUMN
    with your own schema, table, id column, and geometry column names.
  - These examples use non-sensitive placeholder names.
  - Adjust tolerance according to your data accuracy and coordinate system.
*/

--------------------------------------------------------------------------------
-- 1. Basic geometry validation
--------------------------------------------------------------------------------

SELECT
    t.ID_COLUMN,
    SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) AS validation_result
FROM YOUR_SCHEMA.YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL;


--------------------------------------------------------------------------------
-- 2. List invalid geometries only
--------------------------------------------------------------------------------

SELECT
    t.ID_COLUMN,
    SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) AS validation_error
FROM YOUR_SCHEMA.YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL
  AND SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) <> 'TRUE';


--------------------------------------------------------------------------------
-- 3. Count valid, invalid, and null geometries
--------------------------------------------------------------------------------

SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN t.GEOM_COLUMN IS NULL THEN 1 ELSE 0 END) AS null_geometry_count,
    SUM(
        CASE
            WHEN t.GEOM_COLUMN IS NOT NULL
             AND SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) = 'TRUE'
            THEN 1 ELSE 0
        END
    ) AS valid_geometry_count,
    SUM(
        CASE
            WHEN t.GEOM_COLUMN IS NOT NULL
             AND SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) <> 'TRUE'
            THEN 1 ELSE 0
        END
    ) AS invalid_geometry_count
FROM YOUR_SCHEMA.YOUR_TABLE t;


--------------------------------------------------------------------------------
-- 4. Check geometry type distribution
-- Common SDO_GTYPE examples:
-- 2001: 2D Point
-- 2002: 2D Line
-- 2003: 2D Polygon
-- 3001: 3D Point
-- 3002: 3D Line
-- 3003: 3D Polygon
--------------------------------------------------------------------------------

SELECT
    t.GEOM_COLUMN.SDO_GTYPE AS sdo_gtype,
    COUNT(*) AS feature_count
FROM YOUR_SCHEMA.YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL
GROUP BY t.GEOM_COLUMN.SDO_GTYPE
ORDER BY t.GEOM_COLUMN.SDO_GTYPE;


--------------------------------------------------------------------------------
-- 5. Check SRID distribution
-- Example common SRIDs:
-- 4326 / 8307: geographic coordinate systems
-- 3857: Web Mercator
--------------------------------------------------------------------------------

SELECT
    t.GEOM_COLUMN.SDO_SRID AS srid,
    COUNT(*) AS feature_count
FROM YOUR_SCHEMA.YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL
GROUP BY t.GEOM_COLUMN.SDO_SRID
ORDER BY t.GEOM_COLUMN.SDO_SRID;


--------------------------------------------------------------------------------
-- 6. Find geometries with unexpected SRID
-- Replace 8307 with the expected SRID for your dataset.
--------------------------------------------------------------------------------

SELECT
    t.ID_COLUMN,
    t.GEOM_COLUMN.SDO_SRID AS srid
FROM YOUR_SCHEMA.YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL
  AND NVL(t.GEOM_COLUMN.SDO_SRID, -1) <> 8307;


--------------------------------------------------------------------------------
-- 7. Check metadata registration
-- Run this from the schema that owns the table.
--------------------------------------------------------------------------------

SELECT
    table_name,
    column_name,
    srid,
    diminfo
FROM USER_SDO_GEOM_METADATA
WHERE table_name = UPPER('YOUR_TABLE');


--------------------------------------------------------------------------------
-- 8. Check spatial index presence
-- Run this from the schema that owns the table.
--------------------------------------------------------------------------------

SELECT
    i.index_name,
    i.index_type,
    i.status,
    c.column_name
FROM USER_INDEXES i
JOIN USER_IND_COLUMNS c
    ON i.index_name = c.index_name
WHERE i.table_name = UPPER('YOUR_TABLE')
  AND c.column_name = UPPER('GEOM_COLUMN')
ORDER BY i.index_name;


--------------------------------------------------------------------------------
-- 9. Example geometry repair pattern
-- Important:
-- - Always test repair logic on a copy or staging table first.
-- - Do not update production data without backup and validation.
--------------------------------------------------------------------------------

/*
UPDATE YOUR_SCHEMA.YOUR_TABLE t
SET t.GEOM_COLUMN = SDO_UTIL.RECTIFY_GEOMETRY(t.GEOM_COLUMN, 0.005)
WHERE t.GEOM_COLUMN IS NOT NULL
  AND SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) <> 'TRUE';

COMMIT;
*/


--------------------------------------------------------------------------------
-- 10. Re-check invalid geometries after repair
--------------------------------------------------------------------------------

SELECT
    t.ID_COLUMN,
    SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) AS validation_error
FROM YOUR_SCHEMA.YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL
  AND SDO_GEOM.VALIDATE_GEOMETRY_WITH_CONTEXT(t.GEOM_COLUMN, 0.005) <> 'TRUE';

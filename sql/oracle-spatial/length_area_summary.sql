/*
  Generic length / area summary examples.
  Replace YOUR_TABLE, GEOM_COLUMN, and tolerance.
*/

SELECT
    COUNT(*) AS feature_count,
    SUM(SDO_GEOM.SDO_LENGTH(t.GEOM_COLUMN, 0.005)) AS total_length
FROM YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL;

SELECT
    COUNT(*) AS feature_count,
    SUM(SDO_GEOM.SDO_AREA(t.GEOM_COLUMN, 0.005)) AS total_area
FROM YOUR_TABLE t
WHERE t.GEOM_COLUMN IS NOT NULL;

/*
  Generic Oracle Spatial metadata and spatial index checks.
  Replace YOUR_TABLE and GEOM_COLUMN with your own placeholders.
*/

SELECT table_name, column_name, srid, diminfo
FROM USER_SDO_GEOM_METADATA
WHERE table_name = UPPER('YOUR_TABLE');

SELECT i.index_name, i.index_type, i.status, c.table_name, c.column_name
FROM USER_INDEXES i
JOIN USER_IND_COLUMNS c ON i.index_name = c.index_name
WHERE c.table_name = UPPER('YOUR_TABLE')
  AND c.column_name = UPPER('GEOM_COLUMN')
ORDER BY i.index_name;

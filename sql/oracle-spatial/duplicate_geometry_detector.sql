/*
  Generic duplicate geometry detector pattern.
  Replace YOUR_TABLE, ID_COLUMN, and GEOM_COLUMN.
  Test on a copy before using with large production datasets.
*/

WITH geom_hashes AS (
    SELECT
        t.ID_COLUMN,
        STANDARD_HASH(SDO_UTIL.TO_WKTGEOMETRY(t.GEOM_COLUMN), 'SHA256') AS geom_hash
    FROM YOUR_TABLE t
    WHERE t.GEOM_COLUMN IS NOT NULL
)
SELECT geom_hash, COUNT(*) AS duplicate_count
FROM geom_hashes
GROUP BY geom_hash
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

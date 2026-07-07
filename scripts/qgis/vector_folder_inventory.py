"""
Scan a folder for vector datasets and create a CSV inventory report.
Run inside QGIS Python Console.
"""

from pathlib import Path
import csv
from qgis.core import QgsVectorLayer, QgsWkbTypes

INPUT_FOLDER = r"C:\GIS\vector_data"
OUTPUT_CSV = r"C:\GIS\vector_inventory.csv"
RECURSIVE = True

def collect_files(folder):
    folder = Path(folder)
    extensions = ["*.shp", "*.gpkg", "*.geojson", "*.kml", "*.kmz", "*.SHP", "*.GPKG", "*.GEOJSON", "*.KML", "*.KMZ"]
    files = []
    for ext in extensions:
        files.extend(folder.rglob(ext) if RECURSIVE else folder.glob(ext))
    return sorted(set(files))

def geom_name(layer):
    g = QgsWkbTypes.geometryType(layer.wkbType())
    return {QgsWkbTypes.PointGeometry: "Point", QgsWkbTypes.LineGeometry: "Line", QgsWkbTypes.PolygonGeometry: "Polygon"}.get(g, "Unknown")

rows = []
for path in collect_files(INPUT_FOLDER):
    layer = QgsVectorLayer(str(path), path.stem, "ogr")
    rows.append({
        "file": str(path),
        "valid": str(layer.isValid()).lower(),
        "geometry_type": geom_name(layer) if layer.isValid() else "",
        "feature_count": layer.featureCount() if layer.isValid() else "",
        "crs": layer.crs().authid() if layer.isValid() else "",
    })

Path(OUTPUT_CSV).parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file", "valid", "geometry_type", "feature_count", "crs"])
    writer.writeheader()
    writer.writerows(rows)

print(f"[DONE] {OUTPUT_CSV}")

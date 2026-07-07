"""
Merge multiple KML/KMZ vector files from a folder into GeoPackage outputs
grouped by geometry type. Run inside QGIS Python Console.
"""

from pathlib import Path
from qgis.core import QgsCoordinateReferenceSystem, QgsProject, QgsVectorLayer, QgsWkbTypes
import processing

INPUT_FOLDER = r"C:\GIS\input_kml_kmz"
OUTPUT_FOLDER = r"C:\GIS\output"
OUTPUT_CRS = "EPSG:4326"
RECURSIVE = True
ADD_OUTPUTS_TO_PROJECT = True

def collect_files(folder):
    folder = Path(folder)
    patterns = ["*.kml", "*.kmz", "*.KML", "*.KMZ"]
    files = []
    for pattern in patterns:
        files.extend(folder.rglob(pattern) if RECURSIVE else folder.glob(pattern))
    return sorted(set(files))

def group_name(layer):
    g = QgsWkbTypes.geometryType(layer.wkbType())
    if g == QgsWkbTypes.PointGeometry:
        return "points"
    if g == QgsWkbTypes.LineGeometry:
        return "lines"
    if g == QgsWkbTypes.PolygonGeometry:
        return "polygons"
    return "unknown"

def main():
    out_dir = Path(OUTPUT_FOLDER)
    out_dir.mkdir(parents=True, exist_ok=True)
    groups = {"points": [], "lines": [], "polygons": [], "unknown": []}

    for file_path in collect_files(INPUT_FOLDER):
        layer = QgsVectorLayer(str(file_path), file_path.stem[:80], "ogr")
        if not layer.isValid() or layer.featureCount() == 0:
            print(f"[SKIP] {file_path}")
            continue
        groups[group_name(layer)].append(layer)
        print(f"[LOAD] {file_path.name} | {group_name(layer)} | {layer.featureCount()} features")

    for name, layers in groups.items():
        if not layers:
            continue
        output = str(out_dir / f"merged_kml_kmz_{name}.gpkg")
        result = processing.run("native:mergevectorlayers", {
            "LAYERS": layers,
            "CRS": QgsCoordinateReferenceSystem(OUTPUT_CRS),
            "OUTPUT": output,
        })
        if ADD_OUTPUTS_TO_PROJECT:
            merged = QgsVectorLayer(result["OUTPUT"], f"merged_kml_kmz_{name}", "ogr")
            if merged.isValid():
                QgsProject.instance().addMapLayer(merged)
        print(f"[OK] {output}")

main()

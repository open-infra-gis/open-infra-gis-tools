"""
Validate geometries in the active QGIS vector layer and export invalid features.
Run inside QGIS Python Console.
"""

from pathlib import Path
from qgis.core import QgsProject
import processing

OUTPUT_INVALID = r"C:\GIS\invalid_geometries.gpkg"

layer = iface.activeLayer()
if layer is None:
    raise RuntimeError("No active layer selected.")

Path(OUTPUT_INVALID).parent.mkdir(parents=True, exist_ok=True)

result = processing.run("qgis:checkvalidity", {
    "INPUT_LAYER": layer,
    "METHOD": 2,
    "VALID_OUTPUT": "TEMPORARY_OUTPUT",
    "INVALID_OUTPUT": OUTPUT_INVALID,
    "ERROR_OUTPUT": "TEMPORARY_OUTPUT",
})

invalid = result.get("INVALID_OUTPUT")
if invalid:
    print(f"[DONE] Invalid geometries exported to: {OUTPUT_INVALID}")
else:
    print("[DONE] Validation completed.")

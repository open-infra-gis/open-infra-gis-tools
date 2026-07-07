"""
Run nearest-neighbor proximity analysis between two QGIS layers.
Run inside QGIS Python Console after setting layer names.
"""

import processing

INPUT_LAYER_NAME = "YOUR_INPUT_LAYER"
REFERENCE_LAYER_NAME = "YOUR_REFERENCE_LAYER"
OUTPUT_PATH = r"C:\GIS\nearest_proximity.gpkg"

project = QgsProject.instance()
input_layer = project.mapLayersByName(INPUT_LAYER_NAME)[0]
reference_layer = project.mapLayersByName(REFERENCE_LAYER_NAME)[0]

processing.run("native:joinbynearest", {
    "INPUT": input_layer,
    "INPUT_2": reference_layer,
    "FIELDS_TO_COPY": [],
    "DISCARD_NONMATCHING": False,
    "NEIGHBORS": 1,
    "MAX_DISTANCE": None,
    "PREFIX": "near_",
    "OUTPUT": OUTPUT_PATH,
})

print(f"[DONE] {OUTPUT_PATH}")

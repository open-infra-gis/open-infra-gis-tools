"""
Clip an input vector layer by a boundary layer.
Run inside QGIS Python Console after setting layer names.
"""

import processing

INPUT_LAYER_NAME = "YOUR_INPUT_LAYER"
BOUNDARY_LAYER_NAME = "YOUR_BOUNDARY_LAYER"
OUTPUT_PATH = r"C:\GIS\clipped_output.gpkg"

project = QgsProject.instance()
input_layer = project.mapLayersByName(INPUT_LAYER_NAME)[0]
boundary_layer = project.mapLayersByName(BOUNDARY_LAYER_NAME)[0]

processing.run("native:clip", {
    "INPUT": input_layer,
    "OVERLAY": boundary_layer,
    "OUTPUT": OUTPUT_PATH,
})

print(f"[DONE] {OUTPUT_PATH}")
